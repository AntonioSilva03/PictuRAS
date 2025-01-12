FROM python:3.12.3-slim

RUN apt update

RUN apt install ffmpeg -y