import boto3
import datetime
import pandas as pd
import numpy as np


class LogsProcess():
    def __init__(self):
        self.logs_client = boto3.client('logs')
        self.cloudwatch_client = boto3.client('cloudwatch')

    def get_log_streams(self, log_group_name, job_name):
        """
        Retrieves the log stream name for a given log group and job name.
        Parameters
        ----------
        log_group_name : str
            The name of the CloudWatch log group.
        job_name : str
            The name of the job for which to retrieve the log stream.
        Returns
        -------
        str or None
            The name of the log stream if found, otherwise None.
        """

        job_name = f'{job_name}/algo-1'

        response = self.logs_client.describe_log_streams(
            logGroupName=log_group_name,
            logStreamNamePrefix=job_name
        )

        try:
            response = response.get('logStreams', [])[0].get('logStreamName')
        except IndexError:
            response = None

        return response

    def get_log_events(self, log_group_name, log_stream_name):
        """
        Retrieves log events from a specified CloudWatch log group and log stream.
        Parameters
        ----------
        log_group_name : str
            The name of the CloudWatch log group.
        log_stream_name : str
            The name of the CloudWatch log stream.
        Returns
        -------
        str
            A string containing the concatenated log messages from the specified log stream.
            If an exception occurs, returns a message indicating that no logs are available.
        """

        try:
            response = self.logs_client.get_log_events(
                logGroupName=log_group_name,
                logStreamName=log_stream_name,
                limit=5000,
                startFromHead=True
            )

            messages = [event['message'] for event in response['events']]
            messages = '\n'.join(messages)

        except Exception as e:
            messages = "Logs not available..."

        return messages

    def get_filter_log_events(self, log_group_name, log_stream_name):
        """
        Retrieves and filters log events from a specified CloudWatch log group and log stream.
        Parameters
        ----------
        log_group_name : str
            The name of the CloudWatch log group.
        log_stream_name : str
            The name of the CloudWatch log stream.
        Returns
        -------
        str
            A string containing the filtered log messages, concatenated by newlines.
            If an exception occurs, returns a message indicating that no logs are available.
        Raises
        ------
        Exception
            If there is an error in retrieving or filtering the log events.
        """

        patterns = [
            'FromScript',
            'Traceback',
            'Caused',
            '__main__'
        ]

        patterns = ' '.join([f'?{pattern}' for pattern in patterns])

        try:
            response = self.logs_client.filter_log_events(
                logGroupName=log_group_name,
                logStreamNames=[log_stream_name],
                filterPattern=patterns
            )

            messages = [event['message'] for event in response['events']]
            messages = '\n'.join(messages)

        except Exception as e:
            messages = "Logs not available..."

        return messages

    def get_metrics(self, job_name, job_data, job_details):
        """
        Retrieves CloudWatch metrics for a given SageMaker job.
        Parameters
        ----------
        job_name : str
            The name of the SageMaker job.
        job_data : pandas.DataFrame
            DataFrame containing job data, including 'JobName', 'StartTime', and 'EndTime' columns.
        job_details : dict
            Dictionary containing job details, including 'InstanceCount'.
        Returns
        -------
        list
            A list of dictionaries containing the CloudWatch metric data for each thread.
        """

        threads = [x for x in range(1, job_details.get('InstanceCount') + 1)]
        start_time = job_data.loc[job_data['JobName'] == job_name, 'StartTime'].values[0]
        end_time = job_data.loc[job_data['JobName'] == job_name, 'EndTime'].values[0]

        if end_time is None or pd.isna(end_time):
            end_time = datetime.datetime.now()
            end_time = end_time.astimezone(datetime.timezone.utc)

        if isinstance(start_time, np.datetime64):
            start_time = pd.to_datetime(start_time).to_pydatetime()

        if isinstance(end_time, np.datetime64):
            end_time = pd.to_datetime(end_time).to_pydatetime()

        metrics = []

        for thread in threads:
            response = self.cloudwatch_client.get_metric_data(
                MetricDataQueries=[
                    {
                        'Id': f'memoryUtilization{thread}',
                        'MetricStat': {
                            'Metric': {
                                'Namespace': '/aws/sagemaker/ProcessingJobs',
                                'MetricName': 'MemoryUtilization',
                                'Dimensions': [
                                    {
                                        'Name': 'Host',
                                        'Value': f'{job_name}/algo-{thread}'
                                    },
                                ]
                            },
                            'Period': 60,
                            'Stat': 'Average',
                            'Unit': 'Percent'
                        },
                        'ReturnData': True,
                    },
                    {
                        'Id': f'cpuUtilization{thread}',
                        'MetricStat': {
                            'Metric': {
                                'Namespace': '/aws/sagemaker/ProcessingJobs',
                                'MetricName': 'CPUUtilization',
                                'Dimensions': [
                                    {
                                        'Name': 'Host',
                                        'Value': f'{job_name}/algo-{thread}'
                                    },
                                ]
                            },
                            'Period': 60,
                            'Stat': 'Average',
                            'Unit': 'Percent'
                        },
                        'ReturnData': True,
                    },
                    {
                        'Id': f'diskUtilization{thread}',
                        'MetricStat': {
                            'Metric': {
                                'Namespace': '/aws/sagemaker/ProcessingJobs',
                                'MetricName': 'DiskUtilization',
                                'Dimensions': [
                                    {
                                        'Name': 'Host',
                                        'Value': f'{job_name}/algo-{thread}'
                                    },
                                ]
                            },
                            'Period': 60,
                            'Stat': 'Average',
                            'Unit': 'Percent'
                        },
                        'ReturnData': True,
                    },
                ],
                StartTime=start_time,
                EndTime=end_time,
            )

            response['thread'] = f'{job_name}/algo-{thread}'

            metrics.append(response)

        return metrics
