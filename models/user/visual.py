from models.user.base import WS_UserBase 


class WS_Visual(WS_UserBase):


    def __init__(self, id=0, chat_id=0):
        super().__init__(id)
        self.name = ''
        self.role = "visual"
        self.chat_id = chat_id
