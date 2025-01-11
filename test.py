import pika # type: ignore
import uuid
import os
import base64
from tools.scale.scale_message_request import ScaleMessageRequest
from tools.scale.scale_message_reply import ScaleMessageReply
from tools.brightness.brightness_message_request import BrightnessMessageRequest
from tools.brightness.brightness_message_reply import BrightnessMessageReply
from tools.border.border_message_request import BorderMessageRequest
from tools.border.border_message_reply import BorderMessageReply
from tools.rotate.rotate_message_request import RotateMessageRequest
from tools.rotate.rotate_message_reply import RotateMessageReply
from tools.ocr.ocr_message_request import OCRMessageRequest
from tools.ocr.ocr_message_reply import OCRMessageReply
from tools.crop.crop_message_reply import CropMessageReply
from tools.crop.crop_message_request import CropMessageRequest
from tools.contrast.contrast_message_reply import ContrastMessageReply
from tools.contrast.contrast_message_request import ContrastMessageRequest

IN = 'contrast_input_queue'
OUT = 'contrast_output_queue'
REPLY = ContrastMessageReply
REQUEST = ContrastMessageRequest
IMAGE_INPUT = './images/image-5.jpg'
IMAGE_OUTPUT = 'out.png'


RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
INPUT_QUEUE = os.getenv('INPUT_QUEUE', IN)
OUTPUT_QUEUE = os.getenv('INPUT_QUEUE', OUT)


def on_response(ch, method, props, body, correlation_id):

    if props.correlation_id == correlation_id:
        
        print('Received response image')
        reply = REPLY.from_json(body)

        with open(IMAGE_OUTPUT, 'wb') as output_file:
            output_file.write(base64.b64decode(reply.getImage()))

        ch.stop_consuming()


def send_image(image_path):

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=INPUT_QUEUE)
    channel.queue_declare(queue=OUTPUT_QUEUE)

    correlation_id = str(uuid.uuid4())

    with open(image_path, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    request = REQUEST(image_data,-1)

    channel.basic_publish(
        exchange='',
        routing_key=INPUT_QUEUE,
        body=request.to_json(),
        properties=pika.BasicProperties(
            reply_to=OUTPUT_QUEUE,
            correlation_id=correlation_id
        )
    )

    print(f'{image_path} sent to {INPUT_QUEUE} with correlation ID {correlation_id}')

    def consume_response(ch, method, props, body):
        on_response(ch, method, props, body, correlation_id)

    channel.basic_consume(
        queue=OUTPUT_QUEUE,
        on_message_callback=consume_response,
        auto_ack=True
    )

    print('Waiting for response...')
    channel.start_consuming()


if __name__ == '__main__':
    send_image(IMAGE_INPUT)