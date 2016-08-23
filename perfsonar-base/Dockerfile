FROM kreczko/centos6

MAINTAINER Luke Kreczko <kreczko@cern.ch>

RUN yum -y update
RUN yum -y install traceroute net-tools ntp python-setuptools
RUN easy_install supervisor
RUN yum install -y https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum install -y http://software.internet2.edu/rpms/el6/x86_64/main/RPMS/Internet2-repo-0.6-1.noarch.rpm
RUN yum -y install perfsonar-testpoint
RUN yum clean all
RUN mkdir -p /var/log/supervisor

ADD supervisord.conf /etc/supervisord.conf
ADD ls_registration_daemon.conf /opt/perfsonar_ps/ls_registration_daemon/etc/ls_registration_daemon.conf
ADD agent_configuration.conf /opt/perfsonar_ps/mesh_config/etc/agent_configuration.conf
#RUN sed -i 's/<insert_hostname_here>/g/' #TODO


CMD /usr/bin/supervisord -c /etc/supervisord.conf
