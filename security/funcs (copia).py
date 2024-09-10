def filter_event_code(e):
    # Separar por el guión bajo
    parts = e.split('_')
    if not len(parts) > 1: 
        return ""  # Debe haber al menos 1 guion bajo

    if len(e) < 3 or len(e) >= 32:
        return ""

    t1, t2 = parts

    # Verificar que ambas cadenas no estén vacías y no comiencen con números
    if not t1 or not t2 or t1[0].isdigit():
        return ""

    # Verificar que ambas cadenas sean alfanuméricas
    if not t1.isalnum() or not t2.isalnum():
        return ""

    return e
