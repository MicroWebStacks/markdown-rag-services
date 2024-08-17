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
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY *.py /app/

ENTRYPOINT ["python", "markdown.py", "build"]
