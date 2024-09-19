#import os.path
#from helpers.session import call_session_id, create_session_file, delete_session_file
#from common.routes import get_session_name, get_session_path, get_join_path
#from adt.chat import WS_Chat
#from helpers.events.session import user_trasform_to_citizen, user_transform_to_expert
#from adt.session import WS_Session
from helpers.user import user_upcasting
from helpers.session import session_update
from core.console import console_log


'''
'''
def user_login(event, message="", _roc=None):
    print('\n-------------------------')
    console_log(f'Calling events.user_login: {_roc}', 3)

    role = _roc['role']
    username = _roc['username']
    if 'user_pass' in _roc: password = _roc['user-pass'] 

    if role == 'citizen':
        user = user_upcasting(_roc['user'], 'citizen')
        session_update(user, _roc['chat'])
        del _roc['user']; _roc['user'] = user
    elif role == 'expert':
        user = user_upcasting(_roc['user'], username, 'expert', )
        session_update(user, _roc['chat'], role)
        del _roc['user']; _roc['user'] = user

    response = {'event':'user-login', 'user-name':user.role, 'user-role': user.name,'status':200}
    return response 


def user_expert():
    print('\n-------------------------')
    console_log('Calling events.user_expert', 3)
    print('...')


#def session_update(session, messsage=""):
    #last_session_id = dict_header["session"]
    #create_session(dict_header, message)
    #if last_session_id and status_success: delete_session_file(last_session_id)
    #return ""

def  session_auth(session, message=""):
    user = session.user

    auth = WS_Session.authenticate(user.nama, user.password, 7)
    if user.role == "Invite" and user.name:
        session.create(session.user.role)
    elif user.role == "Expert" and auth:
        session.create(user.role)
    #else if session.user.role == "Expert":

    print(f"session id: {session.id}, is created: {is_created}")
    return session.id
