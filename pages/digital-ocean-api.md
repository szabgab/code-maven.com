---
title: "Digital Ocean API"
timestamp: 2018-09-14T12:10:01
tags:
  - curl
  - DO
  - API
published: true
author: szabgab
archive: true
---


[Digital Ocean](/digitalocean) is a cloud provider with a nice and simple interface. I have been using it for many years for a number of servers. It also has a nice API that we can use to automate the administration of instances.


Let's see a few examples that you might need from the API.

## Generate an API token

In order to use it first you need to [sign up to Digital Ocean](/digitalocean). Without
an account there is no point using the API.

Then you need to create an [API token](https://cloud.digitalocean.com/account/api/tokens) with read-write access.

Keep this code somewhere safe as people who have access to this token can manage your instances.

In order no to copy the token in every command I've created an environment variable:

<pre>
export DO_API_TOKEN=....
</pre>

## Get the list of images

```
curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer $DO_API_TOKEN" "https://api.digitalocean.com/v2/images?type=distribution" > images.json
```

Use [jq](https://stedolan.github.io/jq/) to see the file in a readable way:

<pre>
jq . images.json  | less
</pre>

or to list the slugs only:

<pre>
jq .images[].slug images.json
</pre>

## Get the list of Droplet sizes

```
curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer $DO_TOKEN" 'https://api.digitalocean.com/v2/sizes' > sizes.json
```


## Get list of SSH keys in your account

<pre>
curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer $DO_API_TOKEN" "https://api.digitalocean.com/v2/account/keys" > ssh.json
<pre>

And then the following to print the IDs and the names respectively.

<pre>
jq .ssh_keys[].id  ssh.json
jq .ssh_keys[].name  ssh.json
</pre>

or both of them:

<pre>
jq '.ssh_keys[] | "\(.id) \(.name)"'  ssh.json
</pre>

