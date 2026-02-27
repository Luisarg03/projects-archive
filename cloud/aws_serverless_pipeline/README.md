# Repositorio de Data Analytics

Este repositorio está organizado para facilitar el desarrollo y la implementación de proyectos de análisis de datos.

## Estructura del repositorio

### .github

Este directorio contiene configuraciones de flujos de trabajo para GitHub Actions (en el subdirectorio `workflows`), que se utilizan para el control de versiones y la integración continua. Además, encontrará el archivo `CODEOWNERS` que define quién es el responsable de revisar y fusionar las solicitudes de extracción.

### docs

Aquí se almacenarán todos los documentos relacionados con los proyectos de este repositorio.

### project_1

El proyecto 1 es una aplicación completa de análisis de datos que utiliza una variedad de tecnologías de AWS, incluyendo EventBridge, Lambdas, Glue Jobs y StepFunctions.

#### Subdirectorios del `project_1`

- `aws`: Aquí se almacenan los archivos relacionados con los servicios de AWS.
- `iac`: Este directorio contiene los archivos de Infraestructura Como Código (IAC) para el aprovisionamiento y la gestión de la infraestructura del proyecto en AWS utilizando Terraform.

### Archivos del Repositorio

Además de los directorios mencionados, hay otros archivos en la raíz del repositorio que son importantes para el funcionamiento del repositorio:

- `.gitignore`: Define los archivos y directorios que git debe ignorar.
- `README.md`: Este archivo. Proporciona una visión general del repositorio.
- `sonar-project.properties`: Contiene la configuración para SonarQube, una herramienta para la inspección continua de la calidad del código.
- `tox.ini`: Contiene la configuración para Tox, una herramienta para la automatización de pruebas en Python.


### Estructura del Repositorio
```bash
.
┣ 📂.github
┃ ┣ 📂workflows
┃ ┃ ┗ 📂project_1
┃ ┃ ┃ ┣ 📜dev_workflow.yml
┃ ┃ ┃ ┗ 📜pro_workflow.yml
┃ ┗ 📜CODEOWNERS
┣ 📂docs
┣ 📂project_1
┃ ┣ 📂aws
┃ ┃ ┣ 📂events_bridge
┃ ┃ ┃ ┗ 📜event-rule-sm-project.json
┃ ┃ ┣ 📂lambdas
┃ ┃ ┃ ┣ 📂common
┃ ┃ ┃ ┃ ┣ 📜helpers_functions.py
┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┃ ┣ 📂lambda_cur_daily
┃ ┃ ┃ ┃ ┗ 📜lambda_cur_daily.py
┃ ┃ ┃ ┣ 📂lambda_raw_daily
┃ ┃ ┃ ┃ ┗ 📜lambda_raw_daily.py
┃ ┃ ┃ ┣ 📂project_logswriter
┃ ┃ ┃ ┃ ┗ 📜project_logswriter.py
┃ ┃ ┃ ┗ 📂test
┃ ┃ ┃ ┃ ┣ 📜test_helpers_functions.py
┃ ┃ ┃ ┃ ┣ 📜test_project_logswriter.py
┃ ┃ ┃ ┃ ┗ 📜__init__.py
┃ ┃ ┣ 📂pyspark
┃ ┃ ┃ ┗ 📂glue_jobs_1
┃ ┃ ┃ ┃ ┗ 📜glue_jobs_1.py
┃ ┃ ┣ 📂pythonshell
┃ ┃ ┃ ┗ 📂glue_jobs_2
┃ ┃ ┃ ┃ ┗ 📜glue_jobs_2.py
┃ ┃ ┗ 📂stepfunctions
┃ ┃ ┃ ┗ 📜sm-project.json
┃ ┗ 📂iac
┃ ┃ ┣ 📂artifacts-buckets
┃ ┃ ┃ ┣ 📜dev.tfvars
┃ ┃ ┃ ┣ 📜main.tf
┃ ┃ ┃ ┣ 📜outputs.tf
┃ ┃ ┃ ┣ 📜pro.tfvars
┃ ┃ ┃ ┣ 📜provider.tf
┃ ┃ ┃ ┗ 📜variables.tf
┃ ┃ ┣ 📂data_pipeline
┃ ┃ ┃ ┣ 📜aws_eventbridge.tf
┃ ┃ ┃ ┣ 📜aws_glue.tf
┃ ┃ ┃ ┣ 📜aws_lambda.tf
┃ ┃ ┃ ┣ 📜aws_log_to_s3.tf
┃ ┃ ┃ ┣ 📜aws_stepfunction.tf
┃ ┃ ┃ ┣ 📜backend.tf
┃ ┃ ┃ ┣ 📜copy_helper_functions.sh
┃ ┃ ┃ ┣ 📜dev.tfvars
┃ ┃ ┃ ┣ 📜locals.tf
┃ ┃ ┃ ┣ 📜output.tf
┃ ┃ ┃ ┣ 📜pro.tfvars
┃ ┃ ┃ ┣ 📜provider.tf
┃ ┃ ┃ ┗ 📜variables.tf
┃ ┃ ┗ 📂iam
┃ ┃ ┃ ┣ 📜aws_iam_role_eventbridge.tf
┃ ┃ ┃ ┣ 📜aws_iam_role_glue.tf
┃ ┃ ┃ ┣ 📜aws_iam_role_lambda.tf
┃ ┃ ┃ ┣ 📜aws_iam_role_stepfunction.tf
┃ ┃ ┃ ┣ 📜backend.tf
┃ ┃ ┃ ┣ 📜dev.tfvars
┃ ┃ ┃ ┣ 📜locals.tf
┃ ┃ ┃ ┣ 📜outputs.tf
┃ ┃ ┃ ┣ 📜pro.tfvars
┃ ┃ ┃ ┣ 📜provider.tf
┃ ┃ ┃ ┗ 📜variables.tf
┣ 📜.gitignore
┣ 📜README.md
┣ 📜sonar-project.properties
┗ 📜tox.ini
```