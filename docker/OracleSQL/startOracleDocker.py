import os

os.system("docker run -d --name oracledb -p 1521:1521 -p 5500:5500 -e ORACLE_PWD=admin -v oracle-data:/opt/oracle/oradata container-registry.oracle.com/database/express:21.3.0-xe")