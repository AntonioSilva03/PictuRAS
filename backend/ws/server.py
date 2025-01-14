import os
import json
import asyncio
from dotenv import load_dotenv # type: ignore
from websockets.asyncio.server import serve # type: ignore
from backend.ws.processor.processor import ProcessorWorker


class Server:

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port


    async def start(self) -> None:
        async with serve(Server.on_request, self.host, self.port) as server:
            print(f'WebSocket server started at ws://{self.host}:{self.port}')
            await server.serve_forever()


    async def on_request(websocket) -> None:
        async for message in websocket:
            try:
                request = json.loads(message)
                processorWorker = ProcessorWorker(websocket,request)
                await asyncio.create_task(processorWorker.start())

            except json.JSONDecodeError:
                print('Received invalid JSON')
                await websocket.send(json.dumps({'error': 'Invalid JSON'}))

            except Exception as e:
                await websocket.send(json.dumps({'error': f'{e}'}))


if __name__ == '__main__':

    load_dotenv()

    server = Server(
        host=os.getenv('SERVER_SOCKET_HOST', 'localhost'),
        port=int(os.getenv('SERVER_SOCKET_PORT', 8765)))

    asyncio.run(server.start())