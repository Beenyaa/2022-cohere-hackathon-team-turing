import asyncio
import json
import websockets

async def echo(ws):
    await ws.send(json.dumps({'sender': 'Kurt', 'message': 'Bertil is nice'}))
    print(await ws.recv())

async def main():
    print("ABC")
    async with websockets.serve(echo, "localhost", 8000):
        print("KAH")
        await asyncio.Future()  # run forever

asyncio.run(main())