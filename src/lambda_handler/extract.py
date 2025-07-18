import pandas as pd 
import boto3 


def extract_lambda_hander(event, context): 
    pass

#extract data from s3 bucket 
#covert to pandas df 
#Error handling - missing files, bad format, s3 read/write failures (cloudwatch)
#env variables - bucket names
#upload to extract s3
#return a success message print(f"Successfully downloaded {key} from {bucket}") - cloudwatch 

#timestamp?? 
