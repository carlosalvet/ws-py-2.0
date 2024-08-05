from adt.user.base import WS_UserBase 
from adt.session import WS_Session
from config.routes import AUTH_DIR
from pathlib import Path
import zlib
import os


class WS_Expert(WS_UserBase):

    def __init__(self, name=''):
        self.role = 'expert'
        self.name = name

    """
        seed = concat(username, password)
    """
    def authenticate(self, username, password):
        seed = WS_Expert.get_seed_name(username, password)
        auth_name = WS_Expert.get_authentication_name(seed);
        path = self.get_authentication_file(auth_name)
        authpath = Path(path)
        authentication = authpath.is_file()
        if authentication: return True

        return False 


    def get_seed_name(username, password):
        return username.password        



    def get_authentication_name(seed=""):
        authentication_name = str(zlib.crc32(str(seed).encode()))
        return authentication_name 

    def get_authentication_file(self, auth_name):
        auth_file = ""
        auth_dir = os.path.join(AUTH_DIR, 'expert')
        if auth_dir:
            auth_file = os.path.join(auth_dir, auth_name)
        return auth_file

    def persist():
        return True

    def to_string(self):
        string = f"id={self.id},rol:{Experto},name:{self.username},chat_id:self.chat_id"
        return string

    def get_persist_content(self):
        string = f"id={self.id}\nrol={Experto}\nname={self.username}\nchat_id:self.chat_id"
        return string
