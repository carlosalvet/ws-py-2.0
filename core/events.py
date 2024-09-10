import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from events.base import pre_event_data
from security.funcs import filter_event_code


async def call_event(websocket, request, last_data=None):
    print(f'-----[DEBUG] Core call event request: {request}, last_data: {last_data}--')
    response = {}
    websocket_id = websocket

    dict_headers, body = WsRequest.split(request)
    event_code = dict_headers["event"] if 'event' in dict_headers else ''
    clean_code = filter_event_code(event_code)
    print('[E]', event_code)
    if event_code:
        event_data = pre_event_data(dict_headers, last_data) 
        event_response = EventDispatcher.run(event_code, body, event_data)
        response = event_response | response 
        str_response = Router.stringify(response)
        await websocket.send(str_response)
        print('[DEBUG]', f'event: {dict_headers["event"]}, Response: ', str_response)
    else: print('[ERROR]', f'El evento no existe o tiene un formato invalido: {dict_headers["event"]}')


