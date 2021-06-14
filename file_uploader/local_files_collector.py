import os

from tqdm.auto import tqdm


class Local_Files(object):
    """Local_Files  gives all the wanted files in dictionary from the given path
    Maintaining file_type_dicts states which format belongs to which category.
    file_type_dicts Can be uploaded using class methods update_file_type_dicts,add_new_itm_file_type_dicts
    """

    file_type_dicts = {
        "images": ["jpg", "png", "svg", "webp"],
        "media_files": ["mp3", "mp4", "mpeg4", "wmv", "3gp", "webm"],
        "documents": ["doc", "docx", "csv", "pdf", ]
    }

    def __init__(self, root_dir=None, new_file_type_dicts=None):
        """Root path is mandatory to read files from root path and its sub directory
        """
        if root_dir:
            if os.path.exists(root_dir):
                self.root_dir = root_dir
                if new_file_type_dicts:
                    self.result = self.get_files_dict(new_file_type_dicts)
                print("Root Directory set to :\t{}".format(self.root_dir))
                self.result = self.get_files_dict()
        else:
            raise Exception('Root Directory not found')

    def get_files_dict(self, file_type_dict=None, file_type_dicts=None):
        """get_files_dict iterate over all the folders and its sub directory,
        get_files_dict collects all the desired files and create dictionary which is useful in uploading files"""
        if file_type_dict is None:
            file_type_dict = file_type_dicts

        file_wit_key_value = {}
        for root, dirs, files in tqdm(os.walk(self.root_dir)):
            for each_file in files:

                for each_key, each_item in file_type_dict.items():

                    if each_file.rsplit(".")[-1] in each_item:

                        if each_key in file_wit_key_value.keys():
                            file_wit_key_value[each_key].append(
                                os.path.join(root, each_file))
                        else:
                            file_wit_key_value[each_key] = [
                                os.path.join(root, each_file)]

        return file_wit_key_value

    @classmethod
    def udpate_file_type_dicts(cls, key, value):
        """Class method to update values in default dictionary
        Example for document you want to add txt file this method can be useful"""
        if key in cls.file_type_dicts.items():
            cls.file_type_dicts[key].append(value)

    @classmethod
    def add_new_itm_file_type_dicts(cls, key, value):
        if key not in cls.file_type_dicts.items():
            cls.file_type_dicts[key] = value
