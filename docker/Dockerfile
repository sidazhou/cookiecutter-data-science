FROM jupyter/scipy-notebook

MAINTAINER Sida Zhou <sidazhou@gmail.com>

RUN id -u -n #user

RUN conda install -y line_profiler memory_profiler
RUN conda install -c conda-forge jupyter_contrib_nbextensions

# # just for notes, this is now added via nvconfig/notebook.json
# RUN jupyter nbextension enable varInspector/main

# neo4j
RUN pip install neo4j-driver
RUN pip install py2neo

# USER root
# RUN id -u -n #user
# RUN apt-get update && sudo apt-get --yes dist-upgrade
# RUN apt-get install mysql
# RUN pip install mysqlclient
# RUN pip install --upgrade gensim

USER jovyan
RUN id -u -n #user
RUN pip install tqdm
RUN pip install -U imbalanced-learn
RUN pip install scikit-plot
# needed by sklearn utils
RUN pip install nose

RUN conda install numpy
RUN conda install scipy

RUN conda install -y pytables mkl mkl-service mkl-rt

# use root sparingly
# USER root
# RUN id -u -n #user
# installing theano
RUN pip install parameterized
RUN conda install theano pygpu

# installing keras after theano
RUN pip install keras
RUN pip install tensorflow
ENV KERAS_BACKEND=theano
ENV MKL_THREADING_LAYER=GNU

RUN pip install git+https://github.com/hyperopt/hyperopt

# USER jovyan
RUN id -u -n #user
# put ADD or COPY last, they will always invalidate the build cache
RUN python --version
RUN jupyter --version

# Docker 17.09 and up: 
# COPY --chown=someuser:somegroup /foo /bar
USER root
COPY ./.jupyter /home/$NB_USER/.jupyter
RUN chown -R jovyan:100 ./.jupyter

# for auto-sklearn
RUN apt-get update
RUN apt-get -y install curl
RUN apt-get install build-essential swig
# next line fails without root
RUN curl https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt | xargs -n 1 -L 1 pip install
RUN pip install auto-sklearn

# # https://stackoverflow.com/questions/29172874/where-are-core-files-stored-in-a-lxc-container
# RUN echo '/tmp/cores/core.%e.%p.%t' > /proc/sys/kernel/core_pattern
USER jovyan

COPY ./varInspector/var_list.py /opt/conda/share/jupyter/nbextensions/varInspector/var_list.py
COPY ./varInspector/main.js /opt/conda/share/jupyter/nbextensions/varInspector/main.js


#######################
# # commands to run
# docker build --rm -t sidazhou/scipy-notebook:latest -t sidazhou/scipy-notebook:v1.0.4 .

# docker build --rm --no-cache -t sidazhou/scipy-notebook:latest -t sidazhou/scipy-notebook:v1.0.4 .

# docker run -d -p 8888:8888 --name jupyter -v $(pwd):/home/jovyan/work sidazhou/scipy-notebook:latest
# # to run on linux box with security features, make sure the user `id -u` and group `id -g kg` are configured
# docker run -d -p 8889:8888 --name jupyter --user root -e GRANT_SUDO=yes -e NB_UID=1009 -e NB_GID=1009 -v $(pwd):/home/jovyan/work sidazhou/scipy-notebook:latest

# # to do some testing as root
# docker exec -it  --user root -e GRANT_SUDO=yes hengchang_jupyterscipy_1 bash

# # to run ipynb detached
# docker exec -d jupyter nohup jupyter nbconvert --ExecutePreprocessor.timeout=-1 --execute --to notebook --inplace /home/jovyan/work/GEM/notebooks/0.1.2-hyperparam_opt_node2vec.ipynb

# docker rm $(docker ps -q -f status=exited)

# # additional notes
# https://github.com/docker/docker/issues/12193
# Add a way to "APPEND" to a file from within a Dockefile

# docker build --rm -f ./Dockerfile_py27 -t sidazhou/scipy-notebook-py27:latest .

