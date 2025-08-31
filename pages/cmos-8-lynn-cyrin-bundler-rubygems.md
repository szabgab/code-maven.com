---
title: "CMOS #8: Lynn 'Cyrin' Conway on Bundler, RubyGems and Ruby Together"
timestamp: 2016-09-19T08:01:01
tags:
  - podcast
  - Ruby
  - Bundler
  - RubyGems
  - USA
description: "Interview with Lynn 'Cyrin' Conway about her work as a project leader at Ruby Together for Bundler and RubyGems."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-8-lynn-cyrin-bundler-rubygems.mp3
  size: 18590774
  time: 19:54
#img: /img/cmos/lynn_cyrin.jpg
#alt: Lynn 'Cyrin' Conway
published: true
author: szabgab
archive: true
---


Interview with <a href="http://lynncyrin.me/">Lynn <q>Cyrin</q> Conway</a> about being a project
manager at [Ruby Together](https://rubytogether.org/) and deal with
[Bundler](http://bundler.io/) and [RubyGems](https://rubygems.org/).


{% youtube id="oJVfQFcjTJs" file="cmos-8-lynn-cyrin-bundler-rubygems" %}

<podcast>

## Lynn "Cyrin" Conway

* [Lynn Cyrin](http://lynncyrin.me/)
* [Twitter @lynncyrin](https://twitter.com/lynncyrin)
* [GitHub](https://github.com/lynnco)
* [Lynn Cyrin on POCIT](http://peopleofcolorintech.com/interview/episode-60-lynn-cyrin/)


## Links

* [The other Lynn Conway](https://en.wikipedia.org/wiki/Lynn_Conway)
* [Ruby Together](https://rubytogether.org/)
* [Bundler](http://bundler.io/)
* [RubyGems](https://rubygems.org/)
* [Python Ladies](http://www.pyladies.com/)
* [AlterConf](https://www.alterconf.com/)
* [Open Source Bridge](http://opensourcebridge.org/)
* [pip (Python)](https://en.wikipedia.org/wiki/Pip_(package_manager))
* [PyPi, the Python Package Index](https://pypi.python.org/)
* [virtualenv (Python)](https://virtualenv.pypa.io/en/stable/)
* [gem or RubyGems (the tool you can download)](https://rubygems.org/pages/download)
* [JRuby](http://jruby.org/)
* [Slack](https://slack.com/)
* [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat)
* [npm](https://www.npmjs.com/)
* [André Arko](https://twitter.com/indirect)

## Transcript

[transcript]
  [szabgab host1 Gabor Szabo]
  [lynn guest1 Lynn Cyrin]

[00:03] szabgab: Hello there, and welcome to CMOS, the Code Maven Open Source podcast and interview series. I'm your host, Gabor Szabo, and with me is [Lynn "Cyrin" Conway](http://lynncyrin.me/). Hello Lynn, how are you? How are you?

[00:21] lynn: Good, good.

[00:21] szabgab: Good. Before we get on, let's start with your name. I saw you call yourself Lynn "Cyrin" Conway on one hand, but in other places just Lynn Cyrin, can you tell me a little bit about this background?

[00:43] lynn: I would call myself Lynn "Cyrin" Conway everywhere but websites like to not have a proper name field so a lot of it's that. So I picked Lynn first, just independently of my last name, and only changed my first name, not changed my last name. So I changed my first name to Lynn and it ended up Lynn Conway, which coincidentally is also the name of another trans-lesbian web developer. So that was nice, I just ran into that, and I was just, "Oh, well should I change it? No, it's kind of cool to have the same name."

So I started to try to build a web developer program and I realized that you can't Google me and find me through <q>Lynn Conway,</q> I mean maybe in like 20 years from now, but not right now. So I picked <q>Lynn Cyrin,</q> and within two days of using that, I got the whole front page of Google, so now I'm good. I'm safe, you can find me on the internet.

[01:38] szabgab: Good, so do you have contact with her?

[01:42] lynn: Yes, I have. It took, I don't know, two years of having the name, but eventually one of my advisers said, <q>Oh yeah, do you want to meet [the other Lynn Conway](https://en.wikipedia.org/wiki/Lynn_Conway), I know her?</q> I was, <q>Oh it would be very cool to know the other Lynn Conway!</q> I don't have any significant relationship but I said, <q>Oh yeah, cool, we share all these things and have the same name, that's kind of nice, so, yeah.</q>

[02:07] szabgab: That's interesting. Okay, and does she do anything with computers?

[02:12] lynn: Yes, she does something...not like Ruby/Python, I don't know, like Cs/Perl, that type.

[02:23] szabgab: Interesting. Okay so tell me a little about your, you do have tons of stuff, I saw Ruby and Python and all these other things, but how did you get started with programming and open source?

[02:40] lynn: Well, my programming start was, I was in college for a bunch of different engineering degrees and I wasn't too excited about any particular engineering degree. Like I would study Mechanical Engineering, and then Chemical Engineering, and Materials Engineering, and eventually I got to Astronautical Engineering, which is rocket science and I was writing the code that helps guide, launch rockets on their way up to outer space. It was just an assignment, right, because Astronautical Engineering? And it occurred to me that the writing code part was actually much more interesting to me, than getting the rockets to outer space part, and that was coincidentally, also when I started getting into queer and trans stuff.

So I was writing code right about the same time I started getting into queerness stuff and I moved to San Francisco because I'm gay, but also San Francisco is where all the tech is. It was just an accident. I just happened to find myself in San Francisco, because I'm gay, and all of a sudden, that's where all of the tech companies are! And I just learned Python because there's a lot of Python in NASA, so I went there and I started doing Python in a lot of these, there's a lot of work and stuff at the intersection of what I did in AE and coding. So I started going to a lot of these [Python Ladies](http://www.pyladies.com/) meetings, or queer people writing whatever. And that's how that started.

Open source didn't come up as naturally, I just ran into an open source repository and I liked the idea of open source, it just appealed to me, like innately, at such a level. Since then I've become this huge open source. I would get all of the conferences I've talked at, except [AlterConf](https://www.alterconf.com/), which is a diversity conference, they've all been like [Open Source Bridge](http://opensourcebridge.org/) and other alternate conferences. Because I'm just really about open source, I open source all of my stuff, even stuff that people wouldn't ever want to look at, I just put it open source anyway because, <q>Why not?</q> I don't have the <q>Why would I open source this?,</q> for me it's <q>Give me an explicit reason to not open source this,</q> because otherwise I will.

[05:04] szabgab: Yeah, okay, that's nice. So at least on GitHub you mentioned [Ruby Together](https://rubytogether.org/) as sort of your employer, but do you also have a...are they really your employer? Do they pay you, do you have a job, or...?

[05:22] lynn: They are my employer in that I get formally, from the government, an employer and they pay me. Everyone at Ruby Together makes $150 an hour. It's really nice that everyone makes all the same wages, we'll hire a designer and they won't suddenly make less than the programmers, so that's nice. But yeah, Ruby Together pays me to work on [Bundler](http://bundler.io/) and [RubyGems](https://rubygems.org/). I also have a bunch of other things that also pay me but RubyGems is my only formal employer at the moment, everything else is crowdfunded or I own it, so...

[05:56] szabgab: Okay, but do you usually work at companies as well, in the last couple of years, or have you stopped since, I don't know, since you left rocket science?

[06:03] lynn: Actually, in my tech career I've done tiny contracting work here and there, where I was never an employee, and I think I have two interview chances that I'm working on right now, and those would be my first company jobs, like 40 hours a week things. And it took me three years to get to the point where I wanted or could have a fulltime job, so... The only other fulltime job I ever had, I was a janitor. So yeah, I haven't done the company-thing much.

[06:41] szabgab: Yeah, well, it's great, I'm quite sure that many companies would want your capabilities, I mean, seeing what you do in all this stuff, open source. Maybe except the part, that they don't want to open source everything you write.

[06:56] lynn: Yeah, I say in interviews, <q>How much of my work can be open sourced?</q> That's always in my interview questions, when I talk to a new company. But yeah, you can see all my code. I feel that as an interview, that's the best advantage of working so much in open source, is that you can show employers, <q>This is specifically what I've written.</q> This is  everything I've written, in my entire career, you know?

[07:22] szabgab: Yeah, I know, I teach various programming languages and stuff, usually for people working at companies, and they always, I'm trying to tell them, <q>If you want to show to the next employer, something that you do, then you have to do something in open source.</q> Because you can't usually share what you do at your company.

[07:47] lynn: Yeah.

[07:49] szabgab: That's nice. So let's, among all the things that you do, we thought that we'd talk about, Bundler, and I really have no idea because I'm coming from the Perl background and Python and some front end, even though you can't see it on my website. But I really have no knowledge about Ruby?

[08:14] lynn: So in the Ruby world, there's Bundler, RubyGems, and RubyGems.org, which are three different organizations with different, they used to have different ownership, Ruby's got to resolve that, but I'll get to that in a second. And there used to be three different groups of people with all different admins, working on three different things that [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) all does, so [pip's website](https://pypi.python.org/), the Python packages website, that's RubyGems.org. There's two different parts, pip doesn't really do anything that Bundler does really, some of Bundler stuff is what [virtualenv](https://virtualenv.pypa.io/en/stable/) does and it does some stuff that pip would like to have, but really pip is just RubyGems.

[09:03] szabgab: Wait a second. I know pip, a command called pip in Python, do you talk about the same? Or Ruby has the same names for stuff?

[09:15] lynn: No, I mean, RubyGems is essentially pip.

[09:19] szabgab: Okay.

[09:20] lynn: They have basically the same functionality. Then Bundler has some of the functionality of virtualenv, but they're not equivalent. That's where the equivalence starts to get way different, Ruby has a bunch of different environment tools, that one would use. Anyway, what this specifically is, is that there's RubyGems.org, the website. There's RubyGems, the codebase, which that's the thing that downloads and makes RubyGems for you. And then there's Bundler and that handles your environment, and getting your stuff from your package management file, and it stores all the commands of RubyGems, and sends commands to RubyGems.org, and that's how you get the thing.

So there's three different tools, which finally are being merged a bunch. RubyGems, RubyGems.org, and Bundler all have the same managing organization, in Ruby Together. This used to not be the case. There used to be kind of a warring-factions thing going on between Bundler and RubyGems, it was a mess. Anyway, now someone, one person, owns all three of them, and they're trying to make all of this more easy to understand. Sounds nice.

[10:34] szabgab: Okay, so when you're creating a new package in Ruby, do you also use Bundler to bundle together, or is there another thing that you need for packaging? I guess you upload it to RubyGems, right?

[10:51] lynn: Yeah, I'm pretty sure RubyGems handles all of the new package commands, I'm pretty sure, don't quote me on that particular thing. I'm pretty sure that the new package command Gem maps to RubyGems. RubyGems is mostly that, because RubyGems also handles the Gem hosting part in RubyGems.org, and Bundler doesn't do any hosting whatsoever, so...

[11:20] szabgab: Okay, I think I get it. So what kind of things do you do there? What kind of things are there to do now? These days?

[11:29] lynn: So the good thing is that for the average user, there's essentially nothing you still do, with Bundler or RubyGems, it comes installed, well Bundler doesn't come installed by default, you have to install Bundler itself, but we're working on that, we're working on making Bundler be a default thing. But RubyGems comes with the Ruby installation and you use [Gem](https://rubygems.org/pages/download) to install it, and it works like you would expect. That's what happens for most people, there's some edge cases, well actually it's all edge cases from there. 

So if you're on Linux and you want to install a simple Gem file with no requirements, no optional dependencies, I mean no requirement groups, no optional dependencies, nothing like that, then everything's fine. But when you start getting into, like you want to have something different on development, than on production, then that's, it gets kind of messy, there's still some features to work out there. 

If you have optional requirements, there's actually a feature difference that went out on Bundler, about a week ago, where if you had an optional requirement, it would still automatically require them without you having to tell it to do so. And apparently in the past week, invisibly, that broke. Where now in the optional requirements, you have to explicitly require them. 

So it's edge-case things. Also, if you're on anything but Linux, things might just break sometimes. Especially if you're on Java, [JRuby](http://jruby.org/) is a really big thing and things in JRuby break Bundler all the time. Like every week, there's a new way that JRuby has broken Bundler. 

For most people it's fine, but the more edge-cases you stack on, the more stuff there is to do. I don't actually code, I haven't written a single line of Ruby code for Bundler or RubyGems, I'm the project manager, so my main thing is I have a reactive job. I watch all of the [Slack](https://slack.com/) channels, I see what's happening, I report to other people what's happening, I label things, I organize things, and make sure people know what's up, I write the RubyGems monthly updates, I watch all of the Slack channels, all of them, all month. So I have enough information to write the monthly update so everyone else can know what happens, without having to watch every Slack channel. So those sorts of things. I'm basically on GitHub all day. I'm never on command-line and I'm always on GitHub, as my work.

[13:54] szabgab: Oh, that's interesting. Okay, so how do you tell the other people, how do you select what to do or what to work on? How do people decide what to work on? Individually, whatever they think about? Or you, how much do you prioritize the jobs? The tasks?

[14:21] lynn: So the majority of the work, this is becoming only mildly less the case over time, as Ruby Together, the organization, gets more money to pay people to work on Bundler and RubyGems, but most of the work on Bundler and RubyGems, open source contributors can just decide if they want to work on it. Which makes project management really important because when you have employees, you make them work because you pay them, but when you have open source contributors, they can just poof! 

So I have the great job of making sure the open source contributors have a nice time contributing, because if they don't have a nice time, they can just leave, right? So that's how most of the work happens, I do my best to make sure that all of the issues are well-sorted, I try to respond to the more-irate users or point them to where they need to be, when I can, when I have time and hours in the day. Those are things I do to try to make sure that the non-paid contributors can do their best and they aren't having lots of issues, and they get turned off by the source code, and those sorts of things. So that's my general job as project manager, and that's how I guide people to the work that I want them to do.

[15:40] szabgab: And your main communication channels are GitHub, Slack, anything else?

[15:46] lynn: No, I spend most of my time switching between GitHub and Slack.

[15:54] szabgab: So no [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat), for example?

[15:54] lynn: No, there is an IRC channel that nobody uses. I'm not long into because not enough happens on it for me to justify adding it to my list of things to watch, so it's really just Slack at this point. I don't know when it became that, that it's only Slack, but now it is.

[16:13] szabgab: Okay, I see, that's great. Okay, I think I've run out of questions about this. Actually not, there is the Ruby Together, so can you tell a little bit more about the organization, how it works, and how you got together?

[16:36] lynn: So Ruby Together is really, really similar to [npm](https://www.npmjs.com/), another package manager, if anybody knows what npm, Ruby Together is functionally identical. I think their big difference is npm is like a huge start-up, I don't know how much money it makes, I don't know how much it's worth, but compared to Ruby Together, npm is enormous. 

Ruby Together is, I think this is actually how it's legally set up, Ruby Together is basically [André](https://twitter.com/indirect), he's the director of Ruby Together and he's a bunch of other things. So André used to be working on Bundler for free, bundler and RubyGems for free, and he was just working on it, right, because it's open source and he had time, so he was just working on Bundler and RubyGems. 

And it, this was back in the end of the warring-faction days, RubyGems versus Bundler days. RubyGems seemed to push something that broke Bundler's code, almost on purpose, and they wouldn't ask, they wouldn't tell them first. So suddenly people could use RubyGems but they couldn't use Bundler, and so Bundler would have to catch up, or the Bundler people would make RubyGems, like this kept happening back and forth. 

And then André started working on both of them and something happened, where RubyGems was down for three days, and a lot of big companies lost a lot of money, and André was the one who got it back up. About a week after that, people started being, <q>Hey, could we pay you money to make sure you're always around, so when it goes down, it's just down for a few hours, not three days?</q> Three days without being able to install any new packages is huge, <q>What, the package-manager is down?</q> That doesn't even make any sense. That's definitely something people wanted to pay for, so it just started almost by accident, with people going to my boss with, <q>Hey, we'll give you money for this.</q> 

So he got that enough that he made a non-profit out of it and now there's six of us, we go, we help out, we help out on a few other things like smaller libraries, there's some people working on [VCR](https://github.com/vcr/vcr), and a bunch of little tools. But mostly it was that people got really tired of RubyGems and Bundler going down, so they started paying money to André, and then André made a non-profit, and so now this is Ruby Together.

[19:08] szabgab: Okay. Thank you very much. A lot of things I've learned today. Do you have anything we haven't mentioned that you would like to talk about or would you like to shout-out to some people, or...?

[19:24] lynn: I can't think of anything in particular, I mentioned all of the big stuff. There's my other work but this was just my one of three jobs. I could do a half-hour about my other jobs, but I'm not going to do that. For the scope of this work, this is most of the stuff that people will want to know about.

[19:43] szabgab: Okay, great, thank you again for coming on the show and hopefully see you at another episode!

[19:51] lynn: Yeah, cool, thank you.

[19:52] szabgab: Bye bye.

[19:53] lynn: Bye.

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
