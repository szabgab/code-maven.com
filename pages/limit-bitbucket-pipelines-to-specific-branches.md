---
title: "Limit Bitbucket pipelines to specific branches"
timestamp: 2019-01-31T09:30:01
tags:
  - Bitbucket
  - Pipeline
  - CI
published: true
author: szabgab
archive: true
---


Bitbucket pipelines use an inclusive model, that's it, you can only say which branches you would like the pipeline to run
on, and you cannot exclude specific branches.

So you can say <b>run on "master", "dev", and "feature/*"</b>  but you cannot say <b>skip on "experiment"</b>.


All of this is controlled in the <b>bitbucket-pipelines.yml</b> file in the root of the repository.
Whenever you push out some changes to a branch, Bitbucket will look at the file in that branch.
So if you make changes to the pipeline configuration file in master, it will only affect an existing branch
if it merges the changes from master (or rebases onto master).

In the following example we configured that the "master" branch, the "dev" branch and any branch that starts with
"feature/" will execute one set of commands.

The "work" branch will execute a different set of commands.

None of the other branches will initiate a build.

{% include file="examples/bitbucket-branches/bitbucket-pipelines.yml" %}

Pay attention, there are <b>no spaces!</b> in the list of branches!

The above configuration will not run for a branch called <b>feature/a/b</b> as a single <b>*</b> only
captures a single directory level. If you'd like to have any number of directory levels, you can use
<b>**</b>. As in <b>feature/**</b>.

Check out the valid <a
href="https://confluence.atlassian.com/bitbucket/configure-bitbucket-pipelines-yml-792298910.html#Configurebitbucket-pipelines.yml-globbing_patterns">globbing
patterns</a>.

## Exclude or skip specific branches

There is a workaround for the lack of exclusive configuration.
We can configure a default action, that will work on every branch.
Then we can create a basically empty branch-configuration for every branch we want to skip.

In this example we have a <b>default</b> configuration that does the real testing.
Then there is a configuration for certain branches we only call "echo" and tell the world we are skipping this branch.

{% include file="examples/bitbucket-default/bitbucket-pipelines.yml" %}

Bitbucket will still run the pipeline for these branches, and it will report them as successes after running for a
number of seconds. Just to execute the <b>echo</b> command.


## Exclude by removing the bitbucket-pipelines.yml

Another option is to remove the bitbucket-pipelines.yml file in the branches where we don't want the pipeline to run.
This is in a way a clean solution, but it involves either two strange commits (removing the bitbucket-pipelines.yml and
adding it back), or it involves the rewriting the history.
In either case you have to remember to do that before you merge back to the main branch of your project.

```
git checkout -b some-branch
git rm bitbucket-pipelines.yml
git commit -m 'remove bitbucket-pipelines.yml to skip the pipeline in this branch'
```

Then code, commit and push as much as you like.

Then <b>revert</b> the removal of the bitbucket-pipelines.yml file:

```
git revert SHA1-of-the-removal-commit
```

This will add another commit the reverses the one where you removed the file.

From that point the pipeline is live again.

The history will look like this:

![](/img/revert-rm-commit.png)

## Remove the bitbucket-pipelines.yml file and retore it by rewriting history

The other solution involves rewriting the history.
First you remove the bitbucket-pipelines.yml as seen above and make some changes.
The history will look something like this:


![](img/git-remove-file.png)

Then, when you want the <b>bitbucket-pipelines.yml</b> file to come back you remove the commit that removed the file. (You change the history.)

First you run:

```
git rebase -i SHA1-of-the-removal^
```

It will open your default editor listing all the commit starting with the one we wanted to remove.
Something like this:


```
pick 62e820e remove bitbucket-pipelines.yml to skip the pipeline in this branch
pick e94ce98 one
pick 7d15fc5 two
```

We can mark the commit to be deleted by replacing the <b>pick</b> by <b>d</b> at the beginning of the specific row
(first row in this case) like this:

```
d 62e820e remove bitbucket-pipelines.yml to skip the pipeline in this branch
pick e94ce98 one
pick 7d15fc5 two
```


Then we save the file and close it.

The resulting histroy will look like this:

![](img/git-remove-commit-in-middle.png)


