---
title: "Deploying Python with uWSGI and Nginx on Ubuntu 13.10"
timestamp: 2016-11-23T23:30:01
tags:
  - Python
  - uWSGI
  - Nginx
  - Ubuntu
published: true
author: szabgab
---


The following is a tutorial on how to set up uWSGI with an Nginx front end to server simple Python scripts.

In this tutorial we will only use the packages that are supplied by Ubuntu.


It was tested on an Ubuntu 13.10 x64 droplet of [Digital Ocean](/digitalocean).

After you create a droplet with Ubuntu 13.10 x64 you'll get an e-mail with your IP address
and the password of root. In this example I'll use 1.2.3.4 as the IP address. You'll have to replace
the commands with the IP address of your server.

First just ssh to the server. On Linux/Unix/OSX you would type this:

```
$ ssh root@1.2.3.4
```

On Windows you'd probably install [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) and use that.

Once you are logged in you need to update the packages to the latest by typing the following:

```
# aptitude update
# aptitude safe-upgrade
```

Then reboot:

```
# reboot
```

This will disconnect you from the server. After a few seconds you can continue:

I'd recommend copying your public ssh key to let you ssh without password:

```
$ scp ~/.ssh/id_rsa.pub root@1.2.3.4:.ssh/authorized_keys
$ ssh root@1.2.3.4
```

If the first command worked well, then the second won't ask for a password.

## Install uWSGI


```
# aptitude install uwsgi
# aptitude install uwsgi-plugin-python
```

Just to make sure, check the versions we have. I got the following:

```
# python -V
Python 2.7.5+
# uwsgi --version
1.9.13-debian
```

Then create a user called <b>dev</b> so we won't do everything as root.


```
# adduser --gecos '' --disabled-password  dev
```

Switch to the new user and create a directory for the project.

```
# su - dev 
$ mkdir project
$ cd project/
```

In the project/ directory create a file called app.py with the following content:

```
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello World From Python"
```

Run the following script:

```
$ uwsgi --http-socket :9090 --plugin python --wsgi-file app.py 
```

Now you can already visit the we site by following th URL:
http://1.2.3.4:9090 (remember to replace the IP with the one you have).

Without including the python plugin, if I only run

```
$ uwsgi --http-socket :9090 --wsgi-file app.py 
```

I'd get the following error:

```
uwsgi: unrecognized option '--wsgi-file'
getopt_long() error
```


Further uWSGI configuration (3 processes handle the requests) can be provided
on the command line:

```
$ uwsgi --http-socket :9090 --plugin python --wsgi-file app.py --process 3
```

But, instead of  the command line, it is probably better to create a configuration
file called `/home/dev/project/project-uwsgi.ini` with the following content:

```
[uwsgi]
http-socket    = :9090
plugin    = python
wsgi-file = /home/dev/project/app.py
process   = 3
```

Now we can launch the server using the following command:

```
uwsgi --ini project-uwsgi.ini
```

We can shut it down by pressing Ctrl-C.

Then we switch back to user <b>root</b> typing

```
$ exit
```

We can then create a symbolic link so uWSGI will start our server automatically
when the server boots up:

```
# ln -s /home/dev/project/project-uwsgi.ini /etc/uwsgi/apps-enabled/
```

now we can launch the service as root with the following command:

```
# service uwsgi start
```

## Add Nginx to the mix


First thing, replace <b>http-socket</b> by <b>socket</b> in project-uwsgi.ini  file.

Install Nginx and remove the default configuration file:

```
# aptitude install nginx
# service nginx start
# rm /etc/nginx/sites-enabled/default
```

Instead of that create a new configuration file in
`/home/dev/project/nginx-uwsgi.conf`
with the following content:

```
server {
  location /hello/ {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:9090;
  }
}
```


Create a symbolic link in the directory of Nginx so when Nginx starts this configuration
file is taken in account.

```
# ln -s /home/dev/project/nginx-uwsgi.conf /etc/nginx/sites-enabled/
# service nginx restart
```

Now you can visit http://1.2.3.4/hello and see the output of the same script as you saw earlier.

## Show the environment

Edit the `/home/dev/project/app.py` file to have the following in it.

```
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])

    html = "<h1>Hello World From Python</h1>\n"
    html += "<table>\n"
    for k in env:
        html += "<tr><td>{}</td><td>{}</td></tr>\n".format(k, env[k])
    html += "</table>\n"

    return html
```

and visit your home page again. You'll see all the environment it receives.


## Add echo form

Update the script again to include a form and to echo back whatever the user typed in:

```
import cgi

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])

    html = "<h1>Hello World From Python</h1>\n"
    html += "<table>\n"
    for k in env:
        html += "<tr><td>{}</td><td>{}</td></tr>\n".format(k, env[k])
    html += "</table>\n"
    html += "<form>\n"
    html += '<input name="txt" />\n'
    html += '<input type="submit" value="Echo" />\n'
    html += "</form>\n"


    form = cgi.FieldStorage(environ=env)
    if 'txt' in form:
        html += "<hr>You said: <b>{}</b>\n".format(form['txt'].value)

    return html
```


Of course you'd probably not build a real application this way, but it is a good way to
play with the environment and see that everything works fine.

It can also be very useful to write small web interfaces.

## 502 Bad Gateway

If, while already trying to use Nginx you happen to get the above error in the browser and you might also get something like this:

```
upstream prematurely closed connection while reading response header from upstream, client: 192.117.127.193, server: , request: "GET / HTTP/1.1", upstream: "uwsgi://127.0.0.1:9090", host: "159.203.101.19"
```

in `/var/log/nginx/error.log` the error log on Nginx, then you probably have forgotten to replace `http-socket` by `socket` in the <b>project-uwsgi.ini></b> file
or you have forgotten to reload uwsgi after doing so. This happened to me as well, and took me quite some time to figure out the problem.



