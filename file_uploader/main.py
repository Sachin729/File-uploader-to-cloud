

import config
import uploader
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # eaxamples to create different configuration to upload fies
    #case1
    # r = Uploader(r'D:\backup\test\doc',\
    # amazon_credentail_json=r"D:\code\\amazon_config.json")
    # r.file_path.file_type_dicts
    # r.upload(service_type="Amazon",category_type="All")
    #case2
    # r = Uploader(file_path=r'D:\backup\test\doc',
    #              google_client_credentail_json=r"D:\code\key.json",\
    #              google_client_bucket="ssbucket_name",\
    #              google_client_region='US',\
    #              google_client_config_path=r"D:\code\key.json")
    # r.file_path.file_type_dicts
    # r.upload(service_type="Google",category_type="All")
    #case3
    # r = Uploader(file_path=r'D:\code\backup\test\doc', \
    #              amazon_credentail_json=r"D:\code\amazon_config.json",
    #              google_client_credentail_json=r"D:\code\key.json", \
    #              google_client_bucket="ssbucket_name", \
    #              google_client_region='US', \
    #              google_client_config_path=r"D:\code\key.json")
    # r.file_path.file_type_dicts
    # r.upload(category_type="All")


