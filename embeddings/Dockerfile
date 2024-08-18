FROM public.ecr.aws/lambda/python:3.12

WORKDIR /app

RUN pip install --no-cache-dir sentence-transformers && \
    pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

COPY lambda_function.py ${LAMBDA_TASK_ROOT}

RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Set the CMD to your handler
CMD ["lambda_function.lambda_handler"]
