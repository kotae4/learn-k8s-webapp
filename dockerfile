# syntax=docker/dockerfile:1
FROM python:3.10-alpine

ENV FLASK_APP=webapp
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
ENV FLASK_CONFIG=basicwebapp-settings.cfg
ENV BACKEND_HOST=api.testing.private
ENV BACKEND_PORT=27525
ENV BACKEND_PROTOCOL=http
ENV SECRET_KEY=ajoke

EXPOSE $FLASK_RUN_PORT

WORKDIR /webapp

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD learn-k8s-webapp/ .

WORKDIR /
ENTRYPOINT [ "flask", "--app", "webapp", "run", "--debug" ]