import pika # type: ignore
import os
from rotate_tool import RotateTool
from rotate_message_request import RotateMessageRequest
import traceback

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
ROTATE_INPUT_QUEUE = os.getenv('ROTATE_INPUT_QUEUE', 'rotate_input_queue')


def on_message(channel, method, properties, body):

    try:
        print('Received image for processing')
        rotate_request = RotateMessageRequest.from_json(body)
        rotate_tool = RotateTool(rotate_request)
        rotate_reply = rotate_tool.apply()

        channel.basic_publish(
            exchange='',
            routing_key=properties.reply_to,
            body=rotate_reply.to_json(),
            properties=pika.BasicProperties(
                correlation_id=properties.correlation_id
            )
        )

        print('Processed image sent to response queue')
        channel.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        traceback.print_exc()
        print(f'Error processing message: {e}')
        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)


def main():

    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()

        channel.queue_declare(queue=ROTATE_INPUT_QUEUE)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=ROTATE_INPUT_QUEUE, on_message_callback=on_message)

        print(f'Waiting for images on {ROTATE_INPUT_QUEUE}...')
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as e:
        print(f'Connection failed: {e}')

    except KeyboardInterrupt:
        print("Exiting...")
        connection.close()


if __name__ == '__main__':
    main()