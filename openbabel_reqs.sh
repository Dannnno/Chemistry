#!/bin/bash

set -ev

# Thank you to Binux for helping me with the openbabel issue
# http://stackoverflow.com/a/28335512/3076272
sudo apt-get install -qq -y swig python-dev
wget http://mirrors.kernel.org/ubuntu/pool/universe/o/openbabel/libopenbabel4_2.3.2+dfsg-1.1_amd64.deb
sudo dpkg -i libopenbabel4_2.3.2+dfsg-1.1_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/o/openbabel/libopenbabel-dev_2.3.2+dfsg-1.1_amd64.deb
sudo dpkg -i libopenbabel-dev_2.3.2+dfsg-1.1_amd64.deb
