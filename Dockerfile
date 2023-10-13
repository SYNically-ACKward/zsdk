FROM python:3.11-slim

LABEL MAINTAINER="Dax Mickelson <dmickelson@zscaler.com>"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install/Upgrade packages.
COPY pip.conf .
COPY requirements.txt .
RUN pip install -U pip -r requirements.txt

ENTRYPOINT ["python"]
