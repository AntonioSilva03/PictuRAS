FROM border-base

COPY . /app/picturas/tools/objectcounter

WORKDIR /app/picturas/tools/objectcounter

RUN pip install -r requirements.txt

ENV RABBITMQ_HOST=rabbitmq
ENV RABBITMQ_PORT=5672

ENV EXCHANGE=TOOL_EXCHANGE
ENV REQUEST_QUEUE=OBJECT_COUNTER_REQUEST_QUEUE
ENV RESULTS_QUEUE=RESULTS_QUEUE

CMD ["python", "oc_worker.py"]