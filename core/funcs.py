from config.app import CHAT_DIR, CHAT_BASENAME


def compose(obj, cls):
    if isinstance(obj, cls) or obj is None:
        return obj
    else:
        raise TypeError('%s no es de tipo %s ', (type(obj), cls))

def chat_directory():
    return CHAT_DIR 

def chat_basename():
    return CHAT_BASENAME
