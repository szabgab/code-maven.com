---
title: "Enforcing commit message format in Git - on the client side"
timestamp: 2018-08-10T12:30:01
tags:
  - git
  - commit-msg
published: true
author: szabgab
archive: true
---


By default git allows you to include anything in a commit message. This freedom is nice, but when I need to look back on the commit history it is very useful to be able to connect commits to specific issues.

This could be done by including the issue number in every commit message. (Even if in  your setting it is called ticket number or bug number.). e.g. `#42`.

Git provides ways to enforce that you every commit has such a string in it, but this enforcement can only be done on the server. Too late if I made several commit on the client without the required part.

You can, however, ask git on your own computer to help you enforce this rule.


In your workspace on your computer the whole git database is in the `.git` subdirectory of your workspace. Inside there is a directory called `.git/hooks/` with a bunch of file with th extension "sample". These are or example scripts to have actions at various stages of your work life-cycle.

Here is what I did: I create a file called `.git/hooks/commit-msg` with the following content:

```shell
#!/bin/sh

test "" = "$(grep '^#\d* - ' "$1")" && {
   echo >&2 "******  Start the commit message with a # character followed by the task-id!"
   exit 1
}

exit 0
```

Made it executable with

```
chmod +x .git/hooks/commit-msg
```

From this point on, in this repository I'll have to make sure the commit message starts with
`#` followed by a number, followed by a ` - `. The rest is optional.

## How the commit-msg hook works:

Before a commit is recorded the commit message is saved in a temporary file and this script is executed passing the name of the file as the first parameter. If the exit code of this script is 0 (meaning success) then the commit can go on. If the exit code is any other number (meaning failure) then the commit is aborted. The above code checks if the content of the file (of which the name is located in variable `$1` contains the correct format.


## Enforce task-by-name

If you don't have a bug-tracking system, or you don't always want to require a bug number, I'd still suggest to require some kind of identification to the commits that will make it easier later to connect commits that are related to the same task.

This slight modification requires some kind of a word consisting of letters, digits, and the underscore immediately after the `#` tag.

```shell
#!/bin/sh

test "" = "$(grep '^#\w* - ' "$1")" && {
   echo >&2 "******  Start the commit message with a # character followed by the task!"
   exit 1
}

exit 0
```

So a commit message can look like:

```
#refactoring - merging 4 cases of copy-paste into a function call
```


## Select from specific names

The above still allows for typos in the identifier that is mainly a problem as it will make it much harder to list the related commits.

The next one, written in Perl, that should still be called `.git/hooks/commit-msg` has a list of acceptable task names.
It checks if the text starts with one of those.

{% include file="examples/commit-msg.pl" %}

Using this will require you to update the `.git/hooks/commit-msg` file with the current task names, but will enforce the specific names.

## Comments

Thanks for the useful article! I think there is an error in the first two examples, grep with a Regex pattern works only with -P parameter. To make it work, I needed to add it, so for example:

test "" = "$(grep -P '^#(\d+)\s' "$1")" && {

---

Thanks for this, it really solves my problem. However, is there an easy way to deploy it across my teams when they do their next pull? It looks like the .git folder is excluded from the repo.

---

No AFAIK you cannot automatically distribute this. I would also not put any such enforcement on my team. I'd educate them and let them opt for self-enforcement if they feel the need.

---

Why not? Shouldn't we require traceability be established between commits and the tickets that authorize the work?

---

Since I made that comment I learned about the https://pre-commit.com/ project that would make it easy to distribute pre-commit hooks, but unless the computers of the developers are locked down they can always find a way to avoid the pet-commit hooks. If someone so much distrust their employees then, well, I don't have much to say.

I sure think it is a good idea to have traceability, but it should not be extreme. If I want to fix a typo in a comment, do I need to open a ticket, get approval from management in order to do that?

Do I need to get authorization to change a variable name to be more descriptive?

I think that's not the right way to handle development.


---

Wouldn't this make Git consider the line to be comment (and to not include in the final commit message), because it starts with '#'?

---

If you supply the comment on the command-line then this works. If you let it open an editor then indeed the solution is problematic. There are was to tell git to not consider # as a comment. A better solution might be not to use # as the leading character in my commit messages.

---
Yes, you can change comment character to something else with `core.commentChar`.



