import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from events.base import pre_event_data
from security.funcs import filter_event_code, clean_headers, clean_body
from core.console import console_log


async def call_event(websocket, request, open_data=None):
    console_log('-----------------------------------------', 0)
    console_log(f'core.events.call_event request: {request} ', 3)
    console_log(f'core.events.call_event open_data: {open_data}, ', 3)
    response = {}
    websocket_id = id(websocket)
    headers, body = WsRequest.split(request)
    console_log(f'headers dictionary: {headers}, body: {body}', 3)
    event_code = headers.pop("event") if 'event' in headers else ''

    response['event'] = filter_event_code(event_code)
    cls_headers = clean_headers(headers)
    cls_body = clean_body(body)
    console_log(f'CLEAN DATA body: {cls_body}, headers: {cls_headers}, event code:{response["event"]}', 3)
    if response['event']:
        event_data = pre_event_data(response['event'], cls_headers, open_data) 
        response = EventDispatcher.call(response['event'], cls_body, event_data)
    else: 
        response['status'] = 500
        response['message'] = f'Petición incorrecta, código de evento no válido: ' + response['event']

    str_response = Router.stringify(response)
    await websocket.send(str_response)
