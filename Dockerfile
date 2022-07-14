FROM ubuntu:20.04

WORKDIR /visualizacion

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y python3-pip

COPY . /visualizacion 

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 7000

CMD ["python3","app.py"]