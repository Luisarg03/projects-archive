################################
### GLUE JOBS EXECUTION ROLE ###
################################
resource "aws_iam_role" "glue" {
  name = "project-${var.environment}-glue-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "glue.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "glue" {
  name = "project-${var.environment}-glue-policies"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "glue:RunJob",
          "glue:GetJobRun",
          "glue:GetJobRuns",
          "glue:GetJobs"
        ]
        Resource =  [
           for jobs in local.glue_jobs : "arn:aws:glue:${local.region}:${local.account_id}:job/${jobs}"
        ]
      },
      {
        Effect = "Allow",
        Action = [
          "s3:GetObject",
          "s3:GetBucketAcl",
          "s3:ListBucket",
          "s3:ListObjects",
          "s3:ListObjectsV2",
          "s3:PutObject",
          "s3:PutObjectAcl",
          "s3:DeleteObject"
        ],
        Resource = flatten([
          for bucket_name in local.buckets : [
            "arn:aws:s3:::${bucket_name}-${local.region}-${local.account_id}-${var.environment}",
            "arn:aws:s3:::${bucket_name}-${local.region}-${local.account_id}-${var.environment}/*"
          ]
        ])
      },
      {
        Effect = "Allow",
        Action = [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
        ],
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "glue" {
  policy_arn = aws_iam_policy.glue.arn
  role       = aws_iam_role.glue.name
}