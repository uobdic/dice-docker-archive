FROM kreczko/puppet-builder
MAINTAINER Luke Kreczko

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
RUN sh -x ${VO_CMS_SW_DIR}/bootstrap.sh setup -path ${VO_CMS_SW_DIR} -arch ${SCRAM_ARCH} &> $VO_CMS_SW_DIR/bootstrap_$SCRAM_ARCH.log
RUN . $VO_CMS_SW_DIR/$SCRAM_ARCH/external/apt/*/etc/profile.d/init.sh;apt-get update
ADD install_dependencies.py ${VO_CMS_SW_DIR}/install_dependencies.py
RUN python ${VO_CMS_SW_DIR}/install_dependencies.py
RUN . $VO_CMS_SW_DIR/$SCRAM_ARCH/external/apt/*/etc/profile.d/init.sh; apt-get install -y cms+cmssw+CMSSW_${CMSSW_VERSION}
USER root
RUN echo "source /opt/cms/cmsset_default.sh\n\n" > /etc/profile.d/scram.sh
