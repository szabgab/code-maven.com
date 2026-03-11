# Improve test coverage

1. Pick an arbitray project.
    * I'll use the [factpages-py](https://pypi.org/project/factpages-py/) as an example.
1. Find its VCS (PyPI refers to it as the Repository).
    If the project does not indicate its repository then you might need to find it yourself. Refer to the [Link to VCS](./link-to-vcs.md) task.
1. Clone it locally.
    * In the case of the factpages project this was `git clone git@github.com:kkollsga/factpages-py.git`
    * Then cd to the folder `cd factpages-py`
1. Setup the local development evrionment.
    * I use a Docker image for this that already has a bunch of tools installed and it also provides more protection against malicious code in random code downloaded from the Internet.
    * This is the command I run `docker run -it --rm --workdir /opt -v$(pwd):/opt --user ubuntu szabgab/python:latest bash`
    * Seup virtual environment: `virtualenv venv`
    * Enable virtual environment: `source venv/bin/activate`
    * Install pytest: `pip install pytest`
1. Run the tests
    * `pytest`
1. Run the tests generating test coverage.
    * Install the necessary tool: `pip install pytest-cov`
    * Run the tests `pytest --cov=factpages_py --cov-report html --cov-report term --cov-branch` (instead of factpages_py use the name of the module you are testing)
    * This will print a report to the screen and it will also generate an html report in the `htmlcov` folder.
    * On your host computer open the `htmlcov/index.html` file with your browser.
1. Are there areas that are not executed during the tests?
    * Are they even in use?
    * If you think there is a function that is not in use, open an issue and suggest the author to remove that function.
1. If the area that has no test coverage is actuall in use then find a way to use the project that will execute that part of the code.
    * Write a new test doing that.
    * Tests are sually in files called `test_*`.
1. Create a branch.
    * `git checkout -b add-test`
1. Commit the changes.
    * `git add .` make sure you only add the files that you wanted to add!
    * `git commit -m "add tests"` You might provide a more detailed explanation.
1. Create a fork.
    * On GitHub visit the project and click on the "fork" button.
1. Map the forked repository.
    `git remote add fork git@github.com:szabgab/factpages-py.git`
1. Push out the branch to your fork.
    `git push --set-upstream fork add-test`
1. Send a Pull-Request.
    * Visit GitHub and click on the "Send PR button"

