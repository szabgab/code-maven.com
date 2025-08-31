---
title: "Exercise: Linux as a Virtual Environment - install + nginx"
timestamp: 2018-03-08T18:30:01
tags:
  - VirtualBox
  - Ubuntu
  - Linux
  - Nginx
published: true
books:
  - linux
author: szabgab
archive: true
---


These exercises were given to the participants of the [DevOps Workshop](http://devops-workshops.code-maven.com/) on using Linux as a Virtual OS on Windows (or Mac or another Linux).

A few exercises that you could do to practice what we have learned during the workshop.
Some will go way beyond it and make you learn a lot more about using Linux on the command line.


1. Set up another Virtual Box and Install Ubuntu. This time use a different IP address.
1. Make sure you can ping the machine from your host machine (Your Windows or OSX machine)
1. Install the ssh server and check that you can connect to the guest machine using Putty or some other ssh client.
1. Install Nginx on this new machine
1. Check if you can visit the page using your browser on your host machine
1. Edit the default html file to show your name instead, or in addition to the default text
1. Check out what kind of options does the "ls" command have, experiment with it.
1. Is "ls" already an "alias" in your computer?
1. Read the manual of ls by typing in "man ls" You can use space to advanced in the manual. You can use "q" to quit.
1. Once you find a flag combination that you like create an alias so whenever you type a single "l" it will execute "ls" with your favorite flags.
1. Make the above alias permanent in your shell. (Try by logging in in another putty session and check if the new l alias is available there too!)
1. Create a file called workshop.txt add some notes to it.

So far is basically the same as we had during the workshop. Use the [slides](http://code-maven.com/ws1) as your guide.

## Additional tasks

1. Create a new file called a.txt with "hello" in it.
1. Create a new file called b.txt  with "world" in it.
1. Rename a.txt to be b.txt (using mv) observe that Linux does not ask for confirmation when you overwrite a file.
1. Find out how to convince mv to ask for permission before overwriting a file.
1. Try the above with "cp" that stand for copy.

## More

1. Create a sub-directory in your home directory called "web".
1. Inside the "web" directory create a file called "index.html" with some content.
1. Find out where where is the default configuration file of nginx (hint: it was in the slides) and change it so that the default directory will be the "web" sub-directory of home directory. (how do you know the full path to the "web" directory?
1. reload the configuration file of Nginx by running `sudo service nginx reload`.
1. Reload your browser and check if the new page is from the "web" directory.
1. If you managed to do this, you can now create additional files in this directory without root privileges.


