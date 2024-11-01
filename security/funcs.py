def filter_event_code(e):
    if not isinstance(e, str):
        return ''

    #El código sea mayor o igual que 3 y menor o igual que 32
    l = len(e)
    if not (l >= 3 and l <= 65):
        return ""

    #Debe tener un guón medio
    if not '-' in e: 
        return ""  

    te1, te2 = e.split('-')
    l1 = len(te1)
    l2 = len(te2)

    if not (l1 >= 1 and l1 <= 32 and l2 >= 1 and l2 <= 32):
        return ""


    # Verificar que ambas cadenas sean alfanuméricas
    if not te1.isalnum() or not te2.isalnum():
        return ""


    # Verificar no comiencen con números
    if te1[0].isdigit():
        return ""

    return e


def clean_headers(headers):
    clean_headers = headers
    return clean_headers
