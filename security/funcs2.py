def filter_event_code(e):
    if not isinstance(e, str):
        return ''

    #El código sea mayor o igual que 3 y menor o igual que 32
    if len(e) < 3 or len(e) >= 32:
        return ""

    #Debe tener un guón medio
    if not '-' in e: 
        return ""  

    te1, te2 = e.split('-')
    # Verificar que ambas cadenas sean alfanuméricas
    if not te1.isalnum() or not te2.isalnum():
        return ""

    # Verificar no comiencen con números
    if te1[0].isdigit():
        return ""

    return e


if __name__ == "__main__":
    event_code='chat-conversation'
    filtered_code=filter_event_code(event_code)
    print('ćódigo:',event_code)
    print('código filtrado:',filtered_code)
