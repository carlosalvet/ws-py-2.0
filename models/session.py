import os 
from config.app import CACHE_DIR 
from core.filesystem import FileSystem 


class Session:


    def __init__(self):
        self.user = None
        self.chat = None

        print('Inicializando sesión')


    def __contents_format(self):
        contents = f'role={self.user.role}\n'
        contents += f'chat_title={self.chat.title}\n'
        contents += f'chat_date={self.chat.date}'
        return contents


    def persist(self):
        str_user_id = str(self.user.id)
        filename = os.path.join(CACHE_DIR, 'chat-edomex', str_user_id)
        contents = self.__contents_format()
        print('[DEBUG]', f'Persist file: {filename}, contents:{contents}')

        FileSystem.create_file(filename)
        FileSystem.file_put_contents(filename, contents)


    def destroy(self):
        # Armar nombre
        str_user_id = str(self.user.id)
        filename = os.path.join(CACHE_DIR, 'chat-edomex', str_user_id)

        # Eliminar archivo persistente
        response = FileSystem.destroy_file(filename)
