FROM ubuntu:23.04
RUN apt-get update && \
    apt-get install -y sudo && \
    usermod -aG sudo ubuntu && \
    echo "ubuntu  ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

