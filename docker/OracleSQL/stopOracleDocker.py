import os
import time

os.system("docker stop oracledb")
time.sleep(1)
os.system("docker rm oracledb")