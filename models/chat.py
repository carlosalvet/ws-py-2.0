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
