---
title: "Configuring MySQL"
timestamp: 2018-01-01T07:30:02
tags:
  - files
published: false
author: szabgab
archive: true
---



When installing the MySQL server on a Linux box, at least on Ubuntu, it will ask for a password for the `root` user.
Let's say we give it the password "secret".

Then, once the server is intsalled we can access it with the command line tool `mysql`

```
$ mysql
ERROR 1045 (28000): Access denied for user 'vagrant'@'localhost' (using password: NO)
```

I was running this as user 'vagrant' but I was refused access to the server.

```
$ mysql -uroot -p
Enter password: secret
...
mysql>
```

```
mysql>  CREATE USER 'perl_dev'@'localhost' IDENTIFIED BY 'perl_secret';
Query OK, 0 rows affected (0.00 sec)


mysql> GRANT ALL ON perl_db.* TO 'perl_dev'@'localhost';
```

   $ mysql -u root
   mysql> CREATE USER 'perlmaven_user'@'localhost' IDENTIFIED BY 'perlmaven_password';
   mysql> GRANT ALL ON perlmaven_dev.* TO 'perlmaven_user'@'localhost';
   mysql> CREATE USER 'perlmaven_test'@'localhost' IDENTIFIED BY 'perlmaven_test';
   mysql> GRANT ALL ON perlmaven_test.* TO 'perlmaven_test'@'localhost';
   mysql> \q


