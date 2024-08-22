from models.user.base import WS_UserBase 


class WS_Citizen(WS_UserBase):

    def __init__(self, user = None, username=''):
        print('[DEBUG]'f'USER citizen: {user}')
        super().__init__(user.id)
        self.role = "citizen"
        self.name = username
        self.chat_id = user.chat_id

