import unittest
from config import ATTR_SEPARTOR

from core.wsrequest import WsRequest

def test_parse_headers():
    html_request = "chat-id:2\nchat-date:2022-06-30\nevent:chat-conversation\mode:0\n\nhola cara de bolota"
    ws_request = WsRequest()
    dict_request = ws_request.parse_headers(html_request)
    print("dict_request: ", dict_request)

test_parse_headers()


