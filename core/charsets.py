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
