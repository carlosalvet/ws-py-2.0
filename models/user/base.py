from common.routes import get_join_path, get_session_path
import time

class WS_UserBase():

    def __init__(self, _id=0):
        self.id = _id
        self.name = ""
        self.role = ""
        self.chat_id = 0
        self.session = ""


    def set_arr(self, headers):
        if headers['user-name']: self.name = headers['user-name']
        if headers['user-role']: self.role = headers['user-role']
        if headers['chat-id']: self.chat_id = headers['chat-id']

    def __str__(self):
        string = f"id:{self.id}, name:{self.name}, chat_id:{self.chat_id}, session:null"
        return string

    def rseed(self, word):
        timestamp = time.time()
        seed = f"{word}-{timestamp}"
        print(f"[DEBUG] seed created: {seed}")
        return seed
