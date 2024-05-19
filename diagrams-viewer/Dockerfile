FROM httpd:latest

ARG KROKI_RENDERER_URL

COPY . /usr/local/apache2/htdocs/

RUN echo "const baseURL = '${KROKI_RENDERER_URL}';" > /usr/local/apache2/htdocs/config.js
