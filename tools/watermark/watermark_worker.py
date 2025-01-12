import pika  # type: ignore
import os
from watermark_message_request import WatermarkMessageRequest
from watermark_tool import WatermarkTool
from watermark_message_reply import WatermarkMessageReply

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
WATERMARK_INPUT_QUEUE = os.getenv('WATERMARK_INPUT_QUEUE', 'watermark_input_queue')
WATERMARK_IMAGE_PATH = os.getenv('WATERMARK_IMAGE_PATH', 'watermark.png')


def on_message(channel, method, properties, body):
    try:
        print('Received image for watermarking')

        # Parse the incoming message
        watermark_request = WatermarkMessageRequest.from_json(body)
        watermark_tool = WatermarkTool(watermark_image_path=WATERMARK_IMAGE_PATH)
        watermark_reply = watermark_tool.apply(watermark_request)

        # Publish the response to the reply queue
        channel.basic_publish(
            exchange='',
            routing_key=properties.reply_to,
            body=watermark_reply.to_json(),
            properties=pika.BasicProperties(
                correlation_id=properties.correlation_id
            )
        )

        print('Processed watermarked image sent to response queue')
        channel.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(f'Error processing message: {e}')
        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

def main():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()

        channel.queue_declare(queue=WATERMARK_INPUT_QUEUE)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=WATERMARK_INPUT_QUEUE, on_message_callback=on_message)

        print(f'Waiting for images on {WATERMARK_INPUT_QUEUE}...')
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as e:
        print(f'Connection failed: {e}')

    except KeyboardInterrupt:
        print("Exiting...")
        connection.close()

if __name__ == '__main__':
    main()