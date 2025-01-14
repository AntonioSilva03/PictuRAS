FROM python:3.12.3-slim

COPY . /app/picturas/tools/rotate

WORKDIR /app/picturas/tools/rotate

RUN apt update

RUN apt install ffmpeg -y

RUN pip install -r requirements.txt

ENV RABBITMQ_HOST=rabbitmq
ENV RABBITMQ_PORT=5672

ENV EXCHANGE=TOOL_EXCHANGE
ENV REQUEST_QUEUE=ROTATE_REQUEST_QUEUE
ENV RESULTS_QUEUE=RESULTS_QUEUE

CMD ["python", "rotate_worker.py"]