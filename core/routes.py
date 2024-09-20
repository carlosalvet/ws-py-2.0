import os
from config.app import TMP_DIR, USER_DIR, BASE_URL, CHAT_DIR, CHAT_BASENAME, CHAT_DATA_FILENAME


def base_url():
    return BASE_URL

def __chat_directory():
    _base_url = base_url()
    dirname = os.path.join(_base_url, CHAT_DIR)
    abs_path = os.path.abspath(dirname)
    return abs_path 

def __tmp_directory():
    _base_url = base_url()
    dirname = os.path.join(_base_url, TMP_DIR)
    return dirname


def __user_directory():
    _base_url = base_url()
    dirname = os.path.join(_base_url, USER_DIR)
    return dirname


def __chat_basename():
    return CHAT_BASENAME


def __chat_data_filename():
    return CHAT_DATA_FILENAME


def get_chatname(chat):
    directory = __chat_directory()
    basename = __chat_basename()
    chat_id = 0
    if hasattr(chat, 'id'): chat_id = chat.id

    pathfile = os.path.join(directory, str(chat.id), basename)
    return pathfile 


def get_chatdata(chat):
    directory = __chat_directory()
    basename = __chat_data_filename()
    pathfile = os.path.join(directory, str(chat.id), basename)
    return pathfile 


def get_tmp_filename(_filename=''):
    tmp_directory = __tmp_directory()
    basename = _filename
    filename = os.path.join(tmp_directory, 'chat-edomex', basename)
    return filename 

def get_user_filename(_basename=''):
    tmp_directory = __user_directory()
    basename = str(_basename)
    filename = os.path.join(tmp_directory, basename)
    abs_filename = os.path.abspath(filename)
    return abs_filename 
