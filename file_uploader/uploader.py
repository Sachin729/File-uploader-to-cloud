import json

from amazon_cloud_service import Amazon_cloud_operations
from google_cloud_service import Goggle_cloud_operations
from local_files_collector import Local_Files
from config import amazon_credential_list, types_of_files


class Uploader(object):
    """Uploader is a wrapper class which combines all in one place"""

    def __init__(self, file_path=None, amazon_credentail_json=None,
                 google_client_credentail_json=None,
                 google_client_bucket=None,
                 google_client_region=None,
                 google_client_config_path=None,
                 new_file_dict=None):

        self.list_of_self = None
        self.file_path = Local_Files(file_path, new_file_dict)
        self.__amazon_credentail_json = amazon_credentail_json
        self.__google_client_credentail_json = google_client_credentail_json
        self.__google_client_bucket = google_client_bucket
        self.__google_client_region = google_client_region
        self.__google_client_config_path = google_client_config_path
        self.list_input_file = self.file_path.get_files_dict()
        print(" Uploader object created")

    def read_json(self, jsonfile):
        try:
            with open(jsonfile, 'r') as json_file:
                self.key_dict = json.loads(json_file.read())
            return self.key_dict
        except:
            raise Exception('Given Configuration json file not found')

    def upload(self, service_type="Auto", category_type="All"):
        """Upload is main method
        Service_type can be Amazon,Google,Auto
        Category_type can be 'Documents','Media_files','Images','Images and Media files'
        Note: If service type is Auto or default empty then Category_type will not play a role.
        Image and multi media files will be transfred to Amazon s3 and Documents will be sent to google storage.
        """
        print(self.list_input_file)
        if service_type == "Amazon":
            # if service type is Amazon then all the operations are done here
            amazon_credential_file = self.read_json(
                self.__amazon_credentail_json)

            amazon = Amazon_cloud_operations(
                aws_access_key=amazon_credential_file[
                    amazon_credential_list[0]],
                aws_secret_access_key=amazon_credential_file[
                    amazon_credential_list[1]],
                s3_bucket=amazon_credential_file[amazon_credential_list[2]],
                region=amazon_credential_file[amazon_credential_list[3]])
            if category_type == 'Documents':
                if types_of_files[0] in self.list_input_file.keys():
                    amazon.upload_files(self.list_input_file['documents'])
            elif category_type == 'Media files':
                if types_of_files[1] in self.list_input_file.keys():
                    amazon.upload_files(self.list_input_file['media_files'])
            elif category_type == 'Images':
                if types_of_files[2] in self.list_input_file.keys():
                    amazon.upload_files(self.list_input_file['images'])
            elif category_type == 'Images and Media files':
                if types_of_files[1] in self.list_input_file.keys():
                    amazon.upload_files(self.list_input_file['media_files'])
                if types_of_files[2] in self.list_input_file.keys():
                    amazon.upload_files(self.list_input_file['images'])
            else:
                if types_of_files[1] in self.list_input_file.keys():
                    amazon.upload_files(self.list_input_file['media_files'])
                if types_of_files[2] in self.list_input_file.keys():
                    amazon.upload_files(self.list_input_file['images'])
                if types_of_files[0] in self.list_input_file.keys():
                    amazon.upload_files(self.list_input_file['documents'])

        elif service_type == "Google":
            # if service type is Google then all the operations are done here
            google = Goggle_cloud_operations(
                bucket=self.__google_client_bucket,
                region=self.__google_client_region,
                client_config_path=self.__google_client_config_path)
            if category_type == 'Documents':

                if types_of_files[0] in self.list_input_file.keys():
                    google.upload_files(self.list_input_file['documents'])
            elif category_type == 'Media files':
                if types_of_files[1] in self.list_input_file.keys():
                    google.upload_files(self.list_input_file['media_files'])
            elif category_type == 'Images':
                if types_of_files[2] in self.list_input_file.keys():
                    google.upload_files(self.list_input_file['images'])
            elif category_type == 'Images and Media files':
                if types_of_files[1] in self.list_input_file.keys():
                    google.upload_files(self.list_input_file['media_files'])
                if types_of_files[2] in self.list_input_file.keys():
                    google.upload_files(self.list_input_file['images'])
            else:

                if types_of_files[1] in self.list_input_file.keys():
                    google.upload_files(self.list_input_file['media_files'])
                if types_of_files[2] in self.list_input_file.keys():
                    google.upload_files(self.list_input_file['images'])
                if types_of_files[0] in self.list_input_file.keys():
                    google.upload_files(self.list_input_file['documents'])


        else:
            # if its default or Auto then Image and multi media files will be transfred to Amazon s3 and Documents will be sent to google storage.
            google = Goggle_cloud_operations(
                bucket=self.__google_client_bucket,
                region=self.__google_client_region,
                client_config_path=self.__google_client_config_path)
            amazon_credential_file = self.read_json(
                self.__amazon_credentail_json)

            amazon = Amazon_cloud_operations(
                aws_access_key=amazon_credential_file[
                    amazon_credential_list[0]],
                aws_secret_access_key=amazon_credential_file[
                    amazon_credential_list[1]],
                s3_bucket=amazon_credential_file[amazon_credential_list[2]],
                region=amazon_credential_file[amazon_credential_list[3]])
            if types_of_files[1] in self.list_input_file.keys():
                amazon.upload_files(self.list_input_file['media_files'])
            if types_of_files[2] in self.list_input_file.keys():
                amazon.upload_files(self.list_input_file['images'])
            if types_of_files[0] in self.list_input_file.keys():
                google.upload_files(self.list_input_file['documents'])
