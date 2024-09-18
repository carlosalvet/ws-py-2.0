import sys
from config.app import SECTION_SEPARATOR, HEADER_SEPARTOR, HEADER_NAME_SEPARATOR 


class WsRequest():


    @staticmethod
    def split_sections(string):
        sbstr = string.split(SECTION_SEPARATOR, 1) 
        sbstr = string.split(SECTION_SEPARATOR, 1)
        headers = sbstr[0]

        if len(sbstr) == 2: body = sbstr[1] 
        else: body =''

        return headers, body


    """ 
        Split and format the headers in an array
    """
    @staticmethod
    def split(request):
        str_header, body = WsRequest.split_sections(request)
        dict_headers = WsRequest.format_headers(str_header)
        print('[DEBUG]', f'Split request in headers:{dict_headers}, body:{body}')
        return dict_headers, body

    @staticmethod
    def format_headers(str_headers):
        arr_headers = WsRequest.__split_headers(str_headers)
        dict = WsRequest.__arrheaders_to_dict(arr_headers)
        return dict


    @staticmethod
    def parse_header(header):
        index, value = header.split(HEADER_NAME_SEPARATOR)
        return  index, value


    def __split_headers(str_headers):
        headers = str_headers.split(HEADER_SEPARTOR)
        return headers


    def __arrheaders_to_dict(arr_headers):
        dict_headers = dict()
        for header in arr_headers:
            index, value = WsRequest.parse_header(header)
            dict_headers[index] = value
        return dict_headers
