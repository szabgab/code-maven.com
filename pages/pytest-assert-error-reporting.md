---
title: "Python Pytest assertion error reporting"
timestamp: 2017-05-05T09:30:01
tags:
  - pytest
  - assert
published: true
books:
  - python
author: szabgab
archive: true
---


One of the advantages of `Pytest` over the `unittest` module is that we don't need to use different
assert methods on different data structures. Pytest, by way of magic (also known as introspection)
can infere the actual value, the expected value, and the operation used in a plain old `assert` statement and can
provide a rather nice error message.

Let's see a few of those error messages:


In these examples I'll keep both the code under test and the testing function in the same file. You've already seen how it would look normally if we imported the functions under test from another module. If not check out the [getting started with pytest](https://perlmaven.com/pro/getting-started-with-pytest) article.

Also, in order to make the results clear, I've removed the summary of the test runs and kept only the actual
error reporting.

## Comparing numbers for equality in Pytest

Probably the most basic thing to test is whether a function given some input returns an expected number.

{% include file="examples/python/pt3/test_number_equal.py" %}

In the above function `double` someone has mistakenly used `+` instead of `*`. The result of the test looks like this

```
$ pytest test_number_equal.py

    def test_string_equal():
        assert double(2) == 4
>       assert double(21) == 42
E       assert 23 == 42
E        +  where 23 = double(21)
```

The line starting with the `&gt;` sign indicates the assert line that failed. The lines starting with `E` are the details.

## Compare numbers relatively

In certain cases we cannot test for equality. For example if we would like to test if some process finishes within a given time, or whether a timeout is triggered at the right time. In such cases we need to compare if a number is less-than or greater-than some other number.

{% include file="examples/python/pt3/test_number_less_than.py" %}

Running the test will provide the following error message:

```
$ pytest test_number_less_than.py

    def test_string_equal():
>       assert get_number() < 0
E       assert 23 < 0
E        +  where 23 = get_number()
```

The error-report looks quite similar to what we had above, but in this case too it is clear what was the comparision operation that failed.

## Comparing strings

Similar to numbers we might want to know if a string received from some function is the same as we expect it to be.

{% include file="examples/python/pt3/test_string_equal.py" %}

The result looks familiar:

```
$ pytest test_string_equal.py

    def test_string_equal():
>       assert get_string() == "abd"
E       AssertionError: assert 'abc' == 'abd'
E         - abc
E         + abd
```

For such short strings seeing both the expected string and the actual string is ok.
We can look at the strings and compare them character by character to see what was the actual difference.

## Compare long strings


If the strings are much longer however, it would be really hard for us to pinpoint the specific location of the character (or characters) that differ. Luckily the authors of Pytest have thought about this problem as well:

{% include file="examples/python/pt3/test_long_strings.py" %}

`string.printable` is a string containing all the printable ASCII characters:
`0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&amp;\'()*+,-./:;&lt;=&gt;?@[\\]^_`{|}~ \t\n\r\x0b\x0c`

Our brilliant `get_string` function will return it twice with an additional character between them.
We use this to create two nasty and long strings that differ by a single character.

The output looks like this:

```
$ pytest test_long_strings.py

    def test_long_strings():
>       assert get_string('a') == get_string('b')
E       AssertionError: assert '0123456789ab...t\n\r\x0b\x0c' == '0123456789abc...t\n\r\x0b\x0c'
E         Skipping 90 identical leading characters in diff, use -v to show
E         Skipping 91 identical trailing characters in diff, use -v to show
E           {|}~
E
E         - a012345678
E         ? ^
E         + b012345678
E         ? ^
```

I think this explains quite nicely where have the two strings differ and if you really, really want to see the
whole string you can use the `-v` flag.

## Is string in longer string

If you need to check whether a string is part of a larger string we can use the regular `in` operator.

{% include file="examples/python/pt3/test_substring.py" %}

In case of failure the result will include only the beginning and the end of the "long string".
This can be very usefule if you need to test whether a certain string appears or not in an HTML page.

{% include file="examples/python/pt3/test_substring.txt" %}

## Testing any expression

Instead of calling a function we might have an expression on one side of the equation. (Actually I am not sure how often this would happen in the real world.
Maybe we only see these in examples on how pytest works.)

{% include file="examples/python/pt3/test_expression_equal.py" %}

The test result:

```
$ pytest test_expression_equal.py

    def test_expression_equal():
        a = 3
>       assert a % 2 == 0
E       assert (3 % 2) == 0
```

## Is element in a list?

Besides comparing individual values we might also want to compare more complex data. First, let's see what happens if our test must ensure that a value can be found in a list?

{% include file="examples/python/pt3/test_in_list.py" %}

We can use the `in` operator of Python. The result will look like this:

```
$ pytest test_in_list.py

    def test_in_list():
>       assert "dog" in get_list()
E       AssertionError: assert 'dog' in ['monkey', 'cat']
E        +  where ['monkey', 'cat'] = get_list()
```

Pytest will conveniently show us the list that did not contain the expected value.


## Compare lists in Pytest

A more interesting case might be testing if the returned list is the same as the expected list. Using the `==` operator can tell us if the two lists are equal or not, but if we need to understand what went wrong, we'd better know where do the lists differ.
Or at least where do they start to differ.

{% include file="examples/python/pt3/test_lists.py" %}

The result:

```
$ pytest test_lists.py

    def test_long_lists():
>       assert get_list('a') == get_list('b')
E       AssertionError: assert ['0', '1', '2...'4', '5', ...] == ['0', '1', '2'...'4', '5', ...]
E         At index 100 diff: 'a' != 'b'
E         Use -v to get the full diff
```

We could further explore the output for the cases when multiple elements differ and when one list is a sublist of the other.

## Compare dictionaries in Pytest

Dictionaries can differ in a number of ways. The keys might be identical, but some values might differ.
Some keys might be missing in the actual result or there might be some extra keys.

In this example we test all of these:

Using the `string.printable` we create a dictionary where the keys are the printable characters and the values
are their respective ASCII value returned by the `ord` function. Then we add (or replace) one of key-value pair.

{% include file="examples/python/pt3/test_dictionaries.py" %}

The result looks like this:

```
$ pytest test_dictionaries.py

______________ test_big_dictionary_different_value _______________

    def test_big_dictionary_different_value():
>       assert get_dictionary('a', 'def') == get_dictionary('a', 'abc')
E       AssertionError: assert {'\t': 9, '\n...x0c': 12, ...} == {'\t': 9, '\n'...x0c': 12, ...}
E         Omitting 99 identical items, use -v to show
E         Differing items:
E         {'a': 'def'} != {'a': 'abc'}
E         Use -v to get the full diff

_______________ test_big_dictionary_differnt_keys ________________

    def test_big_dictionary_differnt_keys():
>       assert get_dictionary('abc', 1) == get_dictionary('def', 2)
E       AssertionError: assert {'\t': 9, '\n...x0c': 12, ...} == {'\t': 9, '\n'...x0c': 12, ...}
E         Omitting 100 identical items, use -v to show
E         Left contains more items:
E         {'abc': 1}
E         Right contains more items:
E         {'def': 2}
E         Use -v to get the full diff
```

The first test function got two dictionaries where the value of a single key differed.

The second test function had an extra key in both dictionaries.

## Testing for expected exceptions in Pytest

Finally let's look at exceptions!

A good test suite will test the expected behaviour both when the input is fine and
also when the input triggers some exception. Without testing the exception we cannot
be sure that they will be really raiesed when necessary. An incorrect refactoring
might eliminate the error checking of our code therby letting through invalid data
and either triggering a different exception as in our example, or not generating any exception
just silently doing the wrong thing.

In this brilliant example the `divide` function checks if the divider is 0 and raises it
own type of exception instead of letting Python rais its own. If this is the defined behavior
someone using our module will probably wrap our code in some `try` expression and expect
a `ValueError` error. If someone changes our `divide` function and removed our
special exception then we basically have broken the exception-handling of our user.

{% include file="examples/python/pt3/test_exceptions.py" %} 

The test ha actually two parts. The first part:

```
    with pytest.raises(ValueError) as e:
        divide(1, 0)
```

checks if a `ValueError` was raised during our call to `divide(1, 0)`
and will assign the exception object to the arbitrarily named variable `e`.

The second part is a plain `assert` that checks if the text of the exception is what
we expect to be.

This is now the expected behaviour. Our test passes:

```
$ pytest test_exceptions.py

test_exceptions.py .
```

What if someone changes the error message in our exception from Zero to Null?

{% include file="examples/python/pt3/test_exceptions_text_changed.py" %}

The `assert` in the test will fail indicating the change in the text.
This is actually a plain string comparision.

```
$ pytest test_exceptions_text_changed.py


    def test_zero_division():
        with pytest.raises(ValueError) as e:
            divide(1, 0)
>       assert str(e.value) == 'Cannot divide by Zero'
E       AssertionError: assert 'Cannot divide by Null' == 'Cannot divide by Zero'
E         - Cannot divide by Null
E         ?                  ^^^^
E         + Cannot divide by Zero
E         ?                  ^^^^
```


In the second example we show the case when the special exception raising is gone.
Either by mistake or because someone decided that it should not be there.
In this case the first part of our test function will catch the different exception.

{% include file="examples/python/pt3/test_exceptions_failing.py" %} 

The report will look like this:

```
$ pytest test_exceptions_failing.py

    def test_zero_division():
        with pytest.raises(ValueError) as e:
>           divide(1, 0)

test_exceptions_failing.py:10:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

a = 1, b = 0

    def divide(a, b):
    #    if b == 0:
    #        raise ValueError('Cannot divide by Zero')
>       return a / b
E       ZeroDivisionError: division by zero
```

## Exception depositing money to the bank

Another case when checking for proper exceptions might be important is when
we want to avoid silently incorrect behavior.

For example in this code we have a function called `deposit` that expects
a non-negative number. We added our input validation that will raise an exception protecting
the balance of our bank account. (In our example we only indicated the location of the code
that actually changes the balance.)

{% include file="examples/python/pt3/test_bank.py" %} 

We have also created a test-case that will ensure that the protection is there,
or at least that the function raises an exception if -1 was passed to it.

## Conclusion

Pytest and its automatic error reporting is awesome.

