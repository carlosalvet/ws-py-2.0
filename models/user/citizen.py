from adt.user.base import WS_UserBase 
from helpers.session import is_session
from pathlib import Path
from adt.ufile import file_put_contents, create_file, destroy_file
from config.routes import CHAT_DIR, SESSION_CHAT_DIR, AUTH_DIR
import time
import os

class WS_Citizen(WS_UserBase):
    def __init__(self):
        self.role = ''


    def authenticate(self, seed=""):
        return True


    def authorize(self,session, session_name):
        is_existent = is_session(session, session_name)
        return is_existent

    def persist(self):
        is_persisted = True
        content = self.get_persist_content();
        filepath = self.get_filepath()
        is_created = create_file(filepath)
        content_puted = False
        if is_created: content_puted = file_put_contents(filepath, content)
        if not content_puted: is_persisted = False
        print(f"[ OK ]user persisted: {is_created}, {is_persisted}, {filepath}, {content}")
        return is_persisted

    def get_filepath(self):
        name = str(self.id)
        filepath = os.path.join(SESSION_CHAT_DIR, str(self.chat_id), name)
        return filepath

    def to_string(self):
        string = f"id={self.id},rol:ciudadano,name:{self.name},chat_id:{self.chat_id}"
        return string

    def get_persist_content(self):
        content = f"id={self.id}\nname={self.name}\nrol=ciudadano\nchat_id={self.chat_id}"
        return content 
