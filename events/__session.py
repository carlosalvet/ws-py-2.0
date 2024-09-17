import os.path
from helpers.session import call_session_id, create_session_file, delete_session_file
from common.routes import get_session_name, get_session_path, get_join_path
from adt.chat import WS_Chat
from helpers.events.session import user_trasform_to_citizen, user_transform_to_expert
from adt.session import WS_Session


def session_create(user, headers, message=""):
    print(f"[OK]    Processing events.session_create, user: {user.to_string()}")
    print(f"[DEBUG] Headers: {headers}")

    rol = headers['user-role']

    if not (rol or username): 
        print(f"[FAIL] No Data Required")
        return response

    if rol  == 'citizen':  user = user_trasform_to_citizen(user, headers);
    elif rol == 'expert': user = user_transform_to_expert(user, headers)
    user.persist()
    return user.to_string()

def session_update(session, messsage=""):
    last_session_id = dict_header["session"] 
    create_session(dict_header, message)
    if last_session_id and status_success: delete_session_file(last_session_id)
    return ""

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
