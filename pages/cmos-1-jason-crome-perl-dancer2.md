---
title: "CMOS #1: Jason Crome on Perl Dancer 2"
timestamp: 2016-08-23T19:01:01
tags:
  - podcast
  - Perl
  - Dancer
  - web
  - USA
description: "Interview with Jason Crome about the Perl Dancer web framework and how they handled the fine art of changes while providing backward compatibility."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-1-jason-crome-perl-dancer2.mp3
  size: 13879747
  time: 16:09
published: true
author: szabgab
#img: img/cmos/jason_crome.png
#alt: Jason Crome
archive: true
---


Interview with Jason A. Crome one of the core developers of the [Perl Dancer](http://perldancer.org/) web framework. We talked about how he got involved in the project and how they handled the upgrade process from Dancer 1 to Dancer 2 to avoid breaking any of the plugins.


{% youtube id="uVCpubfC9L4" file="cmos-1-jason-crome-perl-dancer2.mp4" %}

<podcast>


<div id="person">
## Jason A. Crome
* [Jason A. Crome](https://www.crome-plated.com/)
* [PAUSE](https://metacpan.org/author/CROMEDOME)
* [@cromedome](https://twitter.com/cromedome)
* [GitHub](https://github.com/cromedome)
</div>

<div id="links">
## Links
* [All Around the World](http://www.allaroundtheworld.fr/)
* [Massively Multiplayer Online Game (MMORPG)](https://en.wikipedia.org/wiki/Massively_multiplayer_online_role-playing_game)
* [Booking.com](http://booking.com/)
* [perldancer.org](http://perldancer.org/)
* [irc.perl.org](http://irc.perl.org)
* [GitHub for Perl Dancer](https://github.com/PerlDancer/)
* [Perl Dancer conference](https://www.perl.dance/)
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [cromedome guest1 Jason A. Crome]

  [0:00] szabgab:
    Hello!
    This is Gabor Szabo with the first episode of the Code Maven news podcast and screencast and interview project, and with me is [Jason A. Crome](https://www.crome-plated.com/), who is going to talk about the Perl Dancer project.

    Hi Jason, how are you?

  [0:20] cromedome:
    Hi! Thanks for having me here today. I am doing great.

  [0:26] szabgab:
    I hope it's going to be good. This is the first interview in this format. Let's get started, tell me a little bit about yourself.

  [0:30] cromedome:
    Okay, let's see, I've been programming professionally for probably about the last 20 years. The last 18 or so I've spent, I've started a technology company with some others in the United States, and we were writing software for the local government, here in the States.

    Last year, I've retired from that, and I've been active off and on in the Perl community for a number of years and when I decided to get back to work last fall, one of the things I've gravitated towards was the Dancer project, something that I've used a little bit in the past.

    Eventually they had me join their team, and I've been doing a lot with that. In November I got hired on by [All Around the World](http://www.allaroundtheworld.fr/), a consulting firm out of France. There I am the technical lead on a project called Veure, which is a [Massively Multiplayer Online Game (MMORPG)](https://en.wikipedia.org/wiki/Massively_multiplayer_online_role-playing_game) written in Perl.

  [1:43] szabgab:
    Nice.

  [1:46] cromedome:
    I spend a lot of time in Perl these days.

  [1:49] szabgab:
    Okay, and is it using Dancer for this project or something else?

  [1:54] cromedome:
    Unrelated to Dancer, but there is a lot of overlap with the technologies I use in that project that I use in other aspects of my life.  I try to use a little bit of Dancer here and there at my day job when I can. Dancer is really personally a passion of mine.

  [2:18] szabgab:
    Tell me about Dancer. What is Dancer?

  [2:26] cromedome:
    My involvement in Dancer is funny actually. Back in [2012 YAPC in Madison, Wisconsin, USA](http://2012.yapcna.org/) I was looking for a new web framework. 
    
    The one that I've been using kind of died out and I sat in a couple of talks and Sawyer, one of the project leads, he is a very engaging speaker and he had a [really good talk about what Dancer was about](https://www.youtube.com/watch?v=2A6ZRZj_MEu4). It really fit the way that I've worked and I submitted a couple of pull-requests to them that got incorporated. I really didn't get back to it until last fall and a project I was using used Dancer, and as I started to run into issues with docs and a coouple of bugs I've noticed, I've started to send in pull-requests and Sawyer contacted me and said, "You know if you keep doing this, then we are going to have to assimilate you into the core team," and a little bit later that's actually what happened.

    But what Dancer is, it is a framework for building web applications. For those of you who are familiar with Perl, Perl has this great saying that "Making Easy Things Easy and Hard Things Possible." 
That's really a philosophy that the Dancer framework has stuck with. If you want to build a web app and get up and running quickly, then Dancer is a great framework to do it with.

    If you've never done web programming, if you've never done Perl programming actually, it's a really nice entry point into the Perl ecosystem. If you are an experienced Perl programmer, you are not going to be disappointed either, because all of the power and flexibility that the Perl ecosystem allows you, you can channel that into your Dancer applications. 
    You can make really large and elaborate web applications pretty easily. The framework takes care of a lot of things most of the web programmers don't want to think about all the time. It does those things really easily. Either through the core of the framework or through the number of plugins that it offers. It just does what you need it to and it kind of stays out of your way, it's great.

  [4:58] szabgab:
    Okay. I understand that there is something called Dancer and Dancer 2. Are these two versions? What is the relationship between them? Are you using the new one?

  [5:10] cromedome:
    Personally my involvement is almost exclusively with Dancer 2. The history behind these is that Dancer started out as a smaller project by our project founder, Alexis ([Alexis Sukrieh](https://twitter.com/sukria)). I don't know if he quite had the vision, at the time when he created Dancer, that it was going to be as wildly successful as it was. 
    It was not really architected with that kind of growth in mind, so when he started to get more elaborate applications there were some things that would shoot you in the foot a little bit. And so the Dancer 2 project was started, from the ground up, to address these concerns. 
    It took a couple of years of development, but early in the middle of last year it hit critical mass, for a lack of a better term, and it was pretty feature equivalent to what Dancer 1 had at that point, with the exception being the plugin ecosystem. Which is what we have spent most of 2016 addressing, actually.

  [6:38] szabgab:
    Okay, so what kinds of plugins are there, that are mostly used or that you use or are recommended or, I don't know...?

  [6:50] cromedome:
    My favorite plugins personally...
    There is a variety of plugins for everything, there is templating plugins, there is session and state management, there are plugins for MongoDB, for Redis, for Memcached, there are plugins available for generating Captcha images, there is authorization frameworks.

    The core of the framework is actually pretty minimalistic. It lets you say, if visitors come to my application and they visit this URL, this is what I am going to present them with, or this is the code that will happen. A lot of the additional magic happens in the plugin ecosystem. Dancer knows how to talk to a templating engine, but other then a very simple templating engine that we have out of the box, all the rest of the templating functionality is provided through plugins. I use a templating framework called Template::Toolkit. I've been using it for years and I am very familiar with it and that functionality is provided through a plugin.

    I use [Redis](http://redis.io/) a lot for caching. We have both a generic Redis plugin that accesses the functionality of Redis, we actually have a session plugin that stores your application state information in Redis, just like it would with any of the other session engines in files or whatever. 

    There is a lot out there. One of the things that you could do with Dancer 1 that you couldn't do in Dancer 2 was plugins that use functionality provided by other plugins and this was kind of a blocker for some people who wanted to move from Dancer 1 to Dancer 2. Actually the code for plugin 2 was done a long time ago, but one of our project focuses is on stability.

  [9:18] szabgab:
Can you repeat...? 

  [9:22] cromedome:
    Plugin 2 was actually done very early in 2016, but one of our key focuses is stability and not breaking production code. So just releasing plugin 2 with a lot of breaking changes, wasn't going to work for us.

    So a couple of our developers, [Peter Mottram](https://metacpan.org/author/SYSPETE) specifically, took on the lion share of it, syspete as he is known in the Perl community.

    He individually tested every plugin in the Dancer ecosystem with the new plugin 2. Figured out what broke and if we had access to those plugins, then we fixed them, and if they were written by somebody else, we actually sent pull-requests to the ones we did not control. So that we knew, out of the gate, that the whole plugin ecosystem would function with our new plugin architecture.

    It was kind of funny, there were still a couple of them that we could not patch, so we even spent some time building a compatibility layer, so that the Dancer 1 plugins could still use plugin 2  with no syntactic changes. Stability and not breaking other peoples code, is very important to us.

  [10:57] szabgab:
    Yeah, It's a known problem, that moving forward and staying backward compatible, is not compatible with each other, and then you have to make a decision at one point, that you more or less stop your progress, I guess. You can move much slower in order to maintain backward compatibility.

    Okay, so what kind of project do you know that exist, that are using Dancer, that you can point out?

  [11:37] cromedome:
    The Perl Dancer conference web site is a piece of software for managing the conference registration and that's one application written in Dancer. There is a blog engine called [PearlBee](http://pearlbee.org/) that was release last year, earlier this year, that is based on Dancer as well. In fact the [Perl community's blog site](http://blogs.perl.org/) is in the middle of being transitioned over to this. I know [Booking.com](http://booking.com/), which is a huge sponsor and hugely involved in the Perl community, has changed some of their blogging tools over to PearlBee as well.

    I can think of a lot of companies that are using Dancer in their applications and behind the scenes, but as far as canned software packages like wikis and blogs, I never see a whole lot of those coming out of the Perl community. It always seems like we are focused on getting other jobs done.

  [12:50] szabgab:
    Yeah, I understand. So I think more or less a closing question here, actually a couple of closing questions. I think I have.

  [13:05] cromedome:
    Sure.

  [13:06] szabgab:
    One of them is if someone wants to get involved in using Dancer or even want to contribute. Where do these people need to go? How can they find you?

  [13:21] cromedome:
    The easiest place to start would be our web site [perldancer.org](http://perldancer.org/), we have an IRC channel at [irc.perl.org](http://irc.perl.org) just come to #dancer and we're there. It is a very friendly community, it is a very beginner friendly we have a very beginner friendly code of conduct, and we don't tolerate abuse of new people.

    We are also on GitHub, if you look on [GitHub for Perl Dancer](https://github.com/PerlDancer/) all the plugins and the actual source code of Dancer can be found there. 
    Our issues, our open tickets are managed at GitHub and we have a lot of tickets out there that are marked as beginner friendly or up for grabs. 
    Anybody who wants to contribute to Dancer, write a plugin, send us a documentation patch, look for one of the beginner friendly tickets. 
    It is a very eassy project to get involved in. It is a very easy to follow codebase. It is a very thriving and happy community of people. It is one of the things that drew me to Dancer over so many of the other open source projects, is that we really have a great community.

  [14:46] szabgab:
    Thanks, that's great input, I hope that some people will join you. Do you have any other things to add that we have not talked about that you'd like to add?

  [14:57] cromedome:
    Yeah actually the [Perl Dancer conference](https://www.perl.dance/) is coming up next month at the end of September in Vienna, Austria. Not only it is a great time to come to Vienna, but it is a great time for both beginning and experienced Dancer programmers, to come and find some great things about Dancer, learn about things that we have in the works, get to hack on Dancer with some of your peers, and just hang out and enjoy time in Austria.

  [15:30] szabgab:
     It's a pretty long flight from the U.S. to Vienna. Are you going to be there?

  [15:37] cromedome:
     Yes, I am.

  [15:38] szabgab:
    That's great. So if anyone wants to meet Jason at the Dancer conference in Vienna, we put links in the show-notes for the conference and for the other things you have mentioned. 
So thank you very much for coming on the show and I hope that in a couple of month, we can catch up again with some updates, new releases, new information about the project. Thank you very much.

  [16:06] cromedome:
    Thank you. Thanks for having me.

  [16:07] szabgab:
    Bye bye.

  [16:08] cromedome:
    Bye.

[/transcript]


<!--
## Technical info

Recorded on 17 August 2016 with "Ecamm Network Call Recorder for Skype v2.6.1" using the following settings:

<pre>
QuickTime Options:
  Audio Encoding: Uncompressed
  Video Quality: High
  Video Image Size: 854 x 480 (Wide)
  Video Frame Rate: Maxium

Recoding Option:
  Record Video: Multi-track
</pre>

There are a couple of places where we had a lot of dropped frames
and by the end of the recording the noise from the ventilator of my computer became pretty disturbing.
-->
