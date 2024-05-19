# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

RUN pip install PyYAML==5.3.1 requests paho-mqtt==1.6.1

COPY *.py /app/
COPY utils/*.py /app/utils/

CMD ["python", "mqtt_client.py"]
