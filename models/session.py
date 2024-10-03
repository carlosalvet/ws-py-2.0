import os 
from core.routes import get_tmp_filename 
from core.filesystem import FileSystem 
from core.console import console_log 


class Session:


    def __init__(self):
        self.id = 0
        self.user = None
        self.chat = None
        console_log('Inicializando sesión', 3)


    def __contents_format(self):
        contents = f"id={self.id}\n"
        if hasattr(self.user, 'name'):
            contents += f"name={self.user.name}\n"
        if hasattr(self.user, 'username'):
            contents += f"username={self.user.username}\n"
        if hasattr(self.user, 'role'):
            contents += f"role={self.user.role}\n"
        if hasattr(self.user, 'chat_id'):
            contents += f"chat={self.user.chat_id}"
        return contents


    def persist(self, filename = ''):
        if not filename: 
            basename = str(self.id)
            filename = get_tmp_filename(basename)

        contents = self.__contents_format()
        console_log(f'models.session session_persist: {self}', 1);

        FileSystem.create_file(filename)
        FileSystem.put_contents(filename, contents)


    def destroy(self):
        console_log('model.session destroy', 1)
        # Armar nombre
        basename = str(self.id)
        filename = get_tmp_filename(basename)

        # Eliminar archivo persistente
        response = FileSystem.destroy_file(filename)
        console_log(f'model.session destroy filename: {filename}, response: {response}', 1)
        return response


    def __str__(self):
        _str = '{'
        _str += f'id: {self.id}, '
        if self.user: _str += f'user: {self.user.id}, '
        if self.chat: _str += f'chat: {self.chat.id}'
        _str += '}'
        return _str
