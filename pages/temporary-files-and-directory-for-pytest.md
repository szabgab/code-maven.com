---
title: "Python: Temporary files and directory for Pytest"
timestamp: 2018-05-18T08:30:01
tags:
  - pytest
  - tmpdir
published: true
books:
  - python
author: szabgab
archive: true
---


When we write tests for complex applications, the application will often rely on some files
that ned to be read. For example configuration files.

In addition the application might create files while the test is running or
change some of the existing files.

We would like to be sure these changes don't interfer with the regular work of the rest of the
computer and even if we run several tets in parallel that might all want to change the same file,
these tests won't interfer with each other.

The best course of action for us is to use a unique temporary directory for each test function.


## PyTest fixtures

A fixture in the testing world is the environment in which the test runs. It can be a certain set of files,
in a directory structure. It can be a database with some well known data in it. It can be anything we control. 

PyTest has a functionality called [fixtures](https://docs.pytest.org/en/latest/fixture.html) that provide
varius tools to create fixtures. It works similar to how [Dependency Injection works in AngularJS](/dependency-injection-in-angularjs). In the declaration of the test function we need to declare that we expect one
of the fixtures to be passed and PyTest will pass the object that provides that fixture.

## The tmpdir fixture

One of the most commonly used PyTest fixture is `tmpdir` that provides a standardized way to create [temporary directories](https://docs.pytest.org/en/latest/tmpdir.html).

In our example we test the [configparser](https://docs.python.org/3/library/configparser.html) module.
The same technique could be used in any application that assumes to have an ini file for configuration.

By declaring that our `test_read_ini` function expects the `tmpdir` variable,
basically we ask PyTest to create a temporary directory, create an object that represents that
directory and pass it to our function. The `tmpdir` variable contains that object.
We can do all kinds of thins with it. For example we can print the content using plain old `print`

```
print(tmpdir)
```

In order to actually see this output we'll have to pass the `-s</h> parameter to `pytest`:

```
pytest -s test_read_ini.py
```


In my case, running on OSX, I got such a path:

```
/private/var/folders/ry/z60xxmw0000gn/T/pytest-of-gabor/pytest-14/test_read0
```

As the `tmpdir` passed to the function is a [py.path](http://py.readthedocs.io/en/latest/path.html)
object it has a number of methods we can use. For example we can call the `mkdir` method to create
a subdirectory in our temporary directory. This can be useful if we need to build a directory hierarchy.

On the object returned by `mkdir` we can call he `join` method that returns an object representing 
a file with the given name. We can use this object and the `write` method of the object to create
the file we need for our test.

Then we can use this file for our tests.

{% include file="examples/python/pt4/test_read_ini.py" %}


## Removing temporary directories

By default `pytest` will leave the temporary intact after the test run.
You could delete it in your code, but actually having the directory around can be quite useful
especially if the test created files in it. Then, in case of failure, you could inspect the files.

You don't have to worry of having too many such temporary directories laying around either
as `tmpdir` will actually remove the earlier temporary directories when you run the test again.
Normally it keeps the 3 most recent directories.

So my suggestion is to just not worry about the directories.

