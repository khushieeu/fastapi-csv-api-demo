FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./api /app/api
COPY ./data.csv /app/data.csv

CMD ["uvicorn", "api.index:app", "--host", "0.0.0.0", "--port", "7860"]
