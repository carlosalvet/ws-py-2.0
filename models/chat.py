from core.console import console_log
from core.routes import get_chatdata_filename
from core.arrays import arr_ini_contents
import os

class Chat:

    def __init__(self):
        self.id = 0
        self.title = ''
        self.description = ''
        self.date = ''

    def save(self):
        print('creando chat #TODO')

    def get(self):
        filename = get_chatdata_filename(self.id)
        arr_ini = arr_ini_contents(filename)
        console_log(f'models.chat array_ini: {arr_ini}', 1)
        self.__formatting_object(arr_ini)
        console_log(f'models.chat get self: {self}', 1)
        return True
        
    def __formatting_object(self, arr_ini):
        if not 'data' in arr_ini:
            console_log('Archivo registro formato no válido, falta cabecera [data]', 2)
            return True

        arr_data = arr_ini['data']
        if 'title' in arr_data: self.title = arr_data['title']
        if 'description' in arr_data: self.description = arr_data['description']
        if 'date' in arr_data: self.date = arr_data['date']


    def __str__(self):
        string = f'id:{self.id}'
        string += f', title:{self.title}'
        string += f', description:{self.description}'
        string += f', date:{self.date}'
        return string
