#!/bin/bash

set -e

lambdas_names=(
  "project_raw_daily"
  "project_cur_daily"
)

for lambda_name in "${lambdas_names[@]}"; do
  cp -r ../../aws/lambdas/common/ ../../aws/lambdas/${lambda_name}/common/
  echo "Carpeta 'common' copiada en la carpeta ${lambda_name}"
  echo "Contenido de la carpeta ${lambda_name}:"
  ls ../../aws/lambdas/${lambda_name}/
  echo ""
done