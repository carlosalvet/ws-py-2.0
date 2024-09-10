#! /usr/bin/env python3

import asyncio
import websockets
import json
import unittest
from pathlib import Path
from core.events import call_event 
from events.base import open_connection, close_connection
from security.funcs import filter_event_code


"""
 await Esta directiva da un problema, si intento pasar como argumento a  otra 
       función async, la variable da problema en su tratamiento, es por eso
       que message no se llama dentro de la función consumer
"""

#request = html_request or await websocket.recv()
async def front_controller(websocket, path):

    try:
        response_opened_conn = await open_connection(websocket, path)
        async for request in websocket: 
            await call_event(websocket, request, response_opened_conn)
        await close_connection(websocket, response_opened_conn)

    except websockets.ConnectionClosedError as error: 
        await close_connection(websocket, response_opened_conn, error)

# Open WebSocket server
async def main():
    async with websockets.serve(front_controller, "192.151.80.126", 8080):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
