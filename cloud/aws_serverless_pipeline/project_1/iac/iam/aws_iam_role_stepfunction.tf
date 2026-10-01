############################
### STATES MACHINES ROLE ###
############################
resource "aws_iam_role" "stepfunctions" {
  name = "project-${var.environment}-stepfunctions-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "states.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "stepfunctions" {
  name = "project-${var.environment}-stepfunctions-policies"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "states:CreateStateMachine",
          "states:UpdateStateMachine"
        ]
        Resource = [
          for sm_name in local.states_machines : "arn:aws:states:${local.region}:${local.account_id}:stateMachine:${sm_name}"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "lambda:InvokeFunction"
        ]
        Resource = [
          for function_name in local.lambdas : "arn:aws:lambda:${local.region}:${local.account_id}:function:${function_name}"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "glue:StartJobRun",
          "glue:GetJobRun"
        ]
        Resource = [
          for job_name in local.glue_jobs : "arn:aws:glue:${local.region}:${local.account_id}:job/${job_name}"
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "stepfunctions" {
  policy_arn = aws_iam_policy.stepfunctions.arn
  role = aws_iam_role.stepfunctions.name
}