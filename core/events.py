import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from helpers.user import user_new

users = set()
async def register(websocket):
    users.add(websocket)


async def unregister(websocket):
    users.remove(websocket)


async def open_connection(websocket, path):
    websocket_id = id(websocket)
    chat_id = path.split('/')[1]
    print(f"[DEBUG]Open connection id {websocket_id}, path: {path}")

    await register(websocket)
    user = user_new(websocket_id, chat_id, 'citizen')
    print(f"[DEBUG]New user: ", user)
    return user


async def process_connection(websocket, message, user):
    print("------------------------------------------------------------------")
    print(f"[DEBUG]Initializing request process, message: {message}, user: {user}")

    #user.__init_()
    response = {"event":"chat-conversation", "header":"value", 'body':message}
    message_id = id(message)
    websocket_id = websocket

    headers, body = WsRequest.parse_request(message)
    response["body"] = EventDispatcher.run(headers['event'], headers, message)

    str_response = Router.stringify(response)
    await websocket.send(str_response)
    print(f"resquest response: {str_response}") 


async def close_connection(websocket, error=None):
    if not error:
        print("Error: Conexión Cerrada", "[OK]")

    await unregister(websocket)
    if error: error_manage(error)


def error_manage(error):
    code = error.code or 0
    reason = error.reason or ""

    if code == 1005: print('Conexión Cerrada Correctamente', "[OK]" , code, reason) 
