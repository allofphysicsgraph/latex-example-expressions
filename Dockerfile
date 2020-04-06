# docker build . -t 'latex'
# docker run -it --rm symp:latest /bin/bash
# docker run -it --rm -v `pwd`:/scratch latex:latest /bin/bash
# docker run -it --rm -v `pwd`:/scratch latex:latest python3 generate_latex_files.py

# https://hub.docker.com/r/phusion/baseimage/tags
FROM phusion/baseimage:0.11

RUN apt-get update && \
    apt-get install -y \
         wget \
         zip \
         vim \
         python3 \
         python3-pip \
         python3-dev \
         texlive

RUN pip3 install antlr4-python3-runtime mpmath

RUN wget https://github.com/msgoff/sympy/archive/master.zip
RUN mv master.zip /opt/

# https://ctan.org/pkg/amsmath?lang=en
RUN wget http://mirrors.ctan.org/macros/latex/required/amsmath.zip
RUN mv amsmath.zip /opt/

WORKDIR /opt/

RUN unzip master.zip
RUN unzip amsmath.zip

WORKDIR /opt/sympy-master/

COPY generate_latex_files.py /opt/sympy-master/

RUN echo "alias python=python3" > /root/.bashrc
#RUN /bin/bash -l /root/.bashrc
