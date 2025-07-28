import pandas as pd 
import boto3 
import logging 
import os 


def extract_lambda_hander(event, context): 
    s3 = boto3.client('s3')  #initialise s3 client 
    
    bucket_name = "project-files-20250717160548064700000001" #TODO: make this dynamic 
    file_keys = 

#extract data from s3 bucket 
#covert to pandas df 
#Error handling - missing files, bad format, s3 read/write failures (cloudwatch)
#env variables - bucket names
#upload to extract s3
#return a success message print(f"Successfully downloaded {key} from {bucket}") - cloudwatch 

#timestamp?? 



# def get_bucket_name(): 
#     bucket_name = os.environ.get("s3_extract_buckt")
#     return{f"ingestion_Bucket:{bucket_name}"}
#TODO: check how .env or best practice for this to be dynamic 