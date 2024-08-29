from config.app import CHAT_DIR, CHAT_BASENAME
import os


def str_to_array(string):
    repr(string)
    rows = string.split('\n')
    array = [row.split('\t') for row in rows]
    return array


def compose(obj, cls):
    if isinstance(obj, cls) or obj is None:
        return obj
    else:
        raise TypeError('%s no es de tipo %s ', (type(obj), cls))


def chat_directory():
    return CHAT_DIR 


def chat_basename():
    return CHAT_BASENAME


def get_chatname(chat):
    directory = chat_directory()
    basename = chat_basename()
    pathfile = os.path.join(directory, chat.date, str(chat.id), basename)
    return pathfile
