---
title: "CI for Plack-Middleware-LogAny"
timestamp: 2022-12-19T22:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


Today I spent about 3-4 hours on various other projects. Managed to make good progress on some really interesting ones, but could not finish the CI for either one of them. I opened GitHub Issues reporting the problems, but I still could not get either of them done.

Finally I found this Perl module called [Plack-Middleware-LogAny](https://metacpan.org/dist/Plack-Middleware-LogAny).


I copied the CI file from [Plack-Middleware-Greylist](https://metacpan.org/dist/Plack-Middleware-Greylist) that I created on [day 9](https://code-maven.com/ci-for-two-perl-projects).

The only difference is that this one passes on Windows as well.

I sent the [Pull-request](https://github.com/XSven/Plack-Middleware-LogAny/pull/1)

## Conclusion

It's better to start earlier working my CI.


