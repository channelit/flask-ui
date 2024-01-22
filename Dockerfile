FROM python:3.9.18-slim

COPY src /opt/program
WORKDIR /opt/program

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 5000