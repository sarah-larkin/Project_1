import pandas as pd 
import boto3 
import logging 
import os 

logger = logging.getLogger() 


#S3_INGESTION_BUCKET = os.getenv("S3_INGESTION_BUCKET")


def extract_lambda_handler(event, context): 
    pass


"""
set up env variables - bucket names (in lambda.tf)
get list of files from source s3 bucket 
check for any new files 
extract files from s3 bucket - download to /tmp? 
covert to pandas df (small files)
Error handling - missing files, bad format, s3 read/write failures (cloudwatch/logger)
upload to (extract) s3
update file name with timestamp once processed / use metadata for timestamp?
return a success message print(f"Successfully downloaded {key} from {bucket}") - cloudwatch 

"""

def list_raw_files(): 
    s3 = boto3.client('s3')
    raw_files_bucket = os.getenv("FILES_BUCKET")
    #add try except blocks/logging
    raw_files = []
    response = s3.list_objects_v2(Bucket=raw_files_bucket)
    for item in response.get("Contents", []):     # .get(keyname, value) -> value default is None if key does not exist, can specify alternative eg. here returns empty list if nothing in contents
        raw_files.append(item["Key"])
    return raw_files

#contents is a list of dicts
#item["key"] accesses the name of the file only

def list_extracted_files(): 
    s3 = boto3.client('s3')
    extracted_files_bucket = os.getenv("S3_INGESTION_BUCKET")
    #add try except blocks/logging
    extracted_files = []
    response = s3.list_objects_v2(Bucket=extracted_files_bucket)
    for item in response.get("Contents", []):     # .get(keyname, value) -> value default is None if key does not exist, can specify alternative eg. here returns empty list if nothing in contents
        extracted_files.append(item["Key"])
    return extracted_files
 
def check_for_new_permitted_files(): 
    """
    args: raw_files, extracted_files

    provide list of permitted files (env var - to keep configurable)
    compare raw_files to permitted files - only extract permitted files

    compare raw_files and extracted_files
    only new files are to be extracted (no duplicates)
    use sets to compare (could add a warning if duplicate files)
    return: list of any new permitted files 

    (start with just inventory_parts.csv to test it out??)
    """
    pass 


def extract_raw_files(): 
    """
    args: bucket, key, local_path
    extract from s3 (to /tmp in Lambda) 
    """
    pass

def convert_raw_to_df(): 
    """
    convert to pandas df eg. pd.read_csv()
    error handling - read failure, empty file...
    return: list of dfs? 
    """
    pass

def upload_to_ingestion_bucket():
    """
    args: df, target key 
    convert back to csv? 
    updload to s3 bucket 
    return/log sucessful upload message 
    """
    pass 




"""
extract inventory_parts.csv first (largest file)
log and store row count
"""