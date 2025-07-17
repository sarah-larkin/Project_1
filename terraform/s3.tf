#no live db so creating bucket to store data which lambda can access 
resource "aws_s3_bucket" "files" {
  bucket_prefix = var.files_prefix

  tags = {
    Name        = "file-storage-bucket"
    Environment = var.environment
  }
}

output "files_bucket"{                         #keeps name dynamic if bucket name (suffix) is ever changed (good practice for CI/CD pipelines)
  value = aws_s3_bucket.files.bucket
}

#ingestion bucket for raw data
resource "aws_s3_bucket" "ingestion_bucket" {
  bucket_prefix = var.S3_ingestion_prefix

  tags = {
    Name        = "ingestion bucket"
    Environment = var.environment
  }
}

#processed bucket for cleaned data
resource "aws_s3_bucket" "processed_bucket" {
  bucket_prefix = var.S3_processed_prefix

  tags = {
    Name        = "processed bucket"
    Environment = var.environment
  }
}

#-----------------------------------------------------
#S3 Object 

#to make the data files initially available in the files s3 bucket: 
#use: cp --recursive, sync or just cp 

#use cp to upload a single doc: 
#aws s3 cp /home/slark/DE-projects/Project_1/data/colors.csv s3://project-files-20250717160548064700000001 

#use cp --recusive for uploading all files in a folder 
#aws s3 cp /home/slark/DE-projects/Project_1/data/ s3://project-files-20250717160548064700000001/project-1/ --recursive

#use sync to keep s3 in sync with your local files, will only upload changes
#aws s3 sync /home/slark/DE-projects/Project_1/data/ s3://project-files-20250717160548064700000001/project-1/ 
#trailing / after data means everything in the folder is copied but not the folder itself 


#to delete (careful!)
#aws s3 rm s3://project-files-20250717160548064700000001/ --recursive