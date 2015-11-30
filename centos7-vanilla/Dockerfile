FROM centos:centos7 

ADD RPM-GPG-KEY-cern /etc/pki/rpm-gpg/RPM-GPG-KEY-cern
ADD cc7-cern.repo /etc/yum.repos.d/HEP_OSlibs.repo
RUN yum update -y
