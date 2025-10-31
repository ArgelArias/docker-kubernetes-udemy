FROM ubuntu:22.04

# Add volume for persistent data
VOLUME /data

# Install OpenSSH Server
RUN apt-get update && \
    apt-get install -y openssh-server && \
    apt-get install -y vim && \
    mkdir -p /var/run/sshd && \
    mkdir -p /root/.ssh
    

# Configure SSH
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Set root password
RUN echo 'root:password' | chpasswd

# Clean up
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# SSH port
EXPOSE 22

# Start SSH service
CMD ["/usr/sbin/sshd", "-D"]