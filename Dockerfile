# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY scripts/worker.sh /scripts/worker.sh
RUN ["chmod", "+x", "/scripts/worker.sh"]
ENTRYPOINT ["/scripts/worker.sh"]