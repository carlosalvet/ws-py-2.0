import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from helpers.user import user_new
from helpers.chat import chat_get
from helpers.session import session_new

users = set()
async def register(websocket):
    users.add(websocket)


async def unregister(websocket):
    users.remove(websocket)


async def open_connection(websocket, path):
    print('[DEBUG]', 'Conexión Abierta', end=" ")
    websocket_id = id(websocket)
    chat_id = path.split('/')[1]
    chat = chat_get(chat_id)

    await register(websocket)
    user = user_new(websocket_id, chat_id, 'visual')
    session = session_new(user, chat)

    response = {'user':user, 'chat': chat}
    print('[DEBUG]', 'Response open ws: ', response, 'OK')
    return response 


async def close_connection(websocket, error=None):
    if not error:
        print("Error: Conexión Cerrada", "[OK]")

    await unregister(websocket)

    if error: error_manage(error)


def error_manage(error):
    code = error.code or 0
    reason = error.reason or ""

    if code == 1005: print('Conexión Cerrada Correctamente', "[OK]" , code, reason) 

def pre_optional_data(request, response_open_conn):
    opt_data = response_open_conn
    #TODO añadir opcionalmentedatos del request al evento

    return opt_data 


