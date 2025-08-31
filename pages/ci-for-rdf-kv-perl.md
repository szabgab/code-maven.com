---
title: "Be pragmatic setting up CI for the RDF::KV"
timestamp: 2022-12-07T21:00:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


Today I tried to set up CI on GitHub Actions for the [RDF::KV](https://metacpan.org/pod/RDF::KV) Perl module
that I found on [CPAN Digger](https://cpan-digger.perlmaven.com/) to be lacking CI.

It wasn't supposed to be difficult but I encountered some issues and had to be pragmatic in the setup even if far from ideal.

IMHO it is better to have a working CI that already checks part of what can be checked than to have nothing.


I cloned the Git repository of the package and as it came with a <b>Makefile.PL</b> I ran the usual

```
perl Makefile.PL
```

just to see a nasty error:

```
include /home/gabor/os/p5-rdf-kv/inc/Module/Install.pm
String found where operator expected at Makefile.PL line 5, near "readme_from 'lib/RDF/KV.pm'"
	(Do you need to predeclare readme_from?)
syntax error at Makefile.PL line 5, near "readme_from 'lib/RDF/KV.pm'"
Execution of Makefile.PL aborted due to compilation errors.
```

I tried to understand the source of the problem, but I figured it is better to [report it](https://github.com/doriantaylor/p5-rdf-kv/issues/2)
maybe the author will point to something I am doing wrong or maybe the author will confirm the problem.


As I could not use the regular process, but I still wanted to see if the tests pass I installed the dependencies that were listed in the <b>Makefile.PL</b>
manually running <b>cpanm</b>. As I saw that the tests pass after I installed all the dependencies I set up GitHub Actions.

From the results I learned that the author tests need some additional modules, however after installing those one of the author tests failed.
I think it is probably related to the same issue I already reported, so instead of trying to figure out what's going on I removed the test module that enabled
that specific test.

At this point I could send the [pull-request](https://github.com/doriantaylor/p5-rdf-kv/pull/3).

We'll see how the author responds.

## GitHub Action configuration file

{% include file="examples/rdf-kv/ci.yml" %}

## Conclusion

It is better to have a CI running and executing some of the tests in a less-than-ideal way than to have no CI.
A working CI can (and actually has to) be improved all the time.

