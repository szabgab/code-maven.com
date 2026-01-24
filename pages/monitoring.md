---
title: "Server Monitoring"
timestamp: 2017-08-31T09:30:01
tags:
  - monitoring
published: true
author: szabgab
archive: true
---


Some notes as I am working on setting up monitoring of some servers.


[Pingdom](https://www.pingdom.com/) - External active monitoring of availability of various services (ping, http, etc.) including transactions.

[Pager Duty](https://www.pagerduty.com/)

[New Relic](https://newrelic.com/)

[Terraform](https://www.terraform.io/)

## The world of StatsD

StatsD is a combination of a number of services and protocols.
* StatsD client (talking in UDP to the dameon)
* StatsD dameon (talking in batches with the data aggregator)
* Data aggregator (some kind of a database)
* Graphing service (used the data in the aggregator)

Data points can be supplied by our application. These use the StatsD client library available in most of the programming languages.
They can also be supplied by tools related to our application. (e.g. the tools used to deploy a new version.)
There can be also some generic data collector that collects generic server-related data. (e.g. CPU load, memory usage, disk usage).

The data points are sent by the StatsD clients to the StatsD daemon that usually runs on the same machine via UDP.
That means the data collection has minimal impact on our service and even if the daemon is down, it does not impact our
service. Just the logging data is lost.

There are several [StatsD daemon](https://github.com/etsy/statsd/wiki) implementations. Apparently the one by Etsy is the most popular.

There are several Data aggregators and Graphings tools ([StatsD Backends](https://github.com/etsy/statsd/wiki/Backends))

[Graphite](https://graphiteapp.org/) is an Open Source backend.
  [Build your own monitoring dashboard with Graphite, Statsd, & Grafana](https://www.youtube.com/watch?v=V6Rxs9LeKew)
  [How To Install and Use Graphite on an Ubuntu 14.04 Server](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-graphite-on-an-ubuntu-14-04-server)

[Ganglia](http://ganglia.sourceforge.net/)

[DataDog](https://www.datadoghq.com/) is an integrated service providing both data aggregation, graphs and integration with lots of other tools and services.

Plain database backends (MySQL, InfluxDB, MongoDB) ?

<h3>Metric types used in StatsD</h3>
* count   (incr, decr) (e.g. every request)
* amount (e.g. elapsed time)

## Other tools

* [Collectd](https://collectd.org/) to collect statistics and save in RDDTool or send to a StatsD data collector. (without the need for a StatsD daemon)
* [RRDTool](http://oss.oetiker.ch/rrdtool/)
* [Grafana](https://grafana.com/)    to display graphs
* [Munin](http://munin-monitoring.org/) - [Practical resource monitoring with Munin](http://www.slideshare.net/zembutsu/practical-resource-monitoring-with-munin-english-editon)
* [Cacti](http://www.cacti.net/)
* [MRTG](https://www.mrtg.com/)
* [Zabbix](http://www.zabbix.com/)
* [Nagios](https://www.nagios.org/)
* [collecting data with Carbon daemon](http://graphite.readthedocs.io/en/latest/carbon-daemons.html)

