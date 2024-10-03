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
from core.filesystem import FileSystem
from core.routes import get_chatname
from helpers.user import user_new
from helpers.session import session_get 
from core.arrays import str_to_array
from core.console import console_log


#response_opened_conn = _roc
def chat_conversation(websocket_id, message="", _roc=None):
    print('\n-------------------')
    console_log("events.chat_conversation", 3)
    session = session_get(websocket_id)
    chat = session.chat
    console_log(f'helpers.session_get session.chat: {session.chat}', 1)

    chat_filename = get_chatname(chat)
    conversation = FileSystem.get_contents(chat_filename);
    arr_conversation = str_to_array(conversation)
    response = {'event':'chat-conversation', 'conversation':arr_conversation, 'status':'200'}
    return response 

