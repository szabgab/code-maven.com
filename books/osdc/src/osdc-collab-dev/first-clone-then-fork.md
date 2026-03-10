# First clone then fork

If you'd like to contribute to a project you'll have to have a fork (a copy of the repository in your GitHub account) and you will also need a copy of the repository locally where you can run the code. You get this by using the `git clone` command.

There are two ways to do this. In my approach I first `clone` from the "official" repository of the project and only when I know I have something to contribute, only then I create the fork.

I have two reasons for this approach:

1. I was experimenting with many projects and I was not sure if I will be able to contribute anything. So I felt there is not point in creating a fork before I need it.
1. This way the original (or "official") repo is called `origin` and my fork is called `fork` locally. It makes more sense to me.

So my process is

1. `git clone` from the "official" repository.
1. Make some changes locally.
1. When satifised create a branch locally.
1. Commit the changes to the branch.
1. Visit GitHub and fork the project.
1. Push out the branch to the fork.
1. Send a Pull-Request.
