import os 
from core.routes import get_tmp_filename 
from core.filesystem import FileSystem 
from core.console import console_log 


class Session:


    def __init__(self):
        self.user = None
        self.chat = None
        console_log('Inicializando sesión', 3)


    def __contents_format(self):
        contents = f'role={self.user.role}\n'
        contents += f'name={self.user.name}\n' if self.user.name else ''
        contents += f'chat_title={self.chat.title}\n'
        contents += f'chat_date={self.chat.date}'
        return contents


    def persist(self, filename = ''):
        if not filename: 
            str_user_id = str(self.user.id)
            filename = get_tmp_filename(str_user_id)
        contents = self.__contents_format()

        FileSystem.create_file(filename)
        FileSystem.put_contents(filename, contents)


    def destroy(self):
        # Armar nombre
        str_user_id = str(self.user.id)
        filename = get_tmp_filename(str_user_id)

        # Eliminar archivo persistente
        response = FileSystem.destroy_file(filename)
