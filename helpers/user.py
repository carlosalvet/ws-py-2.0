from models.user.admin import WS_Admin
from models.user.citizen import WS_Citizen
from models.user.expert import WS_Expert
from models.user.visual import WS_Visual 
from core.console import console_log

def user_new_instance(upcast_type='', user=None, namepass='', username=''):
    console_log(f'helper.user user_new_instance type: {upcast_type}, {user}, namepass:{namepass}', 1)
    if(upcast_type == 'expert'):
        user = WS_Expert(user, username, namepass)
    elif(upcast_type == 'admin'):
        user = WS_Admin()
    elif(upcast_type == 'citizen'):
        user = WS_Citizen(user, namepass)
    else:
        user = WS_Visual()

    return user

# para user_id se usa el fd (file descriptor)
def user_new(websocket_id, _type=''):
    user = user_new_instance(_type)
    user.id = websocket_id
    return user

def user_upcasting(_user, type='', namepass='', username=''):
    console_log(f'helper.user user_upcasting user: {_user}, type: {type}, password, {namepass}', 1)
    if type == 'citizen': user = user_new_instance('citizen', _user, namepass)
    elif type == 'expert': user = user_new_instance('expert', _user, namepass, username)
    console_log(f'User Upcasted: {user}', 1)
    return user 

def role_id(role_name):
    _id = 0
    if role_name == 'admin': _id = 1
    elif role_name == 'expert': _id = 2
    elif role_name == 'citizen': _id = 3 
    return _id

