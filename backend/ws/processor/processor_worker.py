import os
import json
import base64
import asyncio
import aio_pika # type: ignore
from pika.exchange_type import ExchangeType # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 3003))


class ProcessorWorker:

    def __init__(self, websocket, requests, images, save_place):
        self.websocket = websocket
        self.requests = requests
        self.images = images
        self.save_place = save_place
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
            results_queue = await self.channel.declare_queue(request['results_queue'], durable=True)

            await self.channel.declare_exchange(
                request['exchange'],
                aio_pika.ExchangeType.DIRECT,
                durable=True)

            await request_queue.bind(
                exchange=request['exchange'],
                routing_key=request['request_queue'])

            await results_queue.bind(
                exchange=request['exchange'],
                routing_key=request['request_queue'])

        results_queue = await self.channel.get_queue(self.requests[0]['results_queue'])
        self.consumer_tag = await results_queue.consume(self.on_response)


    async def on_response(self, message: aio_pika.IncomingMessage):

        async with message.process():

            properties = message.properties

            if properties.correlation_id in self.images:

                image_id = properties.correlation_id

                self.images[image_id]['iterations'] += 1
                self.images[image_id]['data'] = json.loads(message.body.decode())['image']

                current_iteration = self.images[image_id]['iterations']

                if current_iteration < len(self.requests):
                    current_request = self.requests[current_iteration]
                    current_request['request']['image'] = self.images[image_id]['data']

                    await self.channel.default_exchange.publish(
                        aio_pika.Message(
                            body=json.dumps(current_request['request']).encode(),
                            reply_to=current_request['results_queue'],
                            correlation_id=image_id),
                        routing_key=current_request['request_queue'])

            if all(image['iterations'] == len(self.requests) for image in self.images.values()):

                print('All requests processed')

                results_queue = await self.channel.get_queue(self.requests[0]['results_queue'])
                await results_queue.cancel(self.consumer_tag)

                for image_id in self.images:
                    with open(image_id + '.png', 'wb') as file:
                        image_data = self.images[image_id]['data']
                        file.write(base64.b64decode(image_data))


    async def start(self):

        if len(self.requests) > 0:

            await self.setup()

            for image_id in self.images:

                self.images[image_id]['iterations'] = 0
                self.images[image_id]['data'] = base64.b64encode(self.images[image_id]['data']).decode('utf-8')

                current_request = self.requests[0]
                current_request['request']['image'] = self.images[image_id]['data']

                await self.channel.default_exchange.publish(
                    aio_pika.Message(
                        body=json.dumps(current_request['request']).encode(),
                        reply_to=current_request['results_queue'],
                        correlation_id=image_id),
                    routing_key=current_request['request_queue'])

            print('Start consuming...')

        await asyncio.Future() 