from core.console import console_log
from core.routes import get_chatdata
from core.arrays import arr_ini_contents
import os

class Chat:

    def __init__(self):
        self.id = 0
        self.title = ''
        self.description = ''
        self.date = ''

    def save(self):
        print('creando chat')

    def get(self):
        filename = get_chatdata(self)
        array_ini = arr_ini_contents(filename)
        console_log(f'ini contents: {array_ini}', 2)


    def __str__(self):
        string = f'id:{self.id}'
        string += f', title:{self.title}'
        string += f', description:{self.description}'
        string += f', date:{self.date}'
        return string
