---
title: "CMOS #4: Tom Hudson - gron for making JSON greppable"
timestamp: 2016-09-06T20:01:01
tags:
  - podcast
  - gron
  - JSON
  - go
  - UK
description: "Interview with Tom Hudson about gron, the command line tool that can help you make JSON greppable to learn how an API works."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-4-tom-hudson-gron.mp3
  size: 17224989
  time: 19:24
img: /img/cmos/tom_hudson.png
alt: Tom Hudson
published: true
author: szabgab
archive: true
---


Interview with Tom Hudson about [gron](https://github.com/tomnomnom/gron),
the command line tool that makes JSON greppable.


{% youtube id="dxmsuFqB1tU" file="cmos-4-tom-hudson-gron.mp4" %}

<podcast>

<div id="person">
## Tom Hudson
* [Tom Hudson](https://tomnomnom.com/)
* [@TomNomNom](https://twitter.com/TomNomNom)
* [GitHub](https://github.com/tomnomnom)
</div>

<div id="links">
## Links

* [PHP](http://php.net/)
* [Go lang](https://golang.org/)
* The [Etherpad](http://etherpad.org/) (was Etherpad light) project.
* The [PHP client for Etherpad](https://github.com/tomnomnom/etherpad-lite-client).
* [Node.js](https://nodejs.org/)
* The window manager Tom mentioned: [goomwm](https://github.com/seanpringle/goomwwm) written by [Sean Pringle](https://github.com/seanpringle).
* Blog post on fixing a segfault in it despite not knowing C:
[Debugging a segfault in goomwwm](https://tomnomnom.com/posts/debugging-a-segfault-in-goomwwm)
* [gron](https://github.com/tomnomnom/gron)
* [JSON](http://www.json.org/)
* [AWK](https://en.wikipedia.org/wiki/AWK)
* [Extended Backus–Naur Form (EBNF)](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_Form)
* The [errors package](https://github.com/pkg/errors) written by [Dave Cheney](https://github.com/davecheney).
* The [jq](https://stedolan.github.io/jq/) tool for manipulating JSON.
* Some <q>advanced</q> examples of [gronning and ungronning](https://github.com/tomnomnom/gron/blob/master/ADVANCED.mkd)
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [tom guest1 Tom Hudson]

[00:01] szabgab:
  Hello there, this is the CMOS, the Code Maven Open Source podcast and interview series. I'm your host, Gabor Szabo, and with me is Tom Hudson, and we are going to talk about the project called gron.
Hi Tom, how are you?

[00:19] tom:
Hi, I'm fine, thank you, how are you?

[00:21] szabgab:
Ah, I'm fine, thank you. Let's start with introducing you a little bit. Please tell me a little about yourself, your background, how did you get here?

[00:30] tom:
Okay, so I'm Tom Hudson, I'm a software engineer in the UK, I work for a betting and gaming company, have been for about five years now. Started tinkering with a computer when I was a kid, eventually ended up spending some time as a network engineer and then a software engingeer, did a lot of PHP, more recently writ a bit of Go, mostly I like to make tools, try to make things to make other developer's lives easier, basically. Yeah, not a great deal to say about me, to be  honest.

[01:07] szabgab:
All right, it's okay. How long have you been writing open source stuff?

[01:13] tom:
I really started only to get into it serioiusly for the last couple of years or so. I mean, I'd released bits of code that I'd written before that, but they weren't very useful.
So only really in the last couple of years have I started to think about what other people might need and try to make  tools available for them. I mean, I think sharing code is generally a really good idea but I think only recently have I thought perhaps  my code was actually useful enough for people to actually be using.

[01:51] szabgab:
Have you had experience with contributing to other projects?

[01:56] tom:
Yeah, a few, so I have been a maintainer of the PHP client for the Etherpad Light project for awhile now. It's not a very active project but it's used by quite a few people.

[02:12] szabgab:
Sorry again, which project was it?

[02:14] tom:
Etherpad Light, a PHP client for the API. Etherpad Light is a collaberative text editor. I think nowadays, it's just called Etherpad, it is written in Node.JS. It's worth looking up actually, it's great fun to use. It's a great project.

Other than that, I've made some small contributioins here and there. I made a fix to the Window Manager that I use, one called Get Out of My Way Window Manager, written by a guy called Sean Pringle, it's a really great lightweight tiling Window Manager, or rather floating Window Manager, with a great support for tiling. Just small bits here and there, usually when I find something that's broken, and I need it to work, I'll try to fix it.

[03:07] szabgab:
Yeah, that reminds me there's this broken Window theory, so you fix your broken Window with the broken Window Manager. Okay, whatever. Yeah, but this Window Manager, is not in PHP, is it? So it's.

[03:22] tom:
Oh no, the Window Manager is in C. I don't know C but usually, my only real skill is just figuring things out, just figure out the things I need to achieve what I want, basically, so despite not knowing C, a lot of help from Google, couple of tools that let me get a deeper build and let me figure out where the segfault was happening.
I wrote a blog post about it awhile ago, entitled <q>Debugging a segfault in goomwwm.</q> It's on tomnomnom.com. And again, I don't know C so it's probably laughable to anyone who does, but it's mostly an adventure in finding a problem and fixing it for me.

[04:13] szabgab:
And was it accepted in the project?

[04:15] tom:
Yeah, yeah, so I got my pull request merged and I haven't had a problem with it since, so it's a really, really stable project otherwise. 

[04:21] szabgab:
That's great, I mean, that's a little bit here and a little bit there and that's how it moves forward, I think.

[04:28] tom:
Yeah, absolutely.

[04:29] szabgab:
So let's get to this project, gron.

[04:33] tom:
Okay.

[04:34] szabgab:
What is it? Why did you build it?

[04:37] tom:
So, professionally I deal with quite a few HTTP APIs that return JSON and some of them are quite badly documented but have very, very large responses so sometimes you know what you're looking for in the response and you can sort of grep for it, and some JSON, and you find that it's four, five, six levels deep.

So you don't get any context to go with that value, it can be really difficult to reason about the structure of that JSON, so originally about, I think it's about three, four years ago, I wrote gron in PHP and the idea was to take a JSON structure and output it as a series of individual assignments but as valid JavaScript, so you would end up with something like JSON.city.name = Leeds, for example.

And that means if you were grepping for that value, Leeds, you can see the whole path, all the way through. And you just get that context that allows you to see, what code do I actually need to write to access this value, what things do I need to traverse over? So mostly I wrote it because I needed it, but it didn't really gain any traction, initially, I think mostly because I'd written it in PHP.

The main feedback I had from people was, well, I'm writing Node.JS, or something like that. Or even, I'm writing C# or Perl. I don't have PHP installed, so I can't use this thing. It wasn't of use to that many people.

[06:31] szabgab:
Okay, and then I noticed that recently, I don't know when actually, you switched it to Go and you rewritten the whole thing.

[06:42] tom:
Yeah, so I did that earlier this year, I've been writing Go on and off for maybe two, two and a half, years now. And if I'm honest, the main reason I rewrote in Go was that I was trying to learn more Go and something where I'd already solved sort of some of the main problems and I could just do a straight port to Go, seemed like a good project to work on but then I realized that this means that other people can use this more easily.

So Go produces statically-linked binaries, by default, which means I can build for different operating systems, and just upload a binary and people can just download it and run it. It just works. So I kind of took it from there, started adding some more features, made it a bit more robust, a bit more user-friendly, and initially it was all just about turning the JSON into these discrete assignments, which at some point became a verb, to gron.

So JSON gets gronned, is the official way of putting it now. I then decided that, for the tool to be really powerful, maybe a little bit more than just exploration, it'd be really great if you could do the other, go in the other direction, which has become ungronning or norging, some people would have it put. There was a bit of debate about that early on.

But that means that you can alter the structure of the data in its intermediate state, when it's a list of assignments, with things like grep and sed and awk, if you like, and then turn the result back in to JSON again. I mean, it's not the kind of thing you should really be relying on in scripts, but when you just need like a quick fix for something, hacking on the command-line, it turns out to be actually pretty powerful.

[08:46] szabgab:
Interesting, I've tried the gron part, I haven't tried the opposite way yet and I like that you basically take a JSON structure, which is. My problem is that, in many cases, the JSON structure comes in as one-line basically.

[09:02] tom:
Yeah, okay.

[09:03] szabgab:
Not even, I mean, you can print out JSON normally, it's a readable format, even then it's hard to grep for something because you get the line but you don't get the context, but usually you just get one line and then you get the whole thing, and it's unusable for that purpose.

[09:21] tom:
Yeah.

[09:23] szabgab:
For reading, so what I really like is that you take that format and show the whole tree, all the levels, that go to the point that I was looking for. The fact that it's actually executable JavaScript, I don't know, is that, where do you feel it's a value?

[09:50] tom:
Largely, it's about predictability, so I mean, when I first wrote the tool, I was trying to think, what format could I use to output this data to make it understandable and I thought I could just write it as if it were filepaths, so with slashes, and then I thought, maybe the obvious thing to do is to write it in JavaScript, so I mean, JSON's a subset of JavaScript, and so I thought maybe having my own subset as well, would make sense, because then, in theory at least, anyone who knows JSON would immediately understand the format and what different things mean, like what the square braces mean, for example.

Someone had already come up with that format for me, I just needed to make it work. The fact that it is executable JavaScript is almost more of a curiosity in some ways but it means that I could get away with not defining the grammar properly initially. I just sort of said, the grammar is anything that's valid JavaScript, which was maybe a bit too vague, I have now started to define the grammar properly, particularly when I've been dealing with some bugs and things on the ungronning phase.

Which is fun, it's a real experience for me learning the EBNF, I think it's Extended  Backus-Naur Form, I think, so I'm self-educated, so I didn't do computer science or compiler theory or anything, so it's all a lot of intensive Googling to figure it out. But yeah, I think there's an example in the README, you can pipe the output into a .js file on console that's got log on the end of it, and it will output the object.

And then before the ungronning mode existed, I suppose that was kind of useful because you could do the things where you would grep -b and remove certain statements or you'd set it to change the paths in things and then you could pipe into a JavaScript file to get it back into JSON. But it was always a bit flakey, because you need every step of the way, so your top-level statement has to sort of say, well, this equals an empty object and only then can you refer to properties of that object.

Whereas, when gron does its own gron process, it can imply all of that stuff from a single statement and you don't need those preceding statements to say how things are set up, if that makes sense.

[12:42] szabgab:
Yeah, yeah, I think so. I'm thinking about the slash thing, that's separating it using slashes like a filepath, right? And yeah, that is an obvious solution but I, that came to my mind now, but it's obviously also broken, because slash can be a value and then you have to escape it and then.

[13:00] tom:
Yeah.

[13:00] szabgab:
Yeah, so it's.

[13:03] tom:
And also that means that I have to document it up front, what does the slash mean? Coming up with my own syntax to represent arrays or objects and things like that. Just seems, the fact that I even thought of it, seems silly in hindsight because there's already something that works really well for that.

[13:26] szabgab:
Yeah, yeah, I think so, yeah. Do you have any plans for gron?

[13:33] tom:
So a couple of things, I think need some attention, the error-handling is not very good at the moment.
So, for example, at the moment, you'll get fairly cryptic errors, things like <q>couldn't parse the input statements.</q>
Which is pretty useless, particularly if you're putting a half a megabyte of input into it.
Somewhere in here is an error.

[13:59] szabgab:
Yeah. No.

[14:03] tom:
Just doesn't work, sorry. So I mean, looking at package errors, which is a Go package written by Dave Cheney, I think it is? Which could help me provide a bit more context about the cause of errors by sort of wrapping them, as they go up the callstack.

But really I think my lexer that does the ungronning needs some attention, in terms of actually giving the user some context in terms of what character was it that caused the lexer to choke or what exactly it was that was unexpected so that people can figure out what their problem is a bit more easily.

So that needs some work, there are a few bits of the code, I think, just needs refactoring, where I've set things globally because it's easy and really it makes it a bit difficult to test because I've got to change global state when I'm in the test to make things work and I'd like to change how the adding close to the gron output works, it's kind of added in-line as the statements are built-up at the moment.

But then I need to do a sort, to make sure things are in the right order and an actual or human sort, as well, not just sort of a standard or less than or greater than, but in order to do that, I have to strip the callers back out of the statements again, which is a bit of a pain.
It's a bit inefficient, I mean performance has never really been a primary goal of the tool but if it's unbearably slow, then people aren't going to use it.

[15:52] szabgab:
Yep.

[15:53] tom:
Other than that, I mean, I'm a big fan of the Unix philosophy of just do one thing and do it well.
There's a bit of debate about what constitutes one thing, so should gronning and ungronning be separate tools? I don't think so, I consider them as close enough to one thing that it's okay.

I'm not too keen on adding many more features to it.
I mean the whole idea was that the tool would let you use things that you already knew, like grep and sed and awk, to get things done.
So, one of the common questions I get is, why didn't I just use jq? So jq is a tool for manipulating JSON and it's an amazing tool, it's really, really powerful, does a lot more things than gron, but it's only really useful if you're already able to understand the structure of the JSON itself.

So if you know the path to the key that you want, there's not much in the way of discovery there.
I mean, it'll do pretty printing and things like that but again, if you've got 0.5 megabytes of JSON and you grep for something and it's eight levels deep, you're doing a lot of scrolling to figure out where that actually is.
So really I see it as a complement to jq, which yeah, I think they can work together.

I think probably not like in a script or something like that but certainly, I find myself using gron to figure out what the structure of the JSON is, and then I'll probably use something like jq to do the actual transformations unless I'm feeling lazy.
And then I'll just use that.

[17:41] szabgab:
Okay, that's great, I think we are getting quite close to the time, we are almost 20 minutes already.

[17:50] tom:
Wow, okay.

[17:53] szabgab:
Talking about it, while we were thinking about that we will only have ten minutes or so, so that is interesting. That is interesting, hearing about it. Do you have any other thing that we haven't talked about that you would like to tell people how to contribute or how to get involved?

[18:17] tom:
So contributions are always welcome.
I actually get quite excited when somebody files an issue cause it means that I've got something to do.
I was a little bit upset that I kind of finished, so to speak, I didn't have anything left to do on it.
So just raising issues is the simplest way to contribute, people who've got pull requests or suggestions for enhancements or things like that, I'll always consider them all.
There's a small contributing doc in the root of the repository, the gist of which is just basically, run the tests, use Go format, run the linters, and then issue a pull request, and I'll have a look at it. And yeah.

[19:05] szabgab:
Okay, so I think that's it. Thank you for coming on the show and I hope many people will start using gron, many more people, and that you have more ideas to have others.

[19:19] tom:
All right, thank you for having me on.

[19:20] szabgab:
Thank you, bye bye.

[19:21] tom:
Sorry for talking too much, bye.

[/transcript]

<!--

## Technical info

Recorded on 3 September 2016 with "Ecamm Network Call Recorder for Skype v2.6.1" using the following settings:

<pre>
QuickTime Options:
  Audio Encoding: Uncompressed
  Video Quality: High
  Video Image Size: 854 x 480 (Wide)
  Video Frame Rate: Maxium

Recoding Option:
  Record Video: Multi-track
</pre>

-->
