FROM python:3.12.3-slim

COPY . /app/picturas/tools/border

WORKDIR /app/picturas/tools/border

RUN apt update

RUN apt install ffmpeg -y

RUN pip install -r requirements.txt

ENV RABBITMQ_HOST=rabbitmq
ENV RABBITMQ_PORT=5672

ENV EXCHANGE=TOOL_EXCHANGE
ENV REQUEST_QUEUE=BORDER_REQUEST_QUEUE
ENV RESULTS_QUEUE=RESULTS_QUEUE

CMD ["python", "border_worker.py"]