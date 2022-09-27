#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        await websocket.send("client2-Hello-")
        print(await websocket.recv())

asyncio.run(hello())
