from modules.confs import PipelineConfig
from modules.pandas_tables import PandasTables
from modules.parser_data import ParserData
from modules.cloudwatch import LogsProcess
from modules.get_costs import GetCosts

from ui.control import UiController
import streamlit as st

if __name__ == "__main__":
    csv_instance_csv = '../InstancesUseUSD.csv'
    log_group_name = "/aws/sagemaker/ProcessingJobs"

    pipeline_config = PipelineConfig(csv_instance_data=csv_instance_csv)
    pipelines = pipeline_config.list_pipelines()
    instance_data = pipeline_config.instance_data

    ui = UiController()
    parser = ParserData()
    logs = LogsProcess()

    if pipelines:
        try:
            # Available Pipelines list
            selected_pipeline = ui.selectbox_pipeline(pipelines)
            executions = pipeline_config.get_pipeline_executions(selected_pipeline)

            # Execution ARNs Table
            df_pipeline_arns = PandasTables(executions).json_to_dataframe()
            ui.render_table(df_pipeline_arns)

            # Select Execution ARN
            arn = ui.selectbox_arn(df_pipeline_arns, 'PipelineExecutionArn')

            # Processing JobsName Table
            list_steps_data = parser.get_proccesing_jobs(arn)
            df_list_steps = PandasTables(list_steps_data).json_to_dataframe()

            ui.render_table(df_list_steps)

            # Select JobName
            step = ui.selectbox_arn(df_list_steps, 'JobName')

            col1, col2 = st.columns(2)

            with col1:
                # Jobs Details Instances
                job_details = parser.get_job_details(step)
                cost = GetCosts(instance_data).get_costs(job_details, df_list_steps, step)
                job_details['TotalCost'] = cost
                ui.job_details_area(job_details)

            with col2:
                # Show Logs
                log_id = logs.get_log_streams(log_group_name, step)
                filter_log_events = logs.get_filter_log_events(log_group_name, log_id)
                complete_log_events = logs.get_log_events(log_group_name, log_id)
                ui.text_area_logs(filter_log_events, "Resume Job Logs")
                ui.download_logs(filter_log_events, step, "Resume Job Logs")
                ui.download_logs(complete_log_events, step, "Complete Job Logs")

            # Show Metrics
            try:
                metrics = logs.get_metrics(step, df_list_steps, job_details)
                metrics = PandasTables(None).metrics_dataframe(metrics, instance_data, job_details)
            except Exception as e:
                st.write(f"Error: {e}")
                metrics = None

            if metrics is not None:
                ui.render_metrics(metrics)
            else:
                st.write("Metrics not available")

        except Exception as e:
            st.write(f"Error: {e}")
            st.write("No pipeline executions available")

    else:
        st.write("No pipeline executions available")
