FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requarment.txt /code/
RUN pip install -r requarment.txt

COPY . /code/