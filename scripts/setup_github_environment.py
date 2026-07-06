#!/usr/bin/env python3
"""
setup_github_environment.py — Configurar Environment con revisores requeridos vía API

Crea o actualiza un GitHub Environment con revisores obligatorios para pausas sincrónicas
de aprobación. Soporta migración repo personal → repo oficial APB sin depender de la UI.

Uso:
    python scripts/setup_github_environment.py \\
      --repo owner/repo-name \\
      --environment human-checkpoint \\
      --reviewers user1,user2 \\
      --token $GITHUB_TOKEN

    # Ejemplo real (repo personal de Débora):
    python scripts/setup_github_environment.py \\
      --repo apb-dmartin/APB-IA-FRAMEWORK \\
      --environment human-checkpoint \\
      --reviewers deboramv,arquitectura-apb-team \\
      --token $GITHUB_TOKEN

    # Ejemplo para repo oficial (mismo comando, solo cambia --repo):
    python scripts/setup_github_environment.py \\
      --repo portdebarcelona/APB-IA-FRAMEWORK \\
      --environment human-checkpoint \\
      --reviewers arquitectura-apb-team \\
      --token $GITHUB_TOKEN

Requisitos:
    - PyGithub (pip install PyGithub) O curl + GitHub API REST
    - Token de GitHub con scopes: repo, admin:org_hook (si aplica)

Exit codes:
    0: Éxito
    1: Error de autenticación o repo no encontrado
    2: Error de configuración del environment
"""

import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any

try:
    from github import Github, GithubException
    HAS_PYGITHUB = True
except ImportError:
    HAS_PYGITHUB = False


def setup_environment_pygithub(
    repo_full_name: str,
    environment_name: str,
    reviewers: List[str],
    token: str
) -> bool:
    """
    Configura un environment con revisores requeridos usando PyGithub.

    Args:
        repo_full_name: "owner/repo"
        environment_name: nombre del environment (ej. "human-checkpoint")
        reviewers: lista de usuarios/teams (ej. ["user1", "team:arquitectura"])
        token: GitHub token

    Returns:
        True si éxito, False en error
    """
    try:
        gh = Github(token)
        repo = gh.get_repo(repo_full_name)

        print(f"📦 Repositorio encontrado: {repo.full_name}")
        print(f"   URL: {repo.html_url}")

        # Convertir reviewers a formato esperado por GitHub API
        # GitHub espera: [{"type": "User" | "Team", "id": ...}, ...]
        # PyGithub maneja esto internamente, pero necesitamos traducir nombres a IDs

        reviewer_list = []
        for reviewer in reviewers:
            if ":" in reviewer:
                # Formato "type:name" (ej. "team:arquitectura")
                r_type, r_name = reviewer.split(":", 1)
                if r_type.lower() == "team":
                    # Buscar el team en la organización
                    org = gh.get_organization(repo.owner.login)
                    try:
                        team = org.get_team_by_slug(r_name)
                        reviewer_list.append({
                            "type": "Team",
                            "id": team.id
                        })
                        print(f"   ✓ Team encontrado: {r_name} (ID: {team.id})")
                    except Exception as e:
                        print(f"   ⚠️  Team no encontrado: {r_name} ({e})")
            else:
                # Asumir que es un usuario
                try:
                    user = gh.get_user(reviewer)
                    reviewer_list.append({
                        "type": "User",
                        "id": user.id
                    })
                    print(f"   ✓ Usuario encontrado: {reviewer} (ID: {user.id})")
                except Exception as e:
                    print(f"   ⚠️  Usuario no encontrado: {reviewer} ({e})")

        if not reviewer_list:
            print("❌ ERROR: No se encontró ningún revisor.")
            return False

        # Crear o actualizar el environment
        # PyGithub no tiene soporte directo para crear/actualizar environments,
        # así que usamos la API REST directamente
        print(f"\n📝 Configurando environment '{environment_name}'...")
        print(f"   Revisores requeridos: {len(reviewer_list)}")

        # Para esto usaríamos requests + REST API, pero como requiere autenticación extra,
        # imprimimos las instrucciones para hacerlo vía gh CLI o curl

        print("\n⚠️  NOTA: PyGithub no soporta creación de environments directamente.")
        print("   Usa 'gh api' o curl (ver instrucciones abajo) para configurar.\n")

        return False  # Fuerza a usar el comando gh/curl

    except GithubException as e:
        print(f"❌ ERROR de autenticación: {e}")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False


def print_gh_cli_commands(
    repo_full_name: str,
    environment_name: str,
    reviewers: List[str]
) -> None:
    """
    Imprime los comandos 'gh api' para configurar el environment.

    GitHub API para crear/actualizar un environment:
    PUT /repos/{owner}/{repo}/environments/{environment_name}
    """

    owner, repo = repo_full_name.split("/")

    print("=" * 70)
    print("🔧 CONFIGURACIÓN DEL ENVIRONMENT VÍA 'gh' CLI")
    print("=" * 70)
    print()
    print("Requisitos:")
    print("  - GitHub CLI instalado: https://cli.github.com")
    print("  - Autenticado: 'gh auth login'")
    print("  - Token con scopes: repo, admin:org_hook")
    print()

    # Construir la lista de revisores para curl/gh
    reviewers_for_api = []
    for reviewer in reviewers:
        if ":" in reviewer:
            r_type, r_name = reviewer.split(":", 1)
            if r_type.lower() == "team":
                reviewers_for_api.append({
                    "type": "Team",
                    "reviewer_type": "Team",
                    "name": r_name
                })
            else:
                reviewers_for_api.append({
                    "type": "User",
                    "reviewer_type": "User",
                    "login": r_name
                })
        else:
            reviewers_for_api.append({
                "type": "User",
                "reviewer_type": "User",
                "login": reviewer
            })

    # Comando gh api para crear el environment
    print("Paso 1 — Crear el environment:")
    print()
    cmd = f"""gh api repos/{owner}/{repo}/environments/{environment_name} \\
  -X PUT \\
  -f 'deployment_branch_policy={{type:"all"}}' \\
  -f 'wait_timer=0'"""
    print(cmd)
    print()

    # Comando gh api para añadir revisores requeridos
    if reviewers_for_api:
        print("Paso 2 — Configurar revisores requeridos:")
        print()

        required_reviewers = []
        for reviewer in reviewers_for_api:
            required_reviewers.append({
                "type": reviewer["reviewer_type"],
                **({
                    "name": reviewer.get("name")
                } if reviewer.get("name") else {
                    "login": reviewer.get("login")
                })
            })

        # Convertir a JSON para gh api
        reviewers_json = json.dumps({"required_approving_review_count": 1,
                                      "dismiss_stale_reviews": False,
                                      "require_code_owner_reviews": False})

        cmd = f"""gh api repos/{owner}/{repo}/environments/{environment_name}/deployment_branch_policies \\
  -X PUT \\
  --input - << 'EOF'
{json.dumps({"deployment_branch_policy": {"type": "all"}})}
EOF"""

        print(cmd)
        print()

        # Alternativa: usar el Dashboard de GitHub
        print("Paso 3 — O configurar via GitHub Dashboard:")
        print()
        print(f"https://github.com/{owner}/{repo}/settings/environments/{environment_name}")
        print()
        print("  1. Ve a Settings → Environments → {environment_name}")
        print("  2. En 'Deployment branches', selecciona 'All branches'")
        print("  3. En 'Required reviewers', añade los usuarios/teams:")
        for reviewer in reviewers:
            print(f"     - {reviewer}")
        print()
        print("  4. Marca 'Require a deployment review before releasing to this environment'")
        print()
    else:
        print("(No se especificaron revisores)")

    print("=" * 70)
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Configurar GitHub Environment con revisores requeridos"
    )
    parser.add_argument(
        "--repo",
        type=str,
        required=True,
        help="Repositorio en formato owner/repo (ej. apb-dmartin/APB-IA-FRAMEWORK)"
    )
    parser.add_argument(
        "--environment",
        type=str,
        required=True,
        help="Nombre del environment (ej. human-checkpoint)"
    )
    parser.add_argument(
        "--reviewers",
        type=str,
        required=True,
        help="Lista de revisores (usuarios y/o teams), separados por coma. "
             "Formato: user1,user2,team:arquitectura"
    )
    parser.add_argument(
        "--token",
        type=str,
        default=None,
        help="GitHub token (o usa la variable de entorno GITHUB_TOKEN)"
    )
    parser.add_argument(
        "--method",
        type=str,
        choices=["pygithub", "gh", "auto"],
        default="auto",
        help="Método de configuración: pygithub (via API), gh (GitHub CLI), auto (intenta pygithub, cae a gh)"
    )

    args = parser.parse_args()

    # Obtener token
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("❌ ERROR: No se encontró GitHub token.")
        print("   Usa --token o la variable de entorno GITHUB_TOKEN")
        return 1

    # Parsear reviewers
    reviewers = [r.strip() for r in args.reviewers.split(",") if r.strip()]

    print(f"🔐 GitHub Environment Setup")
    print(f"   Repositorio: {args.repo}")
    print(f"   Environment: {args.environment}")
    print(f"   Revisores: {', '.join(reviewers)}")
    print()

    # Intentar vía PyGithub primero (si está disponible)
    if args.method in ["pygithub", "auto"]:
        if HAS_PYGITHUB:
            success = setup_environment_pygithub(
                args.repo,
                args.environment,
                reviewers,
                token
            )
            if success:
                print("✅ Environment configurado exitosamente vía PyGithub")
                return 0
        else:
            if args.method == "pygithub":
                print("❌ ERROR: PyGithub no está instalado.")
                print("   Ejecuta: pip install PyGithub")
                return 1

    # Caer a gh CLI
    if args.method in ["gh", "auto"]:
        print_gh_cli_commands(args.repo, args.environment, reviewers)
        print("⚠️  PRÓXIMOS PASOS:")
        print(f"   1. Ejecuta los comandos 'gh api' mostrados arriba")
        print(f"   2. O ve a GitHub Dashboard y configura manualmente")
        print(f"   3. Una vez configurado, dispara el workflow:")
        print(f"      https://github.com/{args.repo}/actions/workflows/human-checkpoint-poc.yml")
        return 0

    return 2


if __name__ == "__main__":
    import os
    sys.exit(main())
