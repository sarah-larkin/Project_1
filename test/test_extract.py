from src.lambda_handler.extract import extract_lambda_hander
import pytest
import boto3
import os
from moto import mock_aws 



#pytest fixtures 
#Mock AWS credentials 
@pytest.fixture(scope="function")
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

#Mock s3 client 
@pytest.fixture(scope="function")
def s3(aws_credentials):
    with mock_aws():
        yield boto3.client("s3", region_name="us-east-1") #default location for moto 

#TODO: check fixtures further 



#s3 client mocked above so decorator not needed here 
class TestBaseDataBucket(): 
    def test_fake_data_bucket_creation(self, s3): 
        #create fake bucket 
        s3.create_bucket(Bucket="TestDataBucket") # s3 from fixture
        result = s3.list_buckets()
        assert len(result["Buckets"]) == 1


#TODO: Test lambda handler 
# class TestLambdaHandler(): 
#     def test_lambda_handler(): 
#         assert extract_lambda_hander() == 1



#is the bucket availble 
#is the destination available - extract s3 
#test for missing or incorrect env variables 

#can it access s3 with correct IAM permission? 
#what if the file does not exist? 
#is the key(filename) correct? 
#test for existing and non-existing keys 

#valid csv?
#empty file? 
#file with unexpected columns 

#does pd.read_csv(obj['Body']) work? 
#if returns a non-dataframe or errors? 

