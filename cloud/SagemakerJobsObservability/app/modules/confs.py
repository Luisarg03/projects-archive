import boto3
import pandas as pd


class PipelineConfig:
    def __init__(self, csv_instance_data):
        self.instance_data = self._load_instances_type(csv_instance_data)
        self.sagemaker_client = boto3.client('sagemaker')

    def list_pipelines(self):
        pipeline_names = []
        next_token = None

        while True:
            if next_token:
                response = self.sagemaker_client.list_pipelines(NextToken=next_token)
            else:
                response = self.sagemaker_client.list_pipelines()

            pipeline_names.extend([pipeline['PipelineName'] for pipeline in response['PipelineSummaries']])

            next_token = response.get('NextToken')
            if not next_token:
                break

        return pipeline_names

    def _load_instances_type(self, csv_instance_data):
        return pd.read_csv(csv_instance_data)

    def get_pipeline_executions(self, pipeline_name):
        response = self.sagemaker_client.list_pipeline_executions(
            PipelineName=pipeline_name
        )

        return response.get('PipelineExecutionSummaries', [])
