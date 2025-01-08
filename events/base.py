import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from core.console import console_log
from helpers.user import user_new
from helpers.chat import _chat_get
from helpers.session import session_create, session_destroy

users = set()
async def register(websocket):
    users.add(websocket)

async def unregister(websocket):
    users.remove(websocket)


async def open_connection(websocket):
    print('---------------------------------')
    console_log(f'Conexión Abierta websocket: {id(websocket)}', 3)
    await register(websocket)

    websocket_id = id(websocket)
    if websocket_id: 
        user = user_new(websocket_id, 'visual')
        session = session_create(websocket_id, user)
    else: 
        ''

    response = {'websocket_id': websocket_id}
    return response 


'''
'''
async def close_connection(websocket, opt_data={}):
    console_log(f'Cerrando Conexión id:{id(websocket)}', 1)
    websocket_id = id(websocket)
    session_destroy(websocket_id)


'''
'''
def filter_response_open_conn(event_code, headers, response_open_conn):
    console_log(f'AGREGANDO headers al request antes de despachar el event {headers}, {response_open_conn}', 3)
    opt_data = response_open_conn

    if (event_code == 'user-login'):
        opt_data['role'] = headers['user-role']
        opt_data['username'] = headers['user-name']
        if opt_data['role'] == 'expert':
            opt_data['password'] = headers['user-pass']
    elif (event_code == 'chat-get'):
        opt_data['chat-id'] = headers['chat-id']

    else:
        print('...');

    console_log(f'HEADERS AGREGADOS al request antes de despachar el event {opt_data} - ', 3)
    #TODO añadir opcionalmentedatos del request al evento

    return opt_data 
