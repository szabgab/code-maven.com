---
title: "CMOS #16: Jan Henning Thorsen and Marcus Ramberg about Convos, the web-based IRC client"
timestamp: 2016-10-14T13:45:01
tags:
  - podcast
  - Convos
  - IRC
  - chat
  - Norway
description: "Convos, the web based IRC client that won't lose your connection even when you are off-line."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-16-jan-henning-thorsen-and-marcus-ramberg.mp3
  size: 27466201
  time: 30.02
img: /img/cmos/jan-henning-thorsen-and-marcus-ramberg.jpg
alt: Jan Henning Thorsen and Marcus Ramberg
published: true
author: szabgab
archive: true
---


Interview with [Jan Henning Thorsen](http://thorsen.pm/) and [Marcus Ramberg](http://marcus.nordaaker.com/) about [Convos](https://convos.by/), their open source messaging and chatroom app, with many features. It's written in Perl and uses Mojolicious!


{% youtube id="kUJC_trDR6I" file="cmos-16-jan-henning-thorsen-and-marcus-ramberg" %}

<podcast>

<div id="person">
  <h2>Jan Henning Thorsen and Marcus Ramberg</h2>
  <ul>
    <li>[Marcus Ramber on GitHub](https://github.com/marcusramberg)</li>
    <li>[Marcus Ramberg](http://marcus.nordaaker.com/)</li>
    <li>[@marcusramberg](https://twitter.com/marcusramberg)</li>
    <li>[Jan Henning Thorsen on GitHub](https://github.com/jhthorsen)</li>
    <li>[Jan Henning Thorsen](http://thorsen.pm/)</li>
    <li>[@jhthorsen](https://twitter.com/jhthorsen)</li>
  </ul>
</div>

<div id="links">
  <h2>Links</h2>
  <ul>
    <li>[Convos](https://convos.by/)</li>
    <li>[Convos on GitHub](https://github.com/Nordaaker/convos)</li>
    <li>[IRC](http://www.irchelp.org/)</li>
    <li>[Reisegiganten](http://www.reisegiganten.no/) where they both work now</li>
    <li>[Telenor](http://telenor.no) where Jan used to work</li>
    <li>[UIO (University of Oslo)](http://www.uio.no/) where Marcus used to work</li>
  </ul>
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [batman guest1 Jan Henning Thorsen]
  [marcus guest2 Marcus Ramberg]

[00:01] szabgab:
Hello there, this is the CMOS, the Code Maven Open Source podcast and video interview series and I'm your host, Gabor Szabo, and with me here is Jan Henning Thorsen, also known as Batman, and Marcus Ramberg, also known as Marcus. 
What is your nickname?

[00:31] batman: 
It's actually Batman.

[00:33] szabgab: 
Yeah, Batman. 
Did I say something else?

[00:36] batman: 
No.

[00:38] szabgab: 
Good.

[00:39] batman: 
3D Batman.

[00:43] szabgab: 
So we guys know each other for quite a long time from the Perl community. 
But many of the listeners don't. And I actually don't know why are you Batman?  
So please tell me a little bit about your history, how did you get into programming, how did you get into open source, and then from there we get to the product that you want to talk about.

[01:03] batman: 
Right, so in 2001, I started working for a cable company, and they wanted me to make a provisioning system for them, and I didn't know any programming at the moment. 
So I started Googling and the first thing that came up was some Perl code, so from now I'm really happy that I...like the first hit wasn't PHP instead. 
Because if PHP was number one on Google, then I would be programming in PHP instead.

[01:36] szabgab: 
Okay, I don't know what to say about that. 
Maybe you'd be better off there!

[01:42] batman: 
Maybe, but yeah, who knows. 
Anyway, so I did Perl pretty much by myself for many, many years but then I started getting more active on the [IRC](http://www.irchelp.org/) and I met some people from Oslo who also did Perl and then I started hanging out on the YAPC::Europe Conferences and stuff like that. 
So then I got more into the whole Perl community and everything. 
But for a long time I was just doing scripting by myself, so the code was really awful at that moment.

[02:19] szabgab: 
Marcus, if I am not mistaken, you are both from Oslo, right? 

[02:25] marcus: 
No, I am originally from Lillehammer, but I've lived there since 99 so I guess I'm from Oslo now. 
But I've been active in open source for a really long time. 
I think my first active contribution was translation of the Window Maker project. 
I don't know if you remember Window Maker from the 90s? The window manager for XLM?

Anyways, I've been doing Perl and some C stuff for quite a long time. 
I used to do the development using Mason, back in the early 2000s and I really disliked how disorganized it was, so when Simon Cozens came up with the Maypole project, I got involved in that and I eventually moved on to become part of the Catalyst team. 
I was release manager for Catalyst for a few years.
And more recently, I've been contributing to the Mojolicious project as part of the core. 

[03:22] szabgab: 
We had Joel from the Mojolicious project on the show. 
So do you guys still using Perl a lot in these days?

[03:35] marcus: 
Yeah, well I've been doing operations with it for the years but I've just come back to a Perl job now. 
We're working together at a company called [Reisegiganten](http://www.reisegiganten.no/), which is a travel site.

[03:45] szabgab: 
Okay, so that's not your company, is it?

[03:48] marcus: 
It's not my company, I had my own company for six years and then I went back to being an employee again. 
It's much less stressful to work for someone and get money and go home. So I'm quite happy to work at the Reisegiganten, they are a big Perl shop, they have several Catalyst applications and I've been moving them along to Mojolicious within the last couple of years, which is why they wanted to have us onboard. 
So I'm very glad to be able to do Mojo again in my daytime job, because it gives me an excuse to contribute more back to the project.

[04:20] szabgab: 
Oh that's really nice. 
So you are moving applications from Catalyst over to Mojolicious?

[04:26] batman: 
Yeah, yeah, for sure.

[04:29] szabgab: 
Okay, why is that? 
Why do you do that?

[04:32] batman: 
Well, it's a much leaner framework to work with. 
So it's like, instead of programming Java, you can just...you don't have to program that much to make stuff actually work.

[04:47] marcus: 
And we're really happy with the async capabilities that Mojo gives us. 
And also our travel site is built around Solar, which is like HP based, so using the Mojo IO loop and the async, we can do a lot of operations in parallel and still have really fast responses and stuff like that.
So being async is a really big benefit for us.

[05:07] szabgab: 
Okay, and do you...so the project you created, [Convos](https://convos.by/), that we wanted to talk about and as I understand, it's an IRC client basically, or a web interface for IRC? 
Do you use IRC at work? 
Or only for your open source involvement?

[05:29] batman: 
In my previous work, we used IRC and Convos actively and internally. 
But...

[05:40] marcus: 
At the moment, they are using a proprietary internal chat client at our new job. 
But we are planning on moving them over eventually. 
We just need to make it as good for their purposes. 
So that's one of our internal goals actually. 
So we can get it to work to make the integrations that they require for their workday.

[06:02] szabgab: 
Okay, so let's get to the beginning of Convos. 
Tell me what is it and why did you create it?

[06:11] batman: 
So, I think it's back in 2012, by accident I was talking to Marcus and he was actively using IRC client at the moment, which he really enjoyed. 
But he wanted something for himself, and me, myself, I was really tired of using IRC.

[06:35] marcus: 
Yes, like a screen-based console client, right?

[06:39] batman: 
Because I wanted to have my chat with me everywhere. 
So I was thinking I should make a web-based IRC client so I could use it on my cell phone.

[06:49] marcus: 
And be on the browser where ever you go, right?

[06:51] batman: 
Yeah, so we were starting talking about it and then we just started hacking on Convos.

[06:59] szabgab: 
Are there applications, that you can install on your mobile phone, that would allow you to use IRC?

[07:08] batman: 
At the moment we're focusing on just making it...

[07:12] marcus: 
No, he means older applications.

[07:13] szabgab: 
Others, others?

[07:15] marcus: 
Well, that doesn't really work well, if you're having your IRC and then you're only online while you're running the application and then you need to enter the proxy or something like that, and then it's really suboptimal because maybe some messages get pushed to your desktop while you're there. 
And then you connect with your web-base and you can't see the history because it's scrolled out, and so you won't be always in sync and always have access to all of the history and see what, go back and see what happened to your chat, right? 
If you use native IRC client on your mobile, you'll only connected while you open the phone. 
Now the idea with Convos,  is that you're always online, right? 
You're always connected to IRC and then you just go into your web browser or your application and continue the conversations you were having with another client.

[08:10] szabgab: 
So as I remember, I actually stopped using IRC a couple of years ago because I found that it's too much distraction, too much discussion going on, and I can't get the job done. 
But I had two ways of using IRC. 
One of them was when I had an IRC client on my own desktop and whenever I connected, then I could use it. 
And the other mode was when I had an IRC client running on a server, inside a screen-session, and then I could connect to it. 
So if I understand Convos provides this kind of capabilities?

[08:50] marcus: 
Because you have it running on a server, but it's more like a native client in your web browser, right? 

[08:55] batman: 
So even if you close your web browser, you're still actively on the IRC service that you connected to. 
So that means, let's say if you're using your desktop or your laptop at work, and then you're on your bus on your way home, then you can just open up your cell phone and you can continue the conversations and you can see and read messages on your cell phone. 
And so they are, it doesn't matter where you open up your browser, you are always connected to the same server.

[09:33] marcus: 
Yeah, and if someone mentions you while you're disconnected, you instantly see, there's like a red flag in the corner there, it's like 300 messages.

[09:40] szabgab: 
Okay, do people, how do other people see you? 
So when you're not connected to the server, but the server is still connected to the IRC channel, do they...? 
They can't see you?

[09:55] batman: 
No, just see you as if you're online.

[09:58] marcus: 
Same as if you're on screen.

[10:00] szabgab: 
Okay, so that's...you started to build, or started together? 
How did you start to build? Who started it?

[10:10] batman: 
Marcus started out and then we, after a month or something, I joined in. 
And then we just met regularly and we hacked. We were using GitHub so we could contribute and collaborate that way.

[10:27] marcus: 
I'm a big fan of the GitHub workflow. 
We were using GitHub to track new ideas, and you can see what Jan Henning has been doing for the interface and stuff like that. 
So it makes it really easy to collaborate.

[10:40] szabgab: 
Okay, so if someone doesn't use IRC or... how can you describe this feature or the software and IRC together, so...?

[10:54] batman: 
One of the focuses that we are having is we don't want the user to know that it's IRC, we just want it to be like a regular chat application. So for example, like Facebook Messenger or similar applications. 
They should feel the same way, so even though we're using IRC as a transport now, that's not really a limitation to the application. 
So let's say if you would like to have a Jabber back-end instead, you could build that instead, and you wouldn't know if you were on Jabber or IRC or whatever you're connected to.

[11:42] marcus: 
Or even like, if you just want to use Convos as your internal chat, you could just have a loop back-end. 
And the only people using Convos. Basically it's a generic chat application but IRC's a transport that we've chosen, because we mostly use IRC.

[11:58] szabgab: 
So if you...so okay, if there's a company that wants to have a chat application inside a company for its employees, can they use just Convos without having an IRC server there? 
Or do they still need an IRC server? 
How difficult would it be to set it up?

[12:15] batman: 
So I used to work at [Telenor](http://telenor.no), where one of the biggest telecom company in Norway, where we used Convos internally. 
So the nice thing about Convos there was that I was able to connect and chat with people who have no idea about what IRC was. 
I just gave them an account to Convos and then we just used it as it would be Facebook Messenger, or any other messaging service.

[12:49] marcus: 
But right now to use Convos you need to set up a simple IRC server on the backend. I eventually plan to get rid of that requirement, so that you can just spin-up a chatroom internally in the Convos application, without any IRC server, but really it's not very hard to install. 
It's just apt get install command to get IRC installed.

[13:13] batman: 
So you don't really have to connect to any global IRC server, so that was one of the requirements because some of the things we were discussing, we couldn't share with a public IRC server. 
So that's basically what Marcus was telling about now, is that we just installed IRC server on the RedHat, and then we installed Convos, and then we were up and running. 
So then we would have our own isolated chat application that were local to the company.

[13:47] szabgab: 
So IRC recently released a new version and one of the big things was the easier way of installing it. 
I've never tried to install an IRC server, and I've never tried it, so I wondered, you say, installing an IRC server is just installing the relevant package in your Linux distribution?

[14:09] batman: 
Yeah, Red Hat or Debian or something like that, it's quite easy to get up and running.

[14:16] szabgab: 
And then what do you need to install Convos?

[14:19] batman: 
There's...on our web page, which is [Convos.by](https://convos.by/), there's an installation guide, which is just a one-liner. 
So I guess you shouldn't really pipe something into your shell but if you trust HTTPS, then you can run that one-liner and it will download Convos and install it.

[14:46] marcus: 
Or you can just get the scrapes. I mean, it's very lightweight in its dependencies, so it's very quick to install. 
That was one of the things we wanted to get, the previous version was using Redis as a backend, so then you needed to install Redis and stuff like that. 
So we got rid of that requirement, now we can just use it just by...

[15:03] szabgab: 
What are the building blocks of Convos?

[15:08] batman: 
So right now, we decided to go to a plain file backend. 
So that means you don't need any MySQL or Redis or PostGRES or anything, you can just run the one-liner and then you have Convos up and running. 
And then you can start connecting to global IRC servers, so the only reason you would need to install your own IRC server would be if you need to exchange data that you don't want to...

[15:37] marcus: 
Well, if you need a company chat, basically.

[15:41] batman: 
So Convos is built on the Perl Toolchain but it's...the installer script is custom-made for Convos to make it super
simple to install. And that's one of the things that I think is really cool, is that people are joining our Convos help
chat and then they're, <q>Oh how do I install this?</q> 
And I'm just pointing them to the installation guide and then they're <q>Oh man, I just installed it and it was so simple!<q> 
So you don't need any knowledge of the Perl Toolchain yourself, so you don't need to know how to use CPAN or cpanminus or any of that, you can just download Convos and then it will bootstrap itself.

[16:34] szabgab: 
Okay, that's good, probably for most of the people who are not using Perl. 
And probably also for people who are using Perl, because easy installation is always good. 
So who is using your project?

[16:50] batman: 
We would love to know.

[16:53] marcus: 
We see the people who come and get support but you know the silence of open source people. 
You put it on internet and you don't really know who is using it, right? 
We know that some companies have it but...

[17:04] szabgab: 
Have you received any outside contributions? 
Are you two the team? Or are there more people in the team, building it?

[17:11] batman: 
So it's basically me and Marcus, discussing the design and then Joel, like you mentioned earlier, from the Mojolicious core team, he's also done some stuff and then we had a hackathon, I think it was in June, where we had two other people who were contributing and writing unit tests and implementing free text search and stuff like that. So that was really cool.

[17:43] marcus: 
And we get issues and we get people contributing ideas and stuff like that. 
And we have some pull requests as well, so basically anyone's free to open up a request and contribute.

[17:55] szabgab: 
Do you know any other projects that provide similar service or features?

[18:03] batman: 
There are a lot of different projects that have the same kind of functionality but a lot of them are online so you can't really...so let's say if you see it from a user experience perspective, then there's a lot of contributing, or sorry not, a lot of competing products but our product is...

[18:33] marcus: 
There's not as many like cell phone products like this. 
There is one or two Node-based projects that we're competing with and that makes sense I guess. Node is, just like Mojolicious, an async run-loop so it's a good platform to build the same kind of thing. 
For us it was more obvious to use Perl or course, because we know it very well and we're very happy with it.

[18:58] batman: 
But to mention some, there's Slack and IRC Cloud and you have Shout and MIbbit and there's like...yeah, all of those are hosted. But there's probably at least 20 other projects and maybe 15 of them is written in Node, I guess.

[19:18] szabgab: 
Okay, so the... I guess if I wanted to use something like this, I would probably look for something which is hosted? So I wouldn't want to set up my own..if I was using for my personal use and I wanted to access all kind of public IRC channels, then I would probably not want to run my own, if possible, I would rather run...

[19:47] marcus: 
Why would you trust a random service on the internet with your private data?

[19:55] szabgab: 
If I'm only talking on a public IRC channel?

[19:58] marcus: 
Well, you have private messages as well on an IRC server.

[20:02] szabgab: 
Okay, that's true.

[20:04] marcus: 
One of the problems for me, for instance with IRCCloud, some of the business models are prohibited. 
Like you can get started very cheaply but then if you want to be connected to more IRC servers, they want to have a lot more money per month. 
So you end up with a lot of running costs to pay for this thing, right? 
For instance, a lot of companies are using Slack now, which is fine for free, but then if you want to have your whole history, like you can on Convos, right now you can go back and search in all of the history you chatted, then you have to start paying and for a medium-sized company, that can be hundreds of dollars per month. 
Just to have a company chat.

[20:43] szabgab: 
Yeah, definitely. So the company chat, for a company chat I would definitely want to have my own everything.

[20:50] marcus: 
IRCCloud, I think I was looking, because they were limiting it by the number of IRC servers that you could connect to. 
And I want to be on freenode, or MagNET, or something, and then suddenly the price is running up, like 40 - 50 dollars a month, just for a personal account. 
For that, I can buy a hosted servers and not just run Convos but run several different things there. 
Right? 
So.. customize it or improve it, the way you want.

[21:18] batman: 
But I can see from, let's say you have no experience with CLI or you don't know how to use Linux or anything, then of course it would be difficult to install Convos but that's one of the things we want to do, hopefully in the beginning of next year, is to write a...I forgot what it's called...but in Ubuntu now, you have these self-contained packages instead of using ordinary Debian packages, so then I would like to make one of those, sorry, I can't remember what it's called, but anyway so you could actually download it and then you can install it as easy as you would install XChat or any of the other desktop clients.

[22:12] marcus: 
Even though it's been looking up the solution because I have this set-up for building images of prepared applications. 
Link pages is five dollars a month to get your server with Convos and then one click and it's installed and then you have a server in the cloud, which you can reach from anywhere.

[22:32] batman: 
And then you wouldn't have any limitations like you would have with hosted services. 
So that's probably why I would use Convos instead of just going to a hosted service.

[22:44] szabgab: 
So basically for five dollars a month, you would get unlimited connections? 
And unlimited users?

[22:52] marcus: 
You have your own server and then  you're just limited by the storage of the servers, which is like 40GB or something.

[22:57] batman: 
So you could have a lot of chat history.

[23:00] szabgab: 
So do you have any business plans with this project?

[23:04] batman: 
We were considering it earlier but now we have just been too busy to...like if you were to go into a business, then you would have a business strategy and then you would have, you would need some kind of support plan, and there's a lot of stuff that...so we kind of abandoned that idea. But one of the cool things about Convos is that it's under the MIT license so that means that if anyone else would like to run a business on top of Convos, then they could actually do that. 

[23:35] marcus: 
We are very open to that idea, if someone wants...

[23:37] batman: 
Yeah, I mean that would be awesome, if someone else would...so for example, let's say if you want to make your own hosted Convos server, where people pay you for having their account there, then you're free to do that. There's no limitations on what you can do with our software.

[24:00] szabgab: 
Who would be your dream customers, or dream users, not customers, because you're not a business?

[24:07] batman: 
One of the things that I would just love if people told us that they were using the software. 
I mean there's one of the things that I like the most, when I make an open source project, no matter if it's just a library or it's Convos or it's some other application, then one of the things that fuels me to make the application even better, and of course, fix bugs and all the other stuff, is just knowing that people use it. 
So if they just drop us an email or something and just tell us, <q>Yeah, we're using it,<q> then it would be really cool even though if it's just one person somewhere or if it's a big company.

[24:49] marcus: 
And if they fail to use it, we want to hear about why as well.

[24:51] batman: 
Yeah.

[24:52] marcus: 
So we can make sure that they don't fail any more.

[24:54] batman: 
Exactly.

[24:55] szabgab: 
Actually, regarding that. 
If someone wants to start using Convos, they can go and download, go to the website [Convos.by](https://convos.by/) and download it and install it and start using it. 
But if they need help, where can they go to get help?

[25:14] batman: 
So there's a lot of options for getting help as well and you can also see that on the Convos.by web page. 
But you can contact us on Twitter, or you can send us an email, or you can open an issue on GitHub, or you can join the Convos channel on chat.freenode.net.

[25:34] marcus: 
Or you can just go into our demo application, there's a demo that you can use online if you want to look at it before you try to install it. 
And we'll be online there and eventually will answer you. 
Maybe not 24/7 because we're both in the same timezone and have to sleep sometimes.

[25:53] batman: 
But there are people dropping in, maybe not everyday, but there are questions dropping in on the chat.freenode.net all the time so...

[26:05] szabgab: 
So is the channel, the Convos channel, on the demo server, is it connected to the Convos channel on the public IRC server?

[26:17] batman: 
No, we had some issues, because a lot of the IRC servers, like the public IRC servers, they have limitations on number of connections.

[26:29] marcus: 
Per IP.

[26:29] batman: 
Yeah, per IP. 
So that means that in the beginning we were running, you could connect to whatever you wanted but then we got banned from a lot of the networks so we had some bad publicity in the beginning. 

[26:46] marcus: 
That's why we restricted the demo, to just local IRC server.

[26:51] szabgab: 
Okay, so people were using the demo, and then that triggered a lot of connections, if I understand it right?

[26:56] batman: 
Yeah, but now the demo is locked, so you can't connect to ... you can only connect to one server that we are running. 
So we are running our own IRC server, where we are also connected to. So that means that if someone asks us questions in the demo channel then we will answer there as well.

[27:17] marcus: 
Yeah, because of course, you can be in more than one server with the full-fledged Convos. 
It's just the demo that's locked, the Convos that we are using, you can connect to several IRC servers and get all the channels listed.

[27:31] batman: 
Yeah. So we can talk a little bit about the features, which is what we just said, that you can be connected to as many IRC networks as you like. And of course, you have private conversations and then you also have chatrooms. 
That's the basic stuff with IRC. For people who are used to other internal chat applications at their work, then one of the big benefits of using Convos is that you actually have the chatrooms. 
Because then a lot of people can share ideas and discuss stuff. 
That's basic knowledge for anyone who's been using IRC but for people who are just using chat applications, then it's mostly private messages instead of having collaborative chatrooms.

[28:33] szabgab: 
Okay, and does the server automatically record history of the channel?

[28:38] batman: 
Yes. 
So you have unlimited scrollback and we're also implemented search in the backend but we haven't exposed that feature in the frontend yet. 
But that will also be unlimited, like you can search back whatever you like.

[28:59] marcus: 
I think one of my favorite features is the link embedding. So if someone shares a link to you, for instance, to do it automatically, we embed it into the chat or like GitHub Gists,  you can see a preview of the Gists that someone pastes in the chat. 
So it makes the experience more rich. 
We also have emoji support now, which is obligatory for a modern application of course, so that you can have smiling cats with teary eyes or whatever.

[29:26] batman: 
Yeah.

[29:27] szabgab: 
Okay, guys we're running out of time. 
Actually we've over the regular time limit, but that's okay because it was interesting to talk about this. 
So I would really like to thank you for coming on the show. I hope to...maybe I'll have to try IRC again through Convos, and I'll see if maybe I can handle it and maybe I'll see you there.

[29:54] marcus: 
That would be great.

[29:54] batman: 
Let us know if you have any problems installing Convos.

[29:58] szabgab: 
Okay, thank you. 
Bye bye.

[30:00] marcus: 
Bye.

[30:01] batman: 
Bye.

[/transcript]

