FROM python:3.11.5-slim

WORKDIR /api-gateway

COPY ./requirements.txt /api-gateway/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api-gateway/requirements.txt

COPY ./app /api-gateway/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

