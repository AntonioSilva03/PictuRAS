FROM python:3.12.3-slim

COPY . /var/www/tools_management

WORKDIR /var/www/tools_management

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python", "app.py"]