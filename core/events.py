import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from events.base import pre_optional_data


async def call_event(websocket, request, response_open_conn=None):
    print('[DEBUG] Evento Llamado', request, response_open_conn, 'OK' )
    response = {"event":"chat-conversation", 'body':''}
    websocket_id = websocket

    headers, body = WsRequest.split(request)
    opt_data = pre_optional_data(request, response_open_conn) 
    response["body"] = EventDispatcher.run(headers["event"], body, opt_data)
    str_response = Router.stringify(response)
    await websocket.send(str_response)
    print('[DEBUG]', f'Response {headers["event"]}: ', str_response)
