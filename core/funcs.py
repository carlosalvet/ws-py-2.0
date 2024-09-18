import random
import time
import os
from config.app import BASE_URL, CHAT_DIR, CHAT_BASENAME, CHAT_DATA_FILENAME


def compose(obj, cls):
    if isinstance(obj, cls) or obj is None:
        return obj
    else:
        raise TypeError('%s no es de tipo %s ', (type(obj), cls))
def rand_hash():
    [_time, _milisegs] = str(time.time()).split('.')
    head = random.randint(1, 1000)
    hashnum = str(head)[:4] + str(_milisegs);
    return hashnum
