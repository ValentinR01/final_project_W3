#!/bin/bash

sudo useradd -m -s /bin/bash ${cd_username}
sudo echo ${cd_username}:${cd_password} | chpasswd

# Update and install packages
sudo apt update -y
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common lsb-release git

# Check Docker key and add repository
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Update and docker installation
sudo apt update -y
sudo apt install -y docker-ce

# Add user to docker group
sudo usermod -aG docker ${cd_username}
newgrp docker

# Start and enable docker
sudo systemctl start docker
sudo systemctl enable docker

# Enable docker swarm
sudo docker swarm init