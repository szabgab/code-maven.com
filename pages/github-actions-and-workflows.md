---
title: "GitHub Actions and Workflows"
timestamp: 2023-03-19T11:30:01
tags:
  - Github
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


I feel a bit cheated. Maybe it is only I who misunderstood things, or maybe GitHub had a bit of a name-mess.


For each GitHub project you can set up something they call [GitHub Actions](https://docs.github.com/en/actions), even the link in every project is called "Actions".
So if you happen to visit the [source](https://github.com/szabgab/code-maven.com/) of the [Code Maven](https://code-maven.com/) web site then you'll have a link called [Actions](https://github.com/szabgab/code-maven.com/actions).

However what you see there is actually the output of the [GitHub Workflows](https://docs.github.com/en/actions/using-workflows), or as I see they put it <b>GitHub Actions workflows</b>.

Each such workflow is a combination of some code and some configuration of [GitHub Actions](https://github.com/actions/). However in this sentence the name "GitHub Actions" referred to the building blocks of the workflows.

In a nutshell <b>GitHub Actions</b> refer to two things. The workflows and the building blocks of the workflows.

Earlier, in most of my blog posts and training materials I used the name GitHub Actions to refer to the whole thing, but I'll need to reconsider this to make it easier for people to understand why the actions (workflows) are defined in a folder called workflows and why are they using building blocks that are also called "GitHub Actions" despite not being workflows.

## Workflows

A <b>GitHub Actions workflow</b> is something you define in a YAML file in the <b>.github/workflows/</b> folder of your git repository. It can be built from plain commands in Bash or basically any programming language, but it can also use a huge set of building blocks called <b>Actions</b>.


## Actions

The Actions provided by Github are all stored in the [action GitHub organization](https://github.com/actions/). Each action is a separate repository.

Everyone can create additional actions that can be private or can used by anyone. There is a whole [Marketplace of Actions](https://github.com/marketplace?category=&query=&type=actions&verification=) where you can locate more of these pre-built blocks.

As of this writing on 2023.03.19 there are 17,685 actions in the marketplace and probably there are lot more that were not published to the marketplace.

