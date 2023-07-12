FROM python:3.9.11

WORKDIR /src
COPY requirements.txt /src

RUN pip install -r requirements.txt

ADD ./ src/

CMD [ "python main.py" ]