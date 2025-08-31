---
title: "Set up CGI with Apache on Ubuntu Linux"
timestamp: 2015-11-12T08:30:01
tags:
  - CGI
  - Apache
  - curl
  - Ubuntu
  - Bash
published: true
author: szabgab
archive: true
---


CGI, the Common Gateway Interface is a simple  way to write web applications. Especially when you are running Apache as the web server.
Recently I wanted to show a few examples using CGI in various programming languages, but first I had to make sure CGI is enabled on my server.


I have been using the an [Ubuntu based Vagrant image](https://perlmaven.com/vagrant-perl-development-environment) for my experiments
but I think the same steps will work in any other Ubuntu-based or any Debian based system.


## Install Apache 2

If you don't have it installed yet, you will need to install the web servers itself:

```
$ sudo apt-get install apache2
```

## Install curl

`curl` can be used to fetch web pages. 
It is not a requirement for our set up, but it is nice to have on the server as it can be used to check the pages
without opening a real browser. Besides, at least in my set up, I have configured the web server on a Virtual Environment,
but I have not set up port-forwarding for port 80 yet and thus I would not be able to access the web server from my
desktop. (The article about [Vagrant development environment](https://perlmaven.com/vagrant-perl-development-environment)
has explanation how to set up the port forwarding.)

```
$ sudo apt-get install curl
```

## Try the web server

At this point we can try if the web server works:

```
$ curl http://127.0.0.1/
```

It will print some HTML on the screen.


## Configure CGI

I looked around the `/etc/apache2` directory, which is the standard place to find the
configuration files of Apache. I've found the `/etc/apache2/conf-available/serve-cgi-bin.conf`
file that has a symbolic link from `/etc/apache2/conf-enabled/serve-cgi-bin.conf`.
It has a section that maps the /cgi-bin path in the URLs to the `/usr/lib/cgi-bin/`
directory in the hard disk and enables CGI execution in this directory.

{% include file="examples/apache/serve-cgi-bin.conf" %}

That's not enough though. We also need to enable the CGI module of Apache.

The installed modules of Apache can be found in the `/etc/apache2/mods-available` directory.
The cgi module is called `cgi.load`

The enabled modules have symbolic links in `/etc/apache2/mods-enabled`, but as I found out,
the CGI module did not have a symbolic link there: The CGI module was not enabled by default.

```
$ cd /etc/apache2/mods-enabled
$ sudo ln -s ../mods-available/cgi.load
```

Added the symbolic link.


## Reload Apache configuration

As the configuration of Apache has changed we need to tell Apache to reload its configuration files:

```
$ sudo service apache2 reload
```


## Create the first CGI script

Now that we have enable CGI we can create our first CGI script.

This first CGI example will be created in Bash.
Later on you can check out the solutions to the various [web exercises](/exercises)
Especially the [Hello World!](/exercise-web-hello-world) exercise and
the [Web Echo](/exercise-web-echo) exercise and their solutions.


I've created a file called `/usr/lib/cgi-bin/hw.sh` using `sudo vim /usr/lib/cgi-bin/hw.sh`

{% include file="examples/apache/hw.sh" %}

Made it executable:

```
$ sudo chmod +x /usr/lib/cgi-bin/hw.sh
```

Then I could access it through Apache using:

```
$ curl http://127.0.0.1/cgi-bin/hw.sh
Hello World!
```

## Troubleshooting

If the `curl` request returns `404 Not Found` then either the file is not in the correct place, or the
URL given to curl is incorrect.


If the `curl` requests return `500 Internal Server Error` you might have forgotten to make the script
executable using `sudo chmod +x /usr/lib/cgi-bin/hw.sh`

or the hashbang line (The first line that should look like this `#!/bin/bash` was not typed in correctly.

Another common source of error is the difference between the newlines in MS Windows and Linux in [text files](https://perlmaven.com/what-is-a-text-file).
You have to make sure that your script has the Unix/Linux line-ending. One of the best ways might be to run
`dos2unix hw.sh` that will replace the Windows-newlines by Unix-newlines.

Lastly, the 500 error might occur if the first line printed by the script is not `Content-type: text/html`
followed by 2(!) newlines.

## Further reading

Check out all the articles related to [CGI and Perl](https://perlmaven.com/cgi) and
[CGI and Ruby](/hello-world-using-cgi-in-ruby).

## Comments

A comment that was deleted before I decided to move them over.
---

Well Said. I have been fighting this for 20 years. I set up an Apache Server, it runs for years, and when I go to do it again, everything is all moved around and it takes hours and hours to simply get a hello world program to run under apache. It is never clear on how to do it, they leave no instructions, For petes sake why doesn't the release at least have the file http.conf still there with the whole instruction set on how to get the functionality of http.conf working under the new paradigm??? It boggles the mind.

---

Thumbs up. Moving files around for no real gain makes the software difficult to use. I too spent hours trying to get things straight.

For other users, here's some advice that worked for me:

1: Enable the CGI subsystem with a2enmod cgid

2: Uncomment the CGI handler in mods-enabled/mime.conf, or include this directive in your specific vHost section

AddHandler cgi-script .cgi

3: Include Options ExecCGI in the vHost or topmost directory where you want these programs to be available

---

In fact, very most times I had any issue I lost patience with myself, I was able to get someone to take the the time and lead me step by step. The truth, however, is that you are suposed to spend some time reading and learning stuff yourself as people generally expect some basic level of knowledge.

And you know, I suspect you had neen doing some small stupid mistake, just as I sometimes do. But if you need an advice, you need to ask politely rather than throw feces.

<hr>

Oh thank you thank you thank you. 3 HOURS of searching before I found this article that finally talks about the CGI module and the soft link to fix this in mods-enabled. Why is this so well hidden on the internet is a mystery.

<hr>

After getting it to work with hello world, I tried to run one of my past cgi-perl scripts from an HTML page in my recent home apache2 server. The cgi-perl script runs fine as a webserver elsewhere - developed during my doctoral days. It's a long code: a certain bioinformatic application.

The HTML page calls the cgi-perl script using method 'GET' as follows:

```
<form action="http://127.0.0.1/cgi-bin/newsdnamelt.cgi" method="GET">
<center><input value="Run" type="submit"></center>
</form>
```

I am getting this error both with the HTML as well as with curl on command prompt:

Internal Server Error

The server encountered an internal error or misconfiguration and was unable to complete your request.

Please contact the server administrator at webmaster@localhost to inform them of the time this error occurred, and the actions you performed just before this error.

More information about this error may be available in the server error log.
Apache/2.4.29 (Ubuntu) Server at 127.0.0.1 Port 80

Any hint would be deeply appriciated.

-----------------------------------------------------------------------------------------------------

- Thanks in anticipation and Warm Regards,

---

PS: Interestingly .sh scripts placed at /usr/lib/cgi-bin/ works just fine from HTML submit button - like the hw.sh.
But none of the cgi-perl scripts do.

These scripts start in the following way and all of them have worked just fine from similar HTML submission pages in the past.
So, I wonder what's wrong! Any advice would be of great help!

-------------------------------------------------------------------------------------------

#!/usr/bin/perl

use CGI qw(:standard);
print "Content-type:text/html\n\n";

#============Input Environment variables======
$inptype;$filename;$inpseq;$x;$y;$Temp;$Na;$K;$NH4;$Mg;$tag;$tparam,$ustartbp;
#=============================================

$qstr = $ENV{QUERY_STRING};

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~env input from html~~~~~~~~~~~~~~~~~~~~
$qstr="choice=dirseq&filename=&dnaseq=GCGCGCGCGCGCGatgtcgtacgcatgcgatcagtcagcgacaCGCGC&tag=&tparam=&startbp=&window=20&overlap=0&Temp=37&Na=0.165&K=0&NH4=&Mg=0.01";
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print $qstr,"\n";

@qdata = split(/&/,$qstr);
#open (OUT,">ch.out");

---


Are the scripts executable, can you get the errors from the log file of the server?

<hr>

Excellent discourse. Great sincerity in helping the community. Long live Linux and opensource coding!! 

<hr>

thanks

<hr>

Hey! It works. :)

I'm now a "veteran" PHP dev. Because of that, I've not attempted traditional CGI scripting before but now I'm trying to add REBOL to my web dev toolbox and this is now necessary for me to do that. Funny thing... Your bash script example works but my REBOL script is returning a 500 Error for having a "malformed header" even though there are no typos and 2 newlines preceding the content. Off to find out why! Thanks for getting me going this far!

---

I think this usually happens if the code does not print the Content-Type properly.

<hr>

Thanks a lot sir!!

<hr>

Hi,

Instead of manually creating the symlink with

$ cd /etc/apache2/mods-enabled
$ sudo ln -s ../mods-available/cgi.load

you should use the provided tool a2enmod. Ubuntu also provide a2disconf a2dismod a2dissite a2enconf and a2ensite for enabling and disabling modules, sites and configuration blocks

Thanks for all your work.

---

your post hi-lights exactly what is wrong with the linux community. You seem to think that " Ubuntu also provide a2disconf a2dismod a2dissite a2enconf and a2ensite for [this that and the other thing, that you don't provide any instructions for.]" is somehow better than just cutting and pasting the two lines:

$ cd /etc/apache2/mods-enabled
$ sudo ln -s ../mods-available/cgi.load

this is exactly the problem with the linux community: If it ain't broke don't fix it.

ALL instructions should be cut and paste lines form the command line. The FIRST set of instructions on setting up Apache is getting the welome screen to come up (that actually works pretty well,) and the second thing should be how to set up cgi-bin. For who knows what reason apache instructions instead go into multiple virtual hosting environments with do-decagon multi-plexing, cross-over premium drivers... whatever thing that is so complex I wouldn't have a chance to follow. Meanwhile I'm stuck getting hello_world.c which I can easily compile with gcc: ($ gcc -o hello_world.exe hellow_world.c) to run through the browser. Its absolutely ridiculous. This should be a no-brainer and up and running in less than 30 seconds.

<hr>

thanks for the post. it helped me alot.

<hr>

Ah, is it this easy? Why have I been thinking it is somewhat bloody difficult? :o)

For the record, I had the cgid.load already present in my 2018-09-26 Raspbian Buster AND if you are getting that 500 server error, make sure the bash script is not indented (as was mine upon pasting it to nano).

Indeed, not it works from me from my other machines too, which sugests I will be able to drive my RasPi car from a web interface.

<hr>

Hello sir i am trying to configure apache files to run a cgi script
on Apache2 server from last 5 days. please help. hope for your better reply..

when i ran my python(test.cgi) file on localhost server (localhost/test.cgi) it prints the code

<hr>

Many thanks!!!

<hr>

Thank you so much!!

<hr>

Thanks Gabor,
It really help us . Earlier we were using centos and recently we migrated to Ubuntu and our health check was failing for one service which is exposed using cgi.

<hr>

curl http://127.0.0.1/cgi-bin/hw.sh seems to be throwing an error for me :(
Where does your localhost point to ?

---
What is the error?

aswin@aswin-desktop:~$ curl http://127.0.0.1/cgi-bin/hw.sh

```
<html><head>
<title>500 Internal Server Error</title>
</head><body>
<h1>Internal Server Error</h1>

The server encountered an internal error or
misconfiguration and was unable to complete
your request.


Please contact the server administrator at
webmaster@localhost to inform them of the time this error occurred,
and the actions you performed just before this error.


More information about this error may be available
in the server error log.


<hr>
<address>Apache/2.4.18 (Ubuntu) Server at 127.0.0.1 Port 80</address>
</body></html>

```

and what do you see in the error log of the server?

---

I actually reinstalled lubuntu and tried it again and it works now, this was mostly due to some modifications i did to some of my files.
This article was really helpful :)
Thanks!

<h2>

Thanks a lot for this article! :)

<h2>

The missing symlink saved the day! I had the correct apache conf file for site but the cgi was not enabled.


