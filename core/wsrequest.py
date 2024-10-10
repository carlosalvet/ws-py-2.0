import sys
from config.app import SECTION_SEPARATOR, HEADER_SEPARTOR, HEADER_NAME_SEPARATOR 


class WsRequest():


    @staticmethod
    def split_sections(string):
        body =''

        sbstr = string.split(SECTION_SEPARATOR, 1) 
        headers = sbstr[0]

        if len(sbstr) == 2: body = sbstr[1] 
        return headers, body


    """ 
        Split and format the headers in an array
    """
    @staticmethod
    def split(request):
        str_header, body = WsRequest.split_sections(request)
        dict_headers = WsRequest.dict_headers(str_header)
        return dict_headers, body

    @staticmethod
    def dict_headers(str_headers):
        arr_headers = str_headers.split(HEADER_SEPARTOR)
        dict_headers = WsRequest.__arrheaders_to_dict(arr_headers)
        return dict_headers


    """
        Se ingresa la cadena de texto del request que corresponde a las 
        cabeceras, y esta la guarda en un diccionario donde cada registro
        es el elemento separado por \n y la clave y valor son los que estón
        separados por ':'
        @str_headers 'Header1:value1\nHeader2:value2'
        @return arr {'Header1':'value1',·'Header2':'value2'}
    """
    def __arrheaders_to_dict(arr_headers):
        dict_headers = dict()
        for header in arr_headers:
            index, value = WsRequest.parse_header(header)
            if index and value: dict_headers[index] = value
        return dict_headers


    @staticmethod
    def parse_header(header):
        parts = header.split(HEADER_NAME_SEPARATOR, 1)
        if not len(parts) == 2: return ('', '')
        return  parts[0], parts[1] 


if __name__ == '__main__':
    request = '\n\ncontentbody'
    splited = WsRequest.split(request)
    print(splited)
