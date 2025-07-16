#Lambda IAM role
#--------------------

#Define Lambda trust policy
data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    effect = "Allow" 

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

#create IAM role
resource "aws_iam_role" "lambda" {
  name_prefix        = "lambda_role-" 
  path               = "/" 
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
}


#S3 Access 
#-------------------------

# define IAM permissions policy document with s3 access (JSON)
#(aws_iam_policy_document) 

data "aws_iam_policy_document" "lambda_s3_access" {
  statement {
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:DeleteObject",
      "s3:ListBucket",
    ]
    resources = [
      aws_s3_bucket.ingestion_bucket.arn,          #access to the bucket (needed to list objects)
      "${aws_s3_bucket.ingestion_bucket.arn}/*",   #access to objects inside the bucket (needed to get/put ie. read/write objects in the bucket)
      aws_s3_bucket.processed_bucket.arn,         
      "${aws_s3_bucket.processed_bucket.arn}/*"  
    ]
  }
}

# create IAM policy resource for Lambda s3 access 
#(aws_iam_policy)
resource "aws_iam_policy" "s3_policy" {
  name_prefix   = "lambda_s3_policy"
  policy        = data.aws_iam_policy_document.lambda_s3_access
}


#attach s3 access policy to the lambda IAM role 
#(aws_iam_role_policy_attachment)
resource "aws_iam_role_policy_attachment" "s3_policy_attachment"{
  role       = aws_iam_role.lambda.name
  policy_arn = aws_iam_policy.s3_policy.arn 
}