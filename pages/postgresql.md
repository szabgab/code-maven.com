---
title: "PostgreSQL"
timestamp: 2018-10-30T07:30:01
tags:
  - pg_database
  - PGPASSWORD
  - psql
published: true
author: szabgab
archive: true
---


Just some PostgreSQL related commands.


## Copy a whole database

```
CREATE DATABASE new_db_name WITH TEMPLATE origin_db_name;
```

## Get list of databases
```
SELECT datname FROM pg_database ORDER BY datname
```

## Get the size of all the databases
```
   SELECT
       t1.datname AS db_name,
       pg_database_size(t1.datname) AS db_size
   FROM pg_database t1
   ORDER BY pg_database_size(t1.datname) DESC;
```

The same on the command line:

```
PGPASSWORD=password  psql -h 10.11.12.13  -U username -c "SELECT t1.datname AS db_name, pg_size_pretty(pg_database_size(t1.datname)) AS db_size FROM pg_database t1 ORDER BY pg_database_size(t1.datname) DESC;
```

## Get the size of a single database
```
SELECT pg_database_size('foobar');
```
