---
title: "Enable Travis-CI for Continuous Integration"
timestamp: 2019-10-04T08:30:01
tags:
  - Travis-CI
published: true
author: szabgab
archive: true
---


[Travis-CI](https://travis-ci.org/) provides Continuous Integration for projects in GitHub repositories. For public repositories it is even free.

In other words, if Travis-CI is enabled and configured for your GitHub repository, then every time you `push` changes out to GitHub,
Travis-CI will automatically run the test on the latest commit.

This is great, as it means you can get feedback for your changes within a few minutes.


## You received a Pull Request adding .travis.yml to your repo?

If you have just received a Pull-Request adding .travis.yml to your repository, then you only need to tell Travis to
start looking for it. For this you nee to visit [https://travis-ci.org/](https://travis-ci.org/), login with
your GitHub credentials and allot Travis to access your public repositories.

It needs access because it needs to be able to add a trigger to it so Travis will be notified when there are changes in your repositories.
It also needs to be able to notify GitHub about the status of the most recent build process.

Once you have enabled that Travis will read the list of your repositories.

Visit the top-right corner of your Travis account and click on "Settings". Find the name of the specific repository for
which you'd like to enable Travis-CI and flip the toggle to "on".

That's it. If you merge the Pull-request now, Travis will notice it and will start to run the process within seconds.

From now on any time you push to your repository or any time someone sends you a Pull-Request the Travis-CI process will
run and report you any failures.

