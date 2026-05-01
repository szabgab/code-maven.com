# SQLite version

## Interactive

```
$ sqlite3
sqlite> .version
SQLite 3.46.1 2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69aalt1
zlib version 1.3.1
gcc-15.2.0 (64-bit)

sqlite> .quit
```

## Piped to STDIN

```
$ echo .version | sqlite3
SQLite 3.46.1 2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69aalt1
zlib version 1.3.1
gcc-15.2.0 (64-bit)
```

## Redirect from file


{% embed include file="examples/version.sql" %}

```
$ sqlite3 < examples/version.sql
SQLite 3.46.1 2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69aalt1
zlib version 1.3.1
gcc-15.2.0 (64-bit)

```



