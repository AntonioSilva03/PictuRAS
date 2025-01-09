import pika # type: ignore
import json
import os
from scale_message_request import ScaleMessageRequest
from scale_tool import ScaleTool

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
SCALE_INPUT_QUEUE = os.getenv('SCALE_INPUT_QUEUE', 'scale_input_queue')


def on_message(channel, method, properties, body):

    print('Received image for processing')

    body = json.loads(body)
    scale_request = ScaleMessageRequest.from_dict(body)

    scale_tool = ScaleTool(scale_request)
    scale_reply = scale_tool.apply()

    body = json.dumps(scale_reply.to_dict())

    channel.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        body=body,
        properties=pika.BasicProperties(
            correlation_id=properties.correlation_id
        )
    )

    print('Processed image sent to response queue')
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=SCALE_INPUT_QUEUE)
    channel.basic_consume(queue=SCALE_INPUT_QUEUE, on_message_callback=on_message)

    print(f'Waiting for images on {SCALE_INPUT_QUEUE}...')
    channel.start_consuming()


if __name__ == '__main__':
    main()