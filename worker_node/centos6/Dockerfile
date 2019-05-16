FROM centos:6

RUN yum -y install yum-priorities \
 # CVMFS (for SUM tests only; install before adding other repos to ensure we have the latest version)
 && yum -y install http://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-release-latest.noarch.rpm  \
                   http://ecsft.cern.ch/dist/cvmfs/cvmfs-config/cvmfs-config-default-latest.noarch.rpm \
 # CVMFS (for SUM tests only; install before adding other repos to ensure we have the latest version)
 && yum -y install cvmfs \
 # Needed for access to secure CVMFS repositories
 && yum -y install http://ecsft.cern.ch/dist/cvmfs/cvmfs-x509-helper/cvmfs-x509-helper-1.0-1.el6.x86_64.rpm \
 # EPEL
 && yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm \
 # UMD
 && yum -y install http://repository.egi.eu/sw/production/umd/4/sl6/x86_64/updates/umd-release-4.1.3-1.el6.noarch.rpm \
 # Basic dependencies
 && yum -y install freetype expat gcc glibc-headers compat-expat1 compat-openldap time man unzip quota attr wget \
 # Install HEP_OSlibs
 && yum -y install http://linuxsoft.cern.ch/wlcg/sl6/x86_64/HEP_OSlibs_SL6-1.1.5-1.el6.x86_64.rpm \
 # Install glexec, lcmaps & lcas
 && yum -y install glexec mkgltempdir \
                    lcmaps lcmaps-plugins-verify-proxy lcmaps-plugins-basic lcmaps-plugins-voms lcmaps-plugins-c-pep \
                    lcas lcas-plugins-basic lcas-plugins-voms sssd-client \
 && wget --no-check-certificate https://repo.gridpp.ac.uk/machinejobfeatures/mjf-scripts/00/RPMS/mjf-htcondor-00.19-1.noarch.rpm \
 && yum -y localinstall mjf-htcondor-00.19-1.noarch.rpm \
 && rm -f mjf-htcondor-00.19-1.noarch.rpm \
 # boost
 && yum -y install boost-date-time boost-filesystem boost-graph boost-iostreams boost-program-options \
                    boost-python boost-regex boost-serialization boost-signals boost-system boost-test \
                    boost-thread boost-wave \
 # singularity from EPEL
 && yum -y install singularity-runtime \
 && yum -y update \
 && yum clean all

# glexec
RUN mkdir -p /opt/glite/sbin && ln -s /usr/sbin/glexec /opt/glite/sbin/glexec \
 && mkdir -p /var/log/glexec && chown root:glexec /var/log/glexec

# Required for jobs created by glite-WMS submitted to an ARC CE
RUN touch /usr/etc/globus-user-env.sh

RUN sed -i '/enable overlay/c\enable overlay = no' /etc/singularity/singularity.conf

# hdfs
RUN wget https://archive.cloudera.com/cm5/redhat/6/x86_64/cm/cloudera-manager.repo -O /etc/yum.repos.d/cloudera-manager.repo \
 && yum -y install oracle-j2sdk1.7
RUN wget https://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/cloudera-cdh5.repo -O /etc/yum.repos.d/cloudera.repo \
 && yum -y install hadoop-client

COPY hadoop-conf /etc/hadoop/conf.cloudera.hdfs

RUN rm -f /etc/alternatives/hadoop-conf \
 && mv /usr/bin/hadoop{,.local} \
 && ln -s /etc/hadoop/conf.cloudera.hdfs /etc/alternatives/hadoop-conf \
 && ln -s /opt/cloudera/parcels/CDH/bin/hadoop /usr/bin/hadoop

COPY test_script.sh /scripts/test_script.sh
RUN chmod a+x /scripts/*

COPY 00_grid_c6.sh /etc/profile.d/00_grid.sh

# fixes
RUN mkdir -p /usersc /users /software /hdfs /storage /opt/cloudera \
    /var/singularity/mnt/final/users /var/singularity/mnt/final/usersc

RUN ln -s /bin/bash /usr/bin/bash \
 && ln -s /bin/cat /usr/bin/cat

RUN yum install -y python-argparse python-pip \
 && yum clean all
