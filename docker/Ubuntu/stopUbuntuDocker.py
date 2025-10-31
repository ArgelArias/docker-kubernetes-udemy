import os
import time

os.system("docker stop myubuntu")
time.sleep(1)
os.system("docker rm myubuntu")