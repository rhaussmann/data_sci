#!/usr/bin/env bash

conda install psycopg2


sudo su - postgres
psql -U postgres



$ sudo su - postgres
$ psql -U postgres

# In postgres
CREATE USER ender WITH ENCRYPTED PASSWORD 'bugger';
CREATE DATABASE golf WITH OWNER ender;

Postgres Commands:

\q: Quit/Exit
\c __database__: Connect to a database
\d __table__: Show table definition including triggers
\dt *.*: List tables from all schemas (if *.* is omitted will only show SEARCH_PATH ones)
\l: List databases
\dn: List schemas
\df: List functions
\dv: List views
\di: List indexes
\df+ __function__ : Show function SQL code.
\x: Pretty-format query results instead of the not-so-useful ASCII tables
\copy (SELECT * FROM __table_name__) TO 'file_path_and_name.csv' WITH CSV: Export a table as CSV

\du: List users
\du __username__: List a username if present.
create role __test1__: Create a role with an existing username.
create role __test2__ noinherit login password __passsword__;: Create a role with username and password.
set role __test__;: Change role for current session to __test__.
grant __test2__ to __test1__;: Allow __test1__ to set its role as __test2__

sudo service postgresql stop
sudo service postgresql start
sudo service postgresql restart

sudo vim /etc/postgresql/9.3/main/postgresql.conf

# Uncomment/Change inside:
log_min_messages = debug5
log_min_error_statement = debug5
log_min_duration_statement = -1

sudo service postgresql restart
