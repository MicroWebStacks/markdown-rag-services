FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY *.py /app/
COPY schema.json /app/

ENTRYPOINT ["python", "search.py"]
