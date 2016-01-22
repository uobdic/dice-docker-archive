FROM centos:centos6 

MAINTAINER Luke Kreczko <kreczko@cern.ch>

RUN rpm --import https://yum.puppetlabs.com/RPM-GPG-KEY-puppetlabs
RUN rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm
RUN yum -y update
# install RVM dependencies
RUN yum install -y patch \
				libyaml-devel \
				glibc-headers \
				autoconf \
				gcc-c++ \
				glibc-devel \
				patch \
				readline-devel \
				zlib-devel \
				libffi-devel \
				openssl-devel \
				bzip2 \
				automake \
				libtool \
				bison \
				sqlite-devel \
				which
RUN yum install -y tar
# install RVM
RUN gpg2 --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN /bin/bash -l -c "curl -L get.rvm.io | bash -s stable"
RUN /bin/bash -l -c "rvm install 1.9.3"
# install puppet & r10k
RUN yum -y install puppet tar git
RUN puppet --version
RUN /bin/bash -l -c "gem install r10k"
RUN yum clean all
