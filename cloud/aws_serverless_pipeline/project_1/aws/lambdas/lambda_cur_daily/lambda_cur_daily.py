import json
from common.helpers_functions import configure_logging


def lambda_handler(event, context):
    root_logger = configure_logging()

    root_logger.info(f"Event: {json.dumps(event)}")

    BUCKET_NAME = event['BUCKET_DATA']
    OPERATION = event['PARAMETERS']['OPERATION']
    TABLE = event['PARAMETERS']['TABLE']

    root_logger.info(f'OPERATION: {OPERATION}')
    root_logger.info(f'BUCKET_NAME: {BUCKET_NAME}')
    root_logger.info(f'TABLE: {TABLE}')

    return {
        'statusCode': 200,
        'body': json.dumps('ok')
    }