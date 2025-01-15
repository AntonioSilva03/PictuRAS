import os
import json
import base64
import uuid
import asyncio
import aio_pika # type: ignore
from pika.exchange_type import ExchangeType # type: ignore
from dotenv import load_dotenv # type: ignore
from utils.publisher import update_project_image

load_dotenv()

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 3003))

IMAGES_HOST = os.getenv('IMAGES_HOST', 'localhost')
IMAGES_PORT = int(os.getenv('IMAGES_PORT', 3002))


class ProcessorWorker:

    def __init__(self, websocket, project, requests, images, save_place):
        self.websocket = websocket
        self.project = project
        self.requests = requests
        self.images = images
        self.save_place = save_place
        self.ids = dict()
        self.exclusive_queue = str(uuid.uuid4())
        self.channel = None
        self.connection = None
        self.consumer_tag = None


    async def setup(self):

        self.connection = await aio_pika.connect_robust(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT)

        self.channel = await self.connection.channel()

        for request in self.requests:

            request_queue = await self.channel.declare_queue(request['request_queue'], durable=True)
            results_queue = await self.channel.declare_queue(self.exclusive_queue, durable=True)

            await self.channel.declare_exchange(
                request['exchange'],
                aio_pika.ExchangeType.DIRECT,
                durable=True)

            await request_queue.bind(
                exchange=request['exchange'],
                routing_key=request['request_queue'])

            await results_queue.bind(
                exchange=request['exchange'],
                routing_key=self.exclusive_queue)

        results_queue = await self.channel.get_queue(self.exclusive_queue)
        self.consumer_tag = await results_queue.consume(self.on_response)


    async def on_response(self, message: aio_pika.IncomingMessage):

        async with message.process():

            properties = message.properties

            if properties.correlation_id in self.ids:

                correlation_id = properties.correlation_id
                image_id = self.ids[correlation_id]

                self.images[image_id]['iterations'] += 1
                self.images[image_id]['data'] = json.loads(message.body.decode())['image']
                await self.update_progress()

                current_iteration = self.images[image_id]['iterations']
                print(f'Iteration {current_iteration}/{len(self.requests)}: {image_id}')

                if current_iteration < len(self.requests):

                    current_request = self.requests[current_iteration]
                    current_request['request']['image'] = self.images[image_id]['data']

                    await self.channel.default_exchange.publish(
                        aio_pika.Message(
                            body=json.dumps(current_request['request']).encode(),
                            reply_to=self.exclusive_queue,
                            correlation_id=correlation_id),
                        routing_key=current_request['request_queue'])

                if all(image['iterations'] == len(self.requests) for image in self.images.values()):

                    print(f'All project images processed: {self.project} -> {json.dumps(self.ids, indent=0)}')

                    results_queue = await self.channel.get_queue(self.exclusive_queue)
                    await results_queue.cancel(self.consumer_tag)
                    await results_queue.delete(if_unused=False, if_empty=False)
                    await self.save_results()


    async def update_progress(self):

        tasks_completed = 0
        tasks_total = len(self.requests) * len(self.images)

        for image_id in self.images:
            tasks_completed += self.images[image_id]['iterations']

        content = {"type": "progress", "progress": tasks_completed/tasks_total}
        await self.websocket.send(json.dumps(content))


    async def save_results(self):
        for image_id in self.images:
            image_data = base64.b64decode(self.images[image_id]['data'])
            update_project_image(IMAGES_HOST, IMAGES_PORT, self.project, image_id, image_data)
        await asyncio.sleep(0)


    async def start(self):

        if len(self.requests) > 0:

            await self.setup()

            for image_id in self.images:

                correlation_id = str(uuid.uuid4())
                self.ids[correlation_id] = image_id
                self.images[image_id]['iterations'] = 0
                self.images[image_id]['data'] = base64.b64encode(self.images[image_id]['data']).decode('utf-8')

                current_request = self.requests[0]
                current_request['request']['image'] = self.images[image_id]['data']

                await self.channel.default_exchange.publish(
                    aio_pika.Message(
                        body=json.dumps(current_request['request']).encode(),
                        reply_to=self.exclusive_queue,
                        correlation_id=correlation_id),
                    routing_key=current_request['request_queue'])

            print(f'Start processing project images: {self.project} -> {json.dumps(self.ids, indent=0)}')