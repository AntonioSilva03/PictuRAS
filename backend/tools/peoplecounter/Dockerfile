FROM python:3.12.3-slim

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/picturas/tools/peoplecounter

WORKDIR /app/picturas/tools/peoplecounter

RUN pip install -r requirements.txt

ENV RABBITMQ_HOST=rabbitmq
ENV RABBITMQ_PORT=5672
ENV EXCHANGE=TOOL_EXCHANGE
ENV REQUEST_QUEUE=PEOPLECOUNTER_REQUEST_QUEUE

ENV POOL_SIZE=5

CMD ["python", "pc_worker.py"]