#!/bin/bash 

sudo useradd -m -s /bin/bash ${CD-USER}
sudo echo ${CD-USER}:${CD-PASSWORD} | chpasswd
