FROM ubuntu
 
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt install -y python3-dev python3-pip  python3-opencv vim-tiny libopencv-dev
RUN pip3 install Cython
RUN pip3 install numpy
RUN pip3 install paho-mqtt
COPY haarcascade_frontalface_default.xml haarcascade_frontalface_default.xml
COPY cam.py cam.py
CMD ["xhost +"]
CMD ["python3","cam.py"]
