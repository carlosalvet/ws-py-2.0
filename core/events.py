import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from events.base import pre_event_data
from security.funcs import filter_event_code
from core.console import console_log


async def call_event(websocket, request, extra_data=None):
    console_log('-----------------------------------------', 0)
    console_log(f'core.events.call_event request: {request} ', 3)
    console_log(f'core.events.call_event extra_data: {extra_data}, ', 3)
    response = {}
    websocket_id = id(websocket)
    dict_headers, body = WsRequest.split(request)
    event_code = dict_headers["event"] if 'event' in dict_headers else ''

    clean_code = filter_event_code(event_code)
    if event_code:
        event_data = pre_event_data(dict_headers, extra_data) 
        event_response = EventDispatcher.run(event_code, body, event_data)
        response = event_response 
        str_response = Router.stringify(response)
        await websocket.send(str_response)
    else: console_log(f'El evento no existe o tiene un formato no válido: {event_code}', 4)


