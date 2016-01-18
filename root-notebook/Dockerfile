FROM jupyter/datascience-notebook

MAINTAINER Luke Kreczko <kreczko@cern.ch>
USER root
RUN wget https://root.cern.ch/download/root_v6.06.00.Linux-ubuntu14-x86_64-gcc4.8.tar.gz -O /opt/root.tar.gz
RUN cd /opt; tar xzf root.tar.gz
RUN cd /opt; tar xzf root.tar.gz
ENV ROOTSYS /opt/root
RUN echo 'source $ROOTSYS/bin/thisroot.sh' > /etc/profile.d/root-cern.sh
RUN echo 'export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH' >> /etc/profile.d/root-cern.sh
RUN cp -r $ROOTSYS/etc/notebook/kernels/root $CONDA_DIR/share/jupyter/kernels/ && \
    chmod -R go+rx $CONDA_DIR/share/jupyter
# as per jupyter/datascience-notebook
USER jovyan
RUN pip install metakernel
# CMD ["source $ROOTSYS/bin/thisroot.sh;start-notebook.sh"]
#TODO: 
# - need to compile ROOT as this container comes with gcc 4.9
# - need to make python2 a default for now

