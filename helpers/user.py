from models.user.admin import WS_Admin
from models.user.citizen import WS_Citizen
from models.user.expert import WS_Expert
from models.user.visual import WS_Visual 

def user_instance_of(_type='', username='', password=''):
    user = None
    if(_type == 'expert'):
        user = WS_Expert(username, password)
    elif(_type == 'admin'):
        user = WS_Admin()
    elif(_type == 'citizen'):
        user = WS_Citizen()
    else:
        user = WS_Visual()

    return user

# para user_id se usa el fd (file descriptor)
def user_new(user_id, chat_id, type=''):
    user = user_instance_of(type)
    user.id = user_id 
    user.chat_id = chat_id
    return user
