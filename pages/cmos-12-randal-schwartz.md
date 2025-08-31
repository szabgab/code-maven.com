---
title: "CMOS #12: Randal Schwartz the host of FLOSS Weekly"
timestamp: 2016-09-28T22:01:01
tags:
  - podcast
  - FLOSS Weekly
  - Perl
  - Dart
  - USA
description: "Randal Schwartz the host of FLOSS Weekly, the largest Open Source podcast and the most prolific author of Perl books."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-12-randal-schwartz.mp3
  size: 25823933
  time: 25.01
#img: /img/cmos/randal-schwartz.jpg
#alt: Randal Schwartz
published: true
author: szabgab
archive: true
---


Interview with [Randal Schwartz](https://youtu.be/YU41eecLtNI) the host of the [FLOSS weekly netcast](https://twit.tv/shows/floss-weekly) and the most prolific author of Perl books.


{% youtube id="YU41eecLtNI" file="cmos-12-randal-schwartz" %}

<podcast>

<div id="person">
  <h2></h2>
  <ul>
    <li>[Stonehenge consulting](http://www.stonehenge.com/) the company of Randal</li>
    <li>[GitHub](https://github.com/RandalSchwartz)</li>
    <li>[Twitter: @merlyn](https://twitter.com/merlyn)</li>
    <li>[Google+](https://plus.google.com/+RandalLSchwartz)</li>
    <li>[Randal L. Schwartz](https://en.wikipedia.org/wiki/Randal_L._Schwartz)</li>
  </ul>
</div>

<div id="links">
  <h2>Links</h2>
  <ul>
    <li>[Floss weekly](https://twit.tv/shows/floss-weekly)</li>
    <li>[Leo Laporte](http://www.leoville.com/)</li>
    <li>[Docker](https://www.docker.com/)</li>
    <li>[ECMA 5](https://en.wikipedia.org/wiki/ECMAScript)</li>
    <li>[Dart](https://www.dartlang.org/)</li>
    <li>[Lua](https://www.lua.org/)</li>
    <li>[FISL](http://fisl.softwarelivre.org/)</li>
    <li>[Insight Cruises](http://www.insightcruises.com/)</li>
    <li>[Neil Bauman](http://www.insightcruises.com/standard_interface/about_neil.htm)</li>
    <li>[Perl 6](http://perl6.org/)</li>
    <li>[YAPC::EU](http://act.yapc.eu/)</li>
    <li>[Red Hat](https://www.redhat.com/)</li>
  </ul>
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [randal guest1 Randal Schwartz]

[00:01] szabgab: 
Hello there, this is the CMOS, the Code Maven Open Source podcast and video interview series and this is your host, Gabor Szabo. 
And with me is Randal Schwartz. 
Hi Randal!

[00:12] randal: 
Hey, hi, welcome to me! 
Thank you, from across the pond here, I'm in lovely Lacey, Washington, just a little bit north of Olympia, in my brother's house. 
You might see some album record covers, if you're watching the video, behind me. 
I don't know how the lighting is going to work out, we'll give it a shot. 
The sun's starting to come up so that might effect my lighting, but we'll give it a shot.

[00:36] szabgab: 
Yeah, that's great. 
Actually it's funny, that you are now the person who is being interviewed, not the usual setup that you're interviewing all kinds of people at [FLOSS Weekly](https://twit.tv/shows/floss-weekly). 
So just a little bit, the standard questions, there are probably many people know you, but introduce yourself, please? 
Let us know, how did you get into programming, and how did you get into open source?

[01:04] randal: 
Wow, well those could be an hour already, by themselves. 
But let me give you sort of the high-level view of those. 
My Dad was very career-oriented, and so I picked programming at a fairly young age. 
By the time I was nine, I was actually writing computer programming. 
And we're talking almost 50 years ago, so this was basically reading computer manuals about the [PDP-8](https://en.wikipedia.org/wiki/PDP-8) and the [PDP-11](https://en.wikipedia.org/wiki/PDP-11), back in the early days. 
And writing programs just on paper. 
I eventually got to code on an [ASR 33](https://en.wikipedia.org/wiki/Teletype_Model_33) teletype, time-shared Basic, all upper-case, all very noisy. 
And did that for five or six years, built an [IMSAI 8080](https://en.wikipedia.org/wiki/IMSAI_8080) and then went out in the real world, programming that type of computer more often. 

But by the time I was 16, I was gainfully employed, writing text actually, I was being trained as a technical writer, which made me double-useful, both as a writer and as a programmer. 
And that led me to various other careers, as well as being a trainer and eventually owning a company, that sent trainers all over the world, during the Perl heyday. 
And so that, I enjoyed programming, it seemed to work well, I seemed to be able to do abstract reasoning very well, and I've picked up over the years, probably, I think at one point I listed 45 languages on my resume. 
A lot of those were "can read" and I could probably parse my way through a piece of code in a certain language. 

Right now, I'm probably fluent only in about a half-dozen languages and, of course, the number one of those would be Perl. 
Shell-scripting probably a close second, C being probably third. 
Oh, and [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk)'s in there somewhere, probably Smalltalk is second or third as well. 
I think that's sort of the beginning of an answer that you wanted, how did that work?

[03:02] szabgab: 
Yeah, you're doing quite well. 
It seems that you're not the first time on a podcast or a video interview, right?

[03:11] randal: 
No, clearly not. 
I mean, FLOSS Weekly has been running on for ten years now, and I've been doing a lot of those. 
And prior to that, I was doing the [Geek Cruises News](http://insightcruises.com/top/ll4_top.htm), which were interviews with people that were on the cruises that I get to do frequently, including one coming up in a few weeks, and also actual sections of seminars on those cruises. 
And so I was doing that even before I was doing FLOSS Weekly, sort of tutored by the king himself, [Leo Laporte](http://www.leoville.com/), actually helped me get started in podcasting, and I really appreciate his early guidance. 
Then him inviting me to take over FLOSS Weekly was a real coup, because we're getting somewhere between 30,000 and 50,000 downloads a week on that thing. 
And it's the number one open source podcast.

[04:02] szabgab: 
Well, you know, I'm building an open source podcast, so we will see. 
It will take a couple of years, I guess.

[04:09] randal: 
Good challenge, then.

[04:10] szabgab: 
Yeah, it's a challenge. 
So, tell me your secrets, with the podcast?

[04:17] randal: 
Well, one of the things is that I crowd-source everything. 
As I kept looking at what I needed to do to produce a particular show, it was like well, I've got to have a guest, and when I got through the short-list of all my friends, that would be good guests, I started asking the audience, <q>What do you want to see?</q> 
And then they would throw project names at me, and then I was like, <q>Okay, now I've got to go look up the contact name for that, and I've got to convince him that this little, dinky podcast, which wasn't very well-known in the early days, is something they want to do.</q> 
And I got smarter about it after awhile, just being practical about it, I said, <q>Okay, I don't want to contact these people, I want the audience member to contact these people.</q> 
So I started saying, <q>Here's how you get on the podcast, here's how you get somebody on the podcast. You contact them.</q> 
The project leader, community coordinator, somebody that would be a good representative, and tell them how much you enjoy FLOSS Weekly, and have them contact me, my email address is on the website, merlyn@stonehenge.com. 
And that's how 95% of our guests over the last nine years have been brought in. 
By crowd-sourcing it that way, I only had to close the deal, I had to set up the public spreadsheet of all the upcoming open to-be-scheduled shows.
 Also on that same spreadsheet, I list the people I'm already in process of talking to, so I don't get redundant attempts, so that works out really well. 
That was kind of the secret of that, once I figured that out, that was really nice. 

And now I just see that the sun is now hitting me in the face, really brightly! 
Sorry, let me turn the gain down little bit here, I know this is still being recorded. 
Anyway, so does that answer your question or do you need more on that?

[06:07] szabgab: 
Yeah,  yeah, that's cool. 
I'm sure that I'm going to have a lot of other questions but maybe it's going to be off this interview. 

So, open source...? 

So actually, the podcast and open source contribution, or things that you learn, how much do you feel that the podcast that you're doing, the interviews that you're doing, impact the stuff that you get interested in and start learning?

[06:41] randal: 
Well, one of the things that I've discovered over the years, is that I'm genuinely curious about things. 
And so, one of the things I'm very careful about, is not over-research a particular topic, when I go on. 

I basically, well part of that's practical, I've got maybe an hour I can devote to going over whatever URLs they gave me. 
But part of it is also being a proper proxy for my audience. 
If I know too much, I might not ask a question. 
Whereas, if I just remain genuinely curious about how this fits in here and how that fits in there, and is there anything else like this, that sort of thing, then I'm acting as a proxy for the audience, who are probably having the same questions that I have. 
I'm a little bit of a generalist, so it's kind of nice to be able to look at all things, and try to figure out what's going on. 

The other thing I've been observing is, in the early days, I was always curious about, <q>How do you make money? If you give away your stuff for free?</q> 
And over the years, we've seen probably a dozen different models of how people have done this. 
All the way from, <q>Well, it's just a labor of love, so we really don't care about making money</q> all the way up to, <q>Well we set it on top an entire business, around the idea that we could give away our core product, and leverage the resources of the community, to help us figure out directions to go, to actually get programming resources, people adding features that are appropriate to them, maybe even things like internationalization, which is always a tough issue, if you don't hire 50 different people to translate your stuff for you, but maybe somebody in Brazil wants to tranlate it into Brazilian Portuguese for you.</q> 

That sort of thing, it's been really remarkable, seeing people at both ends of the spectrum. 
We've also seen people sort of in the middle, where they say, <q>Well, we'll open source our core product but we'll keep some of it held back and ...</q> 

Eventually even some of those go to open source from top to bottom, so we're really happy with that. 
We also encourage people who are sort of in the middle there, to create some sort of governance board, that's outside of them, so that the project really does have an independence, and it can be more trustworthy that it will remain even if the company decides, <q>Oh, we're not going to do that any more. We're going to do something in Fortran or something.</q>

[09:07] szabgab: 
So, what are the, I guess you see all kinds of trends, based on your interviews or, can you pick something out from there and point out what kinds of trends you might see?

[09:24] randal: 
Yeah, I think a few years ago, it was all about cloud stuff. 
So it was all about running your application in cloud. 
Starting probably a couple years ago, with the [Docker](https://www.docker.com/) revolution, it's all about containers now. 

But we're also seeing a revolution in smart, JavaScript-based ultimately, front-ends, that are doing things like [single-page applications](https://en.wikipedia.org/wiki/Single-page_application) and stuff, and I'm really pretty excited about that. 
Not that I ever really wanted to spend a lot of time playing with JavaScript, but unfortunately I guess that that's a requirement, so I'm continuing to hone my JavaScript skills. 

I'm also honing my [Dart](https://www.dartlang.org/) skills, because that language out of Google, is really gaining some traction, in terms of being able to do server-side stuff, essentially replacing [Node.JS](https://nodejs.org/en/) with a reasonable language. 
And also client-side stuff for all the modern browsers, and it translating down into JavaScript, so as long as there's a reasonable [ECMA 5](https://en.wikipedia.org/wiki/ECMAScript) or something available in the browser, Dart works really nicely. 
But Dart looks closer, as a language, to something like Java, with optional typing, so if you add types to variables, you can actually get hints from your development environment and that's pretty slick. 
So I'm learning Dart in the background, I actually have a couple applications for it already, that as I learn more, I'll be able to deploy. 
I'm also learning things like [Angular](https://angularjs.org/), so I can have reactive front-ends, and again, it's like there's not enough hours in the day for me to learn everything I want to learn. 

I'm keeping up with Perl, but not really, I still see a feature, like in Perl 5.16, and I go, <q>Oh, that's in relatively modern Perl, no wonder I don't know about it.</q> 
I think of Perl as whatever was back in 5.10 and 5.12, that's the latest that I was writing my books for, my trainings for. 
So the stuff that's coming out in 5.18 and 5.20 and 5.22 now, is sort of beyond me, I just can't keep up with Perl-delta, and that's a scary thing for the number one prolific author about Perl, to not be able to keep up with what's happening in the Perl community, this is clearly an indication that Perl is alive and well, and I've kind of missed the boat, now.

[11:52] szabgab: 
Yeah, well, I guess there are not that many trainings anyway, these days, so maybe that's not such a big issue now. 
But there's another, I'm wondering about another trend, of countries? 
Of the country of origin or the country of location of the current location of the people who are writing open source code? 
Have you seen any changes, any major changes? 
I understand that you travel quite a lot, so I don't know if it's during your, so whatever you see? 
That's the question.

[12:28] randal: 
Yeah, that's a great question. 
I think that we're seeing probably about, well there's a bias in that it's an English-language podcast, although English is sort of the lingua franca of technology for most of the world. 
So we tend to get a bias on who's nominating people. 
But I think probably, if I think about it for a second, I think probably maybe one-fifth or so of the podcasts are interviews with people who are not in the U.S. and the project was originated internationally. 
I'm thinking things like [Lua](https://www.lua.org/), and there was something recently, some sort of a web framework. 
So that's starting to happen there. 
A lot of them probably stay regional, and still the U.S. and English-speaking countries are pounding out most of the code that I'm able to read. 
I do see a bit of a trend towards people solving their own problems, that happen to be problems that other people in other countries also have, so why not share it across borders?

[13:40] szabgab: 
I understand that you travel quite a lot. 
I think that I saw that you had a competition between your age and the number of countries you visited?

[13:50] randal: 
Oh, yeah, yeah. 
That was really amazing! 

Back about early last year, I finally had visited 54 countries and I was 53 at the time, so that was the first time that I'd been in more countries, no excuse me, the second time I'd been in more countries than my age. 
The first time, was when I was a baby and not quite one, I was in one country, the U.S. 
So we finally went full-circle, so now at this point I've been to 57 countries, so I'm set for another couple years, but it's now going to be my goal, throughout the rest of my life to have been in more countries than my current age in years. 

So I think it's a valid challenge, and it's not too difficult, there's a lot of, well, for one thing, I've never been to the Far East. 
In all my travels, I've never been to Japan, I've never been to China, I've never been to any part of Indonesia. 
I have been to Asia, technically, because I've been to the western end of Asia, I've been to, half of Turkey is in Asia, and I've also been up to the Black Sea, so the area up in there, so yes, I have been to Asia for those points, but I have not been to the Far East. 
So that gives me at least half a dozen easy countries to add, once I get to 57, so we'll look forward to that.

[15:10] szabgab: 
So when you travel, what do you do? 
Do you meet open source people? 
Do you talk to programmers? 
Or is it only for hiking or sightseeing?

[15:25] randal: 
No, no, sadly I've maneuvered my work environment to always be fun. 
So yes, I can technically say that pretty much, I travel for work. 

There's two purposes, two major ways that I end up in a different country. 
One is every year, except this year, I've been going down to Porto Alegre, Brazil, to speak at their open source conference, called [FISL](http://fisl.softwarelivre.org/), and there they have about 4,000 attendees, and again, thanks to the fact that English is sort of the lingua franca, I'm able to speak to most of them, except I can't understand what they're saying to each other, when they're not actually talking to me. 

I do know sort of a basic knowledge of Spanish, and a lot of the Portuguese words and the Spanish words are overlapping, so to that degree I can pick up what they're talking about, and maybe read some signs. 
But I've also been to Mexico, I've, about ten years ago, I was invited by the government to go to Venezuela, so I spoke there at an open source conference. 
I've been to Australia a few times for open source conferences, so that's sort of the open source side of things. 

But my primary access for countries around the world has been my oldest client now, 15-16 years, [Insight Cruises](http://www.insightcruises.com/), where my buddy [Neil Bauman](http://www.insightcruises.com/standard_interface/about_neil.htm) puts on a conference onboard the cruise ship, and I get to go along, either to speak, in the early days, when it was about open source a lot, or to assist, or now I just go along to go to these various places all over the world and see the program that they're presenting, either from their partners, in the early days MacWorld Magazine, so I learned more about the Mac and Apple and iPhones. 

And later now, we've partnered with [Scientific American Magazine](http://www.scientificamerican.com/store/archive/?magazineFilterID=Scientific%20American%20Magazine) and [Sky and Telescope](http://www.skyandtelescope.com/) for interesting observations made from cruise ships. 
So yeah, that's been the primary source of being able to check off countries, that's been a lot of fun.

[17:53] szabgab: 
Yeah, so as a closing question, I would like to go back a little bit to the languages and the things you do with open source, and ask you, where are you heading? 
Are you going to go back to Perl and learn what the new things in Perl are, or are you more interested in other languages, and which ones?

[18:16] randal: 
Well, I download and compile [Perl 6](http://perl6.org/) every day. 
And every time I go to [YAPC](http://www.yapc.org/) or some other place where they're talking about Perl 6, I get excited about it, for all of a month, and then I come back and then I go, <q>How am I going to use this practically? None of my current clients are demanding that.</q> 

Clearly if I were to write training materials for that, I'd have to present it at least to 200 people, whether that's 10 classes of 20, or a giant 200 person week-end event, that's sort of the minimum for amortizing the inception cost for any class that I've ever written. 
So I use the 200 number as kind of a rule of thumb. 

And I just don't see that happening, I don't see getting enough people together in the right places, to be able to do that. 
So I continue to watch what people are doing with Perl 6, I continue compiling it every day, and I'd love for it to become extremely popular so I could go back to that, and say I could continue my Perl heritage. 

But, as I mentioned earlier, I think Dart has legs. 
Given that Google's behind it, given that Google and a number of other companies are already deploying public-facing projects in it. 
Given that it does compile down and work in all modern browsers, I easily see the need for like <q>rent a hotel room for a weekend</q> and have 20, 50, 100 people show up to learn about it, because single-page applications are all the rage right now, and Dart is a really solid language for that, and Google is betting on that. 

You may say, <q>Where is Go in that equation?</q> 
Go is great for server-side stuff, and great for the kind of things they're doing on back-ends, and although Dart can also do back-end stuff, essentially replacing Node.JS for that sort of thing, and have a single language for both back-end and front-end. 
Dart's real win is in the front-end, being able to be transpiled over to JavaScript and being able to scale to hundreds of thousands of lines of code for some of their larger applications. 
I think that's got legs, I'm in on the groundfloor, like I was on Perl, I'm already recognized among the Dart people as being someone who can put things together. 
I did a one-hour long intro to Dart talk that was reviewed by some of the key people in the Dart community, and they really like what I did with it, so I seem to have, again, that knack for finding something complex and finding the simplest ends of it, and I'm already there with Dart. 

And also, the whole [Fuchsia](https://en.wikipedia.org/wiki/Google_Fuchsia) announcement a few weeks ago, where Google's coming out with this language for real-time operating systems, and it has a strong Dart component in it. 
I think that's another thing that says, say if they start putting that in [Google Glass](https://en.wikipedia.org/wiki/Google_Glass), or if they even put that as a replacement for the Android operating system, or for Google Chrome, which some people are suspecting that this is all amalgamation of it. 

Especially when somebody's looking at the source code the other day, and it has a lot of files, not only from Android, but also from the old [Be OS](https://en.wikipedia.org/wiki/BeOS), which was sort of the predecessor of what eventually became OS X, kind of interesting that that's part of that project as well. 

So with Fuchsia on the horizon, with Dart already being deployed by numbers of people, with me having a knack for understanding how Dart actually works, given that it was also built by some of the key players in Smalltalk, which I go back 16 years with, I think this is probably the right place for me to look at my future.

[22:02] szabgab: 
And I guess, FLOSS Weekly?

[22:05] randal:  
FLOSS Weekly will continue. 

In fact I just had a converstaion recently with Leo, we're one of the smaller shows on the network, but he's absolutely committed to this show. 
He likes what I'm doing with it, he likes the directions I'm taking it, he likes the team I've put together, who were able to pick up the show, even when I was absent for six weeks, in the hospital recently, without notice unfortunately, I guess that's always the way you end up in the hospital. 

So my team picked up, and Aaron Newcomb did a great job of hosting while I was gone, but Leo likes the team I've built and Leo likes the kinds of guests I'm getting on, the variety especially. 
I've had a lot of people write in and say, <q>I don't always want or understand the thing you're talking about, but I listen to the way you interview them, and I listen to the things you're able to pull out, like what's the governance model, how are you making money with this, what got you started?</q> 
These sorts of things are really sort of cross-project. 
You know, you can learn that sort of stuff about anything you want to start, and like I said, I learned a lot already by doing this show and so a lot of the audience is picking that up. 
And we have a fun time. 

I tell jokes sometimes and I have a bad way of making really bad puns. 
And that's kind of the way it works but I really enjoy the show, I'm going to keep doing it. 
And I told Leo I would just keep doing this as long as he let's me, and he goes, <q>Well then, that makes two of us. So we'll still be doing this in 20 years, if they let us.</q> 
And I said, <q>That sounds like a great promise, Leo, thank you.</q> 
So yeah, I'll be doing FLOSS Weekly for at least awhile longer.

[23:45] szabgab: 
I'm happy to hear that and I hope to see a lot more of that. 
And I hope to see you somewhere, I don't know, maybe at a Dart conference?

[23:56] randal: 
Yeah, that'd be awesome! 

And I think you come to [OSCon](http://conferences.oreilly.com/oscon), occasionally, or maybe, well I've got to get out to a [YAPC::Europe](http://act.yapc.eu/) or a YAPC::Israel or something at some point, but just haven't made those yet. 
I think it's partially because I need to figure out what to pitch to the Perl conference. 

Oh wait, I could just be press again! 
That's the other thing, is that FLOSS Weekly has allowed me to apply as press for OSCon for the last few years, even though I don't have an actual talk to give. 
And [Red Hat](https://www.redhat.com/) actually invited me to their conference, as press. 
And I thought, <q>Well, that's the first time that's happened. That really says I've made it. That really says that FLOSS Weekly is recognized as legitimate press.</q> 
So I'm wearing a whole 'nother hat, so my hat tree of all my hats, hanging up in the corner, has gotten a whole 'nother rung.

[24:52] szabgab: 
Thank you very much.

[24:54] randal: 
Thank you, thank you for inviting me on the show. 
I look forward to seeing this when it gets published.

[24:59] szabgab: 
Bye bye.

[24:59] randal: 
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

