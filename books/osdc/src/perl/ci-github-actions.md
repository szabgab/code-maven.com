# CI - GitHub Actions

Most CPAN modules come with a bunch of automated tests that can verify that the projects works as expected.
These tests are usually execute during the installation of the module.

There are also the volunteers of the [CPAN Testers](https://www.cpantesters.org/) who monitor the new releases to CPAN, download the distributions, run the tests and report the results back to the central database.


Setting up a CI system will ensure that the test are run during the development, even before the release of a new version of the project.

Having such a system has the following additional benefits:

* Fast feedback loop.
* Environment controlled by the developer.
* Allow the customization of test environment (e.g. run a PostgreSQL database so the test can use it)
* It is also free of charge (up to a certain monthly usage).

1. Find a CPAN module that does not have CI yet.
    * The [CPAN Digger](https://cpan-digger.perlmaven.com/recent) has a list of recently uploaded distributions. There is a column called "CI". If it has "Add CI" then there is no CI that CPAN::Digger could identify. (If is has "Add repo" then you might need to start adding the [Link to VCS](./link-to-vcs.md).
    * Of course you can visit the METACPAN page of any distribution, follow the "Repository" link if is has one and check if it has CI configured.
1. Clone the git repository locally.
1. Create a branch.
1. Create a file called `.github/workflows.ci.yaml` based on [this article](https://perlmaven.com/setup-github-actions).
1. Commit the changes.
1. Create a fork on GitHub.
1. Locally add the remote repository.
1. Push out the branch to your fork.
1. On GitHub visit the **Actions** tab and observe if the run succeeds.
    * If not, check the log, adjust the instructions in the GitHub Workflow configuration file, push the new commit. Repeat till the CI works.
    * You might need to open issues if you encounter problems while setting up the CI.
1. Once the GitHub Workflow passes, you can send a pull-request.


