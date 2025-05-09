# docker build . -t 'latex'
# docker run -it --rm symp:latest /bin/bash
# docker run -it --rm -v `pwd`:/scratch latex:latest /bin/bash
# docker run -it --rm -v `pwd`:/scratch latex:latest python3 generate_latex_files.py

# https://hub.docker.com/r/phusion/baseimage/tags
FROM phusion/baseimage:focal-1.1.0

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
         texlive \
         openjdk-21-jdk
#RUN pip3 install antlr4-python3-runtime mpmath

WORKDIR /opt/

#RUN wget https://github.com/msgoff/sympy/archive/master.zip
#RUN unzip master.zip

# this contains the list of all possible symbols the parser can be expected to handle
# https://ctan.org/pkg/amsmath?lang=en
RUN wget http://mirrors.ctan.org/macros/latex/required/amsmath.zip
RUN unzip amsmath.zip

RUN curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
RUN cp antlr-4.13.2-complete.jar /usr/local/lib

#WORKDIR /opt/sympy-master/

#RUN wget https://raw.githubusercontent.com/allofphysicsgraph/proofofconcept/gh-pages/v7_pickle_web_interface/flask/data.json

#COPY generate_latex_files.py /opt/sympy-master/

RUN echo "alias python=python3" > /root/.bashrc
RUN echo 'export CLASSPATH=".:/usr/local/lib/antlr-4.13.2-complete.jar:$CLASSPATH"' >> /root/.bashrc
RUN echo "alias antlr4='java -Xmx500M -cp '/usr/local/lib/antlr-4.13.2-complete.jar:$CLASSPATH' org.antlr.v4.Tool'" >> /root/.bashrc
RUN echo "alias grun='java -Xmx500M -cp '/usr/local/lib/antlr-4.13.2-complete.jar:$CLASSPATH' org.antlr.v4.gui.TestRig'" >> /root/.bashrc

#RUN sed -i "s/antlr4=/antlr4='//g" /root/.bashrc
#RUN /bin/bash -l /root/.bashrc
