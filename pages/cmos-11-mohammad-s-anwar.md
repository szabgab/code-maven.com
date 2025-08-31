---
title: "CMOS #11: Mohammad S. Anwar - Contributing to CPAN every single day"
timestamp: 2016-09-26T08:01:01
tags:
  - podcast
  - Perl
  - CPAN
  - UK
  - India
description: "The leader of the daily CPAN contribution quest by far on inspiration and enjoying the contribution."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-11-mohammad-s-anwar.mp3
  size: 21467513
  time: 23:16
#img: /img/cmos/mohammad_anwar.jpg
#alt: Mohammad S. Anwar
published: true
author: szabgab
archive: true
---


Interview with [Mohammad Anwar](http://www.manwar.org/) on his contribution
to CPAN. Mohammad has released a Perl module to CPAN every single day in the last 699 day
and he still going strong.

Hear him talk about the inspiration.


{% youtube id="hS0LRP3uwW4" file="cmos-11-mohammad-s-anwar" %}

<podcast>

<div id="person">
  <h2></h2>
  <ul>
    <li>[Mohammad Anwar](http://www.manwar.org/)</li>
    <li>[GitHub](https://github.com/Manwar)</li>
    <li>[CPAN](http://www.cpan.org/authors/id/M/MA/MANWAR/)</li>
    <li>[Twitter: @cpan_author](https://twitter.com/cpan_author)</li>
    <li>[LinkedIn](https://uk.linkedin.com/in/mohammadanwar)</li>
  </ul>
</div>

<div id="links">
  <h2>Links</h2>
  <ul>
    <li>[Perl](https://www.perl.org/)</li>
    <li>[Neil Bowers](http://neilb.org/)</li>
    <li>[CPAN](http://www.cpan.org/)</li>
    <li>[Map::Tube::London](https://metacpan.org/pod/Map::Tube::London)</li>
    <li>[Games::Domino](https://metacpan.org/pod/Games::Domino)</li>
    <li>[Calendar::Bahai](https://metacpan.org/pod/Calendar::Bahai)</li>
    <li>[Calendar::Hijri](https://metacpan.org/pod/Calendar::Hijri)</li>
  </ul>
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [manwar guest1 Mohammad S. Anwar]

  [00:02] szabgab: 
Hi there, this is the CMOS, the Code Maven Open Source podcast and video interview series and this is your host, Gabor Szabo, and with me is [Mohammad Anwar](http://www.manwar.org). 
Hi Mohammad!

[00:16] manwar: 
Hi Gabor, how are you?

[00:17] szabgab: 
Fine, really fine, how are you?

[00:19] manwar: 
I'm not too bad, thank you very much for giving me this opportunity.

[00:23] szabgab: 
It's great to have you. 
I passed quite a few Perl modules to you, you took over maintenance of them, so I'm very happy because I didn't really have a lot of time to maintain those.

[00:40] manwar: 
It was my pleasure to be part of this big Perl community.

[00:46] szabgab: 
That's great. 
Let's talk a little bit about your background, your story, how did you get into programming and Perl?

[00:58] manwar: 
Yeah, my background is actually, I'm a science graduate with honors in mathematics, so I wasn't into computer science or anything like that, it was pure science, mathematics with honors. 
I did my graduation in India and then I started playing with [COBOL](https://en.wikipedia.org/wiki/COBOL) language.

[01:22] szabgab: 
COBOL?

[01:24] manwar: 
COBOL,  yes, I started with the COBOL and then moved on to [Pascal](https://en.wikipedia.org/wiki/Pascal_(programming_language)), played with Pascal for a couple of months, and then I got attracted toward the [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic) method, Visual Basic programming with an Oracle database, started with this. 
Then after a couple of years, I moved to Mumbai, where I got the first possibility to work with [Perl](https://www.perl.org/), this was in 98, 99. 
So those days, [CGI](https://en.wikipedia.org/wiki/Common_Gateway_Interface) was in demand, but everybody was using CGI for all the web thing, so yeah, that was my first introduction with Perl. 
And since then, I've been using Perl, so that's how I started with Perl. 
Then I got an offer in London, as a consultant, and I moved from Mumbai to London, and since then I've been here, working for various companies in London, in and around. 
That's how I built the career.

[02:30] szabgab: 
So how is this move from India to London?

[02:35] manwar: 
Honestly speaking, Gabor, it was a big cultural shock and the working culture is so different from India. 
In India, usually people work six days a week, and you start 9:00 in the morning and there's no closing time there, sometimes you work until late, sometimes midnight. 
So when I moved here, it was more organized, I found it and it was a big cultural...first thing I noticed was you only work five days a week here in London! 
So you get more off than in India. 
Also there's no, or you don't need to work more than eight hours a day, so, unless you really wanted yourself, otherwise no one is going to force you, <q>Mohammad, can you stay until 8:00 or 9:00?</q> 
Nobody going to tell you. 
So you come in at 9:00, leave at 5:30, nobody asks any questions. So, yeah. 

And also, for me, English was not my first language, so coming to London was another language barrier for me.  
I had to start from scratch, so to be able to communicate and to be able to understand, what is asked to do. 
I had to understand the language, I had to understand the accent, English accent, is completely new to me. 
And luckily I had a very good people, who I worked under, they were very friendly, very cooperative, and very communicative, so yeah, I was very lucky.

[04:19] szabgab: 
Yeah, I can't say anything about accents, having myself, I guess a really strong one. 
But you definitely don't have the regular Indian accent in English, probably because, I don't know...

[04:35] manwar: 
I've been here for 16 years, nearly, so probably I must have picked up it all here, without realizing it.

[04:43] szabgab: 
Right, okay, so you enjoy being there?

[04:47] manwar: 
I do, honestly speaking, yes, I've had the opportunity to work with very big name, so yeah, very happy, so far.

[04:57] szabgab: 
Great, so how did you get to start to contribute to open source?

[05:05] manwar: 
I remember, in the past, I joined a company called the SpinVox. 
It was a start-up company and their I met [Neil Bowers](http://neilb.org/), you know, Dr. Neil Bowers, and I didn't know him before. 
So when I joined him, I found out about him, that he's a very big name in the Perl community and I had the possibility to work under him. 
I learned a lot from Neil, and I started working, I tried to copy everything that he used to do. 
For example, writing blogs, or writing modules, or contributing to [CPAN](http://www.cpan.org/), or writing helpful things. 
That's where I started, so I wanted to do what he does, on a daily basis. 
But I never got the opportunity, everytime I say, <q>Okay, let's do something and let's add something to CPAN.</q> 
I had absolutely no clue what to do. 
I mean, anything that comes to my mind, I see someone's already done it. 
I don't know where to start and I keep thinking about it. 

And one day I was just looking at the London Tube map, and I think I remember that day, there was some strike, some Tube strike, and I said, <q>Oh my God, how am I going to go back home?</q> 
So I started looking around the map, and I said, <q>Let me find the shortest route, or try to avoid the route that's not working, or there's some trouble in that route.</q> 
And that's where I started, I said, <q>Okay, I'm going to write a Perl program, just write a script to see if I can find the shortest route, avoid a particular line, or do something.</q> 
So that's how I started, it came to my mind, I said, <q>Okay, I don't think anybody has done this!</q> 
But there were already a few algorithms and I thought I'd use one of those sesarching algorithms and try to find the shortest route, using those algorithms. 
Not having the computer science background, I had to try a little bit harder to understand all those algorithms, search algorithms. 
So I started looking around the Google, to see if I can find any paper where it explained to a non-computer science background, how it actually works. 
I came across one, a case-study by some Australian university student and he explained, in very simple language, so I could understand. 
And from there I got the idea how it actually works, and I started using, implemented it and tried to solve my shortest route problem through London Tube map and that was my first contribution. 
So I started with it and [pushed it to CPAN](http://www.cpan.org/authors/id/M/MA/MANWAR/). 
I got a couple of positive feedback from different people, and they came up with a few additions, and that's how I started. 
And a few people also came along and joined me and started working together. 
So that was my first thing.

[08:28] szabgab: 
So is this the module called [Map::Tube](https://metacpan.org/pod/Map::Tube::London)?

[08:30] manwar: 
Yeah, that's called Map::Tube.

[08:32] szabgab: 
And do you know if it's in...so do you use it now, these days?

[08:35] manwar: 
I do use it, yeah, I'm thinking of creating a [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) API for it, and put it on my website, so I can use it online from then on.

[08:47] szabgab: 
Do you know if other people use it?

[08:49] manwar: 
I know a couple of guys who use it, and they have developed their own Map for their different cities and all over the world, so I got a few, I think four or five cities, myself. 
There is another guy, who's got about ten or fifteen different cities, he created a Map, using my framework. 
And there's a guy from Germany, he created a few. 
There are three or four guys, who made different mapping for different cities, using my framework.

[09:30] szabgab: 
So when was this, when did you create this?

[09:34] manwar: 
I think five or six years ago.

[09:38] szabgab: 
Yeah, so back then I don't know how Google Maps worked and how these other various, I guess really there weren't really any of these GPS mapping softwares on the mobile phones, we hardly had any smartphones back then. 
So how, I think you can do something similar with Google Maps today, right?

[10:08] manwar: 
Yeah, you could do that. 
It's not real-time mapping, as I understand, it just gives you the shortest route, it doesn't give you the real-time, if there is any station that is closed in real-time, it doesn't tell you if it's closed or not. 
But it can be implemented, there are various sources where you can get those real-time data, and it can be implemented, so you can get the real-time and change the route, depending whether or not any station is closed on your route, shortest route, or give you another route where everything is clear.

[10:50] szabgab: 
Sounds like you're doing nice and you could build a service around it. 
Either an API or with an interface.

[11:01] manwar: 
I'm thinking of converting it to REST API, so other people can use it. 
So that's very close to me, that one.

[11:15] szabgab: 
That's great. 
So what other modules, you mentioned various calendar and games modules?

[11:24] manwar: 
Yeah, there's one more, I would like to share this with you. 
I remember five or six years ago, I was looking for a new opportunity in London, so I applied for a Perl developer position in one of the big Perl houses in London, and so their selection procedure was, they would send you a Perl task, so you had to produce the task in maybe two hours time and you had to send them back the code. 
So they sent me a Perl task, saying, <q>Okay, write a program to play a game of Domino.</q> 
So for me, that was the first time I had ever heard of the game of Domino. 
So for me, before even I can think of designing this module, I had to understand how the game works, how you play the game. 
As I said, I had to start from scratch and I couldn't finish it in time. 
So whatever I did, I sent it as it is, to them. 
And as I expected, I didn't hear from them, so probably they didn't like it. 
Once I got a feeling that my answer was not accepted, I said, <q>Okay, I'm going to spend more time now because now I've got a pleasure to go back to the design board, I understand how you play the game of Domino, now I went back and re-did everything from scratch.</q> 
I said, <q>I'm going to share it to my Perl community on CPAN, so other people can have a look,</q> that's how I started. 
So I pushed it to CPAN and said, <q>Here's my game of [Domino](https://metacpan.org/pod/Games::Domino).</q> 
So I'll remember, even when I get old, that was the first game I did using Perl.

[13:34] szabgab: 
That's interesting. 
So basically, what you're saying is, when you have to do something because of the job, it's not less fun. 
But when you do it for yourself...?

[13:45] manwar: 
Yeah, yeah, so it was fun. 
Then I did a few other games as well as doing this, also just for fun.

[14:00] szabgab: 
And in the Calendar namespace?

[14:03] manwar: 
Yeah, Calendar one was something, I remember, I came across a JavaScript code, I was looking at it, someone used JavaScript to deal with various types of calendars. 
And this guy just put in online as open, so anybody can use it and do whatever they want to do with the JavaScript code. 
And I look around the calendar thing that's available on the CPAN and I said, <q>Okay, I want to use this JavaScript thing and convert it into Perl.</q> 
But then I said, <q>I need to do something different that's not there on the CPAN already.</q> 
Then I said, <q>Okay, I'm going to do something like on a console, I'm going to display a colorful calendar, where you can have a colorful text and dates announcing, nice and fancy, color-coded calendar.</q> 
So I used the JavaScript code, converted it into Perl, and then started with varous different calendars. 
For example, [Bahai calendar](https://metacpan.org/pod/Calendar::Bahai), or [Islamic calendar, Hijri calendar](https://metacpan.org/pod/Calendar::Hijri), or different type of calendar, using this JavaScript code, and I converted it to a color-coder so you get a nice colorful calendar on your terminal. 
So that's how I started that Calendar thing.

[15:30] szabgab: 
So these are terminal-based calendars, right?

[15:32] manwar: 
Terminal-based, yeah, so there's an app as well, so it just say <b>calendr</b>, with a missing a at the end, so it's a command-line tool, you just say calendr.

[15:55] szabgab: 
Okay, so this is the calendar, this is the game that you mentioned, the Domino, is that also command-line? 
So you can play it command-line?

[16:06] manwar: 
Yeah, it's a command-line. 
When you install this module, it comes with a script to install in your bin part, so you just play the game. 
I think it plays as domino or something like that, that's how it installs, so you can play on the command-line.

[16:24] szabgab: 
So what I noticed was, besides doing these command-line things, you also, I looked at your website and it has quite a few interesting things there, like a dashboard for your CPAN modules, I think, can you tell me a little bit about that?

[16:41] manwar: 
Yeah, I'm glad you asked me this question. 
Because as I said, I try to follow Neil Bowers as closely as possible, so when I came across his personal website, which is [neilb.org](http://neilb.org/), so first thing I did was, <q>Okay, I'm going to reserve my own webname,</q> so I came over to [manwar.org](http://www.manwar.org), just to follow him, the way he did neilb.org, so I said mine was going to be manwar.org. 
So I decided first thing, was my domain. 
And then I thought, <q>What am I going to do?</q> 
So let's see what Neil Bower is doing. 
On his website, one of the sections is where he mentioned his various stats, like how many people uploaded to CPAN on a daily basis or weekly basis or yearly basis, kind of data, I said, <q>Yeah, very nice.</q> 
But I said, <q>I'm not going to copy what he did, I'm going to convert that into a different format.</q> 
Exactly the same data, but in a different format. 
I'm going to convert it into some kind of a graph, using HighCharts Free Graph JavaScript thing, using JSON data, converted that into a friendly chart, so that's how that all started. 

So I try to keep that and that's how I also got into, I came across that Neil Bowers had started this other trend, where he used to push one change to CPAN on a daily basis and he did that for 101 consecutive days and after that he stopped it. 
I think he had some kind of challenge among his friends and some other people in his group started doing that, and he was like a leading and then he stopped after awhile. 
And I said, <q>Oh wow, I wish I could do that 101 consecutive days.</q> 
And that's how I started and since then I've been doing it 692 days, today's the 692 consecutive day I've been pushing one change every day to CPAN. 

And then I came across [Barbie](http://metacpan.org/author/BARBIE) who did, I think, 370-some odd days, consecutive days. 
I thought whether I'm going to beat Barbie or not but I'll try and Barbie even mentioned in one of his [blogs](http://blogs.perl.org/users/barbie/2015/03/a-year-of-cpan-uploads.html), saying, <q>I'm going to stop it after one year, I'm not going to carry on, it's too much. 
But I think Mohammad is going to carry farther from me.</q> 
He said, good luck to me. 
I'm carrying on, I don't know how long I'm going to carry on.

[19:32] szabgab: 
So that's why you needed the modules that I ...?

[19:37] manwar: 
Yeah, after a point, I said <q>I have nothing more to do.</q> 
So I need to go and see if I can adopt some of the most popular modules so I can do some kind of contributions, so I'll have something to push on a daily basis. 
So that's why, yeah.

[19:51] szabgab: 
There are a couple of more modules under my name, so you can take them!

[19:58] manwar: 
I would love to!

[19:59] szabgab: 
Okay, we'll talk about it, off the video.

[20:03] manwar: 
Yeah, of course, yeah, yeah.

[20:08] szabgab: 
That's great. 
Okay, so we have quite a few other things that we wanted to talk about but the time is, we have already talked for 20 minutes. 
So I would like to finish this conversation this time and we'll go on later on, and talk about the other stuff.

[20:28] manwar: 
Sure, why not.

[20:32] szabgab: 
So really thank you very much for coming on the show. 
Would you like to say anything else just for this episode and then...?

[20:42] manwar: 
Yeah, one thing I want to say, the reason I get so much excited towards this contribution part of it is I've seen people who contribute in a big way to Perl, in general. 
My ambition, like every time I do something and contribute in whatever small way I do, I said, <q>I wish I could do a bigger project in Perl,</q> for example, there's a Dancer project going on and for example, [MetaCPAN](https://metacpan.org/), the group of people who are working on that. 
Those are big projects.
My ambition is, my next target is one day, I would like to be part of the core team for those so I can do something very interesting. 
Whatever I do so far, I don't think is anywhere near them, so I wish one day, I can go and join that core team of Perl developers and contribute in a big way.

[21:50] szabgab: 
I don't know, it's interesting, as far as I understand most of the time you work alone and with some contributors helping you, and these are definitely a different kind of contribution, when  you work in a team, there's a couple of other people. 
Yeah, that's interesting.

[22:13] manwar: 
So yeah, I hope to experience that as well, if possible.

[22:19] szabgab: 
Yeah, I remembered one more question that I wanted to ask about your website. 
Is that open source?

[22:26] manwar: 
Yeah, it is.

[22:27] szabgab: 
So other people can copy, take the code for their own modules...?

[22:33] manwar: 
It's available on my [GitHub](https://github.com/Manwar) so anybody can branch, fork it, whatever they want, absolutely free.

[22:44] szabgab: 
Let's direct people there and see if other people will use it, and maybe they will start to try to follow you, and catch up with the daily part.

[22:56] manwar: Maybe. 
Of course, it's absolutely free, yeah.

[22:58] szabgab: 
Okay, so really thank you again, for coming on the show and I really hope that we can continue this conversation because there are quite a few more things that I wanted to hear from you.

[23:08] manwar: 
Absolutely, any time, my friend, any time you want me, I'll be there. 
Thank you very much for the time. Thanks a lot.

[23:15] szabgab:  
Bye Bye.

[23:15] manwar: 
Bye.

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
