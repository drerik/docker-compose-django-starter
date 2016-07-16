#!/bin/bash

echo "Dumping cms db"
export PGPASSWORD=$POSTGRES_ENV_USER_DB_PASSWORD
pg_dump -h localhost -U $POSTGRES_ENV_USER_DB_USER -Fc -v -f /backup/cms.psql
echo "Db dump finished"
