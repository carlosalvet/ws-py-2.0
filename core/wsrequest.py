from config.py import ATTR_SEPARTOR

class WsRequest:

    def __init__():

    def parse_headers(self, str_headers):
        headers = str_headers.split("ATTR_SEPARATOR") 
        dict_header = dict()

        for header in headers:
            index, value = header.split(":")
            dict_header[index] = value

        dict_headers = #TODO implementación que dará valor
        clean_headers(dict_headers);


    def get_event_data(self, event)
        return args['clazz'], args['method'], args['args']


    def clean_headers(arr_headers):
