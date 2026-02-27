import streamlit as st
from datetime import datetime


class UiController:
    def __init__(self):
        st.set_page_config(layout="wide")

    def render_table(self, df):
        status_colors = {
            "InProgress": "#3691e1",
            "Executing": "#3691e1",
            "Completed": "#4CAF50",
            "Succeeded": "#4CAF50",
            "Failed": "#F44336",
            "Stopped": "#E9EFEC",
            "Stopping": "#E9EFEC"
        }

        # Aplicar colores basados en el estado
        def color_status(val):
            color = status_colors.get(val, '')
            return f'color: {color}; font-weight: bold; border: 1px solid {color}; padding: 5px;' if color else ''

        # Verificar si la columna que contiene los estados está presente
        if 'PipelineExecutionStatus' in df.columns:
            df = df.style.applymap(color_status, subset=['PipelineExecutionStatus'])
        elif 'StepStatus' in df.columns:
            df = df.style.applymap(color_status, subset=['StepStatus'])

        st.table(df)

    def selectbox_pipeline(self, pipelines):
        pipelines = st.selectbox("Select Pipeline:", pipelines)

        if pipelines:
            st.title(pipelines)
            if st.button("Actualizar datos"):
                st.cache_data.clear()
                st.rerun()
            return pipelines
        else:
            return None

    def selectbox_arn(self, df, colname):
        msg_execution = "Select PipelineExecutionArn"
        msg_job = "Select JobName"
        if colname == 'PipelineExecutionArn':
            st.subheader(msg_execution)
        else:
            st.subheader(msg_job)

        execution_arns = df[colname].tolist()
        selected_arn = st.selectbox(label="arns", label_visibility="hidden", options=execution_arns)

        if selected_arn:
            return selected_arn
        else:
            return None

    def job_details_area(self, job_details):
        st.markdown("""
            <style>
            .fake-button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 15px;
                color: black;
                font-weight: bold;
                background-color: #ECEFF1;
                border: none;
                border-radius: 5px;
                text-align: center;
                cursor: default;
                user-select: none;
                margin: 4px 0;
            }

            .state-button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 15px;
                color: white;
                font-weight: bold;
                border: 2px solid #7d7e8c;
                border-radius: 5px;
                text-align: center;
                cursor: default;
                user-select: none;
                margin: 4px 0;
            }
            </style>
            """, unsafe_allow_html=True)

        status_colors = {
            "InProgress": "#3691e1",
            "Completed": "#4CAF50",
            "Failed": "#F44336",
            "Stopped": "#2d303b",
            "Stopping": "#2d303b"
        }

        st.subheader("Job Details")

        # Mostrar los identificadores y valores en columnas
        col1, col2 = st.columns([1, 3])

        with col1:
            st.text("InstanceType")
        with col2:
            st.markdown(f"<div class='fake-button'>{str(job_details.get('InstanceType'))}</div>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])
        with col1:
            st.text("InstanceCount")
        with col2:
            st.markdown(f"<div class='fake-button'>{str(job_details.get('InstanceCount'))}</div>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])
        with col1:
            st.text("InstanceVolumeSizeInGB")
        with col2:
            st.markdown(f"<div class='fake-button'>{str(job_details.get('InstanceVolumeSizeInGB'))}</div>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])
        with col1:
            st.text("TotalCost")
        with col2:
            st.markdown(f"<div class='fake-button'>{str(job_details.get('TotalCost'))} USD</div>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])
        processing_status = job_details.get('ProcessingJobStatus')
        color = status_colors.get(processing_status, None)
        with col1:
            st.text("ProcessingJobStatus")
        with col2:
            st.markdown(f"<div class='state-button' style='background-color:{color}'>{processing_status}</div>", unsafe_allow_html=True)

    def text_area_logs(self, logs, tittle):
        st.subheader(tittle)
        logs_container = st.container(height=300, border=True)
        logs_container.info(logs)

    def download_logs(self, logs, step, tittle):
        st.download_button(
            label=f"Download {tittle}",
            data=logs,
            file_name=f'LOG_{step}_{datetime.now().isoformat()}.txt'
        )

    def costs_area(self, costs, job_details):
        st.subheader("Costs")
        st.write(f"Cost per hour: {costs}")
        st.write(f"Total cost: {costs * job_details.get('InstanceCount')}")

    def render_metrics(self, metrics):
        st.subheader("Memory Utilization")
        memory_df = metrics[metrics['Metric'].str.contains('memoryUtilization')]
        st.line_chart(memory_df.pivot(index='Timestamp', columns='Host', values='Value'), use_container_width=True)

        st.subheader("CPU Utilization")
        cpu_df = metrics[metrics['Metric'].str.contains('cpuUtilization')]
        st.line_chart(cpu_df.pivot(index='Timestamp', columns='Host', values='Value'), use_container_width=True)

        st.subheader("Disk Utilization")
        disk_df = metrics[metrics['Metric'].str.contains('diskUtilization')]
        st.line_chart(disk_df.pivot(index='Timestamp', columns='Host', values='Value'), use_container_width=True)
