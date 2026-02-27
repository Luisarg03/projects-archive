# ################
# # GENERAL VARS #
# ################
variable "environment" {
  default = ""
}

variable "project_name" {
  default = ""
}

# ######################
# # BUCKETS NAMES VARS #
# ######################
variable "artifacts_buckets_name" {
  default = ""
}

variable "data_buckets_name" {
  default = ""
}

variable "ml_buckets_name" {
  default = ""
}

variable "logs_buckets_name" {
  default = ""
}

# ####################
# # ROLES NAMES VARS #
# ####################
variable "lambda_role" {
  default = ""
}

variable "stepfunctions_role" {
  default = ""
}

variable "eventbridge_role" {
  default = ""
}

# ################
# # LAMBDAS VARS #
# ################
variable "lambdas_names" {
  description = "Lambdas names to zip"
  default = []
}

variable "lambdas_global_vars" {
  description = ""
  type = map(any)
}

variable "lambdas_project_vars" {
  description = "lamda parameters"
  type        = map(any)
}

# #############
# # GLUE VARS #
# #############
variable "glue_jobs_vars" {
  description = "glue jobs parameters"
  type        = map(any)
}

variable "glue_python_shell_vars" {
  description = "glue pythonshell parameters"
  type        = map(any)
}