import os 
from core.routes import get_tmp_filename 
from core.filesystem import FileSystem 
from core.console import console_log 
from models.user.base import WS_UserBase 
from models.chat import Chat 


class Session:


    def __init__(self, user = None, chat = None):
        self.id = 0
        self._user = user 
        self._chat = chat
        console_log('Inicializando sesión', 3)


    def __contents_format(self):
        contents = f"id={self.id}\n"
        if hasattr(self._user, 'name'):
            contents += f"name={self._user.name}\n"
        if hasattr(self._user, 'username'):
            contents += f"username={self._user.username}\n"
        if hasattr(self._user, 'role'):
            contents += f"role={self._user.role}\n"
        if hasattr(self._user, 'chat_id'):
            contents += f"chat={self._user.chat_id}"
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


    # Propiedad para acceder al user
    @property
    def user(self):
        return self._user


    @user.setter
    def user(self, _user):
        if isinstance(_user, WS_UserBase):
            self._user = _user 
        else:
            raise TypeError("La dirección debe ser un objeto del tipo Usuario.")


    # Propiedad para acceder al chat
    @property
    def chat(self):
        return self._chat


    @chat.setter
    def chat(self, _chat):
        if isinstance(_chat, Chat):
            self._chat = _chat 
        else:
            raise TypeError("La dirección debe ser un objeto del tipo Chat.")


    def __str__(self):
        _str = '{'
        _str += f'id: {self.id}, '
        if self._user: 
            _str += f'user: {self._user}, '
        if self._chat:
            _str += f'chat: {self._chat}'
        _str += '}'
        return _str
