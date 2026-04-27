# CREATE TABLE

Before we can add data to our database we need to create one or more tables to hold the data.
For this we use the DDL (Data Definition Languagea), which part of the SQL language, of dialect in the database system we use.

The statement starts with `CREATE TABLE` followed by the name of the table. Then in parenthese we have the name and the type of each column.
Optionally we can have comments after two dash-es.

* [DDL - Data definition language](https://en.wikipedia.org/wiki/Data_definition_language) (part of SQL)
* Column name
* Column type
* Comments

Some of the popular column types:

* ENUM
* VARCHAR
* FLOAT
* INTEGER
* DATE


{% embed include file="src/examples/create_person.sql" %}

