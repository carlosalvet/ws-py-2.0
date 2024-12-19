import re
from security.sanity import filter_charset


CODE_SEPARATOR = '_'
NUM_SEPARATOR_PARTS = 2
BODY_LENGTH = 128


def _l(e):
    # la longitud es mayor o igual que 3 o menor o igual que 32
    if len(e) < 3 or len(e) >= 32:
        return ""
    return e


def _s_u(e):
    # Separar por el guión bajo
    parts = e.split(CODE_SEPARATOR)
    if not len(parts) == NUM_SEPARATOR_PARTS: 
        return ""  # Debe haber 1 guion bajo
    return e


def _l_p(t1, t2):
    # Verificar que ambas cadenas no estén vacías (longitud mayor o igual que 1)
    if not t1 or not t2:
        return ""
    return t1, t2


def _nsn(t1):
    # Verifica que si el primer caracter no es un digito (nsn)
    if t1[0].isdigit():
        return ""
    return t1


def _is_alnum(t1, t2):
    # Verificar que ambas pertenezcan al alfabeto alfanuméric (T1)
    if not t1.isalnum() or not t2.isalnum():
        return ""
    return t1, t2

"""
    Se usa la función logicamente equivalente, egún la ley de morgan 
    Ley de Morgan `∼(p ∧ q ∧ r) ⇔ ∼p ∨ ∼q ∨ ∼r`
    t1 = modulo, t2 = evento
"""
def filter_event_code(e):
    if not ( e == "" or (_l(e) and _s_u(e)) ):
        return ""

    parts = e.split('_')
    t1, t2 = parts
    if not (_l_p(t1, t2) and _is_alnum(t1, t2) and _nsn(t1)):
        return ""

    return e


def filter_text(text):
    # Verificar si la longitud del text es mayor o igual a 0 y menor o igual a 128
    if not (isinstance(text, str)):
        return ""
    # Expresión regular que permite:
    # - Caracteres alfanuméricos: [a-zA-Z0-9]
    # - Espacios en blanco: \s
    # - Guión medio y guión bajo: \-_ 
    # - Comillas simples y dobles: ' "
    # - Signos de puntuación: , . ! ? : ; ( ) [ ] { } - _
    # - Vocales con acento: áéíóúÁÉÍÓÚ
    # - Diéresis: üÜ
    # - Ñ y ñ: ñÑ
    patron = r"^[a-zA-Z0-9\s\-_\'\"\.\,\!\?\:\;\(\)\[\]\{\}¡¿áéíóúÁÉÍÓÚñÑüÜ]+$"
    if re.match(patron, text):
        return text[:BODY_LENGTH]
    return ""




def _l_tr(text, size):
    return text[:size]

def filter_headername(headername):
    _type = isinstance(text, str)
    if not ( _type and filter_charset(headername, 3)):
        return ""
    return _l_tr(headername, 32)
