#! /usr/bin/env python3

import asyncio
import websockets
import json
from pathlib import Path
from core.events import open_connection, close_connection, process


"""
 await Esta directiva da un problema, si intento pasar como argumento a  otra 
       función async, la variable da problema en su tratamiento, es por eso
       que message no se llama dentro de la función consumer
"""

async def front_controller(websocket, path):

    try:
        await open_connection(websocket, path)
        async for request in websocket: 
            #request = html_request or await websocket.recv()
            await process(websocket, request)
        await close_connection(websocket)

    except websockets.ConnectionClosedError as error: 
        await close_connection(websocket, error)

# Open WebSocket server
async def main():
    async with websockets.serve(front_controller, "192.151.80.126", 8080):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
