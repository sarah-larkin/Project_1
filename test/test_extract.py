from src.lambda_handler.extract import list_raw_files, list_extracted_files
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
        #TODO: check worthwhile test

#is the raw data bucket availble 
#is the extract s3 bucket available
#test for missing or incorrect env variables 

class TestListRawFiles(): 
    def test_list_files_returns_files_in_bukcet(self, s3, aws_credentials): 
        #create fake bucket 
        s3.create_bucket(Bucket="TestDataBucket") # s3 from fixture
        os.environ["FILES_BUCKET"] = "TestDataBucket"   # env variable needs same name as func, so the main function can still run (otherwise will return None) 

        #put files in fake bucket (x2)
        s3.put_object(Body="files_content_1", Bucket="TestDataBucket", Key='file_1.csv')
        s3.put_object(Body="files_content_2", Bucket="TestDataBucket", Key='file_2.csv')

        files = list_raw_files()

        assert len(files) == 2
        assert files == ["file_1.csv", "file_2.csv"]

    #test for no files found 
    def test_list_files_returns_empty_list_if_no_files(self, s3, aws_credentials): 
        #create fake bucket 
        s3.create_bucket(Bucket="TestDataBucket") # s3 from fixture
        os.environ["FILES_BUCKET"] = "TestDataBucket"   # env variable needs same name as func, so the main function can still run (otherwise will return None) 

        files = list_raw_files()

        assert len(files) == 0
        assert files == []

class TestListExtractedFiles(): 
    def test_list_files_returns_files_in_bukcet(self, s3, aws_credentials): 
        #create fake bucket 
        s3.create_bucket(Bucket="TestExtractedBucket") 
        os.environ["S3_INGESTION_BUCKET"] = "TestExtractedBucket"   

        #put files in fake bucket (x2)
        s3.put_object(Body="files_content_1", Bucket="TestExtractedBucket", Key='file_1.csv')
        s3.put_object(Body="files_content_2", Bucket="TestExtractedBucket", Key='file_2.csv')

        files = list_extracted_files()

        assert len(files) == 2
        assert files == ["file_1.csv", "file_2.csv"]

    #test for no files found 
    def test_list_files_returns_empty_list_if_no_files(self, s3, aws_credentials): 
        #create fake bucket 
        s3.create_bucket(Bucket="TestExtractedBucket") 
        os.environ["S3_INGESTION_BUCKET"] = "TestExtractedBucket"   

        files = list_extracted_files()

        assert len(files) == 0
        assert files == []

class TestCheckNewFiles(): 
    def test_check_for_new_files_returns_list_of_new_files(): 
        pass
    def test_check_for_new_files_returns_msg_if_no_new_files(): 
        pass

class TestCheckNewPermittedFiles(): 
    def test(): 
        pass 

class TestExtractRawFiles(): 
    def test(): 
        pass

class TestConvertToDf(): 
    def test(): 
        pass

class TestUploadToIngestionBucket(): 
    def test(): 
        pass

class TestLambdaHandler(): 
    def test(): 
        pass



