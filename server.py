#! /usr/bin/env python3

import settings
import asyncio
import websockets
import json
import unittest
from pathlib import Path
from core.events import call_event 
from events.base import open_connection, close_connection
from security.funcs import filter_event_code
from core.console import console_log


'''
'''
def _print_error(code=0, reason=''):
    if code == 0:
       console_log("Conexión Cerrada Inesperadamente", 4)
    if code == 1005: 
        console_log('Conexión Cerrada Correctamente', 3) 
    if code == 99999:
        console_log("No existe websocke al iniciar conexión", 4)
    else: 
        console_log('Conexión Cerrada Correctamente desconocida, code: {code}', 3) 


"""
 await Esta directiva da un problema, si intento pasar como argumento a  otra 
       función async, la variable da problema en su tratamiento, es por eso
       que message no se llama dentro de la función consumer
"""

#request = html_request or await websocket.recv()
# id(websocket) arroja un entero 'int'
async def front_controller(websocket):
    response_open_conn = ""
    if websocket:
        try:
            response_open_conn = await open_connection(websocket)
            async for request in websocket: 
                await call_event(websocket, request, response_open_conn)
            _print_error(0)

        except websockets.ConnectionClosedError as error: 
            code = error.code or 0
            reason = error.reason or ""
            _print_error(code, reason)
        finally: 
            await close_connection(websocket, response_open_conn)
    else:
      _print_error(99999)


# Open WebSocket server
async def main():
    async with websockets.serve(front_controller, "192.151.80.126", 8080):
    #async with websockets.serve(front_controller, "127.0.0.1", 8080):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
