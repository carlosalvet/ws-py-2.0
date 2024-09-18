import configparser
from core.console import console_log


def arr_ini_contents(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    console_log(f'obteniendo chat desde filename: {filename}', 2)
    return config


def str_to_array(string):
    repr(string)
    rows = string.split('\n')
    array = [row.split('\t') for row in rows]
    return array
