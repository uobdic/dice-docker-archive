FROM kreczko/centos6

MAINTAINER Luke Kreczko <kreczko@cern.ch>

# FROM continuumio/miniconda but changed to centos6
RUN yum update -y && yum install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git tar build-essentials which
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh 
RUN	wget --quiet https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh &&\
    bash /Miniconda-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda-latest-Linux-x86_64.sh
RUN /opt/conda/bin/conda install --yes conda==3.19.0

RUN yum install -y curl grep sed gcc
RUN TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    yum install -y https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.rpm
RUN yum clean all

ENV PATH /opt/conda/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

ENTRYPOINT [ "/usr/bin/tini", "--" ]

CMD ["/bin/bash"]    