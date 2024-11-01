import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from events.base import pre_event_data
from security.funcs import filter_event_code, clean_headers
from core.console import console_log


async def call_event(websocket, request, open_data=None):
    console_log('-----------------------------------------', 0)
    console_log(f'core.events.call_event request: {request} ', 3)
    console_log(f'core.events.call_event open_data: {open_data}, ', 3)
    response = {'event':'', 'status': 500}
    websocket_id = id(websocket)
    headers, body = WsRequest.split(request)
    event_code = headers.pop("event") if 'event' in headers else ''

    cls_event_code = filter_event_code(event_code)
    cls_headers = clean_headers(headers)
    console_log(f'event_code: {event_code}, clean code: {cls_event_code}')
    if cls_event_code:
        event_data = pre_event_data(cls_event_code, headers, open_data) 
        response = EventDispatcher.call(cls_event_code, body, event_data)
    else: 
        response['message'] = f'Petición incorrecta, código de evento no válido: "{cls_event_code}"'

    str_response = Router.stringify(response)
    await websocket.send(str_response)
