FROM python:3.8.5-slim-buster

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app
RUN pip --disable-pip-version-check --no-cache-dir install -r requirements.txt --no-cache-dir
RUN cd src && python manage.py collectstatic --no-input --clear