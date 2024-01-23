FROM python:3.12.1-slim

COPY src /opt/program
COPY ./requirements.txt ./opt/program/requirements.txt
WORKDIR /opt/program

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py" ]