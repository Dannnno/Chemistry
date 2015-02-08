#!/bin/bash

set -ev

# Thank you to Binux for helping me with the openbabel issue
# http://stackoverflow.com/a/28335512/3076272

# Get the python prereqs to cross compile
sudo apt-get install -qq -y swig python-dev
wget http://mirrors.kernel.org/ubuntu/pool/universe/o/openbabel/libopenbabel4_2.3.2+dfsg-1.1_amd64.deb

# Get openbabel dependencies
# cmake is installed by the install_cmake.sh script
sudo apt-get install -qq -y libxml2-dev
sudo apt-get install -qq -y zlib1g-dev
sudo apt-get install -qq -y libeigen2-dev
sudo apt-get install -qq -y libcairo2-dev
sudo apt-get install -qq -y libboost-all-dev

# Get the openbabel source
sudo dpkg -i libopenbabel4_2.3.2+dfsg-1.1_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/o/openbabel/libopenbabel-dev_2.3.2+dfsg-1.1_amd64.deb
sudo dpkg -i libopenbabel-dev_2.3.2+dfsg-1.1_amd64.deb
