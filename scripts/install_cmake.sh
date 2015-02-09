#!/bin/bash

set -ev

wget http://www.cmake.org/files/v2.8/cmake-2.8.11.tar.gz
tar -xzf cmake-2.8.11.tar.gz
cd cmake-2.8.11
./bootstrap --prefix=/usr --system-libs --mandir=/share/man --docdir=/share/doc/cmake-2.8.11
make
make test                        
sudo make install
cd ..