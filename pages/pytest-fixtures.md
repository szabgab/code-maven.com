---
title: "Python testing with Pytest: Order of test functions - fixtures"
timestamp: 2018-04-09T22:30:01
tags:
  - pytest
published: true
books:
  - python
author: szabgab
archive: true
---


After [getting started with pytest](/getting-started-with-pytest) we will
soon have a few questions. For example the order of the tests and how to factor out common code
from the test functions.


## Printing from tests

By default pytest will hide any output generated during the tests.
So if you have a `print` statement in our code, we will not
see its output during normal test run.

{% include file="examples/python/pt2/test_some.py" %}

We can use the `-s` option to tell pytest to display the output that should have gone to the
standard output (stdout) or standerd error (stderr):

```
$ pytest test_some.py  -s
===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /examples/python/pt2, inifile:
collected 1 items

test_some.py hello testing
stderr during testing
.

=================== 1 passed in 0.02 seconds ===================
```

In order to avoid mixing with the regular output of pytest one might need
to to add a newline infront of each string being printed.

## Order of test function

Pytest runs the test in the same order as they are found in the test module:

{% include file="examples/python/pt2/test_order.py" %}

We can see the actual order by including the verbose flag on the command line: `-v`

```
$ pytest test_order.py -v

===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0 -- /examples/python/pt/venv3/bin/python3.5
cachedir: .cache
Using --random-order-bucket=module
Using --random-order-seed=771694

rootdir: /examples/python/pt2, inifile:
plugins: random-order-0.5.4
collected 3 items

test_order.py::test_one PASSED
test_order.py::test_two PASSED
test_order.py::test_three PASSED

=================== 3 passed in 0.01 seconds ===================
```

## Randomizing tests

While normally you'd probably want to run simpler towards more complex test,
sometimes it is useful to run the tests in random order. That might reveal some interdependency among tests.

In order to do this we can install the [pytest-random-order](https://pypi.python.org/pypi/pytest-random-order)
plugin using `pip install pytest-random-order`

Once we install it, it is immediately enabled and if we run `pytest -v` several times we'll see the order changing.

## Default order

In order to get back to the default order we can turn off the plugin we've just installed. For that we need
to add the following code to our test file:

```
import pytest
pytestmark = pytest.mark.random_order(disabled=True)
```

{% include file="examples/python/pt2/test_default_order.py" %}


## Fixture - setup and teardown

Unless we are testing something really simple, we will need to set up some environment before
we can check the actual functionality. This set up can be as simple as creating an instance
object, but it can also involve setting up one ore databases, servers etc.

This setup is usually called `fixture` among the testers.

In any case if several test functions need the same setup we can factor that out.
To make this standardized, `pytest` designated a pair of functions names for this.
If we implement the function called `setup_function` it will be called before
every test function and if implement the `teardown_function` then that will
be called after every test function.

{% include file="examples/python/pt2/test_fixture.py" %}

The execution will show the order:

```
$ pytest test_fixture.py -s

===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
Using --random-order-bucket=module
Using --random-order-seed=100711

rootdir: /examples/python/pt2, inifile:
plugins: random-order-0.5.4
collected 3 items

test_fixture.py
setup_function
test_one
.
teardown_function

setup_function
test_three
.
teardown_function

setup_function
test_two
.
teardown_function


=================== 3 passed in 0.02 seconds ===================
```



