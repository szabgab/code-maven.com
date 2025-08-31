---
title: "Install the ELK stack on CentOS using Ansible"
timestamp: 2021-04-10T16:30:01
tags:
  - ELK
  - ElasticSearch
  - Kibana
  - Logstash
  - Filebeat
  - Metricbeat
  - Ansible
published: true
books:
  - ansible
author: szabgab
archive: true
show_related: true
---


## Create server, configure inventory

Create [Droplet on Digital Ocean](/digitalocean) using CentOS 8.3 x64 with 4GB memory and 2 vCPUs configuring an SSH key to make easy access to it.

We can probably use other version of CentOS as well, but this is what I tried it with.

From the Digital Ocean web site copy the IP address of the drolet and add it to the inventory file replacing the IP address you find there:

{% include file="examples/ansible/elk/inventory.yml" %}


## Verify that we have access to the server using Ansible Ping

```
ansible NAME -m ping
```

First it will want to verify the fingerprint of the server:

```
The authenticity of host '134.122.123.157 (134.122.123.157)' can't be established.
ECDSA key fingerprint is SHA256:L1jIJx45fOP3lFH/qQysD7tAdY9/rNoeC+eA2mO4ijY.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Type in "yes" and press enter.

Then the response is expected to look like this:

```
134.122.123.157 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
    "changed": false,
    "ping": "pong"
}
```

Try the same with our first playbook:

```
ansible-playbook playbooks/ping.yml
```

The response is expected to be:

```
PLAY [all] ****************************************************************************************

TASK [Gathering Facts] ****************************************************************************
ok: [104.236.61.19]

TASK [Ping] ***************************************************************************************
ok: [104.236.61.19]

PLAY RECAP ****************************************************************************************
104.236.61.19     : ok=2  changed=0  unreachable=0  failed=0  skipped=0  rescued=0  ignored=0
```

{% include file="examples/ansible/elk/playbooks/ping.yml" %}

See [Ping module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html)

## Fetch the hostname of the server

OK, so this is not necessary to our task, but I like to see it working.

{% include file="examples/ansible/elk/playbooks/hostname.yml" %}

```
ansible-playbook playbooks/hostname.yml
```

Output:

```
PLAY [all] ***************************************************************************************

TASK [Gathering Facts] ***************************************************************************
ok: [104.236.61.19]

TASK [Bash] **************************************************************************************
changed: [104.236.61.19]

TASK [debug] *************************************************************************************
ok: [104.236.61.19] => {
    "msg": "elk1"
}

PLAY RECAP ***************************************************************************************
104.236.61.19    : ok=3  changed=1  unreachable=0  failed=0  skipped=0  rescued=0  ignored=0
```

See [Ansible shell module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/shell_module.html).

## Install Elasticsearch

The version of ElasticSearch is baked into the playbook file. You can visit the
[download page of Elasticsearch](https://www.elastic.co/downloads/elasticsearch) to pick a different version.

{% include file="examples/ansible/elk/playbooks/elasticsearch.yml" %}

```
ansible-playbook playbooks/elasticsearch.yml
```

{% include file="examples/ansible/elk/files/etc/elasticsearch/elasticsearch.yml" %}


## Setup Nginx with simple authentication


Follow the instructions on how to [configure http basic authentication for Nginx](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/)
create one or more username/password pairs:

```
$ htpasswd -c .htpasswd user1     (pw: secret1)
$ htpasswd .htpasswd user2        (pw: secret2)
```

{% include file="examples/ansible/elk/files/etc/nginx/nginx.conf" %}

{% include file="examples/ansible/elk/files/etc/nginx/conf.d/nginx-elk.conf" %}

Then run the playbook:

```
ansible-playbook playbooks/nginx.yml
```


{% include file="examples/ansible/elk/playbooks/nginx.yml" %}

Visit http://IP:81 after replacing IP with the IP address of your host to get access to Elasticsearch


## Kibana

{% include file="examples/ansible/elk/playbooks/kibana.yml" %}

## Metricbeat

{% include file="examples/ansible/elk/playbooks/metricbeat.yml" %}

## ELK

{% include file="examples/ansible/elk/playbooks/elk.yml" %}

## Ansible Configuration file

{% include file="examples/ansible/elk/ansible.cfg" %}

