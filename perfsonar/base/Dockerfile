FROM centos/centos6

MAINTAINER Luke Kreczko <kreczko@cern.ch>

RUN yum -y update; yum clean all
RUN yum -y install traceroute net-tools ntp python-setuptools
RUN yum install -y https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum install -y http://software.internet2.edu/rpms/el6/x86_64/main/RPMS/Internet2-repo-0.6-1.noarch.rpm
RUN yum -y install perfSONAR_PS-Bundles-Level1 perfSONAR_PS-Bundles-Level2
