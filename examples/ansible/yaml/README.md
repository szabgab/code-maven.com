Create Droplet on Digital Ocean with SSH key
Add IP address to inventory

```
ansible NAME -m ping
ansible-playbook playbook/ping.yml
```


Change /etc/elasticsearch/elasticsearch.yml
to listen on 0.0.0.0
later we might want other configuration, e.g. to listen to the machines on the virtual network

Actually now I'd like to install Kibana - for now on the same machine and access that Kibana

Setup Nginx with simple authentication
