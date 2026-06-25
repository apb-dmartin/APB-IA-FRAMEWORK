#!/usr/bin/env python3
"""
emit_telemetry.py — APB AI Framework
Envía eventos de telemetría a Azure Monitor Logs Ingestion API.

Modos de uso:
  python3 scripts/emit_telemetry.py --stdin              # lee JSON de stdin
  python3 scripts/emit_telemetry.py --event '{"..."}'   # JSON inline
  python3 scripts/emit_telemetry.py --file telemetry/events.jsonl  # procesa JSONL

Requiere variables de entorno (o Azure Key Vault vía Managed Identity):
  AZURE_MONITOR_DCE_ENDPOINT   — Data Collection Endpoint URL
  AZURE_MONITOR_DCR_ID         — DCR Immutable ID
  AZURE_MONITOR_STREAM_NAME    — nombre del stream (default: Custom-APBFrameworkTelemetry_CL)
  AZURE_CLIENT_ID              — client ID (solo si no hay Managed Identity)
  AZURE_CLIENT_SECRET          — client secret (solo si no hay Managed Identity)
  AZURE_TENANT_ID              — tenant ID (solo si no hay Managed Identity)
"""

import argparse
import json
import os
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path


def _get_env(key: str, required: bool = True) -> str:
    value = os.environ.get(key, "")
    if required and not value:
        print(f"ERROR: variable de entorno {key} no definida.", file=sys.stderr)
        sys.exit(1)
    return value


def _get_credential():
    """Obtiene credencial Azure: Managed Identity preferida, Service Principal como fallback."""
    try:
        from azure.identity import DefaultAzureCredential
        return DefaultAzureCredential()
    except ImportError:
        print(
            "ERROR: azure-identity no instalado. Ejecuta: pip install azure-identity azure-monitor-ingestion",
            file=sys.stderr,
        )
        sys.exit(1)


def _enrich_event(event: dict) -> dict:
    """Añade campos obligatorios si faltan."""
    if "TimeGenerated" not in event:
        event["TimeGenerated"] = datetime.now(timezone.utc).isoformat()
    if "invocation_id" not in event:
        event["invocation_id"] = str(uuid.uuid4())
    return event


def _send_event(event: dict) -> bool:
    """Envía un evento a Azure Monitor. Devuelve True si tuvo éxito."""
    try:
        from azure.monitor.ingestion import LogsIngestionClient
    except ImportError:
        print(
            "ERROR: azure-monitor-ingestion no instalado. Ejecuta: pip install azure-monitor-ingestion",
            file=sys.stderr,
        )
        sys.exit(1)

    dce_endpoint = _get_env("AZURE_MONITOR_DCE_ENDPOINT")
    dcr_id = _get_env("AZURE_MONITOR_DCR_ID")
    stream_name = os.environ.get(
        "AZURE_MONITOR_STREAM_NAME", "Custom-APBFrameworkTelemetry_CL"
    )

    credential = _get_credential()
    client = LogsIngestionClient(endpoint=dce_endpoint, credential=credential)

    try:
        client.upload(rule_id=dcr_id, stream_name=stream_name, logs=[event])
        print(f"✅ Telemetría enviada: {event.get('component_id')} [{event.get('outcome')}]")
        return True
    except Exception as exc:
        print(f"⚠️  Error al enviar telemetría: {exc}", file=sys.stderr)
        return False


def _write_local_log(event: dict, sent: bool) -> None:
    """Escribe el evento en telemetry/events.jsonl como registro local."""
    log_path = Path("telemetry/events.jsonl")
    log_path.parent.mkdir(exist_ok=True)
    record = {**event, "sent": sent}
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def _process_jsonl_file(file_path: str) -> None:
    """Reintenta eventos marcados como sent: false en un archivo JSONL."""
    path = Path(file_path)
    if not path.exists():
        print(f"ERROR: fichero no encontrado: {file_path}", file=sys.stderr)
        sys.exit(1)

    lines = path.read_text(encoding="utf-8").splitlines()
    updated_lines = []
    retried = 0
    succeeded = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        record = json.loads(line)
        if record.get("sent") is False:
            retried += 1
            event = {k: v for k, v in record.items() if k != "sent"}
            ok = _send_event(event)
            record["sent"] = ok
            if ok:
                succeeded += 1
        updated_lines.append(json.dumps(record, ensure_ascii=False))

    path.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")
    print(f"Reintentados: {retried} | Enviados correctamente: {succeeded}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Envía eventos de telemetría APB a Azure Monitor."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--stdin", action="store_true", help="Lee JSON de stdin")
    group.add_argument("--event", type=str, help="JSON del evento inline")
    group.add_argument("--file", type=str, help="Procesa JSONL y reintenta sent:false")
    args = parser.parse_args()

    if args.file:
        _process_jsonl_file(args.file)
        return

    if args.stdin:
        raw = sys.stdin.read().strip()
    else:
        raw = args.event

    # Extrae el JSON del TELEMETRY_BLOCK si viene en formato completo de output
    if "TELEMETRY_BLOCK" in raw:
        start = raw.index("{", raw.index("TELEMETRY_BLOCK"))
        end = raw.rindex("}") + 1
        raw = raw[start:end]

    try:
        event = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"ERROR: JSON inválido — {exc}", file=sys.stderr)
        sys.exit(1)

    event = _enrich_event(event)
    sent = _send_event(event)
    _write_local_log(event, sent)

    if not sent:
        print("Evento guardado en telemetry/events.jsonl para reintento por GitHub Actions.")
        sys.exit(1)


if __name__ == "__main__":
    main()
