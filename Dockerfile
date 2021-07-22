# syntax=docker/dockerfile:1
FROM ubuntu:18.04
WORKDIR /code
COPY . .
RUN apt update
RUN apt install --yes openjdk-8-jdk-headless python3-pip
RUN pip3 install -r requirements.txt
EXPOSE 8000