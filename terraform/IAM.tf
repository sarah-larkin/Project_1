#Lambda IAM role

#Define Lambda trust relationship
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

#create role
resource "aws_iam_role" "lambda" {
  name               = "lambda_role" #TODO: check for name prefix instead 
  path               = "/" #TODO: check this required 
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
}


#This won't have any effect yet 
