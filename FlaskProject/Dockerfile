
FROM python:3.12.0a7-buster

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install flask==2.2.2
COPY code/ /var/opt/

WORKDIR /var/opt
CMD python app.py
