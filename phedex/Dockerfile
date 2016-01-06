FROM kreczko/centos6
MAINTAINER Luke Kreczko

RUN yum update -y
RUN yum install -y wget git sudo HEP_OSlibs_SL6 e2fsprogs

ENV myarch slc6_amd64_gcc481
ENV repo comp.pre
ENV sw /home/phedex

RUN useradd phedex
RUN chown phedex:phedex /opt
USER phedex

ADD bootstrap.sh $sw/bootstrap.sh
RUN sh -x $sw/bootstrap.sh setup -path $sw -arch $myarch -repository $repo &> $sw/bootstrap_$myarch.log
RUN source $sw/$myarch/external/apt/*/etc/profile.d/init.sh && apt-get update
RUN source $sw/$myarch/external/apt/*/etc/profile.d/init.sh && apt-cache search PHEDEX|grep PHEDEX+
ENV version 4.1.7-comp
RUN source $sw/$myarch/external/apt/*/etc/profile.d/init.sh && apt-get install cms+PHEDEX+$version -y
RUN source $sw/$myarch/external/apt/*/etc/profile.d/init.sh && apt-get clean
USER root
