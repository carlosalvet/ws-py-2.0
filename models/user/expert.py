from models.user.base import WS_UserBase 
from core.console import console_log
from core.filesystem import FileSystem
from core.routes import get_user_filename
import zlib
import hashlib


class WS_Expert(WS_UserBase):

    def __init__(self, user, password):
        if not password: raise Exception("Password for Expert is needed") 

        self.id = 0
        self.name = ''
        self.username = ''
        self.role = 'expert'
        self.chat_id = user.chat_id
        self.set_uid(password)
        console_log(f'Init USER expert data: {user}', 3)


    def save(password):
        if not password: 
            console_log(f'Password no válido: {password}', 4)
            return

        filename = get_user_filename(basename)
        basename = self.set_uid(self.id)
        contents = self.__freeze()

        FileSystem.create_file(filename)
        FileSystem.put_contents(filename, contents)


    def __freeze(self):
        str_contents = f'name={self.name}\n'
        str_contents += f'username={self.username}\n'
        str_contents += f'role={self.role}'
        return str_contents

    def authenticate(self, password):
        _hash = self.set_uid(password)
        filename = get_user_filename(_hash)
        if FileSystem.is_file(filename): return True 
        return False


    def set_uid(self, password):
        console_log(f'Generating hashname with name: {self.username}, pass: {password}', 2),
        user_info = self.username + password

        # Generar el hash MD5
        user_hash = hashlib.md5(user_info.encode()).hexdigest()
        chars = user_hash[-5:]
        final_string = f"{user_hash}{chars}"
        self.id = zlib.crc32(final_string.encode())
        return self.id
