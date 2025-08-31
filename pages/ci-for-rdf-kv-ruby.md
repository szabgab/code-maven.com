---
title: "GitHub Actions CI for the rdf-kv Ruby Gem"
timestamp: 2022-12-10T07:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


Finally I managed to set up CI for a Ruby Gem.
ere [were some errors](https://github.com/doriantaylor/p5-rdf-kv/issues/2) that stopped me from doing the regular steps.


A few days ago I sent a pull-request with a CI configuration to the [RDF::KV module in Perl](https://code-maven.com/ci-for-rdf-kv-perl).
I was not very happy with the solution, but sent the [pull-request](https://github.com/doriantaylor/p5-rdf-kv/pull/3) anyway.
The author of the module was very responsive and soon pointed me to the step I missed, but also pointed at the [Ruby port of rdf-kv](https://github.com/doriantaylor/rb-rdf-kv).

Today finally I had the time to update the CI I wrote for the Perl version. (See the [PR](https://github.com/doriantaylor/p5-rdf-kv/pull/3)) and also to add
the GitHub Actions configuration to the Ruby implementation and send the [pull-request](https://github.com/doriantaylor/rb-rdf-kv/pull/1)

{% include file="examples/rdf-kv-ruby/ci.yml" %}


## Conclusion

Maybe the earlier failures to set up CI for Ruby Gems wasn't even my fault. Maybe they really had failing tests.
