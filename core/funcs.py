import os
import random
import time
from config.app import CHAT_DIR, CHAT_BASENAME
from config.log import *


def color_terminal_info():
    print(f'\033[{str(c)}{b}m{_type} {_str}\033[0m', end=_end)
    for i in range(256):
        print(f"\033[48;5;{i}m Color {i} ", end="")
        print("\033[0m", end=" ")
        if (i + 1) % 6 == 0:
            print()  # Nueva línea cada 6 colores


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


#print(f"\033[48;5;{i}m Color {i} ", end="")  # 256 colores
#print("\033[48;5;25mEste texto tiene un fondo azul oscuro\033[0m")
def console_log(_str, code=0, _end=None):
    c = '' #color de letra
    b = '' #color de fondo, tiene que comenzar con ;
    _type = ''
    if code == 1: #"DEBUG"
        _type = '[DEBUG]'; c = FG_YELLOW
    if code == 2: #"INFO"
        print('...')

    print(f'\033[{str(c)}{b}m{_type} {_str}\033[0m', end=_end)
    #else:


def file_log(_str, filename, code=0):
    print('...')

def chat_directory():
    return CHAT_DIR 


def chat_basename():
    return CHAT_BASENAME


def get_chatname(chat):
    directory = chat_directory()
    basename = chat_basename()
    pathfile = os.path.join(directory, chat.date, str(chat.id), basename)
    return pathfile


def rand_hash():
    [_time, _milisegs] = str(time.time()).split('.')
    head = random.randint(1, 1000)
    hashnum = str(head)[:4] + str(_milisegs);
    return hashnum
