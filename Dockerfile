FROM python:3.7-alpine
MAINTAINER One Gun Samurai

#This is good practice when runing python inside docker image.
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

#Make an app directory, set it as home directory of a proj.
#Copy the contents of project directory on local machine to docker image.
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser user
USER user
