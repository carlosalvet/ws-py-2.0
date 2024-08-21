from models.user.admin import WS_Admin
from models.user.citizen import WS_Citizen
from models.user.expert import WS_Expert
from models.user.visual import WS_Visual 

def user_new_instance(_type='', username='', password=''):
    user = None
    if(_type == 'expert'):
        user = WS_Expert(username, password)
    elif(_type == 'admin'):
        user = WS_Admin()
    elif(_type == 'citizen'):
        print('[DEBUG]', 'Nuevo usuario (CITIZEN)', end=" ")
        user = WS_Citizen()
    else:
        user = WS_Visual()

    return user

# para user_id se usa el fd (file descriptor)
def user_new(websocket, chat, type=''):
    
    user = user_new_instance(type)
    user.id = id(websocket) 
    user.chat_id = chat.id 
    print('user: ', user) 
    return user
