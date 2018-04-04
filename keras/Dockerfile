# from https://github.com/keras-team/keras/blob/master/docker/Dockerfile
ARG cuda_version=9.0
ARG cudnn_version=7
FROM nvidia/cuda:${cuda_version}-cudnn${cudnn_version}-devel

ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

RUN apt-get update && apt-get install -y \
      bzip2 \
      git \
      graphviz \
      g++ \
      libgl1-mesa-glx \
      libhdf5-dev \
      openmpi-bin \
      wget \
   && rm -rf /var/lib/apt/lists/*

RUN mkdir -p $CONDA_DIR && \
    echo export PATH=$CONDA_DIR/bin:'$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh && \
    echo "c59b3dd3cad550ac7596e0d599b91e75d88826db132e4146030ef471bb434e9a *Miniconda3-4.2.12-Linux-x86_64.sh" | sha256sum -c - && \
    /bin/bash /Miniconda3-4.2.12-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-4.2.12-Linux-x86_64.sh

# Python
ARG python_version=3.6

RUN conda install -y python=${python_version} && \
    pip install --upgrade --no-cache-dir pip && \
    pip install --no-cache-dir tensorflow-gpu && \
#    pip install --no-cache-dir https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp36-cp36m-linux_x86_64.whl && \
    conda install Pillow scikit-learn notebook pandas matplotlib mkl nose pyyaml six h5py && \
    conda install theano pygpu bcolz && \
    pip install --no-cache-dir sklearn_pandas && \
    git clone git://github.com/keras-team/keras.git /src && pip install -e /src[tests] && \
    pip install --no-cache-dir git+git://github.com/keras-team/keras.git && \
    pip install --no-cache-dir opencv-python tqdm && \
    conda clean -yt

ENV JOBLIB_TEMP_FOLDER /data/
ENV NB_USER keras
#
# ARG NB_UID=1000
# RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
#     mkdir -p $CONDA_DIR && \
#     chown  ${NB_USER} $CONDA_DIR -R && \
#     mkdir -p /src && \
#     chown  ${NB_USER} /src
#
# USER ${NB_USER}
#
#
# COPY theanorc /home/${NB_USER}/.theanorc
#
# ENV PYTHONPATH='/src/:/src/workspace:$PYTHONPATH'
#
# WORKDIR /src
#
# EXPOSE 8888
# ARG HOST=localhost
#
# CMD jupyter notebook --port=8888 --ip=$HOST
