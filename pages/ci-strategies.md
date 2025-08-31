---
title: "CI strategies"
timestamp: 2019-01-01T07:30:01
tags:
  - CI
published: false
author: szabgab
archive: true
---


If the company is very small, it might not be the right thing to fully automate everything.

## Two separate instances installed manually

Create a VPS (eg. a Google VM instance), manually install everything needed for the application to run and for the tests
to run. Clone the machibe so we have two copies. One for production and one for testing.
The CI system triggered by a commit, can connect to the test server, upload the current code (e.g. the code from the
current commit in the version control system) and use that machine for testing. Because the two machines are identical
we can be reasonably sure that if the tests pass on the test-machine then that part of the code would work on the
production machine as well.

In order to save money, the test server can be launched and stopped by the CI system, so in environments, such as the
Google Cloud, we would only incur high cost when the tests, and thus the test-machine, are running. (Machines that are not
running are a lot cheaper than running instances.)

The main drawback of this approach is that if we need to add another piece of software to the stack, or if we need to
upgrade some third-party library, we'll need to do it on both the test-instance and the production-instance.
This can be error-prone and time-consuming, but if we only have two machines it might be still cheaper and faster than
automating the whole process.

Another issue with this solution is the question of timing. You might make some changes to your code in development that
requires an upgrade of a third-party library. So you upgrade it on the test-server immediately, but when do you upgrade
it on the production-server? The new version might not be compatible with your old code so these two pieces are
interdependent. You'll have to upgrade them at the same time on the production server as well.

## Using an image to create the test- and production- instances

After manually installing one server we can create an image of the hard disk and then we can use that image to start
both the test-instance and the production-instance. When we need a new piece of software to be installed we launch a new
instance based on the image. Manually install or upgrade the software and create a new image. We should number the
images or use timestamps to be able to tell them apart.
Then during testing we'll use the new image. Once we are ready to deploy we start a new production-server based on the
new image.

This has the advantage that we don't need to remember to install/upgrade packages during the deployment. It also has
a huge disadvantage that we need to make sure to direct the network traffic to the new production-server and that any
persistant information that was on the serve either gets lost or must be transferred. So having this procedure with
a database server is much harder than with a web server that uses a separate machine as a database server.
With a web server, we also need to make sure that all the session information is preserved. Either by transferring them
to the new instances, or by not having them on the web server in the first place.


## Using configuration-management system to create and maintain the instances

An interesting alternative is to create a configuration management script with one of the tools
such as [Ansible](https://www.ansible.com/), [Chef](https://www.chef.io), [Puppet](https://puppet.com/).
(There are many others, and for simple cases you can even write a shell script to do the job).

You would ue this script to setup and change both the test- and production- instances. This has the huge advantage that
even if you have hundreds, or thousands of instances, you can still maintain them with a single script.

When you need a change during development, you make this change in the configuration files in a <b>branch</b>
so that only the test-servers see the change. When time comes to deploy the new code and you need to change
the configuration of your production-servers as well, you merge the changes of the configuration management script
as well and when you run them you will upgrade the production-servers exactly in the same manner as you did with the
test servers.

The big issue with this approach is that setting up a server can take a lot of time.

What do I mean by that?

When we installed the server manually it took as hours of manual labor. Now the configuration script - that we worked
on for days - can handle it in 20 minutes. So am I spoiled now that I say it is a log of time? Well, yes and now.

If setting up the test instance takes 20 minutes that means every time the CI runs I have to pay for the test-servers doing
no useful work for those minutes and the developers don't get their feedback from the CI system for at least 20 minutes.
If the actual test only runs for 5 minutes, then having a 20-minute overhead is not a very good idea.


