import time

class WS_UserBase():

    def __init__(self, _id=0):
        self.id = _id
        self.name = ""
        self.role = ""
        self.chat_id = 0


    def authorize(self):
        return False

    def __str__(self):
        string = '{' 
        separator = ''
        for key, value in self.__dict__.items():
            if isinstance(value, str): value = f"'{value}'"
            string += f"{separator}{key}: {value}"
            separator = ', '
        string += '}'
        return string
