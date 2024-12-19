from core.charsets import *

def filter_event_code(e):
    if not isinstance(e, str):
        return ''

    #El código sea mayor o igual que 3 y menor o igual que 32
    #Debe tener un guón medio
    e = e[:65]
    l = len(e)
    if not (l > 2 and '-' in e):
        return ""

    te1, te2 = e.split('-')
    te1 = te1[:33]
    te2 = te2[:33]

    # Verificar que ambas cadenas sean alfanuméricas
    if not te1.isalnum() or not te2.isalnum():
        return ""

    # Verificar no comiencen con números
    if te1[0].isdigit():
        return ""

    return e


"""
    Dictionary headers array of headers with name in key
    return clean_headers
"""
def clean_headers(headers):
    clean_headers = {}
    if not (type(headers) == dict and len(headers) > 0):
        return clean_headers 

    for key, value in headers.items():
        cl_name = filter_header_name(key)
        cl_value = filter_header_value(value)
        if cl_name: clean_headers[key] = value
    return clean_headers


def str_filter_charset(_str,CHARSET_NUM):
    str_filtered = ''
    ch_filtered = ''
    for _ch in _str:
        ch_filtered = ''
        if in_charset(_ch, CHARSET_NUM): ch_filtered = _ch
        if ch_filtered: str_filtered = str_filtered + ch_filtered

    return str_filtered


def filter_header_name(_str):
    if not (type(_str) == str and len(_str) > 2) : return ''
    _str = _str[:32]

    return str_filter_charset(_str, ALNUMH)


def filter_header_value(_str):
    if not (type(_str) == str and len(_str) > 2) : return ''
    _str = _str[:32]

    return str_filter_charset(_str, ALNUMHU)


def filter_latam_text(_str):
    return str_filter_charset(_str, LATAM_TEXT)


def clean_body(_body):
    cls_body = filter_latam_text(_body)
    return cls_body
