---
title: "Getting Started with Ansible managing CentOS on Digital Ocean"
timestamp: 2018-03-07T16:00:01
tags:
  - Ansible
  - Digital Ocean
  - ssh
  - ping
  - date
  - uptime
  - free
published: true
author: szabgab
archive: true
---


In this example we'll take a freshly installed Linux box running CentOS 7.4 on a
[Digital Ocean droplet](/digitalocean) and use [Ansible](/ansible) to make basic configurations.

I assume that you already have [Ansible installed](/ansible) on your desktop/notebook, whatever machine is
in front of you. If not, check out the linked article.


## Create the host machine on Digital Ocean

For this article I've created the host machine manually.

Visit [Digital Ocean](/digitalocean), sign up if you don't have an account yet. (Using that link you are supposed to get $10 credit).

If you have not done so yet, [Create an ssh keypair](/generate-and-deploy-ssh-private-public-keypair) and upload the public key under the "SSH keys" section of the [Security](https://cloud.digitalocean.com/settings/security) of your [Profile](https://cloud.digitalocean.com/settings/profile). This will be useful as this will allow you to connect to the remote host without providing a password.

Now, in order to create your first Droplet, visit the [list of droplets](https://cloud.digitalocean.com/droplets) and click on the "Create" button and select "Droplets".

<ol>
  <li>Select `CentOS 7.4 64 bit` as that's what we are checking out now. For size select the smallest. Even that is way to big for our needs.</li>
  <li>For `datacenter` select whatever you like. I usually just select New York 1.</li>
  <li>"Select additional options" can be left alone for now.</li>
  <li>At "Add your SSH keys" you should see the SSH key you added earlier. Select the checkbox next to it.</li>
  <li>Make sure you are asking for 1 Droplet.</li>
  <li>The hostname can be anything now. Even the one they offer.</li>
  <li>Click "Create".</li>
</ol>

After about 30 second your Droplet will be ready.

![](/img/digital-ocean-centos-created.png)

Hover over the IP address and a link `copy` will appear. Click on that to get the IP address in your clipboard.
If you can paste from there in your editor then you can save some extra work.

Create a file called `inventory.cfg` with the following content, just use the IP address of your Droplet instead of mine:

{% include file="examples/ansible/centos_first/inventory.cfg" %}

The "inventory file" of Ansible is a single configuration file that holds all the hosts you'd like to manage. The hosts can be grouped in various ways, but now as we only have one machine we created a group called "all". and put the IP address of the machine in that group.

## Check if Ansible can access the hosts using Ping

Let's verify that Ansible can access the machine.
Just as with network you'd use the [ping](https://en.wikipedia.org/wiki/Ping_(networking_utility)) command, Ansible also provides a command called "ping" that checks if the remote machine is accessible to Ansible. Instead of sending [ICMP packets](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol), the ping of Ansible will try to log in to the remote machine using standard SSH.

Run the following command:

```
$ ansible -i inventory.cfg all -u root -m ping
```

It will first ask you to check the authenticity of the host by displaying a message like this:

```
The authenticity of host '159.65.236.52 (159.65.236.52)' can't be established.
ECDSA key fingerprint is SHA256:5G1v0wAEaqgQVfXrrqYlp4kRFTLJc263H3CvcqUEnlg.
Are you sure you want to continue connecting (yes/no)?
```

If you type in `yes` then it will add the signature of the host to 
`~/.ssh/known_hosts` and it won't bother you again with the same question.

The command will continue and print

```
159.65.236.52 | SUCCESS => {
    "changed": false,
    "failed": false,
    "ping": "pong"
}
```


If you don't want to check the authenticity of the host you can tell ansible to tell the ssh command using the `--ssh-common-args` flag to not check the authenticity and to not save the signature in the known_hosts file.

```
$ ansible -i inventory.cfg all -u root -m ping --ssh-common-args "-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
```

This will have the same output as the earlier command.

```
159.65.236.52 | SUCCESS => {
    "changed": false,
    "failed": false,
    "ping": "pong"
}
```

Let's see the details of the command:

* The `-t inventory.cfg` tells ansible the location of the inventory file.
* `all` selects the host(s) upon which we'd like to act.
* `-u root` tells Ansible to use user `root` on the remote server.
* `-m ping` tells Ansible to execute the "ping" module.
* `--ssh-common-args` tells ansible to pass the  `-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no` flags to the ssh command it uses.


## authenticity of the host

For the upcoming command I'll assume that when you ran the previous command you ran it without the special parameter for ssh
and then you typed "yes" when the ssh client wanted to save the signature in the "~/.ssh/known_hosts" file. If not run this again:

```
$ ansible -i inventory.cfg all -u root -m ping
```

The next time you run the above command it should work without asking any further questions.

## Collect information from the remote server

Ansible has plenty of modules, but it also allows you to execute arbitrary command on the remote machine:

<b>Fetch the date of the remote machine</b>

```
$ ansible -i inventory.cfg all -u root -a date 
```

```
159.65.236.52 | SUCCESS | rc=0 >>
Wed Mar  7 11:35:52 UTC 2018
```

<b>Get the hostname of the remote host</b>:

```
ansible -i inventory.cfg all -u root -a hostname
```

```
159.65.236.52 | SUCCESS | rc=0 >>
centos-s-1vcpu-1gb-nyc1-01
```

<b>uptime</b>

```
$  ansible -i inventory.cfg all -u root -a uptime
```

```
159.65.236.52 | SUCCESS | rc=0 >>
11:40:38 up 41 min,  1 user,  load average: 0.05, 0.03, 0.05
```

<b>free memory</b>

```
$  ansible -i inventory.cfg all -u root -a free
```

```
159.65.236.52 | SUCCESS | rc=0 >>
              total        used        free      shared  buff/cache   available
Mem:        1016224       83256      780424       13048      152544      767372
Swap:             0           0           0
```

<b>free memory in megabytes</b>

```
$  ansible -i inventory.cfg all -u root -a "free -m"
```


```
159.65.236.52 | SUCCESS | rc=0 >>
              total        used        free      shared  buff/cache   available
Mem:            992          81         761          12         149         749
Swap:             0           0           0
```


## Upgrade everything on the CentOS server

Usually when you get a new server some of the packages might be already out of date. Some might have had some security fixes.
So updating them to the latest version i usually a good idea.

```
ansible -i inventory.cfg all -u root -m yum -a "name=* state=latest"
```

It will run a long time. Probably several minutes. Hopefully it will end with success with a big blob of output that starts with

```
159.65.236.52 | SUCCESS => {
    "changed": true,
    "failed": false,
```

IF you run the same command again, this time will say everything is up-to-date:

```
159.65.236.52 | SUCCESS => {
    "changed": false,
    "failed": false,
    "msg": "",
    "rc": 0,
    "results": [
        "Nothing to do here, all packages are up to date"
    ]
}
```


## Rebooting the CentOS server using Ansible

We can run the regular `shutdown` command with some flags:

```
$  ansible -i inventory.cfg all -u root -a "/sbin/shutdown -r now"
```

This command will reboot the server immediately, but you will see an error message. Basically
because Ansible does not have time to properly disconnect before the server shuts down its ssh connection.

```
159.65.236.52 | UNREACHABLE! => {
    "changed": false,
    "msg": "Failed to connect to the host via ssh: Shared connection to 159.65.236.52 closed.\r\n",
    "unreachable": true
}
```

You can delay the shutdown by one minutes (it only works with increments of minutes)

```
$  ansible -i inventory.cfg all -u root -a "/sbin/shutdown -r +1"
```

That will return with success and a warning and a minute later the host will reboot itself.

```
 [WARNING]: Module invocation had junk after the JSON data:   Broadcast message from root@centos-s-1vcpu-1gb-nyc1-01 (Wed 2018-03-07
13:46:31 UTC):    The system is going down for reboot at Wed 2018-03-07 13:47:31 UTC!

159.65.236.52 | SUCCESS | rc=0 >>
Shutdown scheduled for Wed 2018-03-07 13:47:31 UTC, use 'shutdown -c' to cancel.
```

To avoid that warnings we can even tell the `shutdown` command to avoid the broadcast:

```
$  ansible -i inventory.cfg all -u root -a "/sbin/shutdown --no-wall -r +1"
```

That looks like the cleanest so far:

```
159.65.236.52 | SUCCESS | rc=0 >>
Shutdown scheduled for Wed 2018-03-07 14:00:08 UTC, use 'shutdown -c' to cancel.
```


## Conclusion

That's enough for now. We'll get deeper in an upcoming article.


