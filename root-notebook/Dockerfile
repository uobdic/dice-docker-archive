FROM jupyter/datascience-notebook
# this will need to come from centos
MAINTAINER Luke Kreczko <kreczko@cern.ch>
USER jovyan

# thanks to https://conda.anaconda.org/NLeSC
RUN conda config --add channels https://conda.anaconda.org/NLeSC &&\
	conda install -p $CONDA_DIR/envs/python2 --yes root=6 root_pandas rootpy gcc cmake scikit-learn 
# Python 3
RUN conda install --yes root=6 root_pandas rootpy gcc cmake scikit-learn
#RUN bash -c 'source activate python2' 
USER root
COPY start-notebook.sh /usr/local/bin/
USER jovyan