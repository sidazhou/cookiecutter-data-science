FROM jupyter/scipy-notebook

MAINTAINER Sida Zhou <sidazhou@gmail.com>

RUN id -u -n #user

# RUN conda info --envs

# RUN ["/bin/bash", "-c", "source activate python2"]

# https://github.com/conda/conda/issues/2031
# RUN conda install -y pytables mkl mkl-service mkl-rt

RUN conda install -y line_profiler memory_profiler
RUN conda install -c conda-forge jupyter_contrib_nbextensions

# # just for notes, this is now added via nvconfig/notebook.json
# RUN jupyter nbextension enable varInspector/main

# neo4j
RUN pip install neo4j-driver
RUN pip install py2neo

USER root
RUN id -u -n #user
RUN apt-get update && sudo apt-get --yes dist-upgrade
# RUN apt-get install mysql
# RUN pip install mysqlclient
RUN pip install --upgrade gensim

USER jovyan
RUN id -u -n #user
RUN pip install tqdm
RUN pip install -U imbalanced-learn
RUN pip install scikit-plot

# put ADD or COPY last, they will always invalidate the build cache
RUN python --version
RUN jupyter --version

COPY ./.jupyter /home/$NB_USER/.jupyter
COPY ./varInspector/var_list.py /opt/conda/share/jupyter/nbextensions/varInspector/var_list.py
COPY ./varInspector/main.js /opt/conda/share/jupyter/nbextensions/varInspector/main.js

USER root

#######################
# # commands to run
# docker build --rm -t sidazhou/scipy-notebook:latest -t sidazhou/scipy-notebook:v1.0.4 .

# docker build --rm --no-cache -t sidazhou/scipy-notebook:latest -t sidazhou/scipy-notebook:v1.0.4 .

# docker run -d -p 8888:8888 --name jupyter -v $(pwd):/home/jovyan/work sidazhou/scipy-notebook:latest
# # to run on linux box with security features, make sure the user `id -u` and group `id -g kg` are configured
# docker run -d -p 8889:8888 --name jupyter --user root -e GRANT_SUDO=yes -e NB_UID=1009 -e NB_GID=1009 -v $(pwd):/home/jovyan/work sidazhou/scipy-notebook:latest

# # to do some testing as root
# docker exec -it  --user root -e GRANT_SUDO=yes hengchang_jupyterscipy_1 bash

# docker rm $(docker ps -q -f status=exited)

# # additional notes
# https://github.com/docker/docker/issues/12193
# Add a way to "APPEND" to a file from within a Dockefile
