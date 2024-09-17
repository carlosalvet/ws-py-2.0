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
from core.funcs import str_to_array, get_chatname
from helpers.user import user_new

#response_opened_conn = _roc
def chat_conversation(event, message="", _roc=None):
    print('\n-------------------')
    print('[DEBUG]',f'Ejecutando chat_conversation event:{event}, body:{message}, user:{_roc["user"]}, chat: {_roc["chat"]}')
    user = _roc['user']
    chat = _roc['chat']

    chat_filename = get_chatname(chat)
    conversation = FileSystem.get_contents(chat_filename);
    arr_conversation = str_to_array(conversation)
    response = {'event':'chat-conversation', 'conversation':arr_conversation, 'status':'200'}
    return response 

