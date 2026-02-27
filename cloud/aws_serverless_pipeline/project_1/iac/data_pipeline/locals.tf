data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

###################
### LOCALS VARS ###
###################
locals {
  account_id = data.aws_caller_identity.current.account_id
  region = data.aws_region.current.name
  path_base = "../../aws"
  lambdas_names = toset(var.lambdas_names)

  ###############################
  ### ADD NEW STATES MACHINES ###
  ###############################
  state_machine_configs = [
      for file in fileset("${local.path_base}/stepfunctions", "*.json") :
      {
          name = replace(file, ".json", "")
          config = jsondecode(
                      templatefile("${local.path_base}/stepfunctions/${file}", {
                          env = var.environment,
                          id_env = "${data.aws_caller_identity.current.account_id}",
                          region = "${data.aws_region.current.name}"
                      }
                  )
              )
      }
  ]

  ####################################
  ### ADD NEW EVENTSBRIDGE CONFIGS ###
  ####################################
  event_rule_configs = [
      for file in fileset("${local.path_base}/events_bridge", "*.json") :
      {
          name = replace(file, ".json", "")
          config = jsondecode(
                      templatefile("${local.path_base}/events_bridge/${file}", { 
                          env = var.environment,
                          id_env = "${data.aws_caller_identity.current.account_id}",
                          region = "${data.aws_region.current.name}"
                      }
                  )
              )
      }
  ]

}