#LAMBDA CREATION 

data "archive_file" "lambda" {
  type        = "zip"
  source_dir = "${path.module}/../src/lambda_handler"  #source_dir  - zips everything in the lambda_handler folder
  output_path = "${path.module}/../deployment/handlers.zip" # folder must already exist (mkdir -p  deployment/handlers) #TODO: add this to CI/CD?
}
#must have installed requirements before zipping - lambda does not install packages from requirements.txt 
#(to install the packages run pip install -r requirements.txt -t dependencies/packages)

#create the Lambda
resource "aws_lambda_function" "extract_lambda" {
  filename      = "${path.module}/../deployment/handlers/lambda_handlers.zip" # check path 
  function_name = "extract_lambda_function"  #could make a variable? 
  role          = aws_iam_role.lambda.arn 
  handler       = "extract.lambda_handler"  
  runtime       = var.python_runtime
#   timeout       = 900
#   memory_size   = 3000

  environment {
    variables = {
      FILES_BUCKET = aws_s3_bucket.files.bucket
      S3_INGESTION_BUCKET = aws_s3_bucket.ingestion_bucket.bucket
    }
  }
}


