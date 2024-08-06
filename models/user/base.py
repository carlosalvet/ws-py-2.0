import time

class WS_UserBase():

    def __init__(self, _id=0):
        self.id = _id
        self.name = ""
        self.role = ""
        self.chat_id = 0


    #def set_arr(self, headers):
        #if headers['user-name']: self.name = headers['user-name']
        #if headers['user-role']: self.role = headers['user-role']
        #if headers['chat-id']: self.chat_id = headers['chat-id']

    def __str__(self):
        string = ""
        if self.id: string += f"id:{self.id}"
        if self.name: string += f", name:{self.name}"
        if self.role: string += f", role: {self.role},"
        if self.chat_id: string += f" chat_id:{self.chat_id}"
        return string
