from config.charsets import LATAM_TEXT

def filter_charset(cadena, code):
    patron = get_charset(code)
    caracteres_validos = re.findall(patron, cadena)
    return ''.join(caracteres_validos)

def filter_text(text):
    if not (isinstance(text, str)): return ""
    text_filtered = filter_charset(text, LATAM_TEXT);
    return text_filtered
    
