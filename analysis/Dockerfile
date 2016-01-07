FROM kreczko/centos6 

MAINTAINER Luke Kreczko <kreczko@cern.ch>

RUN yum update -y
RUN yum install -y wget git sudo bzip2 HEP_OSlibs_SL6 e2fsprogs

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda-3.16.0-Linux-x86_64.sh && \
    /bin/bash /Miniconda-3.16.0-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda-3.16.0-Linux-x86_64.sh && \
    /opt/conda/bin/conda install --yes conda==3.18.3
    
ENV PATH /opt/conda/bin:$PATH
ENV LANG C.UTF-8
# now build & install packages
RUN conda config --add channels https://conda.anaconda.org/NLeSC
RUN conda create --name=analysis root=6 python=2 root_pandas rootpy gcc cmake scikit-learn
CMD [ "/bin/bash" ]
