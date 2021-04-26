package Rex::CodeMaven::Nginx;
use strict;
use warnings;

use Rex -base;

desc 'Setup nginx';
task setup => sub {
    update_package_db;
    pkg 'nginx', ensure => 'present';
    service 'nginx', ensure => 'started';
};

desc 'Configure Nginx';
task configure => sub {
    my $reload_needed = FALSE;
    # We only checked this on CentOs
    my $nginx_root_dir ="/etc/nginx";
    file "$nginx_root_dir/nginx.conf",
        source => 'files/etc/nginx/nginx.conf',
        on_change => sub {
            $reload_needed = TRUE;
        };


    my $nginx_conf_dir = case operating_system, {
                qr{Debian|Ubuntu}i  => "$nginx_root_dir/sites-enabled",
                qr{Fedora|Centos}i  => "$nginx_root_dir/conf.d",
              };

    file "$nginx_conf_dir/default", ensure => 'absent';

    file "$nginx_conf_dir/nginx-elk.conf",
        source => 'files/etc/nginx/conf.d/nginx-elk.conf',
        on_change => sub {
            $reload_needed = TRUE;
        };

    file "/usr/share/nginx/html/.htpasswd",
        source => 'files/usr/share/nginx/html/.htpasswd',
        on_change => sub {
            $reload_needed = TRUE;
        };

    run("setsebool httpd_can_network_connect on -P");

    service 'nginx' => 'reload' if $reload_needed;
};

1;

