# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY *.py /app/

ENTRYPOINT ["python", "service.py"]
