import json
from core.router import Router
from core.wsrequest import WsRequest
from core.eventdispatcher import EventDispatcher 
from core.console import console_log
from helpers.user import user_new
from helpers.chat import chat_get
from helpers.session import *

users = set()
async def register(websocket):
    users.add(websocket)


async def unregister(websocket):
    users.remove(websocket)


async def open_connection(websocket, path):
    print('---------------------------------')
    console_log(f'Conexión Abierta websocket: {id(websocket)}, path:{path}', 3)

    websocket_id = id(websocket)
    chat_id = path.split('/')[1]
    chat = chat_get(chat_id)

    await register(websocket)
    user = user_new(websocket_id, 'visual')
    user.chat_id = chat.id

    session = session_new(websocket_id)
    session.user = user
    session.chat = chat

    response = {'websocket_id': websocket_id, 'user':user, 'chat': chat}
    return response 


'''
'''
async def close_connection(websocket, opt_data={}, error=None):
    console_log(f'Cerrando Conexión id:{id(websocket)}, error: {error}', 1)
    websocket_id = id(websocket)
    session_destroy(websocket_id)

    if error: error_manage(error)
    else: console_log("Conexión Cerrada Inesperadamente", 4)


'''
'''
def error_manage(error):
    code = error.code or 0
    reason = error.reason or ""
    if code == 1005: 
        console_log('Conexión Cerrada Correctamente', 3) 
    else: 
        console_log('Conexión Cerrada Correctamente desconocida, code: {code}') 


'''
'''
def pre_event_data(headers, response_open_conn):
    console_log(f'AGREGANDO datos al request antes de despachar el event {headers} - ', 3)
    opt_data = response_open_conn
    opt_data['password'] = ''

    if (headers['event'] == 'user-login'):
        opt_data['role'] = headers['user-role']
        opt_data['username'] = headers['user-name']
        if opt_data['role'] == 'expert':
            opt_data['password'] = headers['user-pass']
    elif (headers['event'] == 'message_send'):
        print('...');

    console_log(f'DATOS AGREGADOS al request antes de despachar el event {opt_data} - ', 3)
    #TODO añadir opcionalmentedatos del request al evento

    return opt_data 
