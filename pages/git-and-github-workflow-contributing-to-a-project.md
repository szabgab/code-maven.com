---
title: "Git and GitHub workflow contributing to a project"
timestamp: 2016-04-01T07:30:01
tags:
  - Git
  - GitHub
published: false
author: szabgab
archive: true
---


We'll see how to contribute to the a project hosted on GitHub.


## Customize the article

In this exemple we assume our GitHub user name is "cm-demo" and the project we would like to contribute is this repository:
[https://github.com/szabgab/codeandtalk.com](https://github.com/szabgab/codeandtalk.com).

<!--
but if you'd like we can customize the text for you to show the values relevant to you:

<table>
  <tr><td>Project you'd like to contribute to:</td><td><input id="github_project" value="https://github.com/szabgab/codeandtalk.com"></td></tr>
  <tr><td>Your username:</td><td><input id="github_username" value="cm-demo"></td></tr>
</table>
-->

## Preparations

<ol>
  <li>Register on [GitHub](https://github.com/). The user for our example is called <b>cm-demo</b></li>
  <li>Install Git command line client.</li>
  <li>Configure the client setting your name and e-mail.</li>
</ol>


## Clean your GitHub user

In the tutorial we assume you don't have a fork of the repository yet, so if you've already played with this
repository, let's have a clean start. If you have a fork of the repo on GitHub,
that is if you have this: [https://github.com/cm-demo/codeandtalk.com](https://github.com/cm-demo/codeandtalk.com)
(When checking, replace <b>cm-demo</b> with your username, and <b>codeandtak.com</b> with the project you are planning to contribute to), then remove it.
(Click on the <b>Settings</b> and inside click on <b>Delete this repository</b>.)

Also if you have a copy of the project on your own computer, remove that too.

## Forking

The first step is to <q>fork</q> the project on GitHub. That is to create a copy of the project in your account on GitHub.
Visit the URL of the project: [https://github.com/szabgab/codeandtalk.com](https://github.com/szabgab/codeandtalk.com)
click on <b>Fork</b> in thetop-right corner. It will create your copy as [https://github.com/cm-demo/codeandtalk.com](https://github.com/cm-demo/codeandtalk.com).
(Your GitHub username instead of cm-demo.)

## Clone to your computer

Then you need to clone the repository to your computer. (That will copy the repository from <b>your</b> GitHub account to your computer:

```
$ cd projects
$ git clone https://github.com/cm-demo/codeandtalk.com.git
Cloning into 'codeandtalk.com'...
...


$ cd codeandtalk.com
```

This will create a directory called codeandtalk.com inside the current directory.

## Set up upstream

In order for you to be able to follow changes in the original project you need to connect
the original repository. You do this by issuing the following command:

```
$ git remote add upstream https://github.com/szabgab/codeandtalk.com.git
```

The URL here is quite similar to the one we used for cloning the project, but the username
is not our username, but that of the project owner.

## Create a branch for your work

```
$ git checkout -b first
Switched to a new branch 'first'
```

## Make changes

Add files, make changes to files with your regular editor.

Add the changes and the new files to your local copy of the project:

```
git add file/that/changed.txt
git add new/file.txt
git commit -m "Explain your changes here"
```

This is a "commit".  You can make repeted changes and repeated commits. If the project allows you can also verify that
your changes are correct. In the case of the codeandtalk.com project run 

```
python bin/generate.py
```

If it does not give you any error messages then you are good to go.

## Push out your changes to GitHub

Once you are satisfied with your changes you can push them out (all the changes at once) using the follwing command:

```
$ git push --set-upstream origin first
```

Here, the last word is the name of your branch. So I used the word "first".

This command pushes out the whole branch (all the changes in this branch) to your copy of the project on GitHub.

## Send a pull-request

If you visit your copy (clone) of the project on Github at [https://github.com/cm-demo/codeandtalk.com](https://github.com/cm-demo/codeandtalk.com)
you will see a message with the name of your branch  ("first" in our case) and a button "Compare &amp; pull request".
Clicking on that button will show you a form in which there is some text already (usually the message you wrote for the most recent commit).

You can add more text, but that's not a requirement. Click on the button "Create pull request".

This will create a "pull request" and also send a message to the owner of the project (User szabgab in this case.)
It will also redirect you to the page of the "pull request". In our case this was it:
[https://github.com/szabgab/codeandtalk.com/pull/38](https://github.com/szabgab/codeandtalk.com/pull/38) but of
course the actually URL will depend on the project and the number of pull-requests that were sent earlier.

## Failing automatic tests

If the project is configured to have online automatic tests, then after a while those tests will run and you will see the
results on the page of "the pull request".

The <b>codeandtalk.com</b> project is configured to run these automatic tests. If the tests fail you'll see a message
"All checks have failed" and a link to see the "Details". 

<img src="/img/github_tests_failed.png" alt="GitHub tests failed" />

This probably means you've forgotten to run the tests locally, disregarded the failure there, or have committed
andpushed out only part of your changes.

At this point you need to go back to your files, make the necessary changes in the files. Add those changes to
your local git. Exactly as described above in the <b>Make changes</b> section.

Then you can proceed to push out these changes as well but this time it is enough to type

```
git push
```

as git already knows where to push this branch.
This will update the pull-request on GitHub and re-run the automatic tests.


## Succesful automatic test

If the page of the pull-request shows "All checks have passed"> then it means everything was fine.

<img src="/img/github_tests_passed.png" alt="GitHub tests passed" />

At this point you could go on working one more changes, but for simplicity we'll wait till the owner of the project
integrates (merges) your changes.

<img src="/img/github_merged.png" alt="GitHub merged" />

## Update your local copy from the project

```
$ git checkout main
$ git pull upstream main
```


Start new branch:

```
$ git checkout -b second
```

... and repeate the whole thing above starting from the branching.



## Clean up local branches

This is not required, but after a branch you worked on, that you sent the pull-request for,
has been merged you can delete the local copy of the branch using:

```
git branch -D first
```


