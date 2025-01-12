FROM border-base

COPY . /app/picturas/tools/border

WORKDIR /app/picturas/tools/border

RUN pip install -r requirements.txt

ENV RABBITMQ_HOST=rabbitmq
ENV RABBITMQ_PORT=5672

ENV EXCHANGE=TOOL_EXCHANGE
ENV REQUEST_QUEUE=BORDER_REQUEST_QUEUE
ENV RESULTS_QUEUE=RESULTS_QUEUE

CMD ["python", "border_worker.py"]