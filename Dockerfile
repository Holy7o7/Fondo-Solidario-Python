FROM ubuntu:20.04

RUN apt update \
    && apt -y upgrade \
    && apt install -y python3-pip

WORKDIR /app

COPY . /app 

RUN pip --no-cache-dir install -r requirements.txt

#CMD ["python3","app.py"]