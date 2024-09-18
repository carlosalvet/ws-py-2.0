#from helpers.chat import format_register
from core.filesystem import FileSystem
from core.funcs import rand_hash
from core.routes import get_chatname
from helpers.user import role_id

def str_message(string, user, chat):
    body = string
    username = user.name 
    _role_id = role_id(user.role)
    date = chat.date
    message_id = rand_hash()
    message = f'{message_id}	{date}	{_role_id}	False	{username}	{body}'

    return message


def message_send(event, message="", _roc=None):
    print('--------------------------------')
    print("[PROCESS] events.message_send")
    print("[DEBUG]", f"event:{event}, message:{message}, _roc:{_roc}")
    print("[DEBUG]2222", f"user:{_roc['user']}, chat:{_roc['chat']}")
    is_moderated = False
    chat = _roc['chat']
    user = _roc['user']
    response = {'user-name':user.name, 'user-role':user.role, 'event':'message-send', 'message': [], 'status':'200'}

    #is_authorize = session.user.authorize(session, str(headers['session-name']))
    if is_moderated: message_moderate(user, chat, message)
    else: 
        #register_file = format_register(user, chat, message)
    #if is_authorize:
        response['message'] = message
        filename = get_chatname(chat)
        contents = str_message(message, user, chat)
        FileSystem.put_contents(filename, contents, True)

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

