import boto3
import os
from tqdm.auto import tqdm
import warnings

from cloud_operations import Cloud_operations

warnings.filterwarnings("ignore")


class Amazon_cloud_operations(Cloud_operations):
    """Amazon cloud operations are derived class from Cloud_operations
    This class need credentials like aws_access_key, aws_secret_access_key, s3_bucket, region which is mandatory """

    def __init__(self, aws_access_key, aws_secret_access_key, s3_bucket,
                 region):
        """Initializing all the needed credentials during object creation and validating it"""

        self.s3_file_name = os.path.split(each_file)[-1]
        self.__access_key = aws_access_key
        self.__secret_access_key = aws_secret_access_key
        self.__bucket = s3_bucket
        self.__region = region

        self.__s3_resource = None
        self.__validation_result = self.validate_login_credentials()
        print("Amazon S3 cloud operations started")

    def validate_login_credentials(self):
        """validate_login_credentials validates the given credentials from user, This method is from parent class Cloud_operations"""

        self.__s3_resource = boto3.client(service_name='s3',
                                          aws_access_key_id=self.__access_key,
                                          aws_secret_access_key=self.__secret_access_key,
                                          region_name=self.__region)
        try:
            self.__s3_resource.head_bucket(
                Bucket=self.__bucket)  # try to validate credentials if success method return true else stop here
            print("Amazon S3 cloud Authentication set success")
            return True
        except Exception as e:
            raise e

    def upload_files(self, list_of_files):
        """upload_files on success of validation, this method uploads the give list of files to s3 bucket"""
        if self.__validation_result:
            self.count = 0  # local variable which tells count of files uploaded in S3 Buckets

            print(
                "Sample of file to be uploaded to S3 Buckets are \t {} ".format(
                    list_of_files[:20]))
            for each_file in tqdm(list_of_files):
                try:
                    self.__s3_resource = boto3.resource(service_name='s3',
                                                        aws_access_key_id=self.__access_key,
                                                        aws_secret_access_key=self.__secret_access_key,
                                                        region_name=self.__region)
                    self.__s3_resource.Bucket(self.__bucket).upload_file(
                        Filename=each_file, Key=self.s3_file_name)
                    # .upload_file from boto3 package uploads file to s3
                    self.count += 1
                except Exception as e:
                    print("Failed to upload file\n {}".format(each_file, e))

        else:
            print("please update the credentials to proceed further")
        print("Total file successfully uploaded:\t {}".format(self.count))
        return True
