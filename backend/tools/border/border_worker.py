import os
import functools
import pika # type: ignore
from threading import Thread
from pika.exchange_type import ExchangeType # type: ignore
from border_tool import BorderTool
from border_message_request import BorderMessageRequest
import time

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', '5672')

EXCHANGE=os.getenv('EXCHANGE', 'tools-exchange')
REQUEST_QUEUE = os.getenv('REQUEST_QUEUE', 'border-queue')


class BorderWorker:

    def __init__(self):
        self.parameters = pika.ConnectionParameters(host=RABBITMQ_HOST,port=RABBITMQ_PORT)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        self.workers = []


    def setup(self):

        self.channel.queue_declare(queue=REQUEST_QUEUE, durable=True)

        self.channel.exchange_declare(
            exchange=EXCHANGE,
            exchange_type=ExchangeType.direct,
            durable=True)

        self.channel.queue_bind(
            queue=REQUEST_QUEUE,
            exchange=EXCHANGE,
            routing_key=REQUEST_QUEUE)

        self.channel.basic_consume(
            queue=REQUEST_QUEUE,
            on_message_callback=functools.partial(self.on_request))


    def on_request(self, ch, method, properties, body):
        worker = Thread(target=BorderWorker.worker_handle_request, args=(ch, method, properties, body))
        worker.start()
        self.workers.append(worker)


    def worker_handle_request(ch, method, properties, body):

        print(f'BorderWorker received image: {properties.correlation_id}')
        request = BorderMessageRequest.from_json(body.decode())
        tool = BorderTool(request)
        response = tool.apply().to_json()

        print(f'Before sleep: {properties.correlation_id}')
        time.sleep(10)
        print(f'After sleep: {properties.correlation_id}')

        ch.connection.add_callback_threadsafe(
            functools.partial(BorderWorker.publish_response, ch, properties, response))

        ch.connection.add_callback_threadsafe(
            functools.partial(BorderWorker.ack_message, ch, method.delivery_tag))


    def publish_response(ch, properties, response):
        ch.basic_publish(
            exchange=EXCHANGE,
            routing_key=properties.reply_to,
            body=response.encode(),
            properties=pika.BasicProperties(
                correlation_id=properties.correlation_id))
        print(f'BorderWorker sent image: {properties.correlation_id}')


    def ack_message(ch, delivery_tag):
        ch.basic_ack(delivery_tag=delivery_tag)


    def start(self):
        self.setup()
        self.channel.start_consuming()
        for worker in self.workers:
             worker.join()


if __name__ == '__main__':
    server = BorderWorker()
    print('BorderWorker start consuming...')
    server.start()