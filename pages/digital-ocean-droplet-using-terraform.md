---
title: "Create Digital Ocean Droplet using Terraform"
timestamp: 2018-09-15T14:00:01
tags:
  - Terraform
published: true
author: szabgab
archive: true
---


[Terraform](https://www.terraform.io/) makes it easy to manage various cloud resources. In this article we'll see how to use it to create (and destroy) Virtual Machines (aka. Droplets) on [Digital Ocean](/digitalocean).



## Install Terraform

Download [Terraform](https://www.terraform.io/). It is a single executable wrapped in a zip file.
Once you have downloaded it, use `unzip` to extract the executable and them move it to some place that
is in your `PATH` variable so you can easily run it.

For me this was:

<pre>
$ unzip terraform_0.11.8_darwin_amd64.zip
$ sudo mv terraform /usr/local/bin/
</pre>

Then I checked the version number, just to make sure I can run the program:

<pre>
$ terraform --version
Terraform v0.11.8
</pre>

## Prepare the Terraform configuration file

I've created a new directory called `do` (as in Digital Ocean) and in there a file called `do.tf`.
As far as I can see the name of the file does not matter. I added the following content:

{% include file="examples/terraform/do/do1.tf" %}

Instead of the 3 dots, the value of the token was the [Digital Ocean API token](/digital-ocean-api) I've generated.

The "name" will be the name of the instance. It can be anything.
The possible values for "image", "region", and "size" can be fetched via the [Digital Ocean API](/digital-ocean-api) using `curl`.

Once we have the file we need to initialize Terraform. It will download the plugin needed for Digital Ocean and
print some explanation:

```
$ terraform init

Initializing provider plugins...
- Checking for available provider plugins on https://releases.hashicorp.com...
- Downloading plugin for provider "digitalocean" (0.1.3)...

The following providers do not have any version constraints in configuration,
so the latest version was installed.

To prevent automatic upgrades to new major versions that may contain breaking
changes, it is recommended to add version = "..." constraints to the
corresponding provider blocks in configuration, with the constraint strings
suggested below.

* provider.digitalocean: version = "~> 0.1"

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

We can then go ahead an "apply" our configuration.

If you run the following, it will show the configuration information and then wait for your approval.

<pre>
$ terraform apply
</pre>

If you run this, it will just go ahead to do the work.

<pre>
$ terraform apply -auto-approve
</pre>

It will take some 30-40 seconds to create the Digital Ocean instance.
At the end Digital Ocean will send us an e-mail with a one-time password to log in to our new
Droplet as user "root".

We can also see our new [Droplet listed](https://cloud.digitalocean.com/droplets).

Terraform will also create a file called `terraform.tfstate` that will store the state of
the configuration it created.

## Remove the Droplet

After using the droplet you might want to destroy it. You can do it by using the following command:

<pre>
$ terraform destroy
</pre>

or this, if you don't want to review the changes before you approve them.

<pre>
$ terraform destroy -auto-approve
</pre>

## Create Digital Ocean Droplet with SSH key

Getting the password of the new instance in an e-mail is both inconvenient and a bit unsecure.

You can [create a pair of ssh keys](/generate-and-deploy-ssh-private-public-keypair)
if you don't have them yet, and you can upload them to Digital Ocean in the [Security tab](https://cloud.digitalocean.com/account/security). Each ssh key has an internal ID in Digital Ocean that you can only fetch via the
[Digital Ocean API](/digital-ocean-api). (Mine is a 5 digit number, nowedays I see people get 8-digit numbers.)
You can add that ID to the configuration file (actually you can add a list of IDs). The corresponding public keys will be added to the "

{% include file="examples/terraform/do/do2.tf" %}

Create the Droplet:

<pre>
$ terraform apply -auto-approve
</pre>

Take the IP address from the [list of Droplets](https://cloud.digitalocean.com/droplets/)

<pre>
ssh root@IP
</pre>

or use the following flags to avoid the questions of ssh:

<pre>
ssh -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=n  root@IP
</pre>

## Get the IP of the newly created Droplet

Getting the IP from the web interface still prohibits automation, so we need to make another little change to the Terraform configuration file. We declare an output attribute that will contain the IPv4 address of the new instance.

{% include file="examples/terraform/do/do3.tf" %}

If the Droplet already exists when you add these lines you will need to run

<pre>
$  terraform refresh
</pre>

That will already print the IP address, but you can also run

<pre>
terraform output ip
</pre>

That will only include the IP address. Much better to use in some automated script.

If you create a new Droplet with this configuration file then the IP will be included in the default output.


