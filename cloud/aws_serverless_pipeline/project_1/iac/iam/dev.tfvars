project_name = "_project"
environment = "dev"

##################################
### ADD NEW BUCKETS NAMES HERE ###
##################################
buckets_names = [
    "project-data",
    "project-ml",
    "project-logs",
    "project-artifacts"
]

##################################
### ADD NEW LAMBDAS NAMES HERE ###
##################################
lambdas_names = [
    "project_raw_daily",
    "project_cur_daily",
    "project_logswriter"
]

#############################
### ADD NEW SM NAMES HERE ###
#############################
states_machines_names = [
    "sm-project"
]

######################################
### ADD NEW EVENT RULES NAMES HERE ###
######################################
events_rules_names = [
    "event-rule-sm-project"
]

############################
## ADD NEW GLUE JOBS HERE ##
############################
glue_jobs_names = [
    "glue_jobs_1",
    "glue_jobs_2"
]