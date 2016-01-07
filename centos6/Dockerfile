FROM centos:centos6 

MAINTAINER Luke Kreczko <kreczko@cern.ch>

ADD RPM-GPG-KEY-cern /etc/pki/rpm-gpg/RPM-GPG-KEY-cern
ADD slc6-extras.repo /etc/yum.repos.d/HEP_OSlibs.repo
RUN yum update -y
