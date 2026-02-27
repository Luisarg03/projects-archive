import boto3
import datetime


class ParserData:
    def __init__(self):

        self.sagemaker_client = boto3.client('sagemaker')

    def get_proccesing_jobs(self, PipelineExecutionArn):
        response = self.sagemaker_client.list_pipeline_execution_steps(
            PipelineExecutionArn=PipelineExecutionArn,
        )

        response = response.get('PipelineExecutionSteps')

        list_steps_data = []

        for step in response:

            try:
                JobName = step.get('Metadata').get('ProcessingJob').get('Arn')
                JobName = JobName.split('/')[-1]
            except AttributeError:
                continue

            try:
                time_elapsed = step.get('EndTime') - step.get('StartTime')
            except TypeError:
                end_time = datetime.datetime.now()
                end_time = end_time.astimezone(datetime.timezone.utc)
                time_elapsed = end_time - step.get('StartTime')

            step_data = dict(
                StepName=step.get('StepName'),
                JobName=JobName,
                StartTime=step.get('StartTime'),
                EndTime=step.get('EndTime'),
                TimeElapsed=time_elapsed,
                StepStatus=step.get('StepStatus')
            )

            list_steps_data.append(step_data)

        return list_steps_data

    def get_job_details(self, JobName):
        response = self.sagemaker_client.describe_processing_job(
            ProcessingJobName=JobName
        )

        job_details = dict(
            InstanceType=response['ProcessingResources']['ClusterConfig']['InstanceType'],
            InstanceCount=response['ProcessingResources']['ClusterConfig']['InstanceCount'],
            InstanceVolumeSizeInGB=response['ProcessingResources']['ClusterConfig']['VolumeSizeInGB'],
            ProcessingJobStatus=response['ProcessingJobStatus']
        )

        return job_details
