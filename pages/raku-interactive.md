---
title: "Raku Interactive Shell - values in $ variables"
timestamp: 2020-08-26T07:32:02
tags:
  - list
  - keys
  - values
  - Int
  - Pair
  - Hash
  - List
  - Array
published: true
books:
  - raku
author: szabgab
archive: true
---


When learning Raku, one of the best things you can do is to experiment with the language in the interactive shell.
(Also known as [REPL = Read Eval Print Loop](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop))

Once you have [Rakudo](https://rakudo.org/) installed, open a Terminal (or Command Prompt in MS Windows)
and type in <b>raku</b>. If you are using the Docker version of Rakudo Star then run it in interactive mode as

```
docker run --rm -it rakudo-star
```

After a second or so, you will see:


```
To exit type 'exit' or '^D'
>
```

The &gt; sign is the prompt. You can now type in any Raku expression.
Let's start with a few simple ones:

```
> say "hello world"
hello world
> say 42
42
> 19 + 23
42
```

`say` is the keyword to <b>print</b> something to the screen and add a trailing newline.

Strings are in double-quotes. Numbers don't have quotes.

We can use Raku as a calculator. In the interactive shell we don't even need to call <b>say</b>
as it will automatically print the result of the last statement. (The P is in the name REPL for a reason.)


## Variables

Most variables in Raku have one or two special characters at the beginning. The first such character is called
Sigil, the second, optional character is called Twigil.

The `$` sigil means the variable can contain any item.
Let's try to assign a number to a variable that starts with a `$`:

```
> $x = 42
===SORRY!=== Error while compiling:
Variable '$x' is not declared
------> <BOL>⏏$x = 42
```

Even the interactive shell requires us to declare our variables using the `my` keyword:

```
> my $x = 42
42
> $x
42
> $x - 7
35
```

After the declaration and the assignment, we can use the variable in arithmetic operations.

Using the `^name` method we can also ask the variable what type is it. In this case it is of type `Int`:

```
> $x.^name
Int
```


We can replace the content of the variable with a string, and then, when we ask what is
the <b>^name</b> of its type, we get back that it is a <b>Str</b>.

```
> $x = "abc"
abc

> $x.^name
Str
```

Some people love this kind of flexibility, for others this looks crazy dangerous. Don't worry,
In Raku, you can be much stricter with your variable types during declaration. If that's your thing:

```
> my Int $w = 42
42
> $w.^name
Int

> $w = "hello"
Type check failed in assignment to $w; expected Int but got Str ("hello")
  in block <unit> at <unknown file> line 1

>
```

In this case, we've declared the $w variable to be `Int` so we won't be able to
assign any other type to it.


Back to our type declaration free variable, you can put all kind of other types in that variable:

```
> $x = 3.14
3.14
> $x.^name
Rat

> $x = ["foo", "bar", "qux"]
[foo bar qux]
> $x.^name
Array

> $x = ("foo", "bar", "qux")
(foo bar qux)
> $x.^name
List

> $x = {name => "Foo", answer => 42}
{answer => 42, name => Foo}
> $x.^name
Hash

> $x = planet => "Earth"
platent => Earth
> $x.^name
Pair
```


We'll look at these types later on.

## Pair

```
> $x = planet => "Earth"
planet => Earth
> $x.^name
Pair
> $x.gist
planet => Earth
> $x.key
planet
> $x.value
Earth
```

## Hash

A Hash is a key-value store. In other languages it might be called `Associative Array` or `Dictionary`.

We can create a hash using curly-braces, and assign it to a variable starting with a `$`:

```
> my $x = {home => "Earth", answer => 42};
{answer => 42, home => Earth}
```

It is a hash:

```
> $x.^name
Hash
```

We can access the values of the individual keys both with quotes around the keys:

```
> $x{"home"}
Earth
> $x{"answer"}
42
```

And without any quotes:

```
> $x&lt;home>
Earth
> $x&lt;answer>
42
```

We can fetch the `keys` of the hash and the `values`
separately:

```
> $x.keys
(home answer)

> $x.values
(Earth 42)
```

What `keys` really returns is a `Seq` (Sequence) object:

```
> my $z = $x.keys
(home answer)
> $z.^name
Seq
```

We can also iterate over the individual keys using the `for` loop.
($k is the loop variable that will get each key on its turn.)

```
> for $x.keys -> $k { say $k }
home
answer
```

Using the keys we can access the respective values:

```
> for $x.keys -> $k { say $k; say $x{$k} }
home
Earth
answer
42
```

Alternatively we can fetch a list of `pairs`
and on each `Pair` object we can call the `key`
and the `value` methods:

```
> for $x.pairs -> $p { say $p.^name; say $p.key; say $p.value}
Pair
home
Earth
Pair
answer
42
```


## List

If we wrap the right-hand side in parentheses, we get a `List`
on the left-hand side:

```
> $x = ("Earth", "Wind", "Fire")
(Earth Wind Fire)
> $x.^name
List
```

In order to iterate over its elements, we need to call the `list`
method on it:

```
> for $x.list -> $v { say $v }
Earth
Wind
Fire
```

## Array

If we put square brackets around the values on the right-hand side, we
get an `Array`

```
> $x = ["Earth", "Wind", "Fire"]
[Earth Wind Fire]
> $x.^name
Array
```

Here too we need to call the `list` method in order to iterate over the elements:

```
> for $x.list -> $i { say $i }
Earth
Wind
Fire
```

## Forgetting the parentheses

If you forget the parentheses, Raku will silently forget about all the values except the first one.

```
> $x = "Earth", "Wind", "Fire"
(Earth Wind Fire)
> $x.^name
Str
> $x
Earth
```


## Conclusion

The REPL is a nice place to experiment with features, but we have to learn a lot more about Raku to make it useful for us.

