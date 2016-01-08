FROM kreczko/centos6

MAINTAINER Luke Kreczko <kreczko@cern.ch>

RUN yum -y update; yum clean all
RUN yum -y install traceroute net-tools ntp python-setuptools
RUN easy_install supervisor 
RUN rpm -hUv https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN rpm -hUv http://software.internet2.edu/rpms/el6/x86_64/main/RPMS/Internet2-repo-0.5-3.noarch.rpm
RUN yum -y install perfSONAR_PS-Bundles-Level1 perfSONAR_PS-Bundles-Level2
RUN mkdir -p /var/log/supervisor 

ADD supervisord.conf /etc/supervisord.conf
ADD ls_registration_daemon.conf /opt/perfsonar_ps/ls_registration_daemon/etc/ls_registration_daemon.conf
ADD agent_configuration.conf /opt/perfsonar_ps/mesh_config/etc/agent_configuration.conf
RUN sed -i 's/<insert_hostname_here>/g/' #TODO

VOLUME ['/var/run'] #TODO: add data folder?

CMD /usr/bin/supervisord -c /etc/supervisord.conf