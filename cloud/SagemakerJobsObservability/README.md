# SageMaker Pipelines Monitoring

Este proyecto es una aplicación web desarrollada en Streamlit para monitorear pipelines de procesamiento de datos en AWS SageMaker. Proporciona una interfaz de usuario para visualizar detalles de las ejecuciones de pipelines, los costos asociados y los logs de procesamiento.

## Características

- **Selección de Pipelines**: Listado de los pipelines disponibles para su monitoreo.
- **Visualización de Ejecuciones**: Tabla con las ejecuciones del pipeline seleccionado.
- **Selección de Ejecuciones**: Opción para seleccionar un ARN de ejecución y ver los detalles.
- **Monitoreo de Jobs**: Desglose de los jobs de procesamiento asociados a cada ejecución.
- **Visualización de Logs**: Visualización y descarga de logs de los jobs.
- **Cálculo de Costos**: Estimación de los costos de los jobs basados en el uso de instancias.
- **Visualización de Métricas**: Presentación de métricas asociadas a los jobs.

## Requisitos

Para ejecutar este proyecto localmente, asegúrate de tener instalado lo siguiente:

- Python 3.12+
- Streamlit
- Boto3
- Pandas

Puedes instalar las dependencias utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Archivos Principales

- `app.py`: El archivo principal que ejecuta la aplicación y conecta los diferentes componentes.
- `modules/confs.py`: Maneja la configuración del pipeline y los datos de las instancias.
- `modules/pandas_tables.py`: Convierte los datos de JSON a DataFrames para su visualización.
- `modules/parser_data.py`: Procesa los datos y extrae la información necesaria de los jobs.
- `modules/cloudwatch.py`: Obtiene logs y métricas desde AWS CloudWatch.
- `modules/get_costs.py`: Calcula los costos basados en el uso de instancias.

## Uso

1. Ejecuta la aplicación con Streamlit:

```bash
streamlit run app.py
```

1. Selecciona el pipeline que deseas monitorear.
2. Sube un archivo CSV con los datos de uso de instancias actualizados (`InstancesUseUSD.csv`).
3. Visualiza los detalles del pipeline y los jobs asociados.
4. Revisa los logs y las métricas para cada job.

## Estructura de Archivos

``` python
├── app.py
├── modules
│   ├── confs.py
│   ├── pandas_tables.py
│   ├── parser_data.py
│   ├── cloudwatch.py
│   └── get_costs.py
├── ui
│   └── control.py
└── InstancesUseUSD.csv
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más información, consulta el archivo `LICENSE`
