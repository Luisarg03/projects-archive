import re
import json
import warnings
import pandas as pd


class PandasTables:
    def __init__(self, json_data):

        self.json_data = json_data
        self.df = None

        warnings.simplefilter(action='ignore', category=FutureWarning)

    def json_to_dataframe(self):

        try:
            if isinstance(self.json_data, str):
                self.json_data = json.loads(self.json_data)

            if isinstance(self.json_data, list):
                self.df = pd.DataFrame(self.json_data)

            elif isinstance(self.json_data, dict):
                self.df = pd.DataFrame([self.json_data])

        except ValueError as e:
            print(f"Error al convertir JSON a DataFrame: {e}")
            return None

        return self.df

    def metrics_dataframe(self, data, instance_data, job_details):
        self.df = pd.DataFrame(columns=['Timestamp', 'Host', 'Metric', 'Value'])
        virtual_cpu = instance_data.loc[instance_data['Instancias'] == job_details.get('InstanceType'), 'CPUvirtual'].values[0]

        list_df = []

        for response in data:
            for result in response['MetricDataResults']:
                metric_name = result['Id']
                if result['Values']:
                    for i in range(len(result['Timestamps'])):
                        df = self.df._append({
                            'Timestamp': result['Timestamps'][i],
                            'Host': response['thread'],
                            'Metric': metric_name,
                            'Value': result['Values'][i]
                        }, ignore_index=True)

                        list_df.append(df)

        df = pd.concat(list_df)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        try:
            df['Value'] = df.apply(
                lambda row: (row['Value'] / (virtual_cpu * 100)) * 100 if re.search('cpuUtilization', row['Metric']) else row['Value'],
                axis=1
            )
        except ValueError:
            pass

        return df
