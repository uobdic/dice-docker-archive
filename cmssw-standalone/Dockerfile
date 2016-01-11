FROM kreczko/puppet-builder

MAINTAINER Luke Kreczko <kreczko@cern.ch>

RUN yum update -y && yum install -y wget git sudo HEP_OSlibs_SL6 e2fsprogs
    
# set up environment variables - if you want a different CMSSW version, change here
ENV CMSSW_VERSION 7_4_12
ENV SCRAM_ARCH slc6_amd64_gcc491
ENV VO_CMS_SW_DIR /opt/cms
RUN echo "CMSSW_VERSION=${CMSSW_VERSION}" >> /etc/profile.d/cmssw.sh
RUN echo "SCRAM_ARCH=${SCRAM_ARCH}" >> /etc/profile.d/cmssw.sh
RUN echo "VO_CMS_SW_DIR=${VO_CMS_SW_DIR}" >> /etc/profile.d/cmssw.sh

RUN useradd cms
RUN mkdir -p /opt/cms && chown -R cms:cms /opt/cms
# change to cms user
USER cms
RUN wget http://cmsrep.cern.ch/cmssw/cms/bootstrap.sh -O ${VO_CMS_SW_DIR}/bootstrap.sh
RUN sh -x ${VO_CMS_SW_DIR}/bootstrap.sh setup -path ${VO_CMS_SW_DIR} -arch ${SCRAM_ARCH} &> ${VO_CMS_SW_DIR}/bootstrap_$SCRAM_ARCH.log

# try again if download fails
RUN echo "Acquire::Retries 99;" >> ${VO_CMS_SW_DIR}/${SCRAM_ARCH}/external/apt/0.5.16/etc/apt.conf

# make the integration branches available
RUN echo "rpm http://cmsrep.cern.ch cmssw/cms.week0/apt/${SCRAM_ARCH} lcg cms external" >> ${VO_CMS_SW_DIR}/${SCRAM_ARCH}/external/apt/0.5.16/etc/sources.list
RUN echo "rpm http://cmsrep.cern.ch cmssw/cms.week1/apt/${SCRAM_ARCH} lcg cms external" >> ${VO_CMS_SW_DIR}/${SCRAM_ARCH}/external/apt/0.5.16/etc/sources.list

# update the APT cache
RUN . ${VO_CMS_SW_DIR}/${SCRAM_ARCH}/external/apt/*/etc/profile.d/init.sh;apt-get update

# install dependencies for the CMSSW version of interest - first time run use this to create the list in the next step
ADD install_dependencies.py ${VO_CMS_SW_DIR}/install_dependencies.py
RUN python ${VO_CMS_SW_DIR}/install_dependencies.py

# install CMSSW
RUN . ${VO_CMS_SW_DIR}/${SCRAM_ARCH}/external/apt/*/etc/profile.d/init.sh; apt-get install -y cms+cmssw+CMSSW_${CMSSW_VERSION}

# clean the APT cache
RUN . ${VO_CMS_SW_DIR}/${SCRAM_ARCH}/external/apt/*/etc/profile.d/init.sh;apt-get clean all

# change back to root user
USER root
RUN yum install -y bzip2
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda-3.16.0-Linux-x86_64.sh && \
    /bin/bash /Miniconda-3.16.0-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda-3.16.0-Linux-x86_64.sh && \
    /opt/conda/bin/conda install --yes conda==3.18.3
RUN chown -R cms:cms /opt/conda 

RUN echo "source /opt/cms/cmsset_default.sh" > /etc/profile.d/scram.sh

USER cms
RUN export PATH=/opt/conda/bin:$PATH && conda install -q --yes coverage
RUN export PATH=/opt/conda/bin:$PATH && pip install nose2[coverage-plugin]
RUN cd /home/cms && source /opt/cms/cmsset_default.sh && scram project -n cmssw CMSSW_${CMSSW_VERSION}
