#!/bin/bash

echo "Copying postgresql.conf to /var/lib/postgresql/data/postgresql.conf"
cp /docker-entrypoint-initdb.d/postgresql.conf /var/lib/postgresql/data/postgresql.conf

echo "Creating user"
gosu postgres postgres --single -jE <<-EOSQL
create user $PG_USER_DB_USERNAME with password '$PG_USER_DB_PASSWORD';
EOSQL

echo "Creating database"
gosu postgres postgres --single -jE <<-EOSQL
CREATE DATABASE "$PG_USER_DB_DBNAME" WITH OWNER "$PG_USER_DB_USERNAME";
EOSQL
