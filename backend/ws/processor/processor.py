import os
import json
import asyncio
from dotenv import load_dotenv # type: ignore
from utils.preparer import get_prepared_requets
from utils.fetch import get_image_data, get_project, get_project_images
from processor.processor_worker import ProcessorWorker

load_dotenv()

IMAGES_HOST = os.getenv('IMAGES_HOST', 'localhost')
IMAGES_PORT = int(os.getenv('IMAGES_PORT', 3002))

PROJECTS_HOST = os.getenv('PROJECTS_HOST', 'localhost')
PROJECTS_PORT = int(os.getenv('PROJECTS_PORT', 3003))


class Processor:

    def __init__(self, websocket, request):
        self.request = request
        self.websocket = websocket
        self.handlers = {
            'process': lambda websocket, request : Processor.process_project(websocket, request),
            'preview': lambda websocket, request : Processor.process_preview(websocket, request),
            'cancel': lambda websocket, request : Processor.process_cancel(websocket, request),
            'error': lambda websocket, request : Processor.process_error(websocket, request),
        }


    async def process_project(websocket, request):

        project = get_project(PROJECTS_HOST, PROJECTS_PORT, request['project'])
        images = get_project_images(IMAGES_HOST, IMAGES_PORT, request['project'])
        images = {image['id']: {'data': get_image_data(IMAGES_HOST, IMAGES_PORT, image['id'])} for image in images}

        bus_requests = get_prepared_requets(project['tools'])
        print(json.dumps(bus_requests, indent=4))

        processorWorker = ProcessorWorker(websocket, request['project'], bus_requests, images, True)
        await processorWorker.start()


    async def process_preview(websocket, request):

        project = get_project(PROJECTS_HOST, PROJECTS_PORT, request['project'])
        images = {request['image']: {'data': get_image_data(IMAGES_HOST, IMAGES_PORT, request['image'])}}

        bus_requests = get_prepared_requets(project['tools'])
        print(json.dumps(bus_requests, indent=4))

        processorWorker = ProcessorWorker(websocket, request['project'], bus_requests, images, False) 
        await processorWorker.start()


    async def process_cancel(websocket, request):
        project = request['project']
        print('Not implemented')
        print(f'Canceling project: {project}')
        await asyncio.sleep(0)


    async def process_error(websocket, request):
        error = request['error']
        print(f'Error: {error}')
        await asyncio.sleep(0)


    async def start(self):
        type = self.request['type']
        handler = self.handlers.get(type)
        await handler(self.websocket,self.request)