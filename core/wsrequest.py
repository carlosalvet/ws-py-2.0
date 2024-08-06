import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


class WsRequest():


    def split_sections(string):
        headers, body = string.split("\n\n", 1) 
        return headers, body


    def parse_request(request):
        str_header, body = WsRequest.split_sections(request)
        dict_headers = WsRequest.parse_headers(str_header)
        return dict_headers, body

    def parse_headers(str_headers):
        arr_headers = WsRequest.__split_headers(str_headers)
        dict = WsRequest.__arrheaders_to_dict(arr_headers)
        return dict


    def parse_header(header):
        index, value = header.split(":")
        return  index, value


    def __split_headers(str_headers):
        headers = str_headers.split("\n")
        return headers


    def __arrheaders_to_dict(arr_headers):
        dict_headers = dict()
        for header in arr_headers:
            index, value = WsRequest.parse_header(header)
            dict_headers[index] = value
        return dict_headers
