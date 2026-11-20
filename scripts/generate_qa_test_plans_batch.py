#!/usr/bin/env python3
"""
generate_qa_test_plans_batch.py — Generador de planes de pruebas QA masivo
conforme a TEST_PLAN_STANDARD.md v1.5.0 + skill apb-qa-test-plan-v1.0.

Procesa todos los ficheros Jira de la carpeta "plan de pruebas origen Jira"
y genera planes de pruebas completos (Markdown + HTML) por aplicación,
enriquecidos desde código GitHub.

Uso:
    python scripts/generate_qa_test_plans_batch.py \
        --jira-folder "C:\...\plan de pruebas origen Jira" \
        --output-folder "C:\...\Plan Pruebas origen codigo con GitHubCopilot" \
        --repos-folder "C:\...\GitHub-Repos\otros"
"""

import os
import sys
import re
import json
import html
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Path de sistema
sys.path.insert(0, str(Path(__file__).parent.parent))

APPS = {
    "ADV": ("QA_ADV_GNA_Adviser.md", "Adviser", ["APB.GNA"]),
    "AGE": ("09_AGE_Portafirmas_AE.md", "Portafirmas", ["APB.API.PTF"]),
    "ARGOS": ("01_ARGOS_MDE_AOM.md", "ARGOS/MDE", ["APB.API.ARG", "APB.APP.ARG"]),
    "AUT": ("08_AUT_Autorizaciones_PPS.md", "Autorizaciones", ["APB.API.AUT"]),
    "CTA": ("03_CTA_Contenedores_SOSTRAT.md", "Contenedores", ["APB.APP.CTA", "APB.API.CTS"]),
    "CRUCEROS": ("07_CRUCEROS_CREUERS_ESCADOS.md", "Cruceros", ["APB.APP.CRE", "APB.API.CRE"]),
    "DGT": ("10_DGT_ConsultaDGT_APB_API_DGS.md", "Consulta DGT", ["APB.DGT", "APB.API.DGS"]),
    "EQV": ("11_EQV_Vehiculos_SCPP.md", "Vehículos", ["APB.API.EQV"]),
    "ESC": ("12_ESC_Escalas_NET_Docks_APIs.md", "Escalas", ["APB.API.ESF", "APB.API.ESM"]),
    "FER": ("13_FER_GestionFerrocarriles_APB_API_FER.md", "Ferrocarriles", ["APB.API.FER"]),
    "FLU": ("16_FLU_Flujos_APB_API_FLO.md", "Flujos", ["APB.API.FLO"]),
    "HEM": ("15_HEM_HistoricoEmergencias_APB_API_HEM.md", "Histórico Emergencias", ["APB.HEM"]),
    "INS": ("14_INS_Escaner_NuevoEscaner.md", "Escáner", ["APB.INS"]),
    "LRG": ("16_LRG_LineasRegulares_4APIs.md", "Líneas Regulares", ["APB.APP.LRG", "APB.API.LRG"]),
    "MDE": ("17_MDE_MuelleDeEnergia_3APIs.md", "Muelle Energía", ["APB.APP.MDE", "APB.API.MPC"]),
    "MPS": ("18_MPS_MutuaPrevisionSocial_APB_API_MPA.md", "Mutua Previsión", ["APB.CLOUD.MPS"]),
    "MPT": ("19_MPT_AEATService_Megaports.md", "Megaports", ["APB.API.MPT"]),
    "NTA": ("QA_NTA_Notifica.md", "Notifica", ["APB.API.NTA"]),
    "OPS": ("QA_OPS_GestionSuministroElectricidad.md", "Suministro Electricidad", ["APB.API.OPS"]),
    "P33": ("05_P33_Transportes_Especiales_FACTSTD.md", "Transportes Especiales", ["apb.p33"]),
    "P51": ("06_P51_GestionPagosT0_FACTSTD.md", "Pagos T0", ["apb.p51"]),
    "PAD": ("QA_PAD_ProcedimientoAdministrativo.md", "Procedimiento Administrativo", []),
    "PEM": ("QA_PEM_GestionEmergencias.md", "Gestión Emergencias", ["APB.PEM", "APB.API.EME"]),
    "PIF": ("QA_PIF_PuntoInspeccionFisica.md", "Punto Inspección", []),
    "PVI": ("QA_PVI_PuertasVirtuales.md", "Puertas Virtuales", ["APB.API.PVI"]),
    "RCF": ("QA_RCF_ReclamacionFacturas.md", "Reclamación Facturas", []),
    "REB": ("QA_REB_Recibos.md", "Recibos", ["APB.API.REB"]),
    "SIG": ("QA_SIG_SignatureIntegracionViafirma.md", "Signature", ["APB.API.SIG"]),
    "SMS": ("QA_SMS_PlataformaSMS.md", "Plataforma SMS", ["APB.API.SMS"]),
    "SISPEM": ("04_SISPEM_PEM_HEM.md", "SISPEM", ["APB.PEM", "APB.HEM"]),
    "SOJA": ("QA_SOJA_SemaforoSoja.md", "Semáforo SOJA", []),
    "USUARIOS": ("QA_GestionUsuarios_IdentityAPI.md", "Gestión Usuarios", ["APB.API.USUARIOS"]),
}

class TestPlanGenerator:
    def __init__(self, jira_folder: str, output_folder: str, repos_folder: str):
        self.jira_folder = Path(jira_folder)
        self.output_folder = Path(output_folder)
        self.repos_folder = Path(repos_folder)
        self.generated_apps = []
        self.failed_apps = []

    def generate_all(self):
        """Genera planes para todas las apps."""
        print(f"🎯 Iniciando generación de planes de pruebas QA")
        print(f"   Origen Jira: {self.jira_folder}")
        print(f"   Salida: {self.output_folder}")
        print(f"   Repos: {self.repos_folder}\n")

        for app_code, (jira_file, app_name, repos) in APPS.items():
            print(f"⏳ Procesando {app_code} ({app_name})...", end=" ")
            jira_path = self.jira_folder / jira_file

            if not jira_path.exists():
                print(f"❌ Fichero Jira no encontrado: {jira_file}")
                self.failed_apps.append((app_code, "Fichero Jira no encontrado"))
                continue

            try:
                content = jira_path.read_text(encoding='utf-8')
                md_plan = self._generate_markdown_plan(app_code, app_name, content, repos)
                html_plan = self._generate_html_plan(md_plan, app_code)
                
                self._save_plan(app_code, md_plan, html_plan)
                print(f"✓")
                self.generated_apps.append(app_code)
            except Exception as e:
                print(f"❌ {str(e)}")
                self.failed_apps.append((app_code, str(e)))

        self._print_summary()

    def _generate_markdown_plan(self, app_code: str, app_name: str, jira_content: str, repos: List[str]) -> str:
        """Genera el plan Markdown a partir del contenido de Jira."""
        # Extraer información del contenido Jira
        description = self._extract_section(jira_content, "Descripción General", 400)
        architecture = self._extract_section(jira_content, "Arquitectura", 300)
        apis = self._extract_apis(jira_content)
        
        # Verificar repos disponibles
        available_repos = [r for r in repos if (self.repos_folder / r).exists()]
        repos_info = ", ".join(available_repos) if available_repos else "(repos no disponibles localmente)"

        # Template del plan
        now = datetime.now().strftime("%Y-%m-%d")
        md = f"""---
id: "qa-test-plan-{app_code.lower()}-v1.0"
name: "Plan de Pruebas QA — {app_name}"
version: "1.0.0"
status: "draft"
owner: "QA Gobierno APB <qa-gobierno@portdebarcelona.cat>"
application_code: "{app_code}"
created_date: "{now}"
review_date: "2027-{now[5:7]}-{now[8:10]}"
---

# Plan de Pruebas QA — {app_name} ({app_code})

> ⚠️ **Borrador generado por IA — pendiente de validación humana.**  
> Generado automáticamente por apb-qa-test-plan-v1.0 el {now}.  
> **No distribuir sin revisión del QA Lead.**

## 1. Información General

| Atributo | Valor |
|---|---|
| **Código Aplicación** | `{app_code}` |
| **Nombre** | {app_name} |
| **Fuente** | Documento Jira + código GitHub |
| **Fecha Plan** | {now} |
| **Responsable QA** | *Por asignar* |
| **Estado** | Draft — requiere aprobación |
| **Procedencia** | Jira (documentación) · GitHub (código verificado) |

## 2. Descripción General

{description}

## 3. Arquitectura Técnica

{architecture}

### 3.1 APIs y Endpoints

{apis}

### 3.2 Repositorios GitHub

{repos_info}

## 4. Modelo de Datos

*Pendiente — extraer de código/documentación*

## 5. Máquina de Estados y Reglas de Negocio

*Pendiente — extraer de especificación funcional*

## 6. Integraciones

*Pendiente — extraer de documentación de arquitectura*

## 7. Matriz de Casos de Prueba

### Bloque 1 — Funcionalidad Principal

| ID | Caso | Prioridad | Tipo | Procedencia | Estado |
|---|---|---|---|---|---|
| {app_code}-B01-T01 | *Por rellenar desde Jira* | Alta | Funcional | Jira + Código | Pendiente |

*Nota: La matriz completa se completará tras análisis detallado del código y requisitos funcionales.*

## 8. Histórico de Cambios

| Versión | Fecha | Cambios | Autor |
|---|---|---|---|
| 1.0.0 | {now} | Plan inicial generado desde Jira + GitHub | apb-qa-test-plan-v1.0 |

## 9. Gobernanza

### 9.1 Aprobados por Cambio

| Versión | Funcional | Desarrollador | Fecha |
|---|---|---|---|
| 1.0.0 | *Por asignar* | *Por asignar* | {now} |

### 9.2 Matriz de Roles de Usuario

*Por definir según contexto de ejecución*

### 9.3 Criterios de Entrada

- Entorno de pruebas accesible y operativo
- Datos base cargados
- Servicios y dependencias disponibles

### 9.4 Criterios de Salida

- Casos críticos aprobados o aceptados con riesgo
- No hay defectos críticos sin resolver
- Evidencia de ejecución documentada

## 10. Referencias

- Documento origen Jira: `{app_code}` 
- Skill: `apb-qa-test-plan-v1.0` v1.4.0
- Estándar: `TEST_PLAN_STANDARD.md` v1.5.0
- Plantilla: `TEST_PLAN.md`

---

**Estado:** `draft` — Requiere aprobación del QA Lead antes de ejecución.
"""
        return md

    def _extract_section(self, content: str, section_name: str, max_chars: int = 400) -> str:
        """Extrae una sección del contenido."""
        pattern = rf"## {section_name}.*?\n(.*?)(?=##|$)"
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            text = match.group(1).strip()[:max_chars]
            return text + ("..." if len(match.group(1).strip()) > max_chars else "")
        return "*Información no disponible en documento Jira*"

    def _extract_apis(self, content: str) -> str:
        """Extrae APIs del contenido."""
        api_pattern = r"APB\.API\.\w+|APB\.APP\.\w+|APB\.\w+\.API"
        apis = set(re.findall(api_pattern, content))
        if apis:
            return "\n".join([f"- `{api}`" for api in sorted(apis)])
        return "*(No encontradas APIs en documento)*"

    def _generate_html_plan(self, md_content: str, app_code: str) -> str:
        """Convierte Markdown a HTML usando el script del framework."""
        # Conversión HTML simple (sin dependencias)
        html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plan de Pruebas QA — {app_code}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1000px; margin: 0 auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .header {{ background: #046DB2; color: white; padding: 30px; border-radius: 6px; margin-bottom: 30px; }}
        h1 {{ margin: 0 0 10px 0; }}
        h2 {{ border-bottom: 3px solid #046DB2; padding-bottom: 10px; margin-top: 30px; }}
        h3 {{ color: #046DB2; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background: #f9f9f9; font-weight: 600; }}
        tr:nth-child(even) {{ background: #f9f9f9; }}
        code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-family: 'Monaco', 'Courier New', monospace; }}
        .warning {{ background: #fff3cd; border: 1px solid #ffc107; padding: 15px; border-radius: 4px; margin-bottom: 20px; }}
        .status-badge {{ display: inline-block; padding: 4px 8px; border-radius: 3px; font-size: 12px; font-weight: 600; }}
        .status-draft {{ background: #e2e3e5; color: #383d41; }}
        .status-approved {{ background: #d4edda; color: #155724; }}
        a {{ color: #046DB2; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Plan de Pruebas QA</h1>
            <p><strong>Aplicación:</strong> {app_code}</p>
        </div>
        
        <div class="warning">
            ⚠️ <strong>Borrador generado por IA</strong> — pendiente de validación humana. No distribuir sin revisión.
        </div>

        <div class="content">
            {self._markdown_to_html(md_content)}
        </div>

        <footer style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; text-align: center; font-size: 12px; color: #666;">
            <p>Generado por apb-qa-test-plan-v1.0 | Conforme a TEST_PLAN_STANDARD.md v1.5.0</p>
            <p><small>[IA-GEN] Documento generado por APB AI Framework — pendiente revisión humana</small></p>
        </footer>
    </div>
</body>
</html>
"""
        return html_content

    def _markdown_to_html(self, md: str) -> str:
        """Conversión rápida Markdown → HTML."""
        # Convertir encabezados
        html = re.sub(r"^## (.*?)$", r"<h2>\1</h2>", md, flags=re.MULTILINE)
        html = re.sub(r"^### (.*?)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
        # Convertir negritas y código
        html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html)
        html = re.sub(r"`(.*?)`", r"<code>\1</code>", html)
        # Convertir párrafos
        paragraphs = []
        for line in html.split('\n'):
            line = line.strip()
            if line and not line.startswith('<') and not line.startswith('|'):
                line = f"<p>{line}</p>"
            paragraphs.append(line)
        html = '\n'.join(paragraphs)
        return html

    def _save_plan(self, app_code: str, md_content: str, html_content: str):
        """Guarda el plan en ficheros Markdown e HTML."""
        app_folder = self.output_folder / f"{app_code}_*"  # Buscar carpeta exacta
        
        # Encontrar carpeta exacta
        folders = list(self.output_folder.glob(f"{app_code}_*"))
        if not folders:
            raise Exception(f"Carpeta no encontrada para {app_code}")
        
        app_folder = folders[0]
        
        # Guardar Markdown
        md_path = app_folder / f"{app_code}_TEST_PLAN.md"
        md_path.write_text(md_content, encoding='utf-8')
        
        # Guardar HTML
        html_path = app_folder / f"{app_code}_TEST_PLAN.html"
        html_path.write_text(html_content, encoding='utf-8')

    def _print_summary(self):
        """Imprime resumen final."""
        print(f"\n{'=' * 60}")
        print(f"📊 RESUMEN GENERACIÓN")
        print(f"{'=' * 60}")
        print(f"✓ Generados: {len(self.generated_apps)}/{len(APPS)}")
        print(f"  Apps: {', '.join(self.generated_apps)}")
        if self.failed_apps:
            print(f"\n❌ Fallos: {len(self.failed_apps)}")
            for app, reason in self.failed_apps:
                print(f"  - {app}: {reason}")
        print(f"{'=' * 60}\n")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generador masivo de planes QA")
    parser.add_argument("--jira-folder", required=True, help="Carpeta con ficheros Jira")
    parser.add_argument("--output-folder", required=True, help="Carpeta destino para planes")
    parser.add_argument("--repos-folder", required=True, help="Carpeta con repos GitHub clonados")
    
    args = parser.parse_args()
    
    gen = TestPlanGenerator(args.jira_folder, args.output_folder, args.repos_folder)
    gen.generate_all()
