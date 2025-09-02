# Install and configure uwsgi

```
apt install uwsgi
apt install uwsgi-plugin-python3
ln -s /home/dev/python-flask-demo/config/demo-uwsgi.ini /etc/uwsgi/apps-enabled/demo-uwsgi.ini
service uwsgi restart
```



If there is a problem you might find help by looking at the log file:

```
/var/log/uwsgi/app/demo-uwsgi.log
```

I got the following error "Fatal Python error: init_fs_encoding: failed to get the Python codec of the filesystem encoding"

I had make the home directory of the `dev` user to be world readable, that solved the problem:

```
chmod +r /home/dev/
```


