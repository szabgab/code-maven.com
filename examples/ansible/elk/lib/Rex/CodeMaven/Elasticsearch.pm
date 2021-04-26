package Rex::CodeMaven::Elasticsearch;
use strict;
use warnings;

use Rex -base;

desc 'Base Setup';
task base_setup => sub {
    update_package_db;
    pkg 'wget', ensure => 'present';
};


desc 'Setup Elasticsearch';
task setup => sub {
    needs 'base_setup';

    my $elastic = 'elasticsearch-7.11.2-x86_64.rpm';
    my $project_root = '/root';
    my $url = "https://artifacts.elastic.co/downloads/elasticsearch/$elastic";
    my $dest = "$project_root/$elastic";
    file $project_root, ensure => 'directory';
    run("wget $url -O $dest", unless => "test -e $dest");
    run("rpm -vi $dest", unless => "rpm -q elasticsearch");

    needs 'config';
    service 'elasticsearch', ensure => 'started';
};

desc 'Config Elasticsearch';
task config => sub {
    file '/etc/elasticsearch/elasticsearch.yml',
        source => 'files/etc/elasticsearch/elasticsearch.yml',
        on_change => sub {
            service 'elasticsearch' => 'restart';
        };
};

task verify => sub {
    say run("curl http://localhost:9200");
};


1;

