import os
import json
from utils.fetch import *
from utils.preparer import get_prepared_requets

PROJECTS_HOST = os.getenv('PROJECTS_HOST', 'localhost')
PROJECTS_PORT = os.getenv('PROJECTS_PORT', 3003)

class Processor:

    def __init__(self, websocket, request):
        self.request = request
        self.websocket = websocket
        self.handlers = {
            'process_project': lambda websocket, request : Processor.process_project(websocket, request),
            'process_preview': lambda websocket, request : Processor.process_preview(websocket, request),
            'cancel': lambda websocket, request : Processor.process_cancel(websocket, request),
            'error': lambda websocket, request : Processor.process_error(websocket, request),
        }


    async def process_project(websocket, request):

        project = get_project(request['project'])
        images = get_project_images(request['project'])

        images_data = [(image['id'],get_image_data(image['id'])) for image in images]
        bus_requests = get_prepared_requets(project['tools'])

        ### CRIAR UMA NOVA CLASS
        #### images_data = class(websocket,bus_requests,images_data)
        ## esta merda tem de devolver (id, bytes) a conversão de e para base64 é dentro da class

        ### FAZER PUT DAS NOVAS IMAGENS


    async def process_preview(websocket, request):

        project = get_project(request['project'])
        images = get_project_images(request['project'])

        images_data = [(image['id'],get_image_data(image['id'])) for image in images]
        bus_requests = get_prepared_requets(project['tools'])

        ### CRIAR UMA NOVA CLASS
        #### images_data = class(websocket,bus_requests,images_data)
        ## esta merda tem de devolver (id, bytes) a conversão de e para base64 é dentro da class

        ### FAZER POST NA COLLEÇÃO DE PREVIEW


    async def process_cancel(websocket, request):
        project = request['project']
        print(f'Cancel project {project}')
        print('Not implemented')


    async def process_error(websocket, request):
        error = request['error']
        print(f'{error}')
        await websocket.send(json.dumps({'error': error}))


    async def start(self):
        type = self.request['type']
        handler = self.handlers.get(type)
        await handler(self.websocket,self.request)