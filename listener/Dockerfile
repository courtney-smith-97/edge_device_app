FROM ubuntu:latest
# this is needed to make sure we can see the log output
ENV PYTHONUNBUFFERED=1
#WORKDIR /app
RUN apt-get update
RUN apt install -y python3-dev python3-pip
RUN pip3 install paho-mqtt
COPY listener.py listener.py
CMD ["python3","listener.py"]
