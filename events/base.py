import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from helpers.user import user_new
from helpers.chat import chat_get
from helpers.session import session_new, session_destroy, session_destroy

users = set()
async def register(websocket):
    users.add(websocket)


async def unregister(websocket):
    users.remove(websocket)


async def open_connection(websocket, path):
    print('---------------------------------')
    print('[DEBUG]', 'Conexión Abierta', end=" ")
    chat_id = path.split('/')[1]
    chat = chat_get(chat_id)

    await register(websocket)
    user = user_new(websocket, chat, 'visual')
    session = session_new(user, chat)

    response = {'user':user, 'chat': chat}
    print('[DEBUG]', 'Response open ws: ', response, 'OK')
    return response 


async def close_connection(websocket, opt_data={}, error=None):
    print('[DEBUG]',f'Cerrando Conexión", opt_data: {opt_data}')
    user = opt_data['user']
    chat = opt_data['chat']

    await unregister(websocket)
    session_destroy(user, chat)

    if error: error_manage(error)

    if not error:
        print("Error: Conexión Cerrada", "[OK]")


def error_manage(error):
    code = error.code or 0
    reason = error.reason or ""

    if code == 1005: print('Conexión Cerrada Correctamente', "[OK]" , code, reason) 


def pre_event_data(headers, response_open_conn):
    print('[DEBUG]', f'AGREGANDO datos al request antes de despachar el event', f'{headers} - ', response_open_conn)
    opt_data = response_open_conn

    if (headers['event'] == 'user-login'):
        opt_data['role'] = headers['user-role'] or 'visual' 
        opt_data['username'] = headers['user-name'] or '' 
        print('hola mundo desde user-login')

    #TODO añadir opcionalmentedatos del request al evento

    return opt_data 


