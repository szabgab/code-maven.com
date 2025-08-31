---
title: "Add GitHub Actions to the scale_rb Ruby project"
timestamp: 2022-10-13T09:30:01
tags:
  - GitHub
types:
  - screencast
published: true
books:
  - ruby
author: szabgab
archive: true
show_related: true
---


After implementing the initial version of [Ruby Digger](https://ruby-digger.code-maven.com/)
I found the [scale_rb](https://github.com/wuminzhe/scale_rb) project that had a link to its GitHub repository,
but no Continuous Integration configured yet.

I thought this could be a good opportunity to see how is the GitHub Actions configuration file offered by GitHub itself.


{% youtube id="mMuuCHiWRMM" file="ruby-github-actions-for-scale-ruby-project.mp4" %}

I made a few changes to the default file, specifically I have removed some comments and enabled the job an all branches,
not only on the main branch of the project.

This was also important as it is usually better to work on a branch before sending a pull-request.

I committed the change to a branch I called CI.

The first run of the GitHub Actions failed for Ruby 3.0 and was cancelled for Ruby 2.6 and 2.7.
Then I added <b>fail-fast: false</b> to allow all the jobs to run till completition (or failure).

This allowed me to see that the tests pass on Ruby 2.6 and 2.7.

In the next change I've disabled Ruby 3.0 and sent the pull-request with the following file:

{% include file="examples/scale_rb_ci.yml" %}

