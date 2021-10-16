FROM python:3.7-alpine
MAINTAINER One Gun Samurai

#This is good practice when runing python inside docker image.
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
#Added when attaching a postgres
RUN apk add --update --no-cache postgresql-client jpeg-dev
#Temporary dependencies for postgress installation
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

#Make an app directory, set it as home directory of a proj.
#Copy the contents of project directory on local machine to docker image.
RUN mkdir /app
WORKDIR /app
COPY ./app /app

#Data to be shared with other containers
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
