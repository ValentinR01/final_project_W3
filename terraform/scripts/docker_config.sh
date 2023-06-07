#!/bin/bash 

# Update and install packages
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common lsb-release git

# Check Docker key and add repository
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Update and docker installation
sudo apt update
sudo apt install docker-ce

# Add user to docker group
sudo usermod -aG docker ${CD-USER}
newgrp docker

# Start and enable docker
sudo systemctl start docker

# Enable docker swarm
sudo docker swarm init