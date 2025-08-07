import pandas as pd 
import boto3 
import logging 
import os 

logger = logging.getLogger() 


#S3_INGESTION_BUCKET = os.getenv("S3_INGESTION_BUCKET")


# def extract_lambda_hander(event, context): 
#     s3 = boto3.client('s3')  #initialise s3 client 
    
#     bucket_name = "project-files-20250717160548064700000001" #TODO: make this dynamic 
#     file_keys = 

"""
set up env variables - bucket names
get list of files from source s3 bucket 
check for any new files 
extract files from s3 bucket - download to /tmp? 
update file name with timestamp once processed
covert to pandas df (small files)
Error handling - missing files, bad format, s3 read/write failures (cloudwatch/logger)
upload to (extract) s3
return a success message print(f"Successfully downloaded {key} from {bucket}") - cloudwatch 

"""

def list_files(): 
    s3 = boto3.client('s3')
    FILES_BUCKET = os.getenv("FILES_BUCKET")
    files = []
    response = s3.list_objects_v2(Bucket=FILES_BUCKET)
    for item in response.get("Contents", []):     #TODO: look at the .get() and the expected output
        files.append(item["Key"])
    return files
 


"""
extract inventory_parts.csv first (largest file)
log and stor row count
"""