from models.user.base import WS_UserBase 
from core.console import console_log
from core.filesystem import FileSystem
from core.routes import get_user_filename
import zlib
import hashlib
from core.arrays import arr_ini_contents


class WS_Expert(WS_UserBase):

    def __init__(self, user, username, password):
        if not password: raise Exception("Password for Expert is needed") 
        console_log(f'Init USER expert data: {user}', 3)

        self.id = WS_Expert.set_uid(username, password)
        self.name = ''
        self.role = 'expert'
        self.username = username 
        if hasattr(user, 'chat_id'): self.chat_id = user.chat_id

        if self.authenticate():
            self.get()

    def get(self):
        register_filename = self.authenticate()
        if not register_filename: return False
        arr_ini = arr_ini_contents(register_filename)
        self.__formatting_object(arr_ini)
        console_log(f'models.expert get self: {self}', 1)
        return True
        
    def __formatting_object(self, arr_ini):
        if not 'data' in arr_ini:
            console_log('Archivo registro formato no válido, falta cabecera [data]', 2)
            return True

        arr_data = arr_ini['data']
        if 'name' in arr_data: self.name = arr_data['name']
        if 'role' in arr_data: self.role = arr_data['role']
        if 'username' in arr_data: self.username = arr_data['username']



    def save(password):
        if not password: 
            console_log(f'Password no válido: {password}', 4)
            return

        basename = self.id
        filename = get_user_filename(basename)
        contents = self.__freeze()

        FileSystem.create_file(filename)
        FileSystem.put_contents(filename, contents)


    def __freeze(self):
        str_contents = f'name={self.name}\n'
        str_contents += f'username={self.username}\n'
        str_contents += f'role={self.role}'
        str_contents += f'chat={self.chat_id}'
        return str_contents

    def authenticate(self):
        _hash = self.id
        filename = get_user_filename(_hash)
        if WS_Expert.has_register_file(filename): return filename 
        console_log(f'Experto no registrado: {self.id}', 4)
        return '' 

    def has_register_file(filename):
        if FileSystem.is_file(filename): return True 
        return False


    def set_uid(username, password):
        console_log(f'Generating hashname with name: {username}, pass: {password}', 2),
        user_info = username + password

        # Generar el hash MD5
        user_hash = hashlib.md5(user_info.encode()).hexdigest()
        chars = user_hash[-5:]
        final_string = f"{user_hash}{chars}"
        uid = zlib.crc32(final_string.encode())
        return uid
