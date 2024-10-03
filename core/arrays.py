import configparser
from core.console import console_log


def arr_ini_contents(filename):
    console_log(f'core.console.arr_ini_contents filename: {filename}', 1)
    contents = []
    config = configparser.ConfigParser()

    try:
        config.read(filename)
        config.sections()
        contents = config
    except configparser.MissingSectionHeaderError as e:
        console_log(f"Error: El archivo INI no contiene secciones válidas. Detalles: {e}", 4)
    except FileNotFoundError:
        console_log(f"Error: El archivo INI no fue encontrado: {filename}.", 4)
    except Exception as e:
        console_log(f"Ocurrió un error inesperado: {e}", 4)

    console_log(f'obteniendo chat desde filename: {filename}', 2)
    return contents


def str_to_array(string):
    repr(string)
    rows = string.split('\n')
    array = [row.split('\t') for row in rows]
    return array
