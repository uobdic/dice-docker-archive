FROM jupyter/datascience-notebook
# this will need to come from centos
MAINTAINER Luke Kreczko <kreczko@cern.ch>
USER root
RUN git clone https://github.com/root-mirror/root.git /opt/root
ENV ROOTSYS /opt/root

# from https://root.cern.ch/build-prerequisites#ubuntu
RUN apt-get update && \
	apt-get install -y git dpkg-dev make g++ gcc binutils libx11-dev libxpm-dev \
	libxft-dev libxext-dev libx11-6

RUN cd $ROOTSYS && \
	git checkout v6-06-00 && \
	/bin/bash -c 'source activate python2' && \
	./configure  --with-x11-libdir=/usr/lib/x86_64-linux-gnu --with-xpm-libdir=/usr/lib/x86_64-linux-gnu \
    --with-xft-libdir=/usr/lib/x86_64-linux-gnu --with-xext-libdir=/usr/lib/x86_64-linux-gnu \
    --enable-roofit --enable-minuit2 --enable-builtin-freetype --enable-tmva && \
	make jobs=4

ADD activate_root.sh /etc/profile.d/activate_root.sh
RUN cp -r $ROOTSYS/etc/notebook/kernels/root $CONDA_DIR/share/jupyter/kernels/ && \
    chmod -R go+rx $CONDA_DIR/share/jupyter
# as per jupyter/datascience-notebook
USER jovyan
#RUN /bin/bash -c 'source /etc/profile.d/activate_root.sh' && \
	#pip install metakernel

# CMD ["source $ROOTSYS/bin/thisroot.sh;start-notebook.sh"]
#TODO: 
# - need to compile ROOT as this container comes with gcc 4.9
# - need to make python2 a default for now
USER root

