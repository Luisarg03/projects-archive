import json
import base64
import gzip
import pytest
from unittest.mock import patch
from project_logswriter.project_logswriter import lambda_handler


def test_lambda_handler(mocker):
    # Mockear la función boto3.client
    s3_mock = mocker.patch('boto3.client', autospec=True)
    
    # Crear una instancia simulada para s3.put_object
    put_object_mock = s3_mock.return_value.put_object

    # Mockear la función os.getenv
    getenv_mock = mocker.patch('os.getenv', return_value='bucket-region-id-dev')

    event = {
        'awslogs': {
            'data': base64.b64encode(gzip.compress(json.dumps({
                'logGroup': '/test/log/group',
                'logStream': 'test/log/stream',
                'events': [
                    {
                        'id': 'event1',
                        'timestamp': 123456789,
                        'message': 'test message 1',
                        'ingestionTime': 987654321
                    }
                ]
            }).encode('utf-8'))).decode('utf-8')
        }
    }

    lambda_handler(event, '')
    
    # Asegurarse de que se haya llamado a put_object
    assert put_object_mock.called
    # Verificar los argumentos que recibió put_object
    call_args = put_object_mock.call_args[1]
    assert call_args['Bucket'] == 'bucket-region-id-dev'
    assert 'test/log/group' in call_args['Key']
    assert 'test_log_stream' in call_args['Key']

    # Asegurarse de que se haya llamado a getenv con el argumento correcto
    getenv_mock.assert_called_once_with('BUCKET_LOGS')