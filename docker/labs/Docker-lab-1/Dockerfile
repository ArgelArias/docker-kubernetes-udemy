FROM python:latest

RUN apt update
RUN apt install supervisor -y

ADD supervisor_services.conf /etc/supervisor/conf.d/

ADD requirements.txt /tmp
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt
RUN rm -rf /tmp/requirements.txt

ADD src/ /src/

EXPOSE 5000

CMD [ "supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]
