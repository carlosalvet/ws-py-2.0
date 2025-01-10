import os
from helpers.chat import _chat_get, chat_conversation
from helpers.session import session_set_chat
from core.console import console_log


#response_opened_conn = _roc
def chat_get(websocket_id, message="", _roc=None):
    print('\n---------------------------------------------------------------')
    console_log("[CALLING] events.chat_get", 3)
    #console_log(f"websocket_id: {websocket_id}, message: {message}, _roc:{_roc}", 1)

    chat = None
    status = '500'
    chat_id = _roc['chat-id'] if 'chat-id' in _roc else 0
    if _roc and 'chat-id' in _roc:  chat = _chat_get(chat_id)
    if chat: arr_conversation = chat_conversation(websocket_id, chat)
    if arr_conversation: status = '200'
    session_set_chat(websocket_id, chat=chat)

    response = {'event':'chat-get', 'conversation':arr_conversation, 'status':status}
    #console_log(f'response: {response}',1)
    return response
