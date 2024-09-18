from models.chat import Chat
from core.console import console_log

def chat_new(chat_id):
    print('#TODO creando nuevo chat')


def chat_get(chat_id):
    chat = Chat()
    chat.id = chat_id
    chat.get()

    console_log(f'chat: {chat}', 1)

    return chat
