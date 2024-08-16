import sys
from config.app import SECTION_SEPARATOR, HEADER_SEPARTOR, ATTR_SEPARTOR 



class WsRequest():


    @staticmethod
    def split_sections(string):
        headers, body = string.split(SECTION_SEPARATOR, 1) 
        return headers, body


    @staticmethod
    def split(request):
        str_header, body = WsRequest.split_sections(request)
        dict_headers = WsRequest.parse_headers(str_header)
        print('[DEBUG]', 'Split request in headers and body', 'OK')
        return dict_headers, body

    @staticmethod
    def parse_headers(str_headers):
        arr_headers = WsRequest.__split_headers(str_headers)
        dict = WsRequest.__arrheaders_to_dict(arr_headers)
        return dict


    @staticmethod
    def parse_header(header):
        index, value = header.split(ATTR_SEPARTOR)
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
