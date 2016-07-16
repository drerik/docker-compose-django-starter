FROM nginx:stable
MAINTAINER "Erik Kaareng-Sunde <erik@eriksunde.com>"

RUN apt-get update ; apt-get install -y openssl bc curl ; apt-get clean
RUN curl -o /usr/local/bin/certbot-auto https://dl.eff.org/certbot-auto && chmod a+x /usr/local/bin/certbot-auto
ADD uwsgi.conf /etc/nginx/conf.d/default.conf
