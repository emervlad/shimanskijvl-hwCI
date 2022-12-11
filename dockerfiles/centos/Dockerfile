FROM centos:7

RUN yum -y upgrade
RUN yum -y install epel-release
RUN yum install -y python3
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install opencv-python numpy pytest opencv-python-headless opencv-contrib-python-headless