---
title: "CMOS #10: Michael Kennedy - Talk Python To Me"
timestamp: 2016-09-23T20:01:01
tags:
  - podcast
  - Scrapy
  - passlib
  - hypothesis
  - Pyjithon
  - sqlalchemy
  - USA
description: "Interview with Michael Kennedy about several Python project that were discussed on his podcast: Talk Python To Me"
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-10-michael-kennedy.mp3
  size: 44576759
  time: 18:34
#img: /img/cmos/michael_kennedy.jpg
#alt: Michael Kennedy
published: true
author: szabgab
archive: true
---


Interview with [Michael Kennedy](https://blog.michaelckennedy.net/), the host of the
[Talk Python To Me](https://talkpython.fm/) podcast and the author of several
[Talk Python Training courses](https://training.talkpython.fm/).

We talked about a number of project that were discussed on his show: Scrapy, passlib, hypothesis, Pyjithon, and sqlalchemy.


{% youtube id="6cmmK7Gsr7A" file="cmos-10-michael-kennedy" %}

<podcast>

## Michael Kennedy

* [Michael Kennedy](https://blog.michaelckennedy.net/)
* [GitHub](https://github.com/mikeckennedy)
* [Twitter: @mkennedy](https://twitter.com/mkennedy)
* [Talk Python To Me](https://talkpython.fm/)
* [transcripts](https://github.com/mikeckennedy/talk-python-transcripts)
* [Talk Python Training courses](https://training.talkpython.fm/)

## Links

Three courses, via kickstarter:
* [Python Jumpstart by Building 10 Apps](https://talkpython.fm/course)
* [Write Pythonic Code Like a Seasoned Developer](https://talkpython.fm/pythonic)
* [Python for Entrepreneurs](https://talkpython.fm/launch)

The projects mentioned on he podcast
* [Scrapy](https://github.com/scrapy/scrapy)
* [passlib](https://bitbucket.org/ecollins/passlib/wiki/Home)
* [HypothesisWorks / hypothesis-python](https://hypothesis.readthedocs.io/en/latest/)
* [Episode #67 on hypothesis](https://talkpython.fm/episodes/show/67/property-based-testing-with-hypothesis)
* [Microsoft / pyjion](https://github.com/Microsoft/Pyjion)
* [Episode #49 on Pyjiton](https://talkpython.fm/episodes/show/49/microsoft-s-jit-based-python-project-pyjion)
* [sqlalchemy](http://www.sqlalchemy.org/)
* [Episode #5 on sqlalchemy](https://talkpython.fm/episodes/show/5/sqlalchemy-and-data-access-in-python)


[transcript]
  [szabgab host1 Gabor Szabo]
  [michael guest1 Michael Kennedy]

  [00:03] szabgab: 
Hi there, you are welcome to the CMOS, the Code Maven Open Source interview series and podcast. 
I'm your host, Gabor Szabo, and with me is [Michael Kennedy](https://blog.michaelckennedy.net/). 
Hi Michael!

[00:18] michael: 
Hey, guys! 
Hey Gabor, thank you so much for having me, it's great to be here.

[00:21] szabgab: 
It's great to have you! 
You have a great podcast, and you have all sorts of open source experience, and I really would like to hear about all of these, but let's start with introducing you?

[00:36] michael: 
Yeah, I'd be happy to. 
So, those of you who don't know me, my name is Michael Kennedy, like you said. 
Probably the biggest thing I'm doing out in the community, is running the [Talk Python To Me](https://talkpython.fm/) podcast, which is the number one Python podcast, most popular podcast, covering all sorts of stuff that somehow intersects with Python. 
So sometimes it's looking inside, like the [Flask](http://flask.pocoo.org/) web app framework, but other times, it's talking to people at [CERN](https://home.cern/), about how they're using Python to find the Higgs boson and stuff like that.

[01:07] szabgab: 
That's great but let's go further to your history. 
So how did you get into Python?

[01:14] michael: 
Yeah, absolutely. 
So I consider myself an accidental programmer. 
I know lots of people like me. 
So I was working on my PhD in math, working on Silicon Graphics supercomputers, trying to solve math simulations. 
And I ended up getting into C++, and OpenGL, and 3D work around there, and I realized, after about a year of that, <q>Hey, this programming stuff is way more fun than math!</q> 
So I sort of, after a little while, stopped pursuing math and just went into programming, and I've been doing programming for about 20 years. 
And just everyday, I think, I wake up and, <q>Wow, today is even more amazing than the world was yesterday!</q> 
It's just so exciting to be in this industry and I've done a ton of different types of programming, and like I said, Silicon Graphics, C++, C#, JavaScript, and really Python, the last four or five years.

[02:10] szabgab: 
Okay, so four or five years Python. 
That's actually not a lot?

[02:14] michael:  
Yeah, no it's not that much. 
It's odd that I would be one of the more-visible voices in the community, given that I've only been doing it for that long. 
But when I created my podcast, there were zero Python podcasts. 
There had been some good ones, but they all stopped for whatever reason, and there's a year and a half with no Python podcasts. 
And I thought, <q>Well, if I can't listen to one, that's cool, I want these stories to exist, maybe I'll just have to make it myself.</q> 
So I did and the community has been so supportive, and they really seem to appreciate the conversations and the people I have on the show. 
I mean, my show is all about the guests, I try to not make it about me. 
So it's just finding interesting people and projects, and talk about it.

[02:55] szabgab: 
Yeah, so if I recall, somewhere I heard that you are actually turning it into a real business?

[03:03] michael: 
Oh, yeah, so that's an interesting aspect, and I think that that touches on why some of the other podcasts failed. 
As you know, it is a tremendous amount of work to continuously schedule, and produce, and research, the shows, and I had the chance, at the beginning of this year, back in February, a little bit before then, I had more and more ad sponsorships coming on my show. 
I had sold out the ads for all of 2016 and it was, it turned out to be enough revenue that I could use it as a base, to sort of build other projects and what-not. 
And I decided, <q>Go do something amazing, and try to make this my full-time job.</q> 
So in February, I made my podcast my full-time job, and I've been building online courses that go deeper into some of the topics we cover on the podcast, for people. 
And I've done that mostly through Kickstarter, but also through my online [website](https://blog.michaelckennedy.net/).

[04:03] szabgab: 
Okay, so do people buy these podcasts? 
Because I understand some people pre-paid, basically, through Kickstarter, and then other people can just go and buy later on?

[04:17] michael: 
Yeah, exactly, you can go buy everything that was on Kickstarter, it just costs more because I have a pre-paid discount, if you were on Kickstarter. 
To be clear, the podcast is totally free. 
But the courses, the courses that I, you know each course that I produce, I spend probably two full months, full-time, producing it. 
It's a production to put it together. 
I try to create really nice things that don't waste people's time, that are fun, that people can learn from. 
So far the feedback's been really amazing.

[04:46] szabgab: 
Yeah, I know, creating a training course is pretty difficult. 
I do classroom trainings in a couple of subjects, and it's a lot of time to prepare a training. 
A lot longer than giving the training.

[05:01] michael: 
That's for sure. 
But it's super-rewarding, I'm really enjoying it, and my plan for the next few years at least, is to keep doing the podcasts, keep building these online courses, and just try to grow this whole community around Python.

[05:15] szabgab: 
Okay, so let's start and talk a little bit about the open source projects. 
Either those that you're involved in and/or those that you talk about on your shows.
So there are a couple of interesting ones, and I would really like to hear about them.

[05:32] michael: 
Yeah, absolutely. 
So, on the podcast, almost every week I talk to somebody that is doing something cool with open source. 
It may be half the time, they're consuming open source, so I might talk to somebody at Netflix about how they're using existing open source libraries, to manage the cloud-computing infrastructure that they have. 
But other times, it's about people who are doing amazing stuff. 

So it's really cool to see both sides and another component that I'd like to throw in there, I think that fascinates me the most, because it really bodes well for open source, is talking to the people who have companies, that are built upon open source projects. 
And just the amazing stuff that they're doing. 

So an example that really surprised me, was this open source library called [Scrapy](https://github.com/scrapy/scrapy). 
So Scrapy is a screen-scraping library for Python, and you can go in and say, suppose you want to go to some kind of website, they don't have an API but the data is clearly accessible with a CSS selector, as most data is. 
You can go in and basically turn that webpage into an API with the Scrapy library. 
I thought, <q>Okay, that's cool,</q> and I talked to probably the guy who created it, and he said, <q>Now what we're doing is, we create a business around this open source library.</q> 
Now if I had to ask you, how would you create a business around an open source library that does web-scraping? 
It's great that it's popular, maybe consulting, maybe training, but it's not really too much of that. 
What they're doing is they created web-scraping as a service. 
So they have all this infrastructure and the re-tryability, and the bandwidth, and the parallelism, to massively scrape the web with their API that you already know, and they sell basically, like AWS sells infrastructure and so on, they sell the ability to do web-scraping. 

And I think those combinations of open source projects are the most amazing, because you know that open source project is going to be really vibrant, and really well-maintained, because there's a whole business around it. 
They have 130 people work in their company, that does that.

[07:52] szabgab: 
Wow, that's great.

[07:53] michael: 
That really surprised me, when I heard that, but I'm really happy for them, and that's great and so, I picked out a couple that people talk about on my show, that I thought were really cool. 
My favorite one to talk about is this one called [Passlib](https://bitbucket.org/ecollins/passlib/wiki/Home), because day after day we hear about all of these companies that make major security mistakes around their web apps. 
If you have a web app either for your own company, your side project, or for the business that you work for, and it gets hacked, like these things do where the database gets leaked. 
Not even necessarily through your app, like the [Patreon](https://www.patreon.com/) guys got <q>hacked,</q> their site got hacked because somebody left a development server up and running, and the server itself was not properly secured. 
It was not that there was any vulnerability in the code, it's just woops, the testing server was improperly secured. 
And so if somebody gets hold of your code, that's not good. 
Right, it's not good if they get hold of your data, but Passlib, what it does, is it employs all the best practices to automatically use the right hashing for one-way encryption on your code. 
It uses folding and salt, so it doesn't just hash your password once with some salt, it actually will do that 50,000 times, so it's computationally expensive to guess it, and then store that result. 
And it does all that stuff automatically. 
So it makes treating user accounts really safely, drop-dead easy, like one or two lines of code. 
So Passlib, I really like that.

[09:27] szabgab: 
So, as I understand, instead of me trying to figure out how to encrypt the passwords that my users, how to hash them, before storing them, and pick the right encryption, and then maybe tomorrow, update them. 
I just use passlib and then I can hopefully rely on that, that it's using the latest recommended number of encryptions.

[09:55] michael: 
No, number of iterations, absolutely. 
Then how do you store the salt, how do you communicate if over time you want to upgrade passwords so they're harder to compute, how do you do...all that stuff is super...it's just not about your business. 
You want to build an app where people can share pictures or whatever, and you're down in the guts of encryption, and you just shouldn't care about that. 
And so Passlib, if you're doing something in Python with accounts, Passlib, it's amazing. 

Another one that I think is really cool, that I actually did a whole show about, is this thing called [Hypothesis](https://hypothesis.readthedocs.io/en/latest/).
 So, have you heard of property-based testing?

[10:29] szabgab: 
A little bit, I think from you, from another podcast perhaps.

[10:33] michael: 
Yeah, perhaps. 
So the idea is, with a traditional unit test, we had to come up with a nomenclature around this, words, and so we called that example-based testing. 
The way people normally write tests, is they say, <q>Here's a test, and if I have this user, and they have this ID, or maybe they're this age, and they try to create an account with this email, something will happen.</q> 
Or, if you tried to purchase this thing for this price, something would happen. 
And you actually set up those numbers and details. 
With Hypothesis, you express things like, <q>I would like to test, with one of the existing users, buying this product, with some number between 0 and 100.</q> 
And it will try all the permutations and variations, and it will seek out and find those little edge cases, where you're off by one or, if you don't say anything, it'll try to buy it for a negative price, and your system should catch that, but if it doesn't... 
There's all sorts of interesting things, so instead of writing these examples, and having one by one cases, you give it the relationships of the data, and it automatically tries a bunch of variations. 
So Hypothesis is amazing for unit testing, really, really nice.

[11:44] szabgab: 
Actually, I remember now, I heard about it in one of the recent meet-ups, in our [local Python meet-up group](http://www.meetup.com/PyWeb-IL/). 
And the funny thing is that, the same idea, or more or less the same idea, I have been...was part of my training course for a long time. 
As an idea, without an actual implementation.

[12:05] michael: 
Right, not necessarily a framework.

[12:06] szabgab: 
No, no.

[12:09] michael: 
This is what you should try, eh?

[12:09]  szabgab: 
So the way I explained, was in order to create these example-based tests that you would normally, you need the domain expert there, not just the programmer. 
And maybe the domain expert is not available or too expensive, so you can create an additional set of, I called it "random tests." and then you can, to a certain level, to a certain extent, you can actually test whether your code works. 
You might not be able to test whether it's properly works, but you can check that it doesn't crash, or doesn't do something like this. 
So I don't know actually if this Hypothesis is, whether it goes further than that, or can it check actually..? 
It can't give you the expected value, right?

[13:01] michael: 
Yes, I think there are ways to check the expected value, but you have to basically compute the expected value or something like that. 
So it's not automatic. 
It will do interesting things, like if you've got to go through a series of steps, it will try the steps in a bunch of different orders, and if it finds an error, it will say, <q>Well, I tried to create an account and then buy something, and that worked and it should have failed because you didn't enter your billing information</q> or whatever. 
It'll go through some pretty advanced stuff, but it's not magic. 
Most of the time, it's just, instead of writing one example test, you might one property-based test and it's really like 100 example tests. 
Yeah, so Hypothesis, that's definitely one of the cool projects that's out there.

Another one that I'd like to point out, because it's probably the stand-out project in this area, but this area is very interesting right now, is this thing called [Pyjion](https://github.com/Microsoft/Pyjion), from Microsoft of all places, for Python. 
And what it is, it is an extension to the main, primary Python runtime or implementation on the [CPython](http://cython.org/) implementation, that adds [JIT](https://en.wikipedia.org/wiki/Just-in-time_compilation) capability, as a general concept. 
So right now Python is an interpretative language, unless you use other implementations, or runtimes like [PyPy](http://pypy.org/), [IronPython](http://ironpython.net/), [Jython](http://www.jython.org/). 
But those all come with drawbacks, <q>Oh you can get this really great performance, like Pypy's five times faster, but you can't use a bunch of the libraries you know.</q> 
Similarly, for IronPython, and so on. 
But this Pyjion thing is basically, instead of forking the implementation and rewriting it, it's trying to create a framework for people to plugin different JIT implementations into the existing one. 
So as a community, everybody can come together and work on making the language faster, without forking it with these trade-offs.

[15:00] szabgab: 
That's interesting, seems like far, far away from the others, that are more like Python-user modules or libraries and this is really for hard-core, right?

[15:12] michael: 
Well, yes, right, you would not be using this. 
But hopefully this is a foundation of things to come, that makes all of the libraries faster. 
But I think it's really interesting because they're saying, <q>We're building this JIT framework and this library to help you implement JITs in C++,</q> and they actually have two implementations of their JIT. 
One is the .NET core framework, which is cross-platform, this new thing from Microsoft, and it has a JIT in it. 
But they're also using the V8 JavaScript compiler as one of the JIT implementations for Python, which is just, they're trying some funky stuff. 
That's a cool project.
But I bring it up because there's all of this, there's lots of work around JIT, and experimentation on how the internals of Python run, right now.
 And this is just one of them, that highlights it.

[16:01] szabgab: 
That's good.  

Anything else?

[16:06] michael: 
Yeah, I've one more that I think everybody should know about, and probably many people do, but if  you're doing anything with relational databases, [SQLAlchemy](http://www.sqlalchemy.org/), is a really great ORM, or object-relational mapper. 
Write a few classes, input your relationships in there, you can put your constraints, like, <q>Here's an email address, I want this indexed, so I can search quickly and I want it to be unique, so I don't get duplicate registrations, if I have to reset by email.</q> 
Things like that. 
So SQLAlchemy, it's great.

[16:34] szabgab: 
So these four projects, basically you mentioned four projects, did you have individual episodes for each project that you discussed? 
Or how...?

[16:44] michael: 
Let's see... no, yes, yes, yes. 
The Passlib, no I have not had those guys on there yet. 
It might be fun to talk to them, I'm not sure that project is big enough to do a whole episode, but to be honest, it probably is. 
But I've had the guys from Hypothesis project on there, I've had Brett Cannon from Microsoft, who's one of the two folks maintaining/working on Pyjion. 
And I had Mike Bayer on for SQLAlchemy. 
SQLAlchemy was <a href="https://talkpython.fm/episodes/show/5/sqlalchemy-and-data-access-in-python">episode 5</A>, so it was an original one. 
Hypothesis, was [episode 67](https://talkpython.fm/episodes/show/67/property-based-testing-with-hypothesis). 
Pyjion was [episode 49](https://talkpython.fm/episodes/show/49/microsoft-s-jit-based-python-project-pyjion).

[17:21] szabgab: 
Well, we'll find it out and we'll put it in the show notes.

[17:23] michael: 
Yeah, yeah, we'll put it in the show notes, absolutely.

[17:24] szabgab: 
So people will have a good reason to go there, right?

[17:28] michael: 
Yeah, very good. 
All those guys have amazing stories and insights, and it's worth checking out. 
And it's nice to talk to them about how they're growing their open source projects and what's working, and so on.

[17:39] szabgab: 
Okay, that's really great and thank you for introducing us to these projects.

[17:45] michael: 
Right, welcome.

[17:46] szabgab: 
Before wrapping this up, do you have anything you would like to tell to the listeners of my small podcast, maybe they would like to be interested in yours?

[17:59] michael: 
Yeah, sure, so I guess the main thing is, if you're interested in these ideas that we're talking about, every week I spend an hour with one of these folks doing amazing stuff, come check it out at [talkpython.fm](https://talkpython.fm/), that's where the podcast is, and you can subscribe or just browse through the episodes, there's a bunch of really interesting and inspiring stuff there, so check it out.

[18:23] szabgab: 
Hopefully many people will. 
Thank you very much for coming on the show. 
And bye bye.

[18:33] michael: 
Gabor, thank you so much. 
Bye everyone.

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

