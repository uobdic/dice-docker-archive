FROM centos:7

RUN yum -y install yum-priorities \
 # CVMFS (for SUM tests only; install before adding other repos to ensure we have the latest version)
 && yum -y install http://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-release-latest.noarch.rpm \
                    http://ecsft.cern.ch/dist/cvmfs/cvmfs-config/cvmfs-config-default-latest.noarch.rpm \
 && yum -y install cvmfs cvmfs-config-egi \
 # EPEL
 && yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
 # Basic dependencies
 && yum -y install freetype expat gcc glibc-headers compat-expat1 compat-openldap time man unzip quota attr wget \
 # Install HEP_OSlibs
 && yum -y install http://linuxsoft.cern.ch/wlcg/centos7/x86_64/HEP_OSlibs-7.2.6-1.el7.cern.x86_64.rpm \
 # Machine job features
 && yum -y install wget \
 && wget --no-check-certificate https://repo.gridpp.ac.uk/machinejobfeatures/mjf-scripts/00/RPMS/mjf-htcondor-00.14-1.noarch.rpm \
 && yum -y localinstall mjf-htcondor-00.14-1.noarch.rpm \
 && rm -f mjf-htcondor-00.14-1.noarch.rpm \
 # Boost (need to ensure gfal CLI from CVMFS will work for some VOs)
 && yum -y install boost-date-time boost-filesystem boost-graph boost-iostreams boost-program-options \
                   boost-python boost-regex boost-serialization boost-signals boost-system boost-test \
                   boost-thread boost-wave \
 # Singularity
 && yum -y install singularity-runtime \
 # Update & cleanup
  && yum -y update \
  && yum clean all

RUN sed -i '/enable overlay/c\enable overlay = no' /etc/singularity/singularity.conf

# hdfs
RUN wget https://archive.cloudera.com/cm5/redhat/7/x86_64/cm/cloudera-manager.repo -O /etc/yum.repos.d/cloudera-manager.repo \
 && yum -y install oracle-j2sdk1.7
RUN wget https://archive.cloudera.com/cdh5/redhat/7/x86_64/cdh/cloudera-cdh5.repo -O /etc/yum.repos.d/cloudera.repo \
 && yum -y install hadoop-client
 RUN rm -f /etc/alternatives/hadoop-conf \
  && rm -f /usr/bin/hadoop \
  && ln -s /etc/hadoop/conf.cloudera.hdfs /etc/alternatives/hadoop-conf \
  && ln -s /opt/cloudera/parcels/CDH/bin/hadoop /usr/bin/hadoop

COPY test_script.sh /scripts/test_script.sh
RUN chmod a+x /scripts/*

COPY 00_grid_c7.sh /etc/profile.d/00_grid.sh
