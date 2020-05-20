# docker build . -t 'latex'
# docker run -it --rm symp:latest /bin/bash
# docker run -it --rm -v `pwd`:/scratch latex:latest /bin/bash
# docker run -it --rm -v `pwd`:/scratch latex:latest python3 generate_latex_files.py

# https://hub.docker.com/r/phusion/baseimage/tags
FROM phusion/baseimage:0.11

RUN apt-get update && \
    apt-get install -y \
# download files from the internet
         wget \
# extract compressed files
         zip \
# edit source code
         vim \
         python3 \
         python3-pip \
         python3-dev \
# compile .tex to verify the latex is valid
         texlive

RUN pip3 install antlr4-python3-runtime mpmath

WORKDIR /opt/

RUN wget https://github.com/msgoff/sympy/archive/master.zip
RUN unzip master.zip

# this contains the list of all possible symbols the parser can be expected to handle
# https://ctan.org/pkg/amsmath?lang=en
RUN wget http://mirrors.ctan.org/macros/latex/required/amsmath.zip
RUN unzip amsmath.zip

WORKDIR /opt/sympy-master/

RUN wget https://raw.githubusercontent.com/allofphysicsgraph/proofofconcept/gh-pages/v7_pickle_web_interface/flask/data.json

COPY generate_latex_files.py /opt/sympy-master/

RUN echo "alias python=python3" > /root/.bashrc
#RUN /bin/bash -l /root/.bashrc
