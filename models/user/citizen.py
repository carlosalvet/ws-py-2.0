from models.user.base import WS_UserBase 


class WS_Citizen(WS_UserBase):

    def __init__(self, id=0, chat_id=0):
        super().__init__(id)
        self.role = "citizen"
        self.chat_id = chat_id

