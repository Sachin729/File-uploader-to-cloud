import os
from pprint import pprint
from google.cloud import storage
import json

warnings.filterwarnings("ignore")


class Goggle_cloud_operations(Cloud_operations):
    """Goggle_cloud_operations are dervived class from Cloud_operations
    This class need credentials like access_key,secret_access_key, bucket name, region which is manatory,
    client scret key json which should be available inthe local path
    To create client.json file please refer link below
    Creating and managing service account keys:
    https://cloud.google.com/iam/docs/creating-managing-service-account-keys

    Set up your first Google Cloud Project and download Client File (JSON file):

    https://www.dezyre.com/recipes/upload-files-to-google-drive-using-python
    https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf
    Manage Files in Google Cloud Storage With Python
    https://hackersandslackers.com/manage-files-in-google-cloud-storage-with-python/

    Storage classes
    https://cloud.google.com/storage/docs/storage-classes
    """

    def __init__(self, bucket, region, client_config_path):
        """Intilizing all the needed credentials during object creation and validating it"""

    self.__bucket = bucket
    self.__region = region
    #         self.__storage_client = storage_client
    self.__client_config_path = client_config_path
    self.validate_login_credentials()
    print("Google cloud operations started")


def set_credentails_with_env(self, client_config_path):
    """environ varialbe GOOGLE_APPLICATION_CREDENTIALS is set, this is one time activity """
    try:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
            self.__client_config_path)
        print("Google Client config path set success")
        return True
    except:
        raise Exception(
            'Faild to set up environment varialbe for Google cloud storage')


def validate_login_credentials(self):
    """validate_login_credentials validates the given credentials from user,
    This method is from parent class Cloud_operations"""

    self.set_credentails_with_env(self.__client_config_path)
    try:
        self.__storage_client = storage.Client()  # try to validate credentials if success method return true else stop here
        print("Google Client Authentication set success")
    except:
        raise Exception('Authentication failed for Google cloud storage')


def upload_files(self, list_of_files):
    self.count = 0

    print("Sample of file to be uploaded to Google storage are \t {}".format(
        list_of_files))
    bucket = self.__storage_client.get_bucket(self.__bucket)
    for each_file in tqdm(list_of_files):
        try:
            blob_name = os.path.split(each_file)[-1]
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(
                each_file)  # .upload_file from google cloud api package uploads file to google storage
            self.count += 1
        except Exception as e:
            print("Failed to upload file {} \n{}".format(each_file, e))

    print("Total file succefully uploaded:\t {}".format(self.count))
    return True

