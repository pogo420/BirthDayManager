#!/bin/bash
echo "setting environment variables"
export SQLITE_DB=Db/bdm_datbase.db
export DB_SETUP_SCRIPT=Db/SchemaCreate.sql
export MASTER_TABLE=birthday_data
export PYTHONPATH=.
export JWT_SECRET=dummy-secret-1
export JWT_EXPIRE=60
export FLASK_APP=Application.UserQueryHandler.py
bash ./Db/db_setup.sh
echo $SQLITE_DB