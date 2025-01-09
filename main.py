import pika # type: ignore
import uuid
import json
import os
import base64
from tools.scale.scale_message_request import ScaleMessageRequest
from tools.scale.scale_message_reply import ScaleMessageReply

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
SCALE_INPUT_QUEUE = os.getenv("SCALE_INPUT_QUEUE", "scale_input_queue")
SCALE_OUTPUT_QUEUE = os.getenv("SCALE_INPUT_QUEUE", "scale_output_queue")


def on_response(ch, method, props, body, correlation_id):

    if props.correlation_id == correlation_id:
        
        print("Received response image")
        reply = ScaleMessageReply.from_json(body)

        with open("received_image.png", 'wb') as output_file:
            output_file.write(base64.b64decode(reply.getImage()))

        ch.stop_consuming()


def send_image(image_path):

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=SCALE_INPUT_QUEUE)
    channel.queue_declare(queue=SCALE_OUTPUT_QUEUE)

    correlation_id = str(uuid.uuid4())

    with open(image_path, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    request = ScaleMessageRequest(image_data,100,100)

    channel.basic_publish(
        exchange='',
        routing_key=SCALE_INPUT_QUEUE,
        body=request.to_json(),
        properties=pika.BasicProperties(
            reply_to=SCALE_OUTPUT_QUEUE,
            correlation_id=correlation_id
        )
    )

    print(f"{image_path} sent to {SCALE_INPUT_QUEUE} with correlation ID {correlation_id}")

    def consume_response(ch, method, props, body):
        on_response(ch, method, props, body, correlation_id)

    channel.basic_consume(
        queue=SCALE_OUTPUT_QUEUE,
        on_message_callback=consume_response,
        auto_ack=True
    )

    print("Waiting for response...")
    channel.start_consuming()


if __name__ == "__main__":
    send_image("./images/image-1.jpg")