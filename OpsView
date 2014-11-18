#
# Dockerfile - OPSVIEW for Ubuntu/Phusion/baseimage
# Based off work from  ruo91/docker-opsview  - Yongbok Kim <ruo91@yongbok.net>
FROM     phusion/baseimage:0.9.15
MAINTAINER Dwaltermeyer@connectify.me

#SYSTEMPREP
ADD opsview.asc /tmp/
ADD 00Do-not-ask /etc/apt/apt.conf.d/
ENV DEBIAN_FRONTEND noninteractive
RUN cat /tmp/opsview.asc | sudo apt-key add - \
 && echo "deb http://downloads.opsview.com/opsview-core/latest/apt precise main" | sudo tee -a /etc/apt/sources.list 

#SYSTEMAPPS
RUN sudo bash -c 'apt-get update && apt-get -y dist-upgrade'

RUN sudo apt-get install apt-transport-https \
  apt apt-transport-https apt-utils base-files bash bsdutils curl dpkg gnupg \
  gpgv ifupdown iproute libapt-inst1.5 libapt-pkg4.12 libblkid1 libc-bin libc6 \
  libcurl3 libcurl3-gnutls libdbus-1-3 libdrm-intel1 libdrm-nouveau2 \
  libdrm-radeon1 libdrm2 libgcrypt11 libgnutls26 libgssapi-krb5-2 libk5crypto3 \
  libkrb5-3 libkrb5support0 libmount1 libssl1.0.0 libtasn1-6 libudev1 libuuid1 \
  mount multiarch-support openssh-client openssh-server openssl tzdata udev \
  util-linux  pciutils libpciaccess0 libpci3



#CONFIG MySQL
RUN sudo echo mysql-server-5.5 mysql-server/root_password password opsview | debconf-set-selections \
 && sudo echo mysql-server-5.5 mysql-server/root_password_again password opsview | debconf-set-selections 
   
 
 
# OPSVIEW
RUN sudo apt-get install -y opsview opsview-core opsview-web libdbix-class-schema-loader-perl python-setuptools  \
 && service mysqld start && mysqladmin -u root password 'opsview' \
 && sed -i 's/changeme/opsview/g' /usr/local/nagios/etc/opsview.conf \
 && /usr/local/nagios/bin/db_mysql -u root -popsview \
 && /usr/local/nagios/bin/db_opsview db_install \
 && /usr/local/nagios/bin/db_runtime db_install \
 && chmod -R 777 /var/log/opsview \
 && /usr/local/nagios/bin/rc.opsview gen_config

# Supervisord
RUN easy_install pip && pip install supervisor && pip install virtualenvwrapper \
 && echo 'export WORKON_HOME=$HOME/.virtualenvs' >> /root/.bashrc \
 && echo 'source /usr/bin/virtualenvwrapper.sh' >> /root/.bashrc \
 && mkdir /etc/supervisord.d
ADD conf/supervisord.conf /etc/supervisord.d/supervisord.conf

# Supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.d/supervisord.conf"]

# Port
EXPOSE 3000
