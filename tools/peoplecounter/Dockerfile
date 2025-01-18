FROM python:3.12.3-slim

# Install required system libraries
RUN apt-get update && apt-get install -y --no-install-recommends\
    git \
    gcc \
    g++ \
    make \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the application files
COPY . /app/picturas/tools/peoplecounter

# Set the working directory
WORKDIR /app/picturas/tools/peoplecounter

# Install PyTorch (replace 'cpu' with 'cu118' if you have GPU support with CUDA 11.8)
RUN python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install Detectron2 from the GitHub repository
RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

# Install Python dependencies
RUN pip install -r requirements.txt

# Set environment variables
ENV RABBITMQ_HOST=rabbitmq
ENV RABBITMQ_PORT=5672
ENV EXCHANGE=TOOL_EXCHANGE
ENV REQUEST_QUEUE=PEOPLECOUNTER_REQUEST_QUEUE
ENV RESULTS_QUEUE=RESULTS_QUEUE

# Set the command to run the worker
CMD ["python", "pc_worker.py"]