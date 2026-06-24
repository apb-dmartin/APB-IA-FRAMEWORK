---
id: "third-sigridjineth-ansible-enterprise-v1.0"
name: "Ansible Enterprise Multi-platform"
description: "Automatización de infraestructura con Ansible: multi-plataforma, cloud, Kubernetes, seguridad y testing, consolidando community skills y buenas prácticas de Red Hat."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/sigridjineth/hello-ansible-skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# SKILL_PLAT_ANSIBLE — Automation & Configuration Management

## 1. Propósito y Alcance

Esta skill unifica el conocimiento de múltiples fuentes de Ansible (community skills,
best practices de Red Hat, y documentación oficial) en un skill enterprise para el framework APB.

**Plataformas soportadas:**
- **Linux**: RHEL, Ubuntu, Debian, SUSE, Alpine
- **Windows**: Windows Server, Windows 10/11, WinRM/SSH
- **Network**: Cisco, Juniper, Arista, F5 (via network modules)
- **Cloud**: AWS, Azure, GCP (via cloud collections)
- **Kubernetes**: K8s, OpenShift (via k8s collection)
- **Containers**: Docker, Podman (via container tools)
- **Databases**: PostgreSQL, MySQL, MongoDB, Redis

**Casos de uso principales:**
1. Automatización de provisioning y configuración de servidores
2. Migración de scripts shell/bash a playbooks idempotentes
3. Desarrollo de roles reutilizables y collections
4. Testing de roles con Molecule y Testinfra
5. Integración con Ansible Automation Platform (AAP) / AWX
6. Event-driven automation con Event-Driven Ansible (EDA)

## 2. Principios Core de Ansible (APB)

1. **Idempotencia**: Ejecuciones repetidas producen el mismo estado final; usar módulos nativos sobre shell/command.
2. **Declarative**: Describir el estado deseado, no los pasos para llegar allí.
3. **Simplicidad**: YAML legible; evitar complejidad innecesaria; preferir roles sobre plays monolíticos.
4. **Inmutabilidad**: Los playbooks no modifican el código fuente; las variables externas controlan el comportamiento.
5. **Seguridad**: Secrets nunca en texto plano; uso obligatorio de ansible-vault o vaults externos (HashiCorp Vault, Azure Key Vault, AWS Secrets Manager).
6. **Testabilidad**: Todo role debe tener tests con Molecule; check mode y diff mode para validación.
7. **Version control**: Todo playbook, role, inventory, y variable file en Git con commits frecuentes.
8. **FQCN**: Usar Fully Qualified Collection Names para futura-compatibilidad.

## 3. Estructura de Proyecto Ansible (Estándar APB)

### 3.1 Layout de Directorios
```
ansible/
├── inventories/                # Inventarios por entorno
│   ├── production/
│   │   ├── hosts.yml           # Hosts y grupos
│   │   ├── group_vars/         # Variables por grupo
│   │   │   ├── all/
│   │   │   │   ├── vars.yml
│   │   │   │   └── vault.yml   # Encrypted secrets
│   │   │   ├── webservers/
│   │   │   └── databases/
│   │   └── host_vars/          # Variables por host
│   ├── staging/
│   └── development/
├── playbooks/                  # Playbooks organizados por propósito
│   ├── site.yml                # Playbook maestro
│   ├── webservers.yml
│   ├── databases.yml
│   └── maintenance.yml
├── roles/                      # Roles internos (desarrollados por el equipo)
│   ├── common/
│   │   ├── tasks/
│   │   │   ├── main.yml
│   │   │   └── setup.yml
│   │   ├── handlers/
│   │   │   └── main.yml
│   │   ├── templates/
│   │   ├── files/
│   │   ├── vars/
│   │   ├── defaults/
│   │   │   └── main.yml
│   │   ├── meta/
│   │   │   └── main.yml
│   │   └── molecule/           # Tests Molecule
│   │       └── default/
│   ├── webserver/
│   └── database/
├── collections/                # Collections de Ansible Galaxy
│   └── requirements.yml
├── roles_external/             # Roles descargados de Galaxy (no versionados)
│   └── .gitignore             # Ignorar en Git
├── plugins/                    # Plugins personalizados (filtros, lookups, etc.)
├── filter_plugins/
├── lookup_plugins/
├── docs/                       # Documentación generada
├── tests/                      # Tests de integración
├── ansible.cfg                 # Configuración global de Ansible
├── requirements.txt            # Dependencias Python (ansible-core, boto3, etc.)
├── requirements.yml            # Collections y roles de Galaxy
├── vault_password_file         # NO versionar; usar .gitignore
└── .ansible-lint               # Configuración de ansible-lint
```

### 3.2 ansible.cfg (Configuración Base)
```ini
[defaults]
inventory = inventories/production/hosts.yml
roles_path = roles:roles_external
host_key_checking = False
retry_files_enabled = False
interpreter_python = auto_silent
stdout_callback = yaml
bin_ansible_callbacks = True
nocows = 1
forks = 20
timeout = 30

[privilege_escalation]
become = True
become_method = sudo
become_user = root
become_ask_pass = False

[ssh_connection]
pipelining = True
control_path = /tmp/ansible-ssh-%%h-%%p-%%r
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
```

## 4. Convenciones de Estilo YAML

### 4.1 Formato y Indentación
- **Indentación**: 2 espacios (nunca tabs)
- **Líneas máximo 160 caracteres** (preferiblemente 120)
- **Comentarios**: Generosos; describir el POR QUÉ, no el QUÉ
- **Whitespace**: YAML usa espacios para estructura; ser consistente

### 4.2 Nombres y Consistencia
- **Variables**: `snake_case`, prefijo con nombre del role (ej: `nginx_worker_processes`, `postgresql_max_connections`)
- **Tasks**: Nombres descriptivos en español o inglés (consistencia del proyecto)
- **Tags**: Minúsculas, descriptivos, reutilizables entre roles
- **Files/Templates**: Nombres descriptivos con extensión apropiada

### 4.3 Estructura de Playbook
```yaml
---
- name: Configurar servidores web
  hosts: webservers
  become: yes
  gather_facts: yes

  vars:
    nginx_worker_processes: auto

  pre_tasks:
    - name: Verificar conectividad
      ansible.builtin.ping:

  roles:
    - role: common
      tags: ["common"]
    - role: nginx
      tags: ["nginx", "webserver"]

  post_tasks:
    - name: Verificar servicio nginx
      ansible.builtin.uri:
        url: "http://localhost:80"
        status_code: 200
      register: health_check
      failed_when: health_check.status != 200
```

### 4.4 Uso de FQCN (Fully Qualified Collection Names)
```yaml
# ✅ CORRECTO - FQCN
ansible.builtin.copy:
ansible.builtin.template:
ansible.builtin.service:
community.general.mysql_db:
community.postgresql.postgresql_db:
amazon.aws.ec2_instance:
azure.azcollection.azure_rm_virtualmachine:

# ❌ INCORRECTO - Nombres cortos (deprecated en ansible-core 2.14+)
copy:
template:
service:
```

## 5. Roles - Best Practices

### 5.1 Principios de Diseño de Roles
- **Single Responsibility**: Un role = un propósito (ej: `nginx`, `postgresql`, `docker`)
- **Reusabilidad**: Sin dependencias de inventario específico; variables para todo
- **OS Agnostic**: Soportar múltiples distribuciones cuando sea posible
- **Defaults sensibles**: Valores por defecto seguros y funcionales

### 5.2 Estructura de Role
```yaml
# roles/nginx/defaults/main.yml
nginx_worker_processes: auto
nginx_worker_connections: 1024
nginx_user: "www-data"
nginx_server_tokens: "off"  # Security by default

# roles/nginx/vars/main.yml
# Variables que no deberían ser sobrescritas
nginx_package_name: "nginx"
nginx_service_name: "nginx"

# roles/nginx/tasks/main.yml
---
- name: Incluir variables específicas de OS
  ansible.builtin.include_vars: "{{ ansible_os_family }}.yml"

- name: Instalar nginx
  ansible.builtin.package:
    name: "{{ nginx_package_name }}"
    state: present

- name: Configurar nginx
  ansible.builtin.template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
  notify: Reiniciar nginx

- name: Asegurar que nginx está iniciado
  ansible.builtin.service:
    name: "{{ nginx_service_name }}"
    state: started
    enabled: yes

# roles/nginx/handlers/main.yml
---
- name: Reiniciar nginx
  ansible.builtin.service:
    name: "{{ nginx_service_name }}"
    state: restarted

# roles/nginx/templates/nginx.conf.j2
user {{ nginx_user }};
worker_processes {{ nginx_worker_processes }};
events {
    worker_connections {{ nginx_worker_connections }};
}
http {
    server_tokens {{ nginx_server_tokens }};
    include /etc/nginx/conf.d/*.conf;
}
```

### 5.3 Meta y Dependencias
```yaml
# roles/nginx/meta/main.yml
galaxy_info:
  author: apb-team
  description: "Role para instalar y configurar nginx"
  company: APB
  license: MIT
  min_ansible_version: "2.15"
  platforms:
    - name: EL
      versions: ["8", "9"]
    - name: Ubuntu
      versions: ["jammy", "noble"]
  galaxy_tags: ["web", "nginx", "proxy"]

dependencies: []
```

## 6. Gestión de Variables y Vaults

### 6.1 Jerarquía de Precedencia (de menor a mayor)
1. `defaults/main.yml` (role defaults - lowest)
2. Inventory `group_vars/all`
3. Inventory `group_vars/<group>`
4. Inventory `host_vars/<host>`
5. Play `vars`
6. Play `vars_prompt`
7. Play `vars_files`
8. Role `vars/main.yml`
9. Block `vars`
10. Task `vars`
11. Extra vars `-e` (highest)

### 6.2 Vaults para Secrets
```yaml
# group_vars/all/vault.yml (encrypted con ansible-vault)
vault_database_password: "<REPLACE_WITH_REAL_SECRET>"
vault_api_key: "<REPLACE_WITH_REAL_SECRET>"

# group_vars/all/vars.yml (no encrypted - referencia a vault)
database_password: "{{ vault_database_password }}"
api_key: "{{ vault_api_key }}"
```

### 6.3 Buenas Prácticas de Variables
- **NO** hardcodear valores sensibles en playbooks o roles
- **NO** usar `host_vars` a menos que sea absolutamente necesario (preferir `group_vars`)
- **SIEMPRE** usar prefijos de role para evitar colisiones
- **SIEMPRE** definir tipos cuando sea posible (string, int, list, dict)
- **SIEMPRE** usar validaciones cuando sea posible

```yaml
# Ejemplo de validación
postgresql_version:
  type: str
  default: "15"
  choices: ["13", "14", "15", "16"]
  description: "Versión de PostgreSQL a instalar"

postgresql_max_connections:
  type: int
  default: 100
  description: "Número máximo de conexiones concurrentes"
```

## 7. Testing con Molecule

### 7.1 Estructura de Tests
```
roles/<role_name>/molecule/
└── default/
    ├── molecule.yml          # Configuración de Molecule
    ├── converge.yml          # Playbook de test
    ├── verify.yml            # Tests de verificación (Testinfra/Ansible)
    └── prepare.yml           # Preparación del entorno de test
```

### 7.2 molecule.yml (Configuración)
```yaml
---
driver:
  name: docker
platforms:
  - name: instance-ubuntu
    image: geerlingguy/docker-ubuntu2204-ansible
    command: ""
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:ro
    privileged: true
    pre_build_image: true
  - name: instance-rhel
    image: geerlingguy/docker-rockylinux9-ansible
    command: ""
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:ro
    privileged: true
    pre_build_image: true
provisioner:
  name: ansible
  lint:
    name: ansible-lint
verifier:
  name: ansible
scenario:
  name: default
  test_sequence:
    - destroy
    - create
    - prepare
    - converge
    - idempotence
    - verify
    - destroy
```

### 7.3 verify.yml (Tests de Verificación)
```yaml
---
- name: Verify
  hosts: all
  gather_facts: false
  tasks:
    - name: Verificar que nginx está instalado
      ansible.builtin.package:
        name: nginx
        state: present
      check_mode: yes
      register: nginx_installed
      failed_when: nginx_installed.changed

    - name: Verificar que nginx está corriendo
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: yes
      check_mode: yes
      register: nginx_running
      failed_when: nginx_running.changed

    - name: Verificar puerto 80
      ansible.builtin.wait_for:
        port: 80
        state: started
        timeout: 10

    - name: Verificar respuesta HTTP
      ansible.builtin.uri:
        url: "http://localhost:80"
        status_code: 200
      register: http_response
      failed_when: http_response.status != 200
```

### 7.4 Ejecución de Tests
```bash
# Test completo de un role
molecule test

# Solo crear y convergir (desarrollo)
molecule create
molecule converge

# Verificar idempotencia
molecule idempotence

# Verificar estado
molecule verify

# Destruir entorno
molecule destroy
```

## 8. Ansible Automation Platform (AAP) / AWX

### 8.1 Componentes
- **Automation Controller**: Orquestación, scheduling, RBAC, surveys
- **Automation Hub**: Repositorio de collections certificadas y contenido personalizado
- **Event-Driven Ansible (EDA)**: Automatización basada en eventos (webhooks, monitoring alerts)
- **Analytics**: Insights y reporting de automatización

### 8.2 Integration Patterns
```yaml
# Ejemplo de Job Template con Survey
- name: Crear Job Template en AAP
  awx.awx.job_template:
    name: "Deploy Web Application"
    organization: "APB"
    project: "APB Git Repository"
    playbook: "playbooks/webservers.yml"
    inventory: "Production"
    credentials:
      - "SSH Production"
      - "Vault Password"
    survey_enabled: yes
    survey_spec:
      name: "Deployment Parameters"
      description: "Parámetros para el despliegue"
      spec:
        - type: text
          question_name: "Versión de la aplicación"
          question_description: "Tag de la imagen Docker a desplegar"
          variable: "app_version"
          required: true
          default: "latest"
        - type: multiplechoice
          question_name: "Entorno"
          variable: "environment"
          choices:
            - "staging"
            - "production"
          required: true
          default: "staging"
```

### 8.3 Event-Driven Ansible (EDA)
```yaml
# rulebooks/scale-webservers.yml
---
- name: Auto-scale webservers basado en CPU
  hosts: localhost
  sources:
    - ansible.eda.prometheus:
        host: prometheus.monitoring.local
        port: 9090
        query: "avg(cpu_usage_percent) by (job)"
  rules:
    - name: Scale up cuando CPU > 80%
      condition: event.prometheus.avg > 80
      action:
        run_job_template:
          name: "Scale Up Webservers"
          organization: "APB"
    - name: Scale down cuando CPU < 20%
      condition: event.prometheus.avg < 20
      action:
        run_job_template:
          name: "Scale Down Webservers"
          organization: "APB"
```

## 9. Cloud Automation (AWS, Azure, GCP)

### 9.1 AWS con amazon.aws Collection
```yaml
- name: Provisionar instancia EC2
  amazon.aws.ec2_instance:
    name: "web-server-{{ env }}"
    instance_type: t3.micro
    image_id: ami-0c55b159cbfafe1f0
    vpc_subnet_id: "{{ subnet_id }}"
    security_group: "{{ security_group }}"
    key_name: "{{ ssh_key_name }}"
    tags:
      Environment: "{{ env }}"
      Project: "{{ project_name }}"
      ManagedBy: "ansible"
    state: running
    wait: yes
  register: ec2_instance

- name: Agregar a inventario dinámico
  ansible.builtin.add_host:
    name: "{{ ec2_instance.instances[0].public_ip_address }}"
    groups: "webservers"
    ansible_user: ec2-user
    ansible_ssh_private_key_file: "{{ ssh_key_path }}"
```

### 9.2 Azure con azure.azcollection
```yaml
- name: Crear VM en Azure
  azure.azcollection.azure_rm_virtualmachine:
    resource_group: "{{ resource_group }}"
    name: "web-server-{{ env }}"
    vm_size: Standard_B2s
    admin_username: ansible
    ssh_password_enabled: false
    ssh_public_keys:
      - path: /home/ansible/.ssh/authorized_keys
        key_data: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    image:
      offer: UbuntuServer
      publisher: Canonical
      sku: "22.04-LTS"
      version: latest
    tags:
      Environment: "{{ env }}"
      Project: "{{ project_name }}"
```

### 9.3 GCP con google.cloud Collection
```yaml
- name: Crear instancia en GCP
  google.cloud.gcp_compute_instance:
    name: "web-server-{{ env }}"
    machine_type: e2-medium
    zone: "{{ gcp_zone }}"
    project: "{{ gcp_project }}"
    disks:
      - auto_delete: true
        boot: true
        initialize_params:
          source_image: "projects/ubuntu-os-cloud/global/images/family/ubuntu-2204-lts"
    network_interfaces:
      - network: "{{ network }}"
        access_configs:
          - name: External NAT
            type: ONE_TO_ONE_NAT
    tags:
      items:
        - webserver
        - "{{ env }}"
    labels:
      environment: "{{ env }}"
      project: "{{ project_name }}"
    state: present
```

## 10. Windows Automation

### 10.1 Configuración de WinRM
```powershell
# Script de bootstrap (ejecutar en Windows como Administrator)
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
Invoke-WebRequest -Uri $url -OutFile $file
powershell.exe -ExecutionPolicy ByPass -File $file
```

### 10.2 Playbook para Windows
```yaml
- name: Configurar servidores Windows
  hosts: windows_servers
  gather_facts: yes
  vars:
    ansible_connection: winrm
    ansible_winrm_transport: credssp
    ansible_winrm_server_cert_validation: ignore

  tasks:
    - name: Instalar IIS
      ansible.windows.win_feature:
        name: Web-Server
        state: present
        include_management_tools: yes

    - name: Configurar sitio web por defecto
      ansible.windows.win_iis_website:
        name: "Default Web Site"
        state: started
        port: 80
        ip: "*"
        application_pool: "DefaultAppPool"
        physical_path: C:\inetpub\wwwroot

    - name: Crear usuario de servicio
      ansible.windows.win_user:
        name: "svc_webapp"
        password: "{{ vault_windows_service_password }}"
        state: present
        password_never_expires: yes
        user_cannot_change_password: yes

    - name: Configurar firewall
      ansible.windows.win_firewall_rule:
        name: "HTTP"
        direction: in
        action: allow
        protocol: tcp
        localport: 80
        state: present
```

## 11. Kubernetes Automation

### 11.1 K8s con community.kubernetes
```yaml
- name: Desplegar aplicación en Kubernetes
  hosts: localhost
  gather_facts: no
  vars:
    k8s_namespace: "{{ app_namespace }}"
    k8s_app_name: "{{ app_name }}"

  tasks:
    - name: Crear namespace
      kubernetes.core.k8s:
        name: "{{ k8s_namespace }}"
        api_version: v1
        kind: Namespace
        state: present

    - name: Desplegar desde template Jinja2
      kubernetes.core.k8s:
        state: present
        template: 'deployment.yml.j2'
        namespace: "{{ k8s_namespace }}"

    - name: Verificar rollout
      kubernetes.core.k8s_info:
        api_version: apps/v1
        kind: Deployment
        name: "{{ k8s_app_name }}"
        namespace: "{{ k8s_namespace }}"
      register: deploy_info
      until: deploy_info.resources | length > 0 and deploy_info.resources[0].status.readyReplicas == deploy_info.resources[0].spec.replicas
      retries: 30
      delay: 10
```

## 12. Migración Shell → Ansible

### 12.1 Mapping Shell → Módulos Ansible
| Shell Command | Módulo Ansible | Ejemplo |
|---------------|---------------|---------|
| `mkdir -p` | `ansible.builtin.file` | `state: directory` |
| `cp /src /dest` | `ansible.builtin.copy` | `src: /src dest: /dest` |
| `apt-get install` | `ansible.builtin.apt` | `name: package state: present` |
| `systemctl restart` | `ansible.builtin.service` | `name: service state: restarted` |
| `useradd` | `ansible.builtin.user` | `name: user state: present` |
| `chmod/chown` | `ansible.builtin.file` | `mode: '0644' owner: user` |
| `echo "config" >> file` | `ansible.builtin.lineinfile` | `line: "config" path: file` |
| `curl -o file url` | `ansible.builtin.get_url` | `url: url dest: file` |
| `tar -xzf` | `ansible.builtin.unarchive` | `src: file dest: dir` |
| `docker run` | `community.docker.docker_container` | `name: container image: image` |

### 12.2 Ejemplo de Conversión
```bash
# Script shell original (70 líneas)
#!/bin/bash
# Instalar nginx
apt-get update
apt-get install -y nginx
# Configurar nginx
cat > /etc/nginx/nginx.conf <<EOF
user www-data;
worker_processes auto;
EOF
# Iniciar servicio
systemctl restart nginx
systemctl enable nginx
# Verificar
curl -s http://localhost | grep "Welcome"
```

```yaml
# Playbook Ansible equivalente (idempotente, idempotent, testeable)
---
- name: Instalar y configurar nginx
  hosts: webservers
  become: yes
  vars:
    nginx_worker_processes: auto

  tasks:
    - name: Actualizar cache de apt
      ansible.builtin.apt:
        update_cache: yes
        cache_valid_time: 3600

    - name: Instalar nginx
      ansible.builtin.apt:
        name: nginx
        state: present

    - name: Configurar nginx
      ansible.builtin.template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
        owner: root
        group: root
        mode: '0644'
      notify: Reiniciar nginx

    - name: Asegurar que nginx está iniciado y habilitado
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: yes

    - name: Verificar que nginx responde
      ansible.builtin.uri:
        url: "http://localhost"
        status_code: 200
      register: nginx_check
      retries: 5
      delay: 2
      until: nginx_check.status == 200

  handlers:
    - name: Reiniciar nginx
      ansible.builtin.service:
        name: nginx
        state: restarted
```

## 13. Linting y Static Analysis

### 13.1 ansible-lint
```bash
# Instalar
pip install ansible-lint

# Ejecutar en un playbook
ansible-lint playbooks/site.yml

# Ejecutar en un role
ansible-lint roles/nginx/

# Configuración (.ansible-lint)
---
exclude_paths:
  - .cache/
  - .github/
  - molecule/
  - venv/
  - roles_external/

skip_list:
  - yaml[line-length]  # Permitir líneas largas en templates
  - name[template]     # No requerir nombres en tasks de templates

warn_list:
  - experimental

use_default_rules: true
```

### 13.2 yamllint
```yaml
# .yamllint
---
rules:
  braces:
    max-spaces-inside: 1
  brackets:
    max-spaces-inside: 1
  colons:
    max-spaces-after: 1
  commas:
    max-spaces-after: 1
  comments:
    min-spaces-from-content: 1
  document-end: disable
  document-start: enable
  empty-lines:
    max: 2
  indentation:
    spaces: 2
    indent-sequences: yes
  line-length:
    max: 160
  new-line-at-end-of-file: enable
  trailing-spaces: enable
```

## 14. Workflow de Implementación Ansible (APB)

```
1. ANÁLISIS
   └── Mapear infraestructura objetivo (OS, servicios, dependencias)
   └── Identificar secrets y datos sensibles
   └── Seleccionar collections y roles de Galaxy necesarios
   └── Definir estrategia de inventario (estático vs. dinámico)

2. DISEÑO
   └── Diseñar estructura de proyecto según estándar APB
   └── Definir variables y defaults por role
   └── Diseñar templates y archivos estáticos
   └── Planificar handlers y notificaciones
   └── Definir estrategia de testing (Molecule, check mode)

3. DESARROLLO
   └── Implementar roles siguiendo principios de idempotencia
   └── Usar FQCN en todos los módulos
   └── Implementar vaults para secrets
   └── Documentar variables en README.md por role
   └── Ejecutar ansible-lint y yamllint

4. TESTING
   └── Ejecutar tests unitarios con Molecule (create, converge, idempotence, verify)
   └── Ejecutar check mode: ansible-playbook --check --diff
   └── Ejecutar en entorno de staging
   └── Validar con herramientas de seguridad (ansible-vault audit)

5. REVISIÓN
   └── Peer review del código YAML
   └── Validar coverage de OS soportados
   └── Verificar que no hay secrets en texto plano
   └── Aprobar PR con evidencia de tests pasados

6. DESPLIEGUE
   └── Ejecutar playbook en producción con limitación de hosts
   └── Monitorear ejecución con callbacks de error
   └── Verificar estado post-deploy con handlers/verificación
   └── Documentar runbooks de operación

7. OPERACIÓN
   └── Monitorear ejecuciones programadas (AAP/AWX)
   └── Mantener collections y roles actualizados
   └── Rotar secrets según política de seguridad
   └── Revisar y optimizar playbooks periódicamente
```

## 15. Integración con otras Skills APB

- **SKILL_PLAT_TERRAFORM**: Terraform provisiona infraestructura; Ansible configura servidores (pattern: Terraform + Ansible)
- **SKILL_PLAT_CICD**: Pipeline de CI/CD para testing y despliegue de playbooks
- **SKILL_PLAT_FINOPS**: Tags obligatorios para costos en recursos cloud provisionados
- **SKILL_OPS_OBSERVABILITY**: Integración de métricas/logs en playbooks de configuración
- **SKILL_OPS_RUNBOOKS**: Runbooks de operación ejecutados como playbooks Ansible
- **SKILL_GOV_COMPLIANCE**: Políticas de seguridad y compliance en configuración de servidores
- **SKILL_DEV_CODE_BASE**: Playbooks como código base; version control, PRs, code review

## 16. Anti-patrones Ansible (Qué NO hacer)

- **Shell/command por defecto**: Usar shell/command cuando existe un módulo nativo; rompe idempotencia
- **Ignore_errors**: Usar `ignore_errors: yes` sin `failed_when` específico; oculta problemas reales
- **No handlers**: No usar handlers para acciones que deberían ejecutarse solo cuando hay cambios
- **Hardcoded paths**: Rutas hardcodeadas en lugar de variables
- **Secrets en repo**: Passwords, keys, o tokens en archivos no-encriptados
- **Monolithic plays**: Playbooks con cientos de tasks sin roles; difícil de mantener y reutilizar
- **No testing**: Roles sin tests Molecule; imposible validar cambios
- **Static inventory only**: No usar inventarios dinámicos para cloud (EC2, Azure, GCP)
- **No version pinning**: No fijar versiones de collections o roles; builds no reproducibles
- **Become everywhere**: Usar `become: yes` en todo el playbook sin necesidad; principio de mínimo privilegio
- **No tags**: Playbooks sin tags; imposible ejecutar subsets de tasks

## 17. Referencias

- [Ansible Documentation](https://docs.ansible.com/)
- [Ansible Best Practices - Red Hat](https://www.redhat.com/en/blog/10-great-ansible-practices)
- [Ansible Best Practices - enginyoyen](https://github.com/enginyoyen/ansible-best-practises)
- [Ansible Skills for Claude Code - sigridjineth](https://github.com/sigridjineth/hello-ansible-skills)
- [Ansible Automation Platform Documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/)
- [Molecule Documentation](https://ansible.readthedocs.io/projects/molecule/)
- [Ansible Lint](https://ansible.readthedocs.io/projects/lint/)
- [Ansible Galaxy](https://galaxy.ansible.com/)
- [Event-Driven Ansible](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/event-driven_ansible_controller_user_guide/index)
- [Ansible FQCN Guide](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_modules.html#using-modules)
