#import os.path
#from helpers.session import call_session_id, create_session_file, delete_session_file
#from common.routes import get_session_name, get_session_path, get_join_path
#from adt.chat import WS_Chat
#from helpers.events.session import user_trasform_to_citizen, user_transform_to_expert
#from adt.session import WS_Session
from helpers.user import user_upcasting
from helpers.session import session_update, session_get, session_set
from core.console import console_log
from core.routes import get_tmp_filename, get_user_filename


def __citizen_login(websocket_id, _user, name=''):
    user = user_upcasting(_user, 'citizen', name)
    console_log(f'events.user upcasting user: {_user}, user: {user}', 2)

    session = session_get(websocket_id)
    session.user = user
    session.persist()
    return user 


def __expert_login(websocket_id, username, password):
    session = session_get(websocket_id)
    console_log(f'events.expert_login user: {session.user}, username: {username}, password: {password}', 3)
    user = user_upcasting(session.user, 'expert', password, username)
    session.user = user
    console_log(f'events.expert_login user2: {session.user}, username: {username}, password: {password}', 3)
    console_log(f'events.user upcasting user: {user}', 1)
    is_authenticated = user.authenticate()

    #TODO falta rechazar cuando no es autenticado
    #if not is_authenticated: return None

    console_log(f'events.user expert is authenticaded: {is_authenticated}', 2)
    return user


'''
'''
def user_login(websocket_id, message="", data=None):
    print('\n-------------------------')
    session = session_get(websocket_id)
    console_log(f'Calling events.user_login session.user: {session.user}, data:{data}', 3)
    username = data['username']
    password = ''
    user = None
    
    if 'password' in data: password = data['password'] 

    if data['role'] == 'citizen': user = __citizen_login(websocket_id, session.user, username)
    elif data['role'] == 'expert': 
        user = __expert_login(websocket_id, username, password)
        del data['password'] 
        del data['username']

    if user.name: response = {'event':'user-login', 'user-name':user.name, 'user-role': user.role,'status':200}
    else: response = {'event':'user-login', 'status': 500}

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
