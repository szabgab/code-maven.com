---
title: "CI for Win32-Wlan Perl module"
timestamp: 2022-12-05T01:30:01
tags:
  - GitHub
  - CI
  - Perl
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


I found [Win32-Wlan](https://metacpan.org/dist/Win32-Wlan) on [CPAN Digger](https://cpan-digger.perlmaven.com/) as a Perl
package that does not have CI configured in its [GitHub repository](https://github.com/Corion/Win32-Wlan/).


While the indicates that this is a Windows-related thing, there are a number of packages on [CPAN](https://metacpan.org/) that are in the
<a href="https://metacpan.org/search?size=50&q=Win32"><b>Win32</b></a> namespace, but also work on Linux. This one, it seems does not.
It seems at least one of its dependencies, the [Win32-API](https://metacpan.org/dist/Win32-API) does not work on anything else besides
Windows.

In the <b>Makefile.PL</b> of Win32-API I saw this code:

```
my $running_on_windows = $^O eq 'MSWin32' || $^O eq 'cygwin' || $^O eq 'msys';
die qq(OS unsupported\n)
    unless $running_on_windows
    or $ENV{WIN32_API_BUILD}     # So I can build it on Linux too
    ;
```

So it can also work on <b>cygwin</b> and <b>msys</b> and it can be packaged on <b>Linux</b> as well.

We might be able to setup a Linux machine to build the distribution of the module and then we can run the tests
on various versions of Perl on Windows. However I did not want to invest that much time before I even
see that it would be interesting to the maintainer of the package.

The setup was quite simple as you can see from the GitHub Action config file below.

I had to remove the two most recent versions of Perl as it seems they are not available in the GitHub Action I used.
That could be improved.

The [Pull-Request](https://github.com/Corion/Win32-Wlan/pull/4)

## GitHub Actions

{% include file="examples/win32-wlan/ci.yml" %}

## Conclusion

Sometimes you need Windows.


