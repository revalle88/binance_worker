FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y wait-for-it curl gettext

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src src
COPY setup.py setup.py
RUN pip install -e .

COPY . .
