# SQLite version

This is using the version I installed from [SQLite](https://www.sqlite.org/download.html) on Ubuntu Linux.

## Interactive

```
$ sqlite3
sqlite> .version
SQLite 3.53.0 2026-04-09 11:41:38 4525003a53a7fc63ca75c59b22c79608659ca12f0131f52c18637f829977f20b
zlib version 1.3.1
gcc-13.3.0 (64-bit)

sqlite> .quit
```

## Piped to STDIN

```
$ echo .version | sqlite3
SQLite 3.53.0 2026-04-09 11:41:38 4525003a53a7fc63ca75c59b22c79608659ca12f0131f52c18637f829977f20b
zlib version 1.3.1
gcc-13.3.0 (64-bit)
```

## Redirect from file


{% embed include file="examples/version.sql" %}

```
$ sqlite3 < examples/version.sql
SQLite 3.53.0 2026-04-09 11:41:38 4525003a53a7fc63ca75c59b22c79608659ca12f0131f52c18637f829977f20b
zlib version 1.3.1
gcc-13.3.0 (64-bit)
```

## Command line flag

```shell
$ sqlite3 --version
3.53.0 2026-04-09 11:41:38 4525003a53a7fc63ca75c59b22c79608659ca12f0131f52c18637f829977f20b (64-bit)
```

