FROM python:3.7

ADD . /grpc-server
WORKDIR /grpc-server

# Set the C_FORCE_ROOT environment variable for the Celery process, replace later
ENV C_FORCE_ROOT true

# Install pre-requisites
RUN apt-get update
RUN apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r /grpc-server/requirements.txt
