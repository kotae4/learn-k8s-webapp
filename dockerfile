# syntax=docker/dockerfile:1
FROM python:3.10-alpine

ENV FLASK_APP=webapp
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
ENV FLASK_CONFIG=basicwebapp-settings.cfg

EXPOSE $FLASK_RUN_PORT

WORKDIR /webapp

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . .

WORKDIR /
ENTRYPOINT [ "flask", "run", "--debug" ]