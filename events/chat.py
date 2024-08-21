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
from core.funcs import str_to_array, chat_directory, chat_basename
from helpers.user import user_new

def chat_conversation(event, message="", opt_data=None):
    print('[DEBUG]',f'Ejecutando chat_conversation event:{event}, body:{message}, user: {opt_data}, user:{opt_data["user"]}')
    user = opt_data['user']
    chat = opt_data['chat']

    #console_message('Enter to events.chat_conversation', 'DEBUG')
    #chat_path = chat_persist_filename(user.chat_id)
    #session.user = user
    #session.chat = chat

    #print(f"[OK]   Persist chat in: {chat_path}")
    #conversation = get_chat_contents(chat_path)
    #print(f"[OK]   Getting converesation: {conversation}")
    #arr_conversation = chat_log_parse(conversation)

    date = '2022-06-30'

    chat_filename = os.path.join(chat_directory(), date, str(chat.id), chat_basename())
    conversation = FileSystem.file_get_contents(chat_filename);
    arr_conversation = str_to_array(conversation)
    return arr_conversation

def chat_message(session, message=""):
    approved_msg = ""

    formated_register = format_register(session, message)
    print("formated message: ", formated_register)

    #TODO check headers and session, is dan approve message or user message
    has_approval = is_msg_approved(session)
    if not has_approval:
        add_queue_approve(formated_register)
    else:
        print(f"formed register: {formated_register}")
        logchat.add_register(formated_register)

    return approved_msg
