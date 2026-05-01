# SQLite interactive shell - `.help`

The command line tool has a number of internal commands starting with a dot. `.help` will show the list of the commands.
`.quit` or `.exit` will close the shell.

[Command Line Shell For SQLite](https://sqlite.org/cli.html)

The commands can be given
* interactively
* sent through a pipe
* redirected from a file


```
$ sqlite3
SQLite version 3.45.1 2024-01-30 16:01:20
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.

sqlite> .help
...

sqlite> .quit

$
```

