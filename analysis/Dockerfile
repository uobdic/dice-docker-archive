FROM centos:6.7

MAINTAINER Luke Kreczko <kreczko@cern.ch>

RUN yum update -y
RUN yum install -y wget git sudo bzip2 e2fsprogs tar
RUN yum clean all

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh
RUN wget --quiet http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh
RUN /bin/bash /tmp/miniconda.sh -b -p /opt/conda
RUN rm /tmp/miniconda.sh
ENV PATH /opt/conda/bin:$PATH
ENV LANG C.UTF-8

# now build & install packages
RUN conda config --set always_yes yes --set changeps1 no
RUN conda update -q conda
RUN conda install -q psutil
RUN conda config --add channels https://conda.anaconda.org/NLeSC
RUN conda create --name=analysis root=6 python=2 root_pandas rootpy gcc cmake scikit-learn
RUN conda clean -y
RUN source activate analysis
CMD [ "/bin/bash" ]
