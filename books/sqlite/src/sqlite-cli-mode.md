# SQLite CLI - .mode

To show the current mode

```shell
sqlite> .mode
.mode qbox --limits on --quote relaxed --sw auto --textjsonb on
```

List available modes

```shell
sqlite> .mode --list
available modes: ascii box c column count csv html insert jatom jobject json line list markdown off psql qbox quote split table tabs tcl batch tty
```

Set a mode:

```
sqlite> .mode column
```

