import numpy as np


class GetCosts:
    def __init__(self, cost_file):
        self.cost_file = cost_file

    def get_costs(self, job_details, df_list_steps, step):
        instance_type = job_details.get('InstanceType')
        value = self.cost_file[self.cost_file['Instancias'] == instance_type]['PrecioHora'].values[0]
        usd = float(value.replace('USD', '').replace(",", "."))
        step_time = df_list_steps[df_list_steps['JobName'] == step]['TimeElapsed'].values[0]

        time_in_hours = step_time / np.timedelta64(1, 'h')

        total_cost = usd * time_in_hours * job_details.get('InstanceCount')
        total_cost = round(total_cost, 2)

        return total_cost
