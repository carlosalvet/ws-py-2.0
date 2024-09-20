#import os.path
#from helpers.session import call_session_id, create_session_file, delete_session_file
#from common.routes import get_session_name, get_session_path, get_join_path
#from adt.chat import WS_Chat
#from helpers.events.session import user_trasform_to_citizen, user_transform_to_expert
#from adt.session import WS_Session
from helpers.user import user_upcasting
from helpers.session import session_update
from core.console import console_log
from core.routes import get_tmp_filename, get_user_filename


def __citizen_login(_roc):
    user = user_upcasting(_roc['user'], 'citizen')
    session = session_update(user, _roc['chat'])

    str_user_id = str(_roc['user'].id)
    filename = get_tmp_filename(str_user_id)
    session.persist(filename)
    return user 


def __expert_login(_roc, username, password):
    console_log(f'events.expert_login roc: {_roc}, username: {username}, password: {password}', 3)
    user = user_upcasting(_roc['user'], 'expert', password)
    user.username = username
    user.user = 'TEST' 
    console_log(f'events.user upcasting user: {_roc["user"]}, user: {user}', 2)

    is_authenticaded = user.authenticate(password)
    console_log(f'events.user expert is authenticaded: {is_authenticaded}', 2)
    return user


'''
'''
def user_login(event, message="", _roc=None):
    print('\n-------------------------')
    console_log(f'Calling events.user_login: {_roc}', 3)
    role = _roc['role']
    user = None 
    username = _roc['username']
    password = ''
    if 'password' in _roc: password = _roc['password'] 

    if role == 'citizen': user = __citizen_login(_roc)
    elif role == 'expert': user = __expert_login(_roc, username, password)
    del _roc['user']; _roc['user'] = user

    response = {'event':'user-login', 'user-name':user.name, 'user-role': user.role,'status':200}
    console_log(f'events.user_login response: {response}', 1)
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
