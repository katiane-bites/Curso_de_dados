FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
python3-dev \
python3-pip \
build-essential

RUN pip3 install --upgrade pip

RUN pip3 install jupyter numpy matplotlib scipy

RUN mkdir -p /home/user
WORKDIR /home/user





