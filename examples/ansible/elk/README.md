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

Follow the instructions at https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/
and create username/password pairs.

$ htpasswd -c .htpasswd user1     (pw: secret1)
$ htpasswd .htpasswd user2        (pw: secret2)


After intallation it takes some time till Kibana gets ready to be used.

We might need to execute the following command to make it start working.

setsebool httpd_can_network_connect on -P
