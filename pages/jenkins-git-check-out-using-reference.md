---
title: "Jenkins Pipeline: git checkout using reference to speed up cloning large repositories"
timestamp: 2019-04-05T08:30:01
tags:
  - Jenkins
  - git
  - checkout
  - GitSCM
published: true
books:
  - jenkins
author: szabgab
archive: true
---


At one client we have a git repository that is almost 2 Gb large. (Don't ask why, it is a long story.)
Among many other things one problem this causes is that in our CI environment (using Jenkins) every build takes
ages. (Cloning this repo takes between 5-30 minutes depending on the weather and the alignment of the stars.

If we have fixed Jenkins agents it would be fast, because Jenkins would maintain a clone of the repository and
would only need to update the repository with the most recent changes.

However in our situation we used on-demand started Google Compute Instances.


That meant every time ws started a new GCP instance it had to clone the whole repository. Wasting time, bandwidth,
and money.

To improve the situation our solution was the following.

We created an image in GCP and included a full clone of the repository in <b>/opt/code-maven</b>.
Then we used the <b>reference</b> option of git to provide a local reference clone of the repository.

Then, when we wanted to clone the repository we had code like this:

{% include file="examples/jenkins/clone_using_reference.jenkinsfile" %}

This function can get a <b>sha1</b> or a name of a <b>branch</b> to check out.

Internally it has two variables <b>reponame</b> is the short name of the repository.
<b>repo_url</b> is the URL to the original repository. In this case it was in bitbucket.

There is also the name <b>jenkins-git-credentials</b> which is the name of the credentials
we added to Jenkins to be able to access the git repository in Bitbucket. If your git server
needs authentication, you'll need this configured manually in Jenkins.


Every now and then we had to update the image with the recent changes in the repository so the gap
between what we already have in the image and what we have in the reomte repository won't grow
too much, but we had to keep the image up to data anyway so this is not extra work.


