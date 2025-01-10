import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from events.base import filter_response_open_conn
from security.funcs import filter_event_code, clean_headers, clean_body
from core.console import console_log


# r_open_conn == response_open_conn
async def call_event(websocket, request, r_open_conn=None):
    console_log('-----------------------------------------', 0)
    console_log(f'core.events.call_event request: {request} ', 3)
    #console_log(f'core.events.call_event r_open_conn: {r_open_conn}, ', 3)
    response = {'status':'500'}
    websocket_id = id(websocket)
    headers, body = WsRequest.split(request)
    #console_log(f'headers dictionary: {headers}, body: {body}', 3)
    event_code = headers.pop("event") if 'event' in headers else ''

    response['event'] = filter_event_code(event_code)
    cls_headers = clean_headers(headers)
    cls_body = clean_body(body)
    event = response['event'] if 'event' in response else ''
    #console_log(f'CLEAN DATA body: {cls_body}, headers: {cls_headers}, event code:{event}', 3)
    if event:
        event_data = filter_response_open_conn(event, cls_headers, r_open_conn) 
        response = EventDispatcher.call(event, cls_body, event_data)
    else: 
        response['message'] = f'Petición incorrecta, código de evento no válido: ' + event 

    str_response = Router.stringify(response)
    await websocket.send(str_response)
