---
title: "gcloud - the command line tool for Google Cloud Platform"
timestamp: 2018-08-31T08:00:01
tags:
  - gcloud
  - compute
  - config
  - gsutil
published: true
author: szabgab
archive: true
---


[gcloud](https://cloud.google.com/sdk/gcloud/) is a command-line tool to access the services and the configurations of provided by the [console](https://console.cloud.google.com/) of GCP.


## Connect to Google instance

```
gcloud compute ssh NAME
```

List all the instances:

```
gcloud compute instances list
```

Make sure the zone configured in your configuration is the same where the instance can be found or the command will not find the instance by name.

See more about [connecting to instances](https://cloud.google.com/compute/docs/instances/connecting-to-instance).

## Access instance using ssh

In the [SSH Keys](https://console.cloud.google.com/compute/metadata/sshKeys)
of the [Metadata](https://console.cloud.google.com/compute/metadata) of your "Project"
add the public key of your ssh keypair with your username as "username".

After that every <b>new</b> instance will have this public key installed and so you can use plain old ssh (or Putty if you are using MS Windows) to connect to the machine.

If you are ready to take the risk you can also use the following flags to connect without saving the key of the server in the known_hosts file of your local computer.

```
ssh -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no  EXTERNAL_IP
```

## Projects

Projects are the biggest units of organization inside GCP. They allow you to configure access control to your engineers.

This is a collection of a few useful commands.

## Projects and Compute Instances

List all the Compute Instances (virtual machines) in the currently configured project and
return the results as JSON.

```
gcloud compute instances list --format='json'
```

List all the Compute Instances in the project supplied on the command line. For this you don't need to configure each project, you just need to be logged in and you need to have access rights to the specific project.

```
gcloud compute instances list --project PROJECT --format=json
```

<h3>Stop instance</h3>

It will stop the instance (move to TERMINATED state) but won't delete it.

```
gcloud compute instances stop --project PROJECT --zone ZONE NAME --format json
```

<h3>Start instance</h3>

It will start the instance (move to RUNNING state).

```
gcloud compute instances start --project PROJECT --zone ZONE NAME --format json
```

## Get Information about an instance

```
gcloud compute instances describe NAME --zone ZONE --project PROJECT
gcloud compute instances describe NAME --zone ZONE --project PROJECT --format json
```

## List all the values of a label

Each compute instance can have labels on it that can help understanding why do we have a machine and it can be used in billing to see what do spend our money on - by category.

Just to have a look we fetch all the labels called "role" together with the name of each instance from the given project.

```
gcloud compute instances list --format='csv(labels.role,name)' --project development-42
```

In this example we would like to know what values does the label "role" have in the project called "development-42". First we list the values from all the instances in CSV format. This will contain the list but it will also contain the name of the field ("role" in our case) as the first line of the result. So we filter it out using the `tail` command. Then we `sort` the values and run through `uniq`. That gives us each name once.

```
gcloud compute instances list --format='csv(labels.role)' --project development-42 | tail +2 | sort | uniq
```

## List all the local configurations

Instead of supplying all the values on the command line for every command (e.g. name of the project, zone, etc.) we can have local configurations with with defaults. Each configuration has a name and a bunch of key-value pairs.

The command

```
gcloud init
```

can be used to create new configurations or to change existing ones.

BTW the configuration files are stored in `~/.config/gcloud/configurations/`

```
gcloud config configurations list --format json
```

You can switch between local configurations using:

```
gcloud config configurations activate
```


```
gsutil ls
```

## Labels

List all the instances with stop_at label:

```
gcloud compute instances list --filter="labels.stop_at:*" --format='csv(labels.stop_at,name)' --project NAME-OF-PROJECT
```

All the instances with stop_at label with value 'never':

```
gcloud compute instances list --filter="labels.stop_at:never" --format='csv(labels.stop_at,name)' --project NAME-OF-PROJECT
```

List all the instances without a stop_at label:

```
gcloud compute instances list --filter="NOT labels.stop_at:*" --format='csv(name)' --project NAME-OF-PROJECT
```

List all the instances without a stop_at label (without CSV header row):

```
gcloud compute instances list --filter="NOT labels.stop_at:*" --format='csv[no-heading](name)' --project NAME-OF-PROJECT
```

## Set default value in case of missing label

{% include file="examples/perl/gcloud_set_default_label.pl" %}

{% include file="examples/python/list_gcloud_buckets.py" %}


## Images

List all the available images

```
gcloud compute images list
```


List all the images created by the user (non-standard images) and format the output as JSON.

```
gcloud compute images list --no-standard-images --format=json
```

List the names of all the non-standard images.

```
gcloud compute images list --no-standard-images --format='csv[no-heading](name)'
```


## Create an instance using a public image

Creating an instance called "demo".

```
gcloud compute instances create demo --image-project ubuntu-os-cloud --image-family ubuntu-1804-lts
```

## Create an instance using a private image

```
gcloud compute instances create demo --image-project NAME-OF-YOUR-PROJECT --image-family ubuntu-1804-lts
```

## Delete an instance

```
gcloud compute instances delete demo --project NAME-OF-YOUR-PROJECT  --zone us-central1-c --quiet
```

Without the `--quiet` flag it will ask for confirmation.

## Getting started with IAM and service accounts

Install `gcloud` but do not configure it and especially do not authenticate.

```
gcloud config configurations list

NAME     IS_ACTIVE  ACCOUNT  PROJECT  DEFAULT_ZONE  DEFAULT_REGION
default  True
```

Visit [IAM &amp; admin / Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts/create).
Click on Create service account. Type in a name (e.g. demo-account)

Select a Role (Compute Viewer) and click on Continue.

click on "Create a key" , select JSON and click on Create.
It will offer you to download a JSON file.


Make sure you keep this file safe. Both because you won't be able to re-create it (you'll need to create a new key if
you lose this) but also because whoever has this file will automatically have access to your Gcloud account with all the
rights you'll assign to this service account.

```
gcloud auth activate-service-account --key-file=google.json
```

```
export GOOGLE_APPLICATION_CREDENTIALS=/home/foobar/google.json
```


[Google Cloud shutdown script](/gcloud-shutdown-script) triggered by manual or automatic shutdown (of
preemptible instances.)


