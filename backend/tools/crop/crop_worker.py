import os
import json
import functools
import pika # type: ignore
from threading import Thread
from pika.exchange_type import ExchangeType # type: ignore
from crop_tool import CropTool
from crop_message_request import CropMessageRequest

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', '5672')

EXCHANGE=os.getenv('EXCHANGE', 'tools-exchange')
REQUEST_QUEUE = os.getenv('REQUEST_QUEUE', 'crop-queue')
RESULTS_QUEUE = os.getenv('RESULTS_QUEUE', 'results-queue')


class CropWorker:

    def __init__(self):
        self.parameters = pika.ConnectionParameters(host=RABBITMQ_HOST,port=RABBITMQ_PORT)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        self.workers = []


    def setup(self):
        self.channel.queue_declare(queue=REQUEST_QUEUE)
        self.channel.queue_declare(queue=RESULTS_QUEUE)

        self.channel.exchange_declare(
            exchange=EXCHANGE,
            exchange_type=ExchangeType.direct,
            durable=True)

        self.channel.queue_bind(
            queue=REQUEST_QUEUE,
            exchange=EXCHANGE,
            routing_key=REQUEST_QUEUE)

        self.channel.queue_bind(
            queue=RESULTS_QUEUE,
            exchange=EXCHANGE,
            routing_key=RESULTS_QUEUE)

        self.channel.basic_consume(
            queue=REQUEST_QUEUE,
            on_message_callback=self.on_request)


    def on_request(self, ch, method, properties, body):
        worker = Thread(target=self.worker_handle_request, args=(ch, method, properties, body))
        worker.start()
        self.workers.append(worker)


    def worker_handle_request(self, ch, method, properties, body):

        print(f'CropWorker received image: {properties.correlation_id}')
        request = CropMessageRequest.from_json(body.decode())
        tool = CropTool(request)
        response = tool.apply().to_json()

        self.channel.connection.add_callback_threadsafe(
            functools.partial(self.publish_response, ch, properties, response))

        self.channel.connection.add_callback_threadsafe(
            functools.partial(self.ack_message, ch, method.delivery_tag))


    def publish_response(self, ch, properties, response):
        ch.basic_publish(
            exchange=EXCHANGE,
            routing_key=properties.reply_to,
            body=json.dumps(response),
            properties=pika.BasicProperties(
                correlation_id=properties.correlation_id))
        print(f'CropWorker sent image: {properties.correlation_id}')


    def ack_message(self, ch, delivery_tag):
        ch.basic_ack(delivery_tag=delivery_tag)


    def start(self):
        self.setup()
        self.channel.start_consuming()
        for worker in self.workers:
             worker.join()


server = CropWorker()
server.start()