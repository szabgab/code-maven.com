---
title: "Setting up ELK using Rexify"
timestamp: 2021-04-26T11:40:01
tags:
  - Rex
types:
  - screencast
published: true
archive: true
show_related: true
---


During this meeting [Ferenc Erki](https://www.linkedin.com/in/ferki/), the lead developer of [Rex](https://www.rexify.org/)
is going to lead us setting up a system using several different Linux distributions and handling the differences.

We will also attempt to set up a full [ELK stack](https://www.elastic.co/).

We will start where we left of las time when FErki gave us an [introduction to Rex](/automation-with-rex)


<!--
It is scheduled for April 25: 14:00 Israel

<a class="btn btn-lg btn-success" href="https://us02web.zoom.us/meeting/register/tZUtf-usrjMoGtf5wZLaHykTidIuMUl71htT">Register here</a>

For the time in your timezone check out the registration form or visit the page of [all the live events](/live)
-->

## Plan

## ELK

Most of this will be probably delayed to a future meeting:

* Download the rpm file of ElasticSearch and install on a CentOS based box.
* Configure the /etc/elasticsearch/elasticsearch.yml file
* Make sure we can access it locally with curl
* Install Kibana on another machine
* Configure ElastiSearch and Kibana so Kibana can access ElasticSearch
* Configure Nginx on the Kibana machine as a reverse proxy and add Basic Authentication.
* Install Metricbeat on all the machines and make them send the data to the ElasticSearch
* Add different tags to the instances.
* Install our log generator application on one of the boxes.
* Install Logstash on one of the boxes
* Install Filebeat on the box with the log generator application
* Configure filebeat to process the logfile and send it to the Logstash
* Configure Logstash to accept the data from filebeat and send it to ElasTicsearch

{% youtube id="k3uz7-7E3Ws" file="rex-4_1920x1080.mp4" %}

* [ELK with Ansible](/ansible-elk)
* [Rex::Group::Lookup::YAML](https://metacpan.org/pod/Rex::Group::Lookup::YAML) for inventory

{% include file="examples/ansible/elk/Rexfile" %}

{% include file="examples/ansible/elk/rex_inventory.yml" %}

{% include file="examples/ansible/elk/lib/Rex/CodeMaven/Elasticsearch.pm" %}

{% include file="examples/ansible/elk/lib/Rex/CodeMaven/Nginx.pm" %}


```
rex -u root -d -g demo CodeMaven:Elasticsearch:setup
rex -u root -d -g demo CodeMaven:Elasticsearch:config
rex -u root -d -g demo CodeMaven:Elasticsearch:verify
rex -u root -d -g demo CodeMaven:Nginx:setup
rex -u root -d -g demo CodeMaven:Nginx:configure
```


