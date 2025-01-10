from models.chat import Chat
from core.console import console_log
from core.routes import get_chatname
from core.filesystem import FileSystem
from core.arrays import str_to_array


def chat_create(chat_id):
    print('#TODO creando nuevo chat')


def _chat_get(chat_id):
    chat = Chat()
    chat.id = chat_id
    chat.get()
    #console_log(f'chat: {chat}', 1)
    return chat


def chat_conversation(websocket_id, chat):
    print('\n-------------------')
    console_log("events.chat_conversation", 3)
    arr_conversation = []

    if chat:
        chat_filename = get_chatname(chat)
        conversation = FileSystem.get_contents(chat_filename);
        arr_conversation = str_to_array(conversation)
    return arr_conversation 


