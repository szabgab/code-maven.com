---
title: "CI using timescaledb a PostgreSQL based time series database"
timestamp: 2022-12-23T10:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


A couple of days ago while browsing the [Ruby Digger](https://ruby-digger.code-maven.com/) I bumped into the [timescaledb Ruby Gem](https://rubygems.org/gems/timescaledb). It had a <b>.travis.yml</b> file indicating a Travis-CI configuration, but Travis stopped providing free service to open source projects and I already found out that this file is part of the Ruby gem skeleton, so  its existence now does not mean much. Not even that it ever worked.

It took me quite a while and some back-and-forth with the author to make GitHub Actions work and even now some of the tests are failing. Here is what happened:


## Cloning

As always I started by cloning the [timescaledb](https://github.com/jonatas/timescaledb) git repository.

```
git clone git@github.com:jonatas/timescaledb.git
cd timescaledb
```

Then I forked the repository on GitHub and added my fork as another remote:

```
git remote add fork git@github.com:szabgab/timescaledb.git
```


## Using PostgreSQL as a service

At the beginning I thought the module needs a PostgreSQL database to run. As I did not have an example ready first I created an example of using [PostgreSQL as a service in docker compose](https://code-maven.com/slides/docker/docker-compose-postgresql-server).

Then I created an example [PostgreSQL as a service in GitHub Actions](https://github.com/szabgab/github-actions-postgresql/)

With that armed I could create the first version of the GitHub Action for this Ruby Gem.

There at first I had some typos. What an unnecessary waste of time!

## .env

Then, when finally I managed to get the syntax right and fixed the typos I git this error:

```
Errno::ENOENT: No such file or directory @ rb_sysopen - /__w/timescaledb/timescaledb/.env
```

Fail enough, even the README told me to create a <b>.env</b> file with content that looks like this:

```
PG_URI_TEST="postgres://<user>@localhost:5432/<dbname>"
```

So I added the following to the CI configuration file:

```
echo PG_URI_TEST="postgres://username:secret@database:5432/testdb" > .env
```

This made some progress and this time I got a different error:

```
PG::UndefinedFunction: ERROR:  function create_hypertable(unknown, unknown, chunk_time_interval => interval) does not exist
```

I did not know what to do. I thought I am not using the correct version of Ruby or PostgreSQL so I experimented with that a bit.
Added code to print out the version number of PostgreSQL:

```
echo "SELECT version()" | psql -h postgres -U username testdb
echo "SELECT CURRENT_TIME" | psql -h postgres -U username testdb
```

even added this line:

```
tsdb postgres://username:secret@postgres:5432/<dbname> --stats
```

## Timescale DB

Slowly I understood that instead of a vanilla PostgreSQL database I need to use to use [Timescale](https://www.timescale.com/) which is based on PostgreSQL. I am sure others would have come to this conclusion much faster than I did.

So I switched to use a [timescaledb Docker image](https://hub.docker.com/r/timescale/timescaledb).

This too involved several trials and errors, but I won't bore you with my small mistakes.

Instead I got this error:

```
Calling `DidYouMean::SPELL_CHECKERS.merge!(error_name => spell_checker)' has been deprecated. Please call `DidYouMean.correct_error(error_name, spell_checker)' instead.
rake aborted!
Gemika::UnsupportedRuby: No gemfiles were compatible with Ruby 3.1.3
```

OK, so apparently it does not work with the latest version of Ruby.

then I got this error

```
Gemika::UnsupportedRuby: No gemfiles were compatible with Ruby 2.7.7
```

Finally I settled with Ruby 2.7.1.

By this time a lot of tests seemed to have passed, but I got the following error:

```
PG::InvalidSchemaName: ERROR: schema "toolkit_experimental" does not exist
```

This was the time when I decided to open an [issue](https://github.com/jonatas/timescaledb/issues/36).

## TimescaleDB-HA

The author quickly replied and suggested I use the [timescaledb-ha Docker image](https://hub.docker.com/r/timescale/timescaledb-ha).

I tried and failed and then tried another tag and after a while the tests started to fail at a new location. I even added several different tags so we will be able to see if any of those work, but no.

However it seems we are left with only two tests failing. So I pasted the failure reports to the [open issue](https://github.com/jonatas/timescaledb/issues/36).

At this point the author suggested I send the PR and he'll try to deal with these failures. So I sent the [pull-request](https://github.com/jonatas/timescaledb/pull/37).

## GitHub Actions

{% include file="examples/ruby/timescaledb/ci.yml" %}

## Conclusion

Wow, this was really tiring even to describe what happened and I left out a lot of the smaller steps as those were primarily my mistakes and lack of reading the README of the project. However at the end I think I managed to put together something that will be useful for the developers and hopefully will also help others to set up CI for other libraries.



