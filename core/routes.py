import os
from config.app import BASE_URL, CHAT_DIR, CHAT_BASENAME, CHAT_DATA_FILENAME


def base_url():
    return BASE_URL

def __chat_directory():
    _base_url = base_url()
    dirname = os.path.join(_base_url, CHAT_DIR)
    abs_path = os.path.abspath(dirname)
    return abs_path 


def __chat_basename():
    return CHAT_BASENAME


def __chat_data_filename():
    return CHAT_DATA_FILENAME


def get_chatname(chat):
    directory = __chat_directory()
    basename = __chat_basename()

    pathfile = os.path.join(directory, str(chat.id), basename)
    return pathfile 


def get_chatdata(chat):
    directory = __chat_directory()
    basename = __chat_data_filename()
    pathfile = os.path.join(directory, str(chat.id), basename)
    return pathfile 


