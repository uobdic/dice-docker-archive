FROM kreczko/centos6
MAINTAINER Luke Kreczko

RUN rpm --import https://yum.puppetlabs.com/RPM-GPG-KEY-puppetlabs
RUN rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm
RUN yum -y update
RUN yum -y install puppet tar git
