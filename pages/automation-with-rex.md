---
title: "Learn automation using Rexify"
timestamp: 2021-03-09T07:30:01
tags:
  - Rex
types:
  - screencast
published: true
archive: true
show_related: true
---


During this meeting [Ferenc Erki](https://www.linkedin.com/in/ferki/), the lead developer of [Rex](https://www.rexify.org/) taught
us to set up and configure his hosts using Rex.

We started from an empty management machine. Installed Rex. Created two Ubuntu-based servers. First we had some basic experimentation with Rex
then installed and configured Nginx.


{% youtube id="bLJ3Q0Je8p8" file="rex-1920x1080.mp4" %}

## The content

Create Droplet with Ubuntu 20.04 in New York 1.  Hostname code-maven-rex

Created ssh keypair on the new machine to be used as a management host.
Add the public key to the Digital Ocean admin interface as "Rex" to be used from the management server.

Create 2 Droplets with Ubuntu 20.04 in New York 1 Hostname ubu-1 and ubu-2


## Rexfile

During the session we put together a Rexfile with a number of tasks. This is what we got. Whatch the video for explanations.

{% include file="examples/rex/infra/Rexfile" %}

## HTML file

{% include file="examples/rex/infra/files/main.html" %}

## Nginx config file

{% include file="examples/rex/infra/files/ubu-1.conf" %}

## ~/.ssh/config

The SSH config file we created:

{% include file="examples/rex/infra/config" %}

## History

This is the history of the shell commands that we used during the meetig. I tried to clean the duplicate entries.
I hope having them here makes it easier to reproduce the commands.

{% include file="examples/rex/infra/history.txt" %}


## Links that were mentiond

[RexOps](https://github.com/rexops) - Central Repository for all RexOps projects.

[Repology](https://repology.org/project/rex/versions) showing which version of Rex is packaged in each Linux distribution.

<a hrf="https://metacpan.org/pod/Rex">Rex on MetaCPAN</a> and the list of [reverse dependencies](https://metacpan.org/requires/module/Rex?size=200),
that is CPAN distributions that use Rex.

## FErki's answers to questions from the session

<blockquote>
  <p>What is a meaning of name Rex itself ? :)</p>
</blockquote>

<p><strong>R</strong>emote <strong>ex</strong>ecution (see also in the [FAQ](https://www.rexify.org/docs/faq/index.html#isitcalledrexorrex)).</p>

<blockquote>
  <p>Does each version of Rex have own features ? <em>(about [feature flags](https://metacpan.org/pod/Rex#FEATURE-FLAGS))</em></p>
</blockquote>

<p>Rex has named feature flags to opt in or out of various behavior based on your exact needs. Versioned feature flags control multiple named feature flags at once, so they can set defaults across the board. That is, the versioned feature flag of ```1.4</code> means "please use all the default from rex-1.4".</p>

<p>A versioned feature flag is only introduced if we think the default behavior should change in some way. In other words, default behavior shouldn't change unless explicitly asked for by specifying a different feature flag.</p>

<blockquote>
  <p>So better to use cpan Rex ? <em>(after installing with ```apt</code> from default Ubuntu repositories)</em></p>
</blockquote>

<p>Short answer: Yes, the recommended way to install Rex is from CPAN, because that's the canonical upstream source of releases.</p>

<p>Longer version: It depends on the use case and circumstances. You can [get Rex](https://www.rexify.org/get/index.html) from CPAN, from many different [package repositories](https://repology.org/project/rex/versions), or build it from source. Choose the option that fits your use case the best.</p>

<blockquote>
  <p>Is any issue to use key auth from Windows to Linux machines ?</p>
</blockquote>

<p>No, in general no issues.</p>

<p>The important detail is that Rex must use the Net::SSH2 backend for SSH connections on Windows, and that needs different configuration for authentication details. Net::SSH2 is based on libssh2 so the public and private key path need to be specified explicitly.</p>

<p>The other backend, Net::OpenSSH uses the ssh binary, so it doesn't have to rely on Rex configuration, but it doesn't support Windows.</p>

<blockquote>
  <p>Is there an option to send 'yes' when we run rex? <em>(after being prompted to accept the SSH host key of a remote endpoint)</em></p>
</blockquote>

<p>An important part of the story is that the prompt belongs to SSH, not Rex.</p>

<p>Ideally, the SSH host keys from all the hosts belonging to an infrastructure would be part of the site's inventory. Then the keys would be distributed to those who need to use SSH to connect to these hosts. There's even a [dedicated DNS record type](https://en.wikipedia.org/wiki/SSHFP_record) to store this information.</p>

<p>Apart from that, there are multiple ways to disable this prompt. Some examples, depending on the security and other requirements you might be looking for:</p>

* configure SSH to don't check the host key strictly, e.g. specify ```StrictHostKeyChecking no</code> in <code>~/.ssh/config</code> or <code>/etc/ssh/ssh_config</code>
* configure Rex to pass the same option to SSH with ```Rex::Config-&gt;set_openssh_opt( StrictHostKeyChecking =&gt; 'no', );</code>

<blockquote>
  <p>Is it posisble to pass something like ssh  -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no  -i ~/.ssh/id_rsa</p>
</blockquote>

<p>Yes, arbitrary SSH options can be set on the SSH side via ```~/.ssh/config</code> or <code>/etc/ssh_ssh_config</code> when Net::OpenSSH is being used.</p>

<p>SSH options (```-o</code>) can also be set on the Rex side with <a href="https://metacpan.org/pod/Rex::Config#set_openssh_opt"><code>Rex::Config-&gt;set_openssh_opt();</code></a>, and identity files (<code>-i</code>) can be set via <a href="https://metacpan.org/pod/Rex::Commands#public_key($key)"><code>public_key $path;</code></a> and <a href="https://metacpan.org/pod/Rex::Commands#private_key($key)"><code>private_key $path;</code></a></p>

<blockquote>
  <p>Are there any OS (Linux distributions) dependencies for command like service ?</p>
</blockquote>

<p>No explicit dependencies.</p>

<p>Right after connecting to the managed endpoint, Rex discovers which operating system it is supposed to manage, and chooses a service and package manager module accordingly. If systemd is active, it uses that for service management.</p>

<p>So on Ubuntu it might choose ```upstart</code> and <code>apt</code>, on Gentoo <code>OpenRC</code> and <code>emerge</code>.</p>

<blockquote>
  <p>is rex IRC channel still active? </p>
</blockquote>

<p>The [Rex IRC channel](https://webchat.freenode.net/#rex) is very much alive, yes! Come by and say hi!:)</p>

<blockquote>
  <p>I’ve never used other common server management software like Ansible or puppet. How does Rex compare?</p>
</blockquote>

<p>To get into the right mindset about Rex, maybe the shortest way is to think about it like: "it's possible to implement tools like Ansible and Puppet with Rex, but not the other way around".</p>

<p>In other words, Rex follows a different trade-off by being a framework to build your own tool. It gives you more freedom about what to automate and how to automate, but this also means you have more responsibility to carefully analyse your exact situation and implement your choices.</p>

<p>If you need a tool that pushes changes over SSH from a YAML-based configuration syntax, you can build that. If you need an agent that runs every 30 minutes to pull configuration from a central server, then you can build that too. It's your choice. Any of those systems and approaches can be good enough solutions when applied correctly to the situation at hand.</p>

<blockquote>
  <p>Is it possible to use Rex for deploying Perl modules to remote machines?</p>
</blockquote>

<p>Yes, in fact the original use case of Rex was deployment management (as far as I know).</p>

<p>In the end, any management system boils down to running commands and managing files. If there's a command to run, or a file to configure, it's possible to do that with Rex too. This includes Perl module deployment as well.</p>

<blockquote>
  <p>How should we share and distribute useful Rex tasks we’ve written with other developers?</p>
</blockquote>

<p>Rex code is Perl code, so the same rules apply for distributing the results as well. Like with most things, the "best" method depends on the exact needs.</p>

<p>I prefer the following approaches in general:</p>

* share small snippets as gists
* put my code under version control and share the repo with others
* build a module around a specific scope and publish it on CPAN
