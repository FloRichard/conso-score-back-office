#!/bin/bash

cd $HOME/dev/database/conso-score || exit

default_db="postgres"
db="consoscore"

psql -d "${default_db}" -c "create database ${db};"
psql -d "${default_db}" -c "create user conso_score_user with encrypted password 'conso_score_user_pwd';"

files=("scheme.sql" "import.sql" "user.sql")

for file in "${files[@]}"
do
    echo "exec script : $file"
    psql -d "${db}" -f "./$file"
done