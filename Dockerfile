FROM python:3.13.0

WORKDIR /urs/src/app
ADD . /urs/src/app

CMD [ "pythong", "hello.py"]