import pika # type: ignore
import os
from contrast_tool import ContrastTool
from contrast_message_request import ContrastMessageRequest
import traceback


RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
CONTRAST_INPUT_QUEUE = os.getenv('CONTRAST_INPUT_QUEUE', 'contrast_input_queue')


def on_message(channel, method, properties, body):

    try:
        print('Received image for processing')
        contrast_request = ContrastMessageRequest.from_json(body)
        contrast_tool = ContrastTool(contrast_request)
        contrast_reply = contrast_tool.apply()

        channel.basic_publish(
            exchange='',
            routing_key=properties.reply_to,
            body=contrast_reply.to_json(),
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

        channel.queue_declare(queue=CONTRAST_INPUT_QUEUE)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=CONTRAST_INPUT_QUEUE, on_message_callback=on_message)

        print(f'Waiting for images on {CONTRAST_INPUT_QUEUE}...')
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as e:
        print(f'Connection failed: {e}')

    except KeyboardInterrupt:
        print("Exiting...")
        connection.close()


if __name__ == '__main__':
    main()