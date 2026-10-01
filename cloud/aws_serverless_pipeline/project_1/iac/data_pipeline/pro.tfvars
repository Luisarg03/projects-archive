project_name = "project_1"
environment = "prod"
artifacts_buckets_name = "project-artifacts"
data_buckets_name = "project-data"
ml_buckets_name = "project-ml"
logs_buckets_name = "project-logs"


#############
### ROLES ###
#############
lambda_role = "project-dev-lambda-role"
stepfunctions_role = "project-dev-stepfunctions-role"
eventbridge_role = "project-dev-eventbridge-role"


##################################
### ADD NEW LAMBDAS NAMES HERE ###
##################################
# VIEW "aws_lambda.tf" -> data "archive_file" "create_lambdas_zip"
lambdas_names = [
  "lambda_raw_daily",
  "lambda_cur_daily",
  "project_logswriter"
]


# ############
# LAMBDAS VARS
# ############
lambdas_global_vars = {
  project_logswriter = {
    function_name = "project_logswriter"
    description = "Catch logs from CLoudWatch and write on S3."
    data_code = "project_logswriter"
    handler = "project_logswriter.lambda_handler"
    architectures = "arm64"
    memory_size = 256
    runtime = "python3.9"
    timeout = 180
    }
}

# TRIGGER: EVENTBRIDGE CRON. VIEW FILE "aws_eventbridge.tf" + " aws/events_bridge/* "
lambdas_project_vars = {
  lambda_raw_daily = {
    function_name = "lambda_raw_daily"
    description = "Extract data from Wellington API REST"
    data_code = "lambda_raw_daily"
    handler = "lambda_raw_daily.lambda_handler"
    architectures = "arm64"
    memory_size = 10240
    runtime = "python3.9"
    timeout = 180
    layers_1 = "arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python39-Arm64:3"
  },
  lambda_cur_daily = {
    function_name = "lambda_cur_daily"
    description = "Extract data from Wellington raw zone and transform data into cur zone"
    data_code = "lambda_cur_daily"
    handler = "lambda_cur_daily.lambda_handler"
    architectures = "arm64"
    memory_size = 10240
    runtime = "python3.9"
    timeout = 180
    layers_1 = "arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python39-Arm64:3"
  }
}


# ##############
# GLUE VARS JOBS
# ##############
glue_jobs_vars = {
  glue_jobs_1 = {
    name = "glue_jobs_1"
    script_location = "pythonshell/glue_jobs_1/glue_jobs_1"
    command_name = "glueetl"
    max_retries = 0
    timeout = 15

    glue_version = "4.0"
    command_python_version = "3"
    worker_type = "G.2X"
    number_workers = 2
    max_concurrent_runs = 1
    args = {
      "--job-language" = "python"
      "--job-bookmark-option" = "job-bookmark-disable"
      "--enable-continuous-cloudwatch-log" = "false"
      "--enable-continuous-log-filter" = "false"
      "--enable-glue-datacatalog" = "false"
      
      "--additional-python-modules" = "awswrangler==3.1.1"
    }
  },
  glue_jobs_2 = {
    name = "glue_jobs_2"
    script_location = "pythonshell/glue_jobs_2/glue_jobs_2"
    command_name = "glueetl"
    max_retries = 0
    timeout = 15

    glue_version = "4.0"
    command_python_version = "3"
    worker_type = "G.4X"
    number_workers = 2
    max_concurrent_runs = 1

    args = {
      "--job-language" = "python"
      "--job-bookmark-option" = "job-bookmark-disable"
      "--enable-continuous-cloudwatch-log" = "false"
      "--enable-continuous-log-filter" = "false"
      "--enable-glue-datacatalog" = "false"
      
      "--additional-python-modules" = "awswrangler==3.1.1"
    }
  }
}