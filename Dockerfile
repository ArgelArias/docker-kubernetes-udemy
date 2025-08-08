FROM ubuntu:20.04

RUN apt update
RUN apt install nginx -y
RUN apt install supervisor -y
RUN echo 'Hello world supervisor' > /var/www/html/index.html

ADD supervisor_services.conf /etc/supervisor/conf.d/
EXPOSE 80

CMD supervisord -n -c /etc/supervisor/supervisord.conf
