---
title: "Testing Python: Getting started with Pytest"
timestamp: 2017-09-06T17:30:01
tags:
  - pytest
published: true
books:
  - python
author: szabgab
archive: true
---


While we can use either [doctest](/doctest-in-python) or
[unittest](/introduction-to-python-unittest) without installing
any extra module, today, it seems to most recommended testing library for Python is the
[pytest](http://pytest.org/). In this article we'll see how to start using it.


## Code under test

We'll use the same simple module with a single function called `is_anagram`
as our subject for testing that can check if the two supplied strings
are [anagrams](https://en.wikipedia.org/wiki/Anagram) or not.
That is, if they consist exactly the same characters.
Later we'll get to more complex cases as well.

{% include file="examples/python/pt/mymod_1.py" %}


## Setup Virtualenv - install Pytest

Before we can use it, we need to install Pytest. There are several ways to install Python modules.
These days I usually use `virtualenv` and tell it to use python3. Once the virtualenv is
ready, I install the `pytest` module.

```
virtualenv venv3 -p python3
source venv3/bin/activate
pip install pytest
```

## Simple test code

In order to test our code, we create a separate file that looks like this:

{% include file="examples/python/pt/test_mymod_1.py" %}

We need to load the code that we are testing. In this case `from mymod_1 import is_anagram`
does it.

We need to declare a function with a name that starts with `test_`.
Inside that function we call the function we are testing, and using the
`assert` statement of Python we check if the value is as we expect it.
(In the first 2 cases we expect `is_anagram` to return `True`
in the 3rd case we expect it to return `False`.)

At this point the name of the test file does not matter, but using a name that starts
with test_ is both makes it easier for the reader to know which files contain the tests
and will also allow pytest to locate these files automatically.


Once we have this we can run our test by typing in `pytest test_mymod_1.py`

```
$ pytest test_mymod_1.py

===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /examples/python/pt, inifile:
collected 1 items

test_mymod_1.py .

=================== 1 passed in 0.03 seconds ===================
```

After some information about our environment (e.g. version of Python and pytest)
we can see the name of the test file and a dot `.` after it.
That dot indicates that we encountered a single test function.
The number of assertions within a test function is not indicated.

At the end we see that there was a total of 1 test methods and it passed.

## Test with failure

After a while someone might come to you and complain that strings with spaces
sometimes are not recognized as anagrams.
"ana gram" and "naga ram" are found as anagrams but, "anagram" and "nag a ram" are not.

Before attempting to fix the code we need to make sure that we can reproduce the problem
and what would be a better way than to write a test?

We add a new test function with the two test case. We expect both to return `True`
as both pairs are anagrams.

{% include file="examples/python/pt/test_mymod_2.py" %}

We run the test using `pytest test_mymod_2.py` and get the following output:

```
$ pytest test_mymod_2.py

===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /examples/python/pt, inifile:
collected 2 items

test_mymod_2.py .F

=========================== FAILURES ===========================
____________________ test_multiword_anagram ____________________

    def test_multiword_anagram():
       assert is_anagram("ana gram", "naga ram")
>      assert is_anagram("anagram", "nag a ram")
E      AssertionError: assert False
E       +  where False = is_anagram('anagram', 'nag a ram')

test_mymod_2.py:10: AssertionError
============== 1 failed, 1 passed in 0.09 seconds ==============
```

After the name of the test script we see now two characters for the two test functions.
The dot `.` indicates that one of the functions passed. The `E` indicates that
the other test function failed. (Error)

Below that we can see the actual failure indicating that a `False` was received.

## Verbose mode

`pytest` also has a verbose mode that you can trigger with the `-v` flag.

Running `pytest -v test_mymod_2.py` will provide the following additional output
that might or might not make you happier:

```
test_mymod_2.py::test_anagram PASSED
test_mymod_2.py::test_multiword_anagram FAILED
```

## Selective running of test functions

If you have a large test suite and one of the test functions fail, then while
trying to fix the bug you'll want to repeatedly run that test function without
bothering with all the rest of the test function.

This might be even more important if several of the test functions are failing
and even when you are adding a new feature.

During development you'd probably want to focus on a specific test function and
only when you are done with that test function and with the code it test,
only then run all the other tests.

We can easily accomplish this with `pytest` and the verbose mode mentioned
above can actually help us as it shows the fully qualified names of each test function.

We can run the individual test function by appending them to the name of the test file.
So 

```
pytest -v test_mymod_2.py::test_anagram
```

will run the `test_anagram` function and

```
pytest -v test_mymod_2.py::test_multiword_anagram
```

will run the `test_multiword_anagram` function.


## Test discovery

If we have many tests we'll want to spread them to several test files, but then the
question comes: how to run them all.

If they are all in the same directory we can do something like this: `pytest test_mymod_*`
but if we have a whole hierarchy of test files in many directories then the best is to rely
on the test discovery feature of Pytest.

If we run `pytest` without any parameters, it will traverse all the directories starting from
the current directory, locate every file that looks like a test file and run it.

The problem with this is that we use `virtualenv` with a directory called `venv3` in the
root directory of our project. By default `pytest` will look for test files inside this directory
as well.

Luckily it is easy to exclude one or more directories from the test-discovery process by using the `--ignore`
parameter: `pytest --ignore venv3/`.

```
$ pytest --ignore venv3/

===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /examples/python/pt, inifile:
collected 3 items

test_mymod_1.py .
test_mymod_2.py .F

=========================== FAILURES ===========================
____________________ test_multiword_anagram ____________________

    def test_multiword_anagram():
       assert is_anagram("ana gram", "naga ram")
>      assert is_anagram("anagram", "nag a ram")
E      AssertionError: assert False
E       +  where False = is_anagram('anagram', 'nag a ram')

test_mymod_2.py:10: AssertionError
============== 1 failed, 2 passed in 0.09 seconds ==============
```

The output shows that two test files were found.

In the first one (test_mymod_1.py) there was one test function which has passed.
(The single dot `.` after the filename shows this.)

In the second one (test_mymod_2.py) there were two test functions.
The first one passed (`.`) the second failed `F`.


## Comments

I have a project which has about 2000 lines of code in it. When I started writing it, my ideas of unit testing was putting a bunch of code in a section beginning with:

if __name__ == "__main__":
    def test_something ( actual_answer, expected_answer, error_message ):
        assert actual_answer == expected_answer, "%s : actual_answer is %s expected_answer is %s" % ( str(actual_answer), str(expected_answer), error_message )

    my_object = MyClass( arg )
    test_something ( my_object.function( arg_1 ), expected_answer_1, "my_object.function flunked test 1"
    test_something ( my_object.function( arg_2), expected_answer_2, "my_object.function flunked test 2"
 


So I am doing unit testing, but I get the sense that I am not doing unit testing the way it "ought" be done.

I have been looking through the internet, and I find that the literature on testing code in general and testing using pytest in particular is vast. What I have not found, and maybe that's because what I am looking for is buried in something else, is how to take my existing code base and revamp it for use with pytest or some other testing framework.

In particular, I have a function that uses <tt>subprocess.run</tt> to run a command and then parses the command's output. I'd like to test it. I have several ideas on how to go about doing this, such putting the subprocess call in a subroutine or method which detects if it is "production" or "test" and returns a canned output if in test. This idea doesn't scale very well, and IMHO clutters up the production code unnecessarily,

<hr>

nice post, very simple and clear. I have a question though, is there any recommendation on how to organize our .py files that will contain all of these test_ functions? I know this always depends on preferences but I'd like to know if there are any recommended guidelines on how to structure our testing for instance if I have a module called connectors.py does it make sense to say that we will need a test_connectors.py that will unit test every function in it?

--
That's a good strategy.

