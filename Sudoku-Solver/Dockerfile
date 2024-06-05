FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apk add --no-cache gcc musl-dev libffi-dev postgresql-dev
RUN pip install jwt
RUN pip install psycopg2
COPY . .