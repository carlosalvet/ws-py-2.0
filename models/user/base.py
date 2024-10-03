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
        string = '{' 
        separator = ''
        for key, value in self.__dict__.items():
            if isinstance(value, str): value = f"'{value}'"
            string += f"{separator}{key}: {value}"
            separator = ', '
        string += '}'
        return string
