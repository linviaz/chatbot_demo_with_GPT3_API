FROM python:3.10-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app code/app
CMD ["uvicorn", "code.main:app", "--host=0.0.0.0", "--reload", "--port", "8000"]