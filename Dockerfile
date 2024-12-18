FROM python:3.12-alpine

COPY requirements.txt /temp/requirements.txt
COPY genetic_tests /genetic_test
COPY manage.py /

WORKDIR /

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

# RUN adduser --disabled-password sevice-user

# USER service-user