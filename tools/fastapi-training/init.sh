#!/bin/bash
# Levantar los servicios con Docker Compose
docker-compose up -d

echo "Ejecutando generate_data.py en data-loader..."
docker-compose exec -t data-loader python generate_data.py

echo "Ejecutando generate_users.py en data-loader..."
docker-compose exec -t data-loader python generate_users.py

echo "Ejecutando sqlacodegen para generar los pre-modelos..."
sqlacodegen_v2 --generator declarative-dataclasses postgresql://myuser:mypassword@localhost:5432/mydatabase > app/modules/models_gen.py

echo "Proceso completado. Revisa "app/modules/models_gen.py" para ver los modelos generados."