FROM centos:centos7 

MAINTAINER Luke Kreczko <kreczko@cern.ch>

ADD RPM-GPG-KEY-cern /etc/pki/rpm-gpg/RPM-GPG-KEY-cern
ADD cc7-cern.repo /etc/yum.repos.d/HEP_OSlibs.repo
RUN yum update -y
