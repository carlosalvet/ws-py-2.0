from models.user.base import WS_UserBase 
from core.console import console_log
from core.filesystem import FileSystem
from core.routes import get_user_filename



class WS_Expert(WS_UserBase):

    def __init__(self, user=None):
        console_log(f'Init USER expert', 3)
        super().__init__()
        self.role = 'expert'
        if user and hasattr(user, 'name'): self.name = user.name


    def save(password):
        if not password: 
            console_log(f'Passwor no válido: {password}', 4)
            return

        str_user_id = str(self.id)
        basename = WS_Expert.set_uid(self.name, password)
        contents = self.__get_file_contents(basename)

        FileSystem.create_file(filename)
        FileSystem.put_contents(filename, contents)


    def __get_file_contents(self, basename):
        filename = get_user_filename(basename)
        contents = self.__contents_format()
        return contents


    def __contents_format(self):
        contents = f'name={self.name}\n' if self.name else ''
        contents += f'role={self.role}\n'
        contents += f'chat_date={self.chat_id}'
        return contents

    def authenticate(self, password):
        _hash = self.set_uid(self.name, password)
        filename = get_user_filename(_hash)
        FileSystem.is_file(filename)
        return hash 

    def set_uid(username, password):
        user_info = username + password

        # Generar el hash MD5
        user_hash = hashlib.md5(user_info.encode()).hexdigest()
        chars = user_hash[-5:]
        final_string = f"{user_hash}{chars}"
        crc32_hash = zlib.crc32(final_string.encode())
        return crc32_hash
