FROM kreczko/puppet-builder 
MAINTAINER Luke Kreczko

RUN yum update -y && yum install -y wget git sudo HEP_OSlibs_SL6 e2fsprogs
    
                                
RUN ls /etc/puppet
RUN cd /etc/puppet/modules && git clone https://github.com/ktf/puppet-cmsdist cmsdist
RUN cd /etc/puppet/modules/cmsdist && git checkout ac5133e

ADD manifest.pp /manifest.pp
RUN puppet apply -d --modulepath=/etc/puppet/modules /manifest.pp
