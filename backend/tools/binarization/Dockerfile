FROM python:3.12.3-slim

COPY . /app/picturas/tools/binarization

WORKDIR /app/picturas/tools/binarization

RUN apt update

RUN apt install ffmpeg -y

RUN pip install -r requirements.txt

ENV RABBITMQ_HOST=rabbitmq
ENV RABBITMQ_PORT=5672

ENV EXCHANGE=TOOL_EXCHANGE
ENV REQUEST_QUEUE=BINARIZATION_REQUEST_QUEUE

ENV POOL_SIZE=5

CMD ["python", "binarization_worker.py"]