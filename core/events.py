import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from events.base import pre_event_data


async def call_event(websocket, request, last_data=None):
    print(f'[DEBUG] Core call event request: {request}, last_data: {last_data}')
    response = {"event":""}
    websocket_id = websocket

    dict_headers, body = WsRequest.split(request)
    response['event'] = dict_headers['event']
    event_data = pre_event_data(dict_headers, last_data) 
    event_response = EventDispatcher.run(dict_headers["event"], body, event_data)
    response = event_response | response 
    str_response = Router.stringify(response)
    await websocket.send(str_response)
    print('[DEBUG]', f'event: {dict_headers["event"]}, Response: ', str_response)
