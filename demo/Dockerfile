FROM jupyter/scipy-notebook

RUN pip install python-igraph

ADD . .
USER root
RUN python3 ./setup.py install
USER jovyan
WORKDIR demo

