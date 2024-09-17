from models.chat import Chat

def chat_new(chat_id):
    print('#TODO creando nuevo chat')


def chat_get(chat_id):
    chat = Chat()
    chat.id = chat_id
    chat.get()

    chat.id = 2
    chat.title = 'TITULO DE PRUEBA'
    chat.description = 'HARDCODED DESDE LE MÓDELO'
    chat.date = '2022-06-30'
    return chat
