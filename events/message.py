#from helpers.chat import format_register
from core.filesystem import FileSystem
from core.funcs import rand_hash
from core.console import console_log 
from core.routes import get_chatname
from helpers.user import role_id
from helpers.session import session_get 

def str_message(string, user, chat):
    body = string
    username = user.name 
    _role_id = role_id(user.role)
    date = chat.date
    message_id = rand_hash()
    message = f'{message_id}	{date}	{_role_id}	{username}	{body}'

    return message


def message_send(websocket_id, message="", data=None):
    print('--------------------------------')
    console_log(f"events.message_send {websocket_id} message: {message}", 3)
    console_log(f"data: data{data}", 3)
    session = session_get(websocket_id)
    console_log(f"session: {session}", 1)
    is_moderated = False
    chat = session.chat
    user = session.user
    response = {'user-name':user.name, 'user-role':user.role, 'event':'message-send', 'message': "", 'status':'200'}

    console_log(f'message_send user:{user}, {type(user)}', 1)
    filename = get_chatname(chat)
    contents = str_message(message, user, chat)
    FileSystem.put_contents(filename, contents, True)

    response['message'] = message
    return response 
    #format_message(session, message)
    #add_log (fmessage)


def message_citizen(event, message="", _roc=None):
    #approved_msg = ""

    #formated_register = format_register(session, message)
    #print("formated message: ", formated_register)

    ##TODO check headers and session, is dan approve message or user message
    #is_approval = is_msg_approved(session)
    #if not is_approval:
        #add_queue_approve(formated_register)
    #else:
        #print(f"formed register: {formated_register}")
        #logchat.add_register(formated_register)

    return approved_msg

