class Chat:

    def __init__(self):
        self.id = 0
        self.title = ''
        self.description = ''
        self.date = ''

    def save(self):
        print('creando chat')

    def get(self):
        print(f'obteniendo chat desde {self.id}')

    def __str__(self):
        string = f'id:{self.id}'
        string += f', title:{self.title}'
        string += f', description:{self.description}'
        string += f', date:{self.date}'
        return string
