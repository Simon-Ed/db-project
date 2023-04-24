# syntax=docker/dockerfile:1
FROM python:3-alpine3.17

WORKDIR /app
COPY . /app

# Install app dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python project/app.py