FROM ubuntu
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt install -y python3-dev python3-pip
RUN pip3 install numpy boto3 paho-mqtt
COPY im_upload.py im_upload.py

CMD ["python3","im_upload.py"]
