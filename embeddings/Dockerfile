FROM public.ecr.aws/lambda/python:3.12

WORKDIR /app

RUN pip install --no-cache-dir sentence-transformers && \
    pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

COPY lambda_function.py ${LAMBDA_TASK_ROOT}
COPY load_models.py ./
RUN python load_models.py

# Set the CMD to your handler
CMD ["lambda_function.lambda_handler"]
