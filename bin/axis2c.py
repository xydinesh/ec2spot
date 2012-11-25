from ec2spot.spot import SpotInstanceRequest
import logging as logger

class Axis2CTestInstance(SpotInstanceRequest):
    def __init__(self):
        self.price = "0.007"
        self.instance = "m1.small"
        self.key = "DjangoTutorial"
        self.packages = ["gcc", "g++", "make", "autoconf", "python-dev", "git", "subversion", "libapr1",
                         "libapr1-dev", "libaprutil1", "emacs", "autoconf", "automake", "libxml2", "libtool",
                         "libxml2-dev", "zlibc", "apache2-mpm-worker", "sendmail", "pkg-config"]

        logger.basicConfig(filename='ec2.log', level=logger.DEBUG, format='%(asctime)s %(message)s',
                           datefmt='%m/%d/%Y %I:%M:%S %p')

        super(Axis2CTestInstance, self).__init__()

    def  config_script(self):
        self.script = """#!/bin/bash
set -e -x
echo "From: dinesh@apache.org" >> /tmp/mail.tmp
echo "To: xydinesh@gmail.com" >> /tmp/mail.tmp

apt-get update
apt-get install -y %s &> /tmp/apt.log
cat /tmp/mail.tmp > /tmp/sendmail.txt
echo "Subject: apt log" >> /tmp/sendmail.txt
cat /tmp/apt.log >> /tmp/sendmail.txt
sendmail -ti   < /tmp/sendmail.txt

cd /tmp
wget http://people.apache.org/~dinesh/axis2c/1.7.0/RC6/axis2c-src-1.7.0.tar.gz -o /tmp/wget.log
cat /tmp/mail.tmp > /tmp/sendmail.txt
echo "Subject: wget log" >> /tmp/sendmail.txt
cat /tmp/wget.log >> /tmp/sendmail.txt
sendmail -ti < /tmp/sendmail.txt

tar xvfz axis2c-src-1.7.0.tar.gz
cd axis2c-src-1.7.0
./configure --prefix $PWD/deploy &> /tmp/axis2.log
cat /tmp/mail.tmp > /tmp/sendmail.txt
echo "Subject: config log" >> /tmp/sendmail.txt
cat /tmp/axis2.log >> /tmp/sendmail.txt
sendmail -ti < /tmp/sendmail.txt

make &> /tmp/make.log
cat /tmp/mail.tmp > /tmp/sendmail.txt
echo "Subject: make log" >> /tmp/sendmail.txt
cat /tmp/make.log >> /tmp/sendmail.txt
sendmail -ti < /tmp/sendmail.txt

make install > /tmp/make.install.log
cat /tmp/mail.tmp > /tmp/sendmail.txt
echo "Subject: make install log" >> /tmp/sendmail.txt
cat /tmp/make.install.log >> /tmp/sendmail.txt
sendmail -ti < /tmp/sendmail.txt
""" % (" ".join(self.packages))


class Axis2CTestUbuntu(Axis2CTestInstance):
    def __init__(self):
        self.image = "ami-3b4ff252"
        super(Axis2CTestUbuntu, self).__init__()

    def spot_request(self):
        self.config_script()
        self.spot = self.conn.request_spot_instances(self.price,
                                                     image_id=self.image,
                                                     availability_zone_group=self.region,
                                                     key_name=self.key,
                                                     instance_type=self.instance,
                                                     user_data=self.script)


class Axis2CTestFedora(Axis2CTestInstance):
    def __init__(self):
        self.image = "ami-84db39ed"
        super(Axis2CTestFedora, self).__init__()

    def spot_request(self):
        self.config_script()
        self.spot = self.conn.request_spot_instances(self.price,
                                                     image_id=self.image,
                                                     availability_zone_group=self.region,
                                                     key_name=self.key,
                                                     instance_type=self.instance,
                                                     user_data=self.script)









