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
        if not request: return ('', '')
        str_header, body = WsRequest.split_sections(request)
        dict_headers = WsRequest.format_headers(str_header)
        return dict_headers, body

    @staticmethod
    def format_headers(str_headers):
        arr_headers = WsRequest.__split_headers(str_headers)
        dict = WsRequest.__arrheaders_to_dict(arr_headers)
        return dict


    def __split_headers(str_headers):
        arr_headers = str_headers.split(HEADER_SEPARTOR)
        return arr_headers


    def __arrheaders_to_dict(arr_headers):
        dict_headers = dict()
        for header in arr_headers:
            index, value = WsRequest.parse_header(header)
            dict_headers[index] = value
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
