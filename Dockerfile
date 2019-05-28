FROM python:3

ADD temp.py /

ADD . /Users/nitinmore/Git/Python

RUN pip install numpy

RUN pip install matplotlib


CMD [ "python", "./temp.py" ]