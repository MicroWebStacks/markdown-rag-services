FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir sentence-transformers && \
    pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

COPY lambda_function.py ./ 

RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Set the CMD to your handler
CMD ["python", "lambda_function.py"]
