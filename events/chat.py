#from adt.session import WS_Session
#from adt.ufile import get_chat_contents
#from helpers.chat import format_register, manage_error_queue_approve, add_queue_approve, is_msg_approved, chat_persist_filename, chat_log_parse
#from helpers.user import user_instance_of
#from common.ws_log import WS_Log
#from common.routes import get_logchattmpname, get_logchatname
#import os
#from config.routes import SESSION_CHAT_DIR
#from config.variables import CHATS, fd
#from core.console.funcs import console_message
import os
from helpers.user import user_new
from helpers.chat import _chat_get, chat_conversation
from helpers.session import session_get, session_chat_set
from core.console import console_log


#response_opened_conn = _roc
def chat_get(websocket_id, message="", _roc=None):
    print('\n-------------------')
    console_log("events.chat_get", 3)
    console_log(f"websocket_id: {websocket_id}, message: {message}, _roc:{_roc}", 1)

    chat = None
    status = '500'
    if _roc and 'chat-id' in _roc:  chat = _chat_get(_roc['chat-id'])
    if chat: arr_conversation = chat_conversation(websocket_id, chat)
    if arr_conversation: status = '200'
    session_chat_set(websocket_id, chat)

    response = {'event':'chat-get', 'conversation':arr_conversation, 'status':status}
    console_log(f'response: {response}',1)
    return response
