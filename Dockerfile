FROM ubuntu:20.04

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y python3-pip

WORKDIR /app

COPY . /app 

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 7000

CMD ["python3","app.py"]