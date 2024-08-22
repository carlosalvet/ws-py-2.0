#import os.path
#from helpers.session import call_session_id, create_session_file, delete_session_file
#from common.routes import get_session_name, get_session_path, get_join_path
#from adt.chat import WS_Chat
#from helpers.events.session import user_trasform_to_citizen, user_transform_to_expert
#from adt.session import WS_Session
from helpers.user import user_upcasting
from helpers.session import session_update


def user_login(event, message="", opt_data=None):
    print('[DEBUG]',f"Calling events.user_login, opt_dat: {opt_data}")
    print("[DEBUG]", f"User: {opt_data['user']}, message: {message}")
    role = opt_data['role']
    username = opt_data['username']

    user = user_upcasting(opt_data['user'], username, 'citizen')
    session_update(user, opt_data['chat'])
    print('[DEBUG]', 'called events.user_login', f'ouser: {opt_data["user"]}, user: {user}')
    response = {'status':200}
    return response 


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
