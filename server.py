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


"""
 await Esta directiva da un problema, si intento pasar como argumento a  otra 
       función async, la variable da problema en su tratamiento, es por eso
       que message no se llama dentro de la función consumer
"""

#request = html_request or await websocket.recv()
async def front_controller(websocket):
    if websocket:
        try:
            open_data = await open_connection(websocket)
            async for request in websocket: 
                await call_event(websocket, request, open_data)
            await close_connection(websocket, open_data)

        except websockets.ConnectionClosedError as error: 
            await close_connection(websocket, open_data, error)

# Open WebSocket server
async def main():
    async with websockets.serve(front_controller, "192.151.80.126", 8080):
    #async with websockets.serve(front_controller, "127.0.0.1", 8080):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
