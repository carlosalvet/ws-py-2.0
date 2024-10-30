import random
import time
import os
from collections.abc import Iterable
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


def get_var_value(value, default=None, key=''):
    datum = ''
    first_data =''
    if isinstance(value, Iterable):
        if not default: default = get_first_default(value)
        datum = value[key] if key in value else default
    return datum


def get_first_default(value):
    first_data = value 
    default = None
    #First value from value
    if isinstance(value, Iterable) and len(value):
        key, value = next(iter(value.items()))
        first_data = value

    if isinstance(first_data, str): default = ''
    if isinstance(first_data, int): default = 0 
    return default


