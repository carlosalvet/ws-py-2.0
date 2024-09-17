from models.user.base import WS_UserBase 



class WS_Expert(WS_UserBase):

    def __init__(self, name=''):
        self.role = 'expert'
        self.name = name
