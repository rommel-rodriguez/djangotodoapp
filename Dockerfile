# FROM python:3.9.13-bullseye
# FROM python:3.10-slim-bullseye
# NOTE: Seems like I will have to go with an older (and performance-wise slower)
# version of python, because my Django project is written with python 3.8.10 
# TODO: Find out how to update your whole project to another version of Python
# without breaking it.
FROM python:3.8-slim-bullseye


# NOTE: Consider setting this options in an environment file
# NOTE: PYTHONDONTWRITEBYTECODE, will be set in the compose file
# ENV PYTHONUNBUFFERED=1
# ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get upgrade -y

RUN pip3 install --no-cache --upgrade pip setuptools


COPY requirements.txt /tmp/

# NOTE: Should I start thinking about Python virtual environments here?

RUN pip3 install -r /tmp/requirements.txt

COPY ./django_app /src 

WORKDIR /src

