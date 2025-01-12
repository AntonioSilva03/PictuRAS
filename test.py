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
from tools.rembg.rembg_message_request import RembgMessageRequest
from tools.rembg.rembg_message_reply import RembgMessageReply
from tools.peoplecounter.pc_message_request import PeopleCountingMessageRequest
from tools.peoplecounter.pc_message_reply import PeopleCountingMessageReply
from tools.objectcounter.oc_message_request import ObjectCountingMessageRequest
from tools.objectcounter.oc_message_reply import ObjectCountingMessageReply
from tools.watermark.watermark_message_request import WatermarkMessageRequest
from tools.watermark.watermark_message_reply import WatermarkMessageReply

IN = 'watermark_input_queue'
OUT = 'watermark_output_queue'
REPLY = WatermarkMessageReply
REQUEST = WatermarkMessageRequest
IMAGE_INPUT = './images/image-12.jpg'
IMAGE_OUTPUT = 'out'


RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
INPUT_QUEUE = os.getenv('INPUT_QUEUE', IN)
OUTPUT_QUEUE = os.getenv('INPUT_QUEUE', OUT)


def on_response(ch, method, props, body, correlation_id):
    if props.correlation_id == correlation_id:
        print('Received response')

    try:
        # Deserialize the response
        reply = REPLY.from_json(body)

        # Check the type of the reply
        if hasattr(reply, 'getPeopleCount'):  # It's a people count response
            people_count = reply.getPeopleCount()

            # Add '.txt' extension to IMAGE_OUTPUT for text responses
            output_file_path = f"{IMAGE_OUTPUT}.txt"

            # Write the count to a text file
            with open(output_file_path, 'w') as output_file:
                output_file.write(f'{people_count}')

        elif hasattr(reply, 'getObjectCounts'):  # It's an object count response
            object_counts = reply.getObjectCounts()

            # Add '.txt' extension to IMAGE_OUTPUT for object counts
            output_file_path = f"{IMAGE_OUTPUT}.txt"

            # Write the object counts to a text file
            with open(output_file_path, 'w') as output_file:
                for obj, count in object_counts.items():
                    output_file.write(f'{obj}: {count}\n')

        elif hasattr(reply, 'getText'):  # It's a text response
            text = reply.getText()

            # Add '.txt' extension to IMAGE_OUTPUT for text responses
            output_file_path = f"{IMAGE_OUTPUT}.txt"

            # Write the text to a text file
            with open(output_file_path, 'w') as output_file:
                output_file.write(text)

        elif hasattr(reply, 'getImage'):  # It's an image response
            image_data = reply.getImage()

            # Add '.png' extension to IMAGE_OUTPUT for image responses
            output_file_path = f"{IMAGE_OUTPUT}.png"

            # Write the image to an output file
            with open(output_file_path, 'wb') as output_file:
                output_file.write(base64.b64decode(image_data))
        else:
            print("Unrecognized response format.")

    except Exception as e:
        print(f"Error processing response: {e}")

    ch.stop_consuming()


def send_image(image_path):

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=INPUT_QUEUE)
    channel.queue_declare(queue=OUTPUT_QUEUE)

    correlation_id = str(uuid.uuid4())

    with open(image_path, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    request = REQUEST(image_data)

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