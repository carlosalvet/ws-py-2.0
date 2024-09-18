from config.log import *


def color_terminal_info():
    print(f'\033[{str(c)}{b}m{_type} {_str}\033[0m', end=_end)
    for i in range(256):
        print(f"\033[48;5;{i}m Color {i} ", end="")
        print("\033[0m", end=" ")
        if (i + 1) % 6 == 0:
            print()  # Nueva línea cada 6 colores


#print(f"\033[48;5;{i}m Color {i} ", end="")  # 256 colores
#print("\033[48;5;25mEste texto tiene un fondo azul oscuro\033[0m")
def console_log(_str, code=0, _end=None):
    c = '' #color de letra
    b = '' #color de fondo, tiene que comenzar con ;
    _type = ''
    if code == 1: #"DEBUG"
        _type = '[DEBUG]'; c = FG_YELLOW
    if code == 2: #"INFO"
        _type = '[INFO]'; c = FG_BLUE
        print('...')

    print(f'\033[{str(c)}{b}m{_type} {_str}\033[0m', end=_end)
    #else:


def file_log(_str, filename, code=0):
    print('...')


