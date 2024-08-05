from core.swrequest import WsRequest
from core.funcs import compose

class EventDispatcher():

    def __init__(html_request):
        strheader, strbody = WsRequest.html_request_split(html_request)
        headers = WsRequest.parse_headers(strheader)
        clazz, method, args = get_event_data(headers['event'])

        modulepath = f"events.{clazz}"
        namespace = self.__import__(modulepath)
        accout = getattr(namespace, clazz)
        func = getattr(accout, method)
