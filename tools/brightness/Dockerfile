FROM border-base

COPY . /app/picturas/tools/brightness

WORKDIR /app/picturas/tools/brightness

RUN pip install -r requirements.txt

ENV RABBITMQ_HOST=rabbitmq
ENV RABBITMQ_PORT=5672

ENV EXCHANGE=TOOL_EXCHANGE
ENV REQUEST_QUEUE=BRIGHTNESS_REQUEST_QUEUE
ENV RESULTS_QUEUE=RESULTS_QUEUE

CMD ["python", "brightness_worker.py"]