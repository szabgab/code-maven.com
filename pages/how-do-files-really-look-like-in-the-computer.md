---
title: "How do files really look like in the computer?"
timestamp: 2022-11-30T09:30:01
tags:
  - Unicode
  - UTF-8
description: "When you create a file with some text in it, you would think that that text is stored in the computer as it is. It is not. It is just numbers."
types:
  - screencast
published: true
author: szabgab
archive: true
show_related: true
---


When you create a file with some text in it, you would think that that text is stored in the computer as it is.

It is not like that. Each letter, each number, each punctuation (e.g. !?:) has a number and that number is stored.

Then the various programs you use to show that file will automatically convert the number to the drawing you are familiar with.


{% youtube id="ALnV06KaONk" file="how-do-files-really-look-like-in-the-computer.mp4" %}

The generic name of all these "drawings" (digits, letters, punctuation, even emojies) is <b>character</b> or <b>glyph</b>.
So we say we type in characters. Each character has a number associated with based on the standard called [Unicode](https://en.wikipedia.org/wiki/Unicode).
Each such value is then stored on the disk in one of the encodings. What we see here is the most common representation called [UTF-8](https://en.wikipedia.org/wiki/UTF-8).

We are going to use a program called <b>xxd</b> to show the real numbers representing each character in our files. It is available on Linux and I think on Mac OSX as well,
and I am quite sure you can find something similar for Windows as well.

Actually this program shows the hexa value of each byte. A byte can hold a number between 0-255 or in hexa between 0-ff. As you'll later see some characters are
represented by a single byte. Some by 2 and some even by 4.

Hexa numbers are represented by 0-9 and then a-f or A-F. The capitalization of these letters does not matter.

This program displays the hexadecimal values of each byte. That is, it uses base 16. We are going to also convert the numbers to base 10 as that's more familiar for most of us.

## Hello World

This is the file I created. This is how you'd see it if you opened it with any text editor:

{% include file="examples/hello_world.txt" %}

This is how I run the <b>xxd</b> program:

```
$ xxd -c 1 -d examples/hello_world.txt
```

(<b>-c 1</b> tells xxd to show only one byte per line, <b>-d</b> tells it to show the first column as decimal numbers)

This is its output:

```
00000000: 48  H
00000001: 65  e
00000002: 6c  l
00000003: 6c  l
00000004: 6f  o
00000005: 20
00000006: 57  W
00000007: 6f  o
00000008: 6c  l
00000009: 64  d
00000010: 21  !
00000011: 0a  .
00000012: 48  H
00000013: 61  a
00000014: 76  v
00000015: 65  e
00000016: 20
00000017: 61  a
00000018: 20
00000019: 6e  n
00000020: 69  i
00000021: 63  c
00000022: 65  e
00000023: 20
00000024: 64  d
00000025: 61  a
00000026: 79  y
00000027: 21  !
```

The left-most column shows the location of the bytes. It is just an index starting from 0.
Then we see the hexadecimal (hexa) values in the file and finally, on the right hand side, we see our real characters. More-or-less.

Here you can see that the capital H is represented by the hexa number 48 which is decimal 72 (4*16+8)
You can see a subset of the [Unicode characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters).
I found it by searching for "Latin capital letter h" on that page.

Then the letter e is hexa 65 which is decimal 101.

The next interesting thing comes on the 6th row (index 5) where you can see that a space is represented by the hexa number 20 which is decimal 32.

A bit further (index 10) you can see an exclamation mark <b>!</b> which is represented by hexa 21 which is decimal 33.

Then there is a dot <b>.</b> in this view. This dot is used by <b>xxd</b> to show that there is something, but that it cannot properly display it.
There are several so-called control characters that have a number in the Unicode table, but that instead of representing a drawing (a character or glyph)
the give an instruction to the computer what to do. For example, strange as it is, there is one called the "<b>bell character</b>" (hexa 7, decimal 7)
that will make a beeping sound when the computer encounters it.

In our case it the dot is shown instead of a character called "<b>line feed</b>" or <b>LF</b> (hexa a or 0a, decimal 10).

This tells the computer, well, at least Linux and Mac OSX, that the next character should be displayed in the next line.
If you look at how the file is displayed "normal" you will see that indeed the next thing, the letter H is displayed on a new line.
On Windows this works slightly differently, but I don't want to get into that. At least not now.

The reset is easy as we only have Latin letters, spaces and an exclamation point. All of which we have already seen.

## Hungarian

Next we'll see some text that uses Latin letters, but with a few additional characters.

English has 5 vowels: a, e, i, o, u, but depending on the word and the country where you are from, they might sound in various ways.

Hungarian has 14 vowels, each one has its distinct sound and they only slightly change based on the area the person is from.
They are represented using the 5 Latin vowels with some extra accent marks on the top.

This is how they look like:

{% include file="examples/hungarian.txt" %}

This is how they are represented in a file:

```
$ xxd -c 1 -d examples/hungarian.txt
```

```
00000000: 61  a
00000001: c3  .
00000002: a1  .
00000003: 65  e
00000004: c3  .
00000005: a9  .
00000006: 69  i
00000007: c3  .
00000008: ad  .
00000009: 6f  o
00000010: c3  .
00000011: b3  .
00000012: c3  .
00000013: b6  .
00000014: c5  .
00000015: 91  .
00000016: 75  u
00000017: c3  .
00000018: ba  .
00000019: c3  .
00000020: bc  .
00000021: c5  .
00000022: b1  .
```

The letter "a" did not cause any problems. It is hexa 61 which is decimal 97.

Given that a single byte can hold only up to 255 and there are way more characters in the world, the Unicode table has numbers that are higher than 255
and thus their will take up 2 or more bytes.

The <b>á</b> letter is represented by the bytes c3 and a1 (decimal 50081) in rows 1 and 2 above. See the row about UTF-8 on [this page](https://unicode-table.com/en/00E1/).

Because <b>xxd</b> shows us the content byte-by-byte it won't combine these two bytes and thus it uses dots in both of these lines to indicate that there
is something it cannot really show.

Then comes the letter "<b>e</b>" hexa 65 decimal 101 which is easy again. See [here](https://unicode-table.com/en/0065/).

The the letter "<b>é</b>" hexa c3 a9, decimal 50089. See  [here](https://unicode-table.com/en/00E9/).

The rest is similar.

## Spanish

Spanish has the famous <b>ñ</b> that actually sounds like the Hungarian <b>ny</b>, but let's not go into the Hungarian double and triple letters.

This is the text:

{% include file="examples/spanish.txt" %}

These are the numbers behind it:

```
$ xxd -c 1 -d examples/spanish.txt
00000000: 6d  m
00000001: 61  a
00000002: c3  .
00000003: b1  .
00000004: 61  a
00000005: 6e  n
00000006: 61  a
```

The only thing that stands out here is the <b>ñ</b> that is represented by c3 b1 (decimal 50097) See [here](https://unicode-table.com/en/00F1/).

## Hebrew

Hebrew, Arabic, and Persian text can add an extra level of fun. Not just because they use a different alphabet, but also because they are written
from right to left. Here is an example in Hebrew:

{% include file="examples/hebrew.txt" %}

And here are the numbers behind the scene:

```
$ xxd -c 1 -d examples/hebrew.txt
00000000: d7  .
00000001: a9  .
00000002: d7  .
00000003: 9c  .
00000004: d7  .
00000005: 95  .
00000006: d7  .
00000007: 9d  .
00000008: 20
00000009: d7  .
00000010: a2  .
00000011: d7  .
00000012: 95  .
00000013: d7  .
00000014: 9c  .
00000015: d7  .
00000016: 9d  .
00000017: 0a  .
```

The only familiar item here is the space index 8 that is represented by the hexa 20 decimal 32 as in the other cases.

The letter <b>ש</b> is the first character, on the right-hand side of the text. It is represented by d7 a9 (decimal 55209). See it [here](https://unicode-table.com/en/05E9/).

Then comes <b>ל</b> the second character from the right. It is d7 9c (decimal 55196). See [here](https://unicode-table.com/en/05DC/)

## Korean, Japanese, Chinese, Thai, Urdu, ...

I won't go into that as I am not familiar with either of those

## Emojies

However emojies are very common and well understood. Sort of.

{% include file="examples/emojies.txt" %}

```
$ xxd -c 1 -d examples/emojies.txt
00000000: f0  .
00000001: 9f  .
00000002: 91  .
00000003: b7  .
00000004: f0  .
00000005: 9f  .
00000006: 91  .
00000007: b8  .
00000008: f0  .
00000009: 9f  .
00000010: 91  .
00000011: b9  .
00000012: f0  .
00000013: 9f  .
00000014: 91  .
00000015: ba  .
00000016: f0  .
00000017: 9f  .
00000018: 91  .
00000019: bb  .
00000020: e2  .
00000021: 9c  .
00000022: 8d  .
00000023: f0  .
00000024: 9f  .
00000025: 91  .
00000026: bc  .
00000027: f0  .
00000028: 9f  .
00000029: 91  .
00000030: bd  .
00000031: f0  .
00000032: 9f  .
00000033: 91  .
00000034: be  .
00000035: f0  .
00000036: 9f  .
00000037: 91  .
00000038: bf  .
00000039: f0  .
00000040: 9f  .
00000041: 92  .
00000042: 80  .
00000043: f0  .
00000044: 9f  .
00000045: 92  .
00000046: 81  .
00000047: f0  .
00000048: 9f  .
00000049: 92  .
00000050: 82  .
```

The first one is apparently called [construction worker](https://unicode-table.com/en/1F477/)
It is represented by 4 bytes. In hexa: F0 9F 91 B7 (in decimal 4,036,989,367. Yes that's a big number).

The rest are similar.


## Unicode Table

You can copy any character, including an emoji from this article or from elsewhere and paste it in the search form of the
[Unicode table](https://unicode-table.com/) to find the information about it.


## Conclusion

There is a lot more to say about representation of content in files, both historically and the current best practices,
but I think this will be enough for now. I'll cover some related subjects later on.

