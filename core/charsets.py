from config.charsets import *


"""
    Charset Keywords
    sp  space (espacio en blanco)
    h   hyphen (guión medio)
    u   underscore (guión bajo)
"""


def get_string_charset(number):
    if 1 <= number < len(A) and A[number] is not None:
         return f"{T[number]}"
    return ""


def in_charset(_ch, number):
    AL = get_string_charset(number)
    if _ch in AL: return True
    return False


def str_filter_charset(_str,CHARSET_NUM):
    str_filtered = ''
    ch_filtered = ''
    for _ch in _str:
        ch_filtered = ''
        if in_charset(_ch, CHARSET_NUM): ch_filtered = _ch
        if ch_filtered: str_filtered = str_filtered + ch_filtered

    return str_filtered


def str_filter_alnum_sphu(_str):
    return str_filter_charset(_str, ALNUMSPHU)


def str_filter_latam_text(_str):
    return str_filter_charset(_str, LATAM_TEXT)
