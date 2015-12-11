FROM kreczko/centos6
MAINTAINER Luke Kreczko

RUN yum -y update && yum -y install rubygems \
                                    ruby-devel \
                                    gcc \
                                    ruby193
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc && \
    gem install puppet && \
    gem install librarian-puppet -v 1.0.9
