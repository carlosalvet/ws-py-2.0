from config.charsets import *
from core.charsets import get_string_charset


def get_charset(code):

def filter_charset(cadena, code):
    patron = get_string_charset(code)
    caracteres_validos = re.findall(patron, cadena)
    return ''.join(caracteres_validos)

def filter_latam_text(text):
    if not (isinstance(text, str)): return ""
    text_filtered = filter_charset(text, LATAM_TEXT);
    return text_filtered
    

def filter_header_name(name):
    filtered_name = name
    return filtered_name


def filter_header_value(value)
    filtered_value = value
    return filtered_value
