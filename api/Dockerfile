FROM python:3-alpine3.17

RUN pip install mysql-connector-python
RUN pip install Flask

WORKDIR /usr/app/src

COPY ./endpoints ./endpoints
COPY ./templates ./templates
COPY ./utility ./utility
COPY ./db ./db
COPY main.py ./

EXPOSE 5000