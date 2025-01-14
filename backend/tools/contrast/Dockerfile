FROM python:3.12.3-slim

COPY . /app/picturas/tools/contrast

WORKDIR /app/picturas/tools/contrast

RUN apt update

RUN apt install ffmpeg -y

RUN pip install -r requirements.txt

ENV RABBITMQ_HOST=rabbitmq
ENV RABBITMQ_PORT=5672

ENV EXCHANGE=TOOL_EXCHANGE
ENV REQUEST_QUEUE=CONTRAST_REQUEST_QUEUE
ENV RESULTS_QUEUE=RESULTS_QUEUE

CMD ["python", "contrast_worker.py"]