#!/bin/bash

# Running certbot to generate or renew certificates
# First time run
if [[ "x$SSL_EMAIL" == "x" ]]
then
  echo "SSL_EMAIL variable is not defined, aborting!"
  echo "Let's encrypt needs an email address to use "
  exit 3
fi

if [[ "x$SSL_DOMAINS" == "x" ]]
then
  echo "SSL_DOMAINS not defined, aborting!"
  echo "Add domains as environtment variable as colon separated list."
  exit 4
fi

if [[ -d /etc/letsencrypt/live ]]
then
  certbot-auto certonly --standalone -m $SSL_EMAIL -d test.eriksunde.com --agree-tos -q
else
  # Update certificate
  certbot-auto renew --quiet --no-self-upgrade
fi

# Launching Nginx
nginx -g "daemon off;"
