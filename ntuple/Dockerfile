FROM kreczko/miniconda

MAINTAINER Luke Kreczko <kreczko@cern.ch>

RUN conda install anaconda-client
RUN conda create -q -n ntuple python=2.7 nose pytest flake8 gcc && \
    source activate ntuple && \
    conda install -q -c https://conda.anaconda.org/nlesc root rootpy

ENTRYPOINT [ "/usr/bin/tini", "--" ]

CMD ["/bin/bash"]  