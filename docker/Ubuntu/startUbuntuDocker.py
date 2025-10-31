import os

os.system("docker run -d --name myubuntu -p 22:22 -v ubuntu-data:/data ubuntu:22.04")