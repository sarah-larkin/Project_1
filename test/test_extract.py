from src.lambda_handler.extract import list_raw_files, list_extracted_files
import os
from moto import mock_aws

"""fixtures for mock bucket/files etc in conftest.py file"""
#TODO: incorporate fixtures created in conftest.py

class TestBaseDataBucket(): 
    def test_fake_data_bucket_creation(self, s3_client): 
        #mock_s3_client = s3_client
        #bucket = mock_storage_bucket
        s3_client.create_bucket(Bucket="MockStorageBucket",
                                CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
        result = s3_client.list_buckets()
        assert len(result["Buckets"]) == 1
        assert result["Buckets"][0]["Name"] == "MockStorageBucket"

        #TODO: check worthwhile test

#is the raw data bucket availble 
#is the extract s3 bucket available
#test for missing or incorrect env variables 

class TestListRawFiles(): 
    def test_list_files_returns_files_in_bukcet(self, s3_client): 
        #create fake bucket 
        s3_client.create_bucket(Bucket="TestDataBucket",
                                CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
        os.environ["FILES_BUCKET"] = "TestDataBucket"   # env variable needs same name as func, so the main function can still run (otherwise will return None) 

        #put files in fake bucket (x2)
        s3_client.put_object(Body="files_content_1", Bucket="TestDataBucket", Key='file_1.csv')
        s3_client.put_object(Body="files_content_2", Bucket="TestDataBucket", Key='file_2.csv')

        files = list_raw_files()

        assert len(files) == 2
        assert files == ["file_1.csv", "file_2.csv"]

    #test for no files found 
    def test_list_files_returns_empty_list_if_no_files(self, s3_client): 
        #create fake bucket 
        s3_client.create_bucket(Bucket="TestDataBucket", 
                                CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'}) 
        os.environ["FILES_BUCKET"] = "TestDataBucket"   # env variable needs same name as func, so the main function can still run (otherwise will return None) 

        files = list_raw_files()

        assert len(files) == 0
        assert files == []

class TestListExtractedFiles(): 
    def test_list_files_returns_files_in_bukcet(self, s3_client): 
        #create fake bucket 
        s3_client.create_bucket(Bucket="TestExtractedBucket", 
                                CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'}) 
        os.environ["S3_INGESTION_BUCKET"] = "TestExtractedBucket"   

        #put files in fake bucket (x2)
        s3_client.put_object(Body="files_content_1", Bucket="TestExtractedBucket", Key='file_1.csv')
        s3_client.put_object(Body="files_content_2", Bucket="TestExtractedBucket", Key='file_2.csv')

        files = list_extracted_files()

        assert len(files) == 2
        assert files == ["file_1.csv", "file_2.csv"]

    #test for no files found 
    def test_list_files_returns_empty_list_if_no_files(self, s3_client): 
        #create fake bucket 
        s3_client.create_bucket(Bucket="TestExtractedBucket", 
                                CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'}) 
        os.environ["S3_INGESTION_BUCKET"] = "TestExtractedBucket"   

        files = list_extracted_files()

        assert len(files) == 0
        assert files == []

class TestCheckNewFiles(): 
    def test_check_for_new_files_returns_list_of_new_files(self): 
        pass
    def test_check_for_new_files_returns_msg_if_no_new_files(self): 
        pass

class TestCheckNewPermittedFiles(): 
    def test(self): 
        pass 

class TestExtractRawFiles(): 
    def test(self): 
        pass

class TestConvertToDf(): 
    def test(self): 
        pass

class TestUploadToIngestionBucket(): 
    def test(self): 
        pass

class TestLambdaHandler(): 
    def test(self): 
        pass



