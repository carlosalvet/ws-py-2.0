from core.funcs import compose
import json


class Router():

    def __init__(self):
        self.data
        return 0

    @staticmethod
    def stringify(array):
        arr = compose(array, dict)
        return json.dumps(arr)
