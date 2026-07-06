#!/usr/bin/env python3
"""
integrate_test_plans.py — Integra todos los planes QA generados en la carpeta final.
Crea la estructura Markdown unificada enriqueciendo con GitHub procedencia.
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime

def main():
    # Rutas
    source_folder = Path(r"C:\Users\martinde\OneDrive - Port de Barcelona\Proyectos\SDD - Framework desarrollo asistido por IA\documentos apoyo para construir con claude\Plan Pruebas origen codigo con GitHubCopilot")
    output_folder = Path(r"C:\Users\martinde\OneDrive - Port de Barcelona\Proyectos\SDD - Framework desarrollo asistido por IA\documentos apoyo para construir con claude\planes de pruebas")
    
    # Crear carpeta destino si no existe
    output_folder.mkdir(parents=True, exist_ok=True)
    
    print("📋 Integrando planes de pruebas...")
    print(f"   Origen: {source_folder}")
    print(f"   Destino: {output_folder}\n")
    
    # Listar todas las carpetas de aplicaciones
    app_folders = sorted([f for f in source_folder.iterdir() if f.is_dir()])
    
    generated_count = 0
    
    for app_folder in app_folders:
        app_name = app_folder.name
        
        # Buscar ficheros Markdown e HTML
        md_files = list(app_folder.glob("*.md"))
        html_files = list(app_folder.glob("*.html"))
        
        if md_files and html_files:
            md_src = md_files[0]
            html_src = html_files[0]
            
            # Copiar a destino con mismo nombre de aplicación
            md_dst = output_folder / f"{app_name}_{md_src.stem}.md"
            html_dst = output_folder / f"{app_name}_{html_src.stem}.html"
            
            shutil.copy2(md_src, md_dst)
            shutil.copy2(html_src, html_dst)
            
            print(f"✓ {app_name}")
            generated_count += 1
        else:
            print(f"⚠ {app_name} (sin archivos MD/HTML)")
    
    # Crear índice master
    create_master_index(output_folder, app_folders)
    
    print(f"\n✓ Integración completa: {generated_count} aplicaciones")
    print(f"📁 Destino: {output_folder}")

def create_master_index(output_folder: Path, app_folders):
    """Crea un índice maestro en HTML."""
    
    apps = []
    for app_folder in sorted(app_folders):
        app_code = app_folder.name.split('_')[0]
        app_name = app_folder.name.replace(app_code + '_', '')
        
        md_files = list(app_folder.glob("*.md"))
        html_files = list(app_folder.glob("*.html"))
        
        if md_files and html_files:
            md_file = md_files[0].name
            html_file = html_files[0].name
            
            apps.append({
                'code': app_code,
                'name': app_name,
                'md': md_file,
                'html': html_file
            })
    
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índice de Planes de Pruebas QA — APB-IA-FRAMEWORK</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .header {{
            background: linear-gradient(135deg, #046DB2 0%, #035A95 100%);
            color: white;
            padding: 40px;
            border-radius: 6px;
            margin-bottom: 30px;
            text-align: center;
        }}
        h1 {{ margin: 0; font-size: 28px; }}
        .subtitle {{ font-size: 14px; opacity: 0.9; margin-top: 10px; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 30px 0;
        }}
        th {{
            background: #046DB2;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
        }}
        tr:hover {{
            background: #f9f9f9;
        }}
        .app-code {{
            font-weight: 600;
            color: #046DB2;
            font-family: 'Monaco', monospace;
        }}
        a {{
            color: #046DB2;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .stats {{
            background: #f0f8ff;
            padding: 20px;
            border-radius: 6px;
            margin-bottom: 30px;
        }}
        .stats-item {{
            display: inline-block;
            margin-right: 30px;
        }}
        .stats-number {{
            font-size: 24px;
            font-weight: 600;
            color: #046DB2;
        }}
        footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
            font-size: 12px;
            color: #666;
        }}
        .warning {{
            background: #fff3cd;
            border: 1px solid #ffc107;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Planes de Pruebas QA</h1>
            <p class="subtitle">APB-IA-FRAMEWORK · Generado automáticamente</p>
        </div>

        <div class="warning">
            ⚠️ <strong>Documentos en estado DRAFT</strong> — Generados por IA, pendientes de validación y aprobación humana antes de ejecución.
        </div>

        <div class="stats">
            <div class="stats-item">
                <div class="stats-number">{len(apps)}</div>
                <div>Aplicaciones documentadas</div>
            </div>
            <div class="stats-item">
                <div class="stats-number">{len(apps) * 2}</div>
                <div>Planes (Markdown + HTML)</div>
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Código</th>
                    <th>Nombre Aplicación</th>
                    <th>Plan Markdown</th>
                    <th>Plan HTML</th>
                    <th>Estado</th>
                </tr>
            </thead>
            <tbody>
"""
    
    for app in apps:
        html_content += f"""                <tr>
                    <td class="app-code">{app['code']}</td>
                    <td>{app['name']}</td>
                    <td><a href="{app['md']}">📄 Ver</a></td>
                    <td><a href="{app['html']}">🌐 Ver</a></td>
                    <td><span style="background: #e2e3e5; padding: 4px 8px; border-radius: 3px; font-size: 12px;">draft</span></td>
                </tr>
"""
    
    html_content += f"""            </tbody>
        </table>

        <footer>
            <p>Generado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} por apb-qa-test-plan-v1.0</p>
            <p><small>[IA-GEN] Documento generado por APB AI Framework — pendiente revisión humana</small></p>
            <p><small>Conforme a TEST_PLAN_STANDARD.md v1.5.0 | Estándar de marcado IA: POLICY_AI_USAGE §6</small></p>
        </footer>
    </div>
</body>
</html>
"""
    
    index_path = output_folder / "INDEX.html"
    index_path.write_text(html_content, encoding='utf-8')
    
    print(f"\n✓ Índice maestro creado: {index_path.name}")

if __name__ == "__main__":
    main()
