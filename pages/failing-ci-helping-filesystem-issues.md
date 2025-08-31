---
title: "Failing CI to help fixing filesystem issues in a Python package"
timestamp: 2022-12-15T07:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


A few days ago, while I was looking for a Python package to set up with CI, I bumped into the [vfxpaths](https://github.com/VFXToolkits/vfxpaths).
I tried to run the tests on my Ubuntu-based Docker container, but they failed due to some [path-issues I reported](https://github.com/VFXToolkits/vfxpaths/issues/4).

Yesterday the author updated the issue saying that it has been fixed so today I tried it again.


It failed again, but this time on a test-file that was added a few hours ago. I updated the issue, but now that I see the author is actually interested
fixing this issue, I though it might be more useful if I configured GitHub Action on the 3 platforms.
Once [this pull-request](https://github.com/VFXToolkits/vfxpaths/pull/6) is accepted on every push the tests will run on
Linux, Windows, and macOS so the author will get almost immediate feedback if the path issue was solved and later if that
or anything else breaks again it will be much faster to notice and therefor much easier to fix.

## GitHub Actions

{% include file="examples/python/vfxpaths/ci.yml" %}


## Conclusion

Sometimes there is clear evidence that having a CI running on every push can shorten the feedback cycle and allow people who might have
no direct access to all 3 operating system (which is about everyone) to see if their code works there and to experiment fixing
issue on other platforms as well.
