FROM python:3.9-slim

#FROM node:20
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

RUN npm install -g pnpm
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/MicroWebStacks/astro-big-doc.git /builder
WORKDIR /builder

RUN pnpm install
RUN pnpm astro telemetry disable

WORKDIR /app
RUN pip install PyYAML==5.3.1 requests paho-mqtt==1.6.1
COPY *.py /app/
COPY utils/*.py /app/utils/

ENTRYPOINT ["python", "service.py"]
