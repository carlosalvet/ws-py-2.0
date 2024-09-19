from models.user.admin import WS_Admin
from models.user.citizen import WS_Citizen
from models.user.expert import WS_Expert
from models.user.visual import WS_Visual 
from core.console import console_log

def user_new_instance(_type='', user=None):
    if(_type == 'expert'):
        user = WS_Expert(user)
    elif(_type == 'admin'):
        user = WS_Admin()
    elif(_type == 'citizen'):
        print('[DEBUG]', 'Creando usuario (CITIZEN): ', user, end=" ")
        user = WS_Citizen(user)
    else:
        user = WS_Visual()

    return user

# para user_id se usa el fd (file descriptor)
def user_new(websocket=None, chat=None, _type=''):
    
    if chat and hasattr(chat, 'id'):
        chat_id = chat.id
    user = user_new_instance(_type)
    user.id = id(websocket) 
    user.chat_id = chat_id 
    return user

def user_upcasting(user, type='', password=''):
    _tmp = user
    if type == 'citizen': user = user_new_instance('citizen', _tmp)
    elif type == 'expert': user = user_new_instance('expert', _tmp,)
    del _tmp 
    console_log(f'User Upcasted: {user}', 1)
    return user 

def role_id(role_name):
    _id = 0
    if role_name == 'admin': _id = 1
    elif role_name == 'expert': _id = 2
    elif role_name == 'citizen': _id = 3 
    return _id

