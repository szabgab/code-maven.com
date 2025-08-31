---
title: "CMOS #13: Trung Đinh Quang on GitHub Explorer - a progressive web app"
timestamp: 2016-10-03T22:01:01
tags:
  - podcast
  - progressive
  - CSS
  - JavaScript
  - Windows 7
  - Vietnam
description: "About GitHub Explorer and build a web site that looks like a Windows 7 desktop."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-13-trung-dinh-quang.mp3
  size: 15891910
  time: 17:26
img: /img/cmos/trung-dinh-quang.jpg
alt: Trung Đinh Quang
published: true
author: szabgab
archive: true
---


Interview with [Trung Đinh Quang](http://dinhquangtrung.net/) from Vietnam
is talking about [GitHub Explorer](https://github-e.com/) his showcase for progressive
web app and the [Windows 7 clone](http://dinhquangtrung.net/).


{% youtube id="HzF_BZeo-cg" file="cmos-13-trung-dinh-quang" %}

<podcast>

<div id="person">
  <h2>Trung Đinh Quang</h2>
  <ul>
    <li>[Trung Đinh Quang](http://dinhquangtrung.net/)</li>
    <li>[GitHub](https://github.com/trungdq88)</li>
    <li>[Twitter](https://twitter.com/trungdq88)</li>
  </ul>
</div>

<div id="links">
  <h2>Links</h2>
  <ul>
    <li>[Single-page applications](https://en.wikipedia.org/wiki/Single-page_application)</li>
    <li>[GitHub Explorer](https://github.com/trungdq88/github-explorer)</li>
    <li>[Progressive Web Apps](https://en.wikipedia.org/wiki/Progressive_web_app)</li>
    <li>[Website code on GitHub](https://github.com/trungdq88/dinhquangtrung.net)</li>
    <li>[Public Talks - GitHub](https://github.com/trungdq88/public-speaks)</li>
  </ul>
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [trung guest1 Trung Đinh Quang]

  [00:02] szabgab: 
Hello there, this is the CMOS, the Code Maven Open Source podcast and video interview series, I'm your host, Gabor Szabo, and with me is [Trung Đinh Quang](http://dinhquangtrung.net/). 
Hello there!

[00:15] trung: 
Hi.

[00:17] szabgab: 
Have I pronounced your name properly or could you...?

[00:20] trung: 
Yeah, it's correct, Trung Đinh Quang, yeah.

[00:23] szabgab: 
Okay, great.

[00:24] trung: 
You can call me Trung for short.

[00:25] szabgab: 
Okay, great, thank you. 
So, it's really nice to meet you, I understand that you're in some kind of a coffee shop right now, or...? 
Place where you work...?

[00:36] trung: 
Yeah, I'm in a coffee shop.

[00:39] szabgab: 
Okay, good. 
Is that a place where you work at?

[00:45] trung: 
This is actually my company because the company has the coffee shop for the employee to work, if they want to, or sit in the coffee shop if they want to, instead of in the office. 
Yeah, so I kind of spend eight hours a day, in this place. 
And the condition is quite good here, so it's no problem.

[01:04] szabgab: 
Oh, so you prefer to sit there instead of in the office, right?

[01:08] trung: 
Yeah, the company is quite open on the place to work, I can even work at home, but I think it's better to come to work at the coffee shop and meet people and have a better condition, yeah.

[01:23] szabgab: 
Okay, so what kinds of things do you do, at this company?

[01:28] trung: 
Let's see, at the company, I do web engineering, so a lot of stuff about development and web technologies, [single-page applications](https://en.wikipedia.org/wiki/Single-page_application), those things. 
I also do lots of R&D development, which is, I find new technologies, new stuff, to bring in, and then sharing the knowledge back to the company. 
That's what I do in my company.

[01:57] szabgab: 
Oh, that's interesting. 
So do you give presentations or how do you do this sharing?

[02:03] trung: 
We have internal sharing systems and the external as well. 
So I will find new technologies to learn about and then we do a small session, in total a one hour session, and all the employees get in and share and stuff. 
But the last session, I was talking about web artistry. 
So the next thing will be, I don't know, maybe [Angular 2](http://angularjs.blogspot.com/2016/09/angular2-final.html), you know Anglular 2 just released yesterday, it's interesting.

[02:39] szabgab: 
Okay, so you're talking about these subjects within the company, right?

[02:45] trung: 
Yeah, new technology.

[02:47] szabgab: 
How did you get into programming? 
Or high tech or, I don't know how to define this, where you are?

[02:54] trung: 
I got a lot of interest going in computers when I was very young. 
I started working when I was 15, back then I was using [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic) to write Window applications, so some fun projects. 
And then I got into the [.NET framework](https://en.wikipedia.org/wiki/.NET_Framework), the Microsoft technologies and just three years ago, I started to work on web development heavily, with [Restive](http://www.restivejs.com/) single-page web applications, and web technology with a lot of cool stuff on the Google technologies, and simple [React from Facebook](https://facebook.github.io/react/) and [Angular](https://angular.io/), and a lot of framework and libraries in the web development.

[03:46] szabgab: 
So you mostly do front-end development, right? 
Do you also do back-end?

[03:50] trung: 
Yeah, I used to, when I was still doing back-end, I used a [PSP](https://en.wikipedia.org/wiki/Personal_software_process) developer, but mostly I am more interested in front-end development.

[04:02] szabgab: 
Okay, I see. 
So I saw, at least one project on [your GitHub](https://github.com/trungdq88), the [GitHub Explorer](https://github.com/trungdq88/github-explorer), that's how I found you, I think.

[04:15] trung: 
Yeah, you found me with [GitHub Explorer](https://github.com/trungdq88/github-explorer)?

[04:20] szabgab: 
I don't remember.

[04:21] trung: 
Okay.

[04:22] szabgab: 
Maybe I was just browsing GitHub itself, and then I somehow bumped into your name and the project? 
Interesting, tell me about it?

[04:33] trung: 
The project was an experiment on the [progressive web app](https://en.wikipedia.org/wiki/Progressive_web_app) technologies, have you ever heard about that?

[04:41] szabgab: 
Well not really, I heard about progressive web app, but I don't really know what that means.

[04:47] trung: 
Yeah, so the progressive web apps is a new kind of the way to build applications. 
You don't have to build native application for every kind of applications. 
So now, progressive web app is a way to build app, to have native experience in it, it performs very fast, it can send you push notifications, it can work offline, and a lot of cool stuff, you'll look at that later. 
And [GitHub Explorer](https://github-e.com/) is one of the experiments that I have built and that one is particularly took a lot of invention from the community, which is why you found it on GitHub, right? 
So the main reason, the purpose of the project is, I want to demonstrate how a web application can perform as well as a native application. 
So if you go to the [GitHub-e.com](https://github-e.com), on your mobile browser, and you start to touch anywhere, you can see the animation and the transition of the pages, as very, very well. 
I have started it on my three-years old phone, which is a kind of low-budget phone, and I think that phone is not compatible to the native applications, so that's what's the purpose of the project. 

[06:23] szabgab: 
So that you say that it's mostly interesting to view using a phone? 
Or some kind of a mobile device? 
Not so much a desktop.

[06:33] trung: 
Yeah, on this stuff, I haven't built a lay-out for that stuff yet, so if you go with a desktop, the layout will kind of look weird. 
But yeah, you can try to simulate the phone on your browser, to see how it works, or you can use a phone, physical phone, as well.

[06:55] szabgab: Okay.

[06:56] trung: 
The progressive web app now is working very well on Android and you can use some advanced features like, at your home screen, working offline. 
You can open the app without connection. 
So, that's a lot of conditions I have put in.

[07:17] szabgab: 
I see, so is this still under development? 
Or do you add more features?

[07:24] trung: 
Right now, it's not actively developed any more, because I got interested in some other projects, and I think I finished the purpose of the project, which is I wanted to demonstate how the web app can animate very fast and perform very well on mobile devices. 
So I think I have finished that. 
And the next one, I want to build something else, to use more features in the progressive web app. 
The GitHub however, they don't have features like push notification, so maybe I'm trying to build something else with the progressive web app.

[08:17] szabgab: 
Do you have a specific idea, what you're going to build?

[08:22] trung: 
Well, yes, several but I'm still choosing for, but one thing it has to demonstate all the stuff from the progressive web app and it has to be useful as well. 
The GitHub Explorer, it can demonstrate something, but if you look at my app, you can see that it's not very useful, because the GitHub as well, they have their mobile layout for the mobile devices. 
So yeah, it's kind of more a demonstration, and I want to build something more useful. 
So it's going to take time for that.

[09:10] szabgab: 
You might build something and then sell it to the company? 
For whose web site you build it, right?

[09:22] trung: 
You mean the new company, for the website, for the idea?

[09:25] szabgab: 
Yeah, so if GitHub didn't have its own UI for mobile, then they would want to take yours, right?

[09:38] trung: 
I think that would be the case, too, but right now they do have mobile layouts for mobile devices but it's not progressive. 
It cannot work offline or cannot send main notification when I have a new pull-request, it's very simple. 
So yeah, maybe I don't know, maybe they will contact me for, or some other guy, to make a progressive web app version of their mobile layout, I don't know. 
But that could be the case.

[10:09] szabgab: 
That would be interesting, I think so. 
Okay, so I also saw your [own website](http://dinhquangtrung.net/), which was really surprising when I visited it, because it has Windows. 
It basically looks like a Windows desktop was running in my browser. 
So what's that about?

[10:33] trung: 
Yeah, that was my very old project, from two or three years ago, when I got bored. 
In the time, I was learning CSS and trying to emulate some fancy design from a famous designer. 
And nothing, whenever I make a version of my Windows 7, that was the system I was using at the time, and I was trying to build that with pure CSS and JavaScript, and when I got the interface done, I thought maybe we could try to make that work, as well. 
And then, if we can spend more time, we can build that into some kind of cloud-computing, cloud operating system, where everyone can log in and feel like they are using their own PC, on the web. 
So that was kind of interesting, but I wasn't have enough time to do all of that, and with the technology, and I think I can't finish that at the time. 

So it was stopped at the stage where I passed my interest in stuff on the website and it's become more like my portfolio website, where I put my small contributions, as you see. 
If you take a look at the [Counter Strike Game](http://dinhquangtrung.net/game/cstrike/) in there, in that Windows, because I tried to build the whole ecosystem for the apps, and yeah, it stopped right there. 
Right now, I don't want to actively develop that any more.

[12:23] szabgab: 
Okay, and is that open source? 
Can we find it on GitHub?

[12:28] trung: 
Yeah, it's a [project on my GitHub](https://github.com/trungdq88/dinhquangtrung.net), as well.

[12:32] szabgab: 
Okay, that's great.

[12:34] trung: 
I can send you a link later. 
The problem with this project is I tried not to use any framework or library, everything was written in Vanilla JavaScript, which right now, I wouldn't say that it's a good idea. 
Because if I'm going to build that right now, I'm going to use React or other single-page application framework, Angular 2 maybe, but yeah, that website wasn't using any other libraries or...I think that's one reason why it took me so long to finish and the source code is not very well-structured, as well, I was learning JavaScript with OOP from a book, and that's what I was experimenting with it. 
It was kind of fun to work on and I was happy when people went into my website and see that and they are suprised, <q>What is this? Is this a real Windows?</q> 
Because it's not, you know.

[13:48] szabgab: 
Yeah, but it really looks real and...

[13:52] trung: 
Yeah, I try my best to make it look very real.

[13:56] szabgab: 
You might want to add this [Blue Screen of Death](https://en.wikipedia.org/wiki/Blue_Screen_of_Death) once in awhile?

[14:04] trung: 
Yeah, maybe. 
Instead of throwing out exceptions, you show a Blue Screen, yeah. 
Just an idea.

[14:14] szabgab: 
Anyway, do you have other projects that you might want to talk about?

[14:20] trung: 
Let me see. 
Besides of writing code, I'm actively working on, sharing in the community, in Vietnam, I come from Vietnam, we have technology events like [Barcamp](http://www.barcampsaigon.org/), [TechCon](http://2017.vietnamtechconference.org/) for our university, and [Free Code Camp](https://www.freecodecamp.com/), which is popular in the world, too. 
And I got a lot of sharing in those events, which sharing knowledge about technology is, it's what I do in my company, so yeah, that's an interesting thing I want to do.

[15:06] szabgab: 
Do you have a lot of these meet-ups or community things in Vietnam?

[15:14] trung: 
I have just graduated one year ago, so I started to join in meet-ups and events from one year ago and from now, let me remember, I gave out about [six or seven talks](https://github.com/trungdq88/public-speaks) about web technologies in the community, and doing open source. 
That's not very much, but I'm keen to do it more in the future.

[15:49] szabgab: 
Well, that's great. 
As a closing question, I would want to.. Do you have any suggestions to people who want to get into open source or programming, especially people from Vietnam?

[16:07] trung: 
I talk about that a lot at the events, where I got a lot of people who are at the medium level. 
So one resource, I went a long ways trying to share with them, is [Free Code Camp](https://www.freecodecamp.com/) website. 
They have a well-designed, well-structured tutorial in open source, especially for front-end development and I think it's a good resource. 
And for open source projects, GitHub is the way to go, and one thing people want to put their foot into the community, is to join the events and meet-ups and do open source a lot, so they can share and learn more about the web development as well.

[17:09] szabgab: 
Okay, that was great. 
Thank you for coming on the show and sharing with me and the audience, all this.

[17:20] trung: 
Yeah, thank you for having me.

[17:22] szabgab: 
Thank you and bye bye!

[17:25] trung: 
See you, bye!

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
