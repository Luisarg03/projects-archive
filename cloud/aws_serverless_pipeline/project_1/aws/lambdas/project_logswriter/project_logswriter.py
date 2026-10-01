import os
import boto3
import gzip
import base64
import json
import re
import datetime


def lambda_handler(event, context):
    BUCKET_LOGS = os.getenv('BUCKET_LOGS')

    s3 = boto3.client('s3')
    compressed_data = base64.b64decode(event['awslogs']['data'])
    uncompressed_data = gzip.decompress(compressed_data)

    logs = json.loads(uncompressed_data)
    print('LOG:', logs)

    # Obten el nombre del grupo de logs
    log_group = logs['logGroup']
    log_group = log_group.lstrip('/')
    # print('LOG GROUP:', log_group)

    log_stream = logs['logStream']
    # Reemplaza los caracteres especiales
    log_stream = re.sub(r'[/$\[\]]', '_', log_stream)

    # Obten un sello de tiempo formateado
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")[:-3]

    logs = json.dumps(logs)
    
    # Escribe los logs en S3
    s3.put_object(
        Body=logs,
        Bucket=BUCKET_LOGS,
        Key=f'{log_group}/{log_stream}_{timestamp}.json'
    )