---
title: "CMOS #18: Timi Ajiboye on Client Manager, Resque, Friendly ID and other Rails gems"
timestamp: 2016-10-25T11:01:01
tags:
  - podcast
  - Ruby Gems
  - Sails.js
  - Nigeria
description: "Timi Ajiboye, A Nigerian Ruby developer, tells us about his current and future projects, some in Sails.js."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-18-timi-ajiboye.mp3
  size: 17224989
  time: 19:24
#img: /img/cmos/timi-ajiboye.png
#alt: Timi Ajiboye
published: true
author: szabgab
archive: true
---


Interview with Timi Ajiboye, a great discussion of his view of open source, and his work in Ruby, his favorite Ruby Gems, and his new projects in Sails.js!


{% youtube id="KcDTf0B3S00" file="cmos-18-timi-ajiboye" %}

<podcast>

<div id="person">
  <h2>Timi Ajiboye</h2>
  <ul>
    <li>[timigod on GitHub](https://github.com/timigod)</li>
    <li>[@timigod](https://twitter.com/timigod) on Twitter</li>
    <li>[@timigod](https://medium.com/@timigod) on Medium</li>
    <li>[Hello World](http://helloworld.ng/)</li>
  </ul>
</div>

<div id="links">
  <h2>Links</h2>
  <ul>
    <li>[Cruncher](http://cruncherapp.co/)</li>
    <li>[Client Manager](https://github.com/timigod/client_manager)</li>
    <li>[Resque](https://github.com/resque/resque)</li>
    <li>[API Pagination](https://github.com/davidcelis/api-pagination)</li>
    <li>[Friendly ID](https://github.com/norman/friendly_id)</li>
    <li>[HelloSails](https://hellosails.com/)</li>
    <li>[Ruby](https://www.ruby-lang.org/en/)</li>
    <li>[Ruby on Rails](http://rubyonrails.org/)</li>
  </ul>
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [timigod guest1 Timi Ajiboye]

[00:02] szabgab: 
Hello there, this is the CMOS, the Code Maven open source podcast and interview video series. I'm Gabor Szabo, your host, and with me is Timi Ajiboye from Nigeria. How are you, Timi? 

[00:15] timigod: 
I'm good, you? 

[00:17] szabgab: 
I'm really great, and I'm really happy to have you on the show. Actually, you are the fifth from Nigeria and I was wondering, do you know what a Nigerian scam is? 

[00:34] timigod: 
Yeah, yeah, I do. It's quite...yes, I do. Everybody does. 

[00:43] szabgab: 
Okay, I was wondering because I actually haven't seen a lot of those from Nigeria recently, but I saw a lot from other places, so I was wondering whether, at one point I started joking about it, oh, so many people from Nigeria on my podcast, so that's cool. Anyway, so let's start with your background a little bit, how did you get into programming and how did you get into open source? 

[01:14] timigod: 
Okay, how I got into programming. I've always been sort of drawn towards computers and technology. What really got me into programming was when I was ten, I saw my uncle messing around on his computer and I was like, <q>What are you doing?</q> And he said, <q>This is Visual Basic.</q> Like, show me. So he taught me how to hide UI elements or display them, or how to get values from what the user's inputting, so I made like a calculator, around when I was eleven. Yeah, so since then, I've always understood sort of programming, since I was ten. 

[01:56] szabgab: 
Okay, and when did you get into open source? 

[02:02] timigod: 
I'll say, I think about a year or two ago. I think a year ago. It was me and a friend of mine, we built this tool called [Cruncher](http://cruncherapp.co/), it helps you make sense of your bank statement. 
So we wanted an open source gem where people can add process for other banks. It wasn't say, there are no standards for banks in Nigeria, all the banks just do as they like. 
So you have to make something that will read each statement. 
So it made sense to make this open source project where anybody who wants to use the parser and the module, then do whatever they like, and if they want to add stuff, for us, it would be better. 
It means our project will parse more statements. So yeah, that was at least a year and a half ago. 

[03:05] szabgab: 
Okay, so why does it make sense to have it open source, and why does that plug-in system and then let people...? 

[03:10] timigod: 
Yeah, open source, for me, people tend to paint it like it's an altruistic, selfless, I think it's a tactic. 
When I say tactic or tool to be employed, in certain use cases. 
So there are some things that would never be as good as they are, if hundreds of developers didn't contribute, so open source is selfish in a sense where, so okay I build because I want, but then I know other people would like to use this, and still make it better for me and for those people making it better, it's selfish, too, so they're like, <q>Okay, this thing has some of the functionality I want but I need to add this one to it, so I can use it.</q> 
So that way everybody writes less code but gets it better, much better, much more stable. People are so different and you'd be surprised how differently people can see your code and show you what's wrong or what can be better. 
It's which is why, I think, open source is...yeah, I think it's pretty selfish. 
It's not in every scenario that it applies, that you can use open source just like, expose all the code. 
I don't think it's everything Facebook does is open source, everything that Apple does, but it makes sense in some scenarios like React or tools that we use everyday to write code, it makes sense. 

[04:49] szabgab: 
So you, if I understand, you're self-employed or you have your own company, right? 

[04:55] timigod: Yeah. 

[04:57] szabgab: 
Can you tell me about that a little bit? What kind of soft, things you are doing there? 

[05:03] timigod: 
Yeah, mostly, I do stuff for clients. 
That's most of my workload. But I have some, we have, [Helloworld](http://helloworld.ng/) has, we have some personnel, projects that we would like to get off the ground. 
One of them was Cruncher, like I said. 
To help you make sense of your bank statements, how you spent money. 
There are some other ones in the pipeline, like chat bots, but mostly we just build anything for clients. 

[05:38] szabgab: 
Web applications? What kind of applications, web applications or...? 

[05:44] timigod: 
All kinds. I personally can do web and Android and iOS. Yeah, all kinds, all sorts, anything really. 

[05:53] szabgab: 
Okay, so what is the biggest open source project that you have been involved, or the most, the one that's most interesting that you think?

[06:08] timigod: 
Most interesting...yeah, the bank parser one. 
The one where we all had to make...there were like five of us so we said, <q>Okay, you make a parser for this bank, this format, you do Excel and this bank.</q> 
It was fun, that was my first gem, so for me it was the first gem that I had something to do with. It was fun. It was nice to see how everybody just works on separate parts and everything come together. 
The other one, which is the one I made alone, for now, with no contributors, is [Client Manager](https://github.com/timigod/client_manager). 
Basically it is to authenticate clients from, if you've been in an API and you want to make it from an application or your iOS to access that API, you just need to install Client Manager to your app and it does a lot of that for you automatically. 
You can just use the GAuth auth client or you can add users like you add clients. 
And then they get their token and they can add that together. So that's two, those have been pretty... 

[07:24] szabgab: 
Okay, I'm trying to understand. 
This is called Client Manager, is it for people who want to register on the website or...? 

[07:33] timigod: 
The people who want to build Rails APIs. 

[07:37] szabgab: 
Rails APIs? 

[07:39] timigod: 
Yeah. 

[07:40] szabgab:  
Okay, and what kind of problem does it solve? I'm not sure I understand... 

[07:47] timigod: 
Okay, let me try to break it down again. 

[07:49] szabgab: 
Just so you understand, I am not a Rails person, I have never done Rails, so... 

[07:54] timigod:  
Yeah, okay, cool. 
So let me give an example, it's the same example in the ReadMe, if you built a blog with the Rails API and a JavaScript for the framework, you're going to probably have some endpoints that only users who are authors can access. 
The request that you've built in, like creating or do you think lockpoints. 
And then endpoints, like reading posts, would be unauthenticated, and this means that if someone should go to the endpoint in their browser, they will get the JSON response. 
And what would be ideal, would be to make it such that only the frontend application can access all the read murals. 
To do this, you might have to generate a random UUID and ask your frontend developer to put it in the header of their request. 
And it doesn't scale well. 
So what if you wanted to add an Android app? Or an iOS one? 
So this is where Client Manager comes in, it helps you manage all of this, with the user interface. 
You can easily just create clients, and it gets a...it generates an automatic JSON web-token, which can be used to authenticate requests, or you can create users. 
So I can just add Client Manager to my API, go to /client_manager, create a user, frontend developer, and tell him, okay, this is a client who only creates five clients. 
And he does that, and he forgets talking to each of those clients, and putting it in the header of all the requests. So it has more possibilities, like you can manage your stats, you can privately rate limits for clients, each received. 
Those are things that I would like to do in the future of the gem, so it's pretty straightforward to install, you just need to go to /client_manager and use UI to create clients or to add users that can create clients, it's there. 

[09:53] szabgab: 
Okay, do you know how many people are using it? 

[09:58] timigod: 
It's sort of dropped around ten days ago, but I have seen on [RubyGems](https://rubygems.org/), I have about 170 downloads, yeah 172 downloads. 

[10:15] szabgab: 
Do you get feedback from people? 

[10:18] timigod: 
So far, yeah, a few people. 
One person says he wants to help with tests, so I was on a call with him, telling him how it works. 
A couple of people, mostly Nigerian people, yeah. 

[10:37] szabgab: 
Mostly, sorry? 

[10:39] timigod: 
Everybody else is set and mostly people around me in Nigeria. 

[10:43] szabgab: 
Okay so you don't have a lot of access for contact with people in other countries? 
I mean, this is nothing to do with Nigeria, this... 

[10:54] timigod: 
Yeah, I know, but when I check the people who've actually stars it on, say on GitHub, they're not from around here at all.  
And there's about 50 stars, so... It means, there can't be many issues, some stars, so... 

[11:14] szabgab: 
Okay do you know, are there other alternatives for this gem, that people might use? 

[11:21] timigod: 
No, I wish there was, I wouldn't have had to build it. 
Well, maybe I don't know how to search, but I spent a large amount of time looking for something that did this, I didn't find. 
The only other thing that came close was like an Oauth manager, but it doesn't do this, because you have to be, you have to want to implement Oauth. 
But this, I can extend this to implement [Oauth 2](https://oauth.net/2/), in case you want. 
But I haven't seen anything else that does this, I wish I had, I wouldn't have had to build it. 

[11:56] szabgab: 
Okay, other open source projects? Do you have other of yours or others that you want to talk about? 

[12:05] timigod: 
Yeah, I really, really love the Ruby Rails community. 
Besides Rails, I also build API with [Sails](http://sailsjs.org/), and I do like Android and Ember. 
But no community like [Ruby Rails](http://rubyonrails.org/), which isn't surprising, I know when I build Client Manager, there is a gem for everything, everything. 
And even sometimes, people say there are too many gems, or they are too heavy, or they're too...someone will go and make a gem that is lightweight. 
Like I love Rails and the core group of them that I really like, it's small and they do tiny but indispensable things. 

There's one called [Friendly ID](https://github.com/norman/friendly_id). So Friendly ID automatically helps you handle slogs for your modules, so you can have your blog posts but you want to have slogs and you want that slog you be in the URL, rather than in /post/number, you know? 
Friendly ID just automatically does it with ease, you just need to add like two lines to your model, and it automatically handles slog creation. 

[13:26] szabgab: 
Slog creation? I'm not sure what is a slog? 

[13:29] timigod:  
So you know if you go to a blog post of something, the thing you see in the URL, it's the name of the post but it doesn't have any spaces, it doesn't have special characters, that's a slog. 
So even if you're creating stuff in WordPress, you'd use td to add it and get the slog the way you'd like. 
Well, most of the time it's automatically generated. 

[13:54] szabgab: 
So it's basically the part of the URL for that particular post, okay. 

[14:00] timigod: 
Yeah, so generally everything has to have their slog and you have to be able to find by slog so Friendly ID does that, it's very simple, and it just takes a lot of stress. 
So you can just do like a post to find by Friendly ID. And if you pass in the number ID, it works, if you pass in the slog, it works. So Friendly ID is quite nice. 

Another thing I use, I use [Resque](https://github.com/resque/resque) for a synchronous purposes. 
I don't know why I choose Resque over something like DelayedJob, I think it was just easier for me to learn how to use. 
But first of all, you create jobs in a jobs folder and you can en queue them. 
And if has this other open source gem, that's the Web Interface to see your jobs and your workers. 
So I really like how it works, I've used it for stuff like moving images from a workstation to a CDN, you don't want to have it blocking your requests. 
You just want it to spot them and move them, and it happened really fast, it moved about 16,000 images in minutes, because I had 14 different workers processing these jobs... 

[15:31] szabgab: 
And then...so the Resque API is a gem for Rails, right? 

[15:38] timigod: 
R-E-S-Q-U-E, right, for Rails. 

[15:45] szabgab: 
And then you just add it to your Rails application? 
And how do you write the client for it? Or did you have the client? 

[15:58] timigod: 
I didn't catch that? 

[15:58] szabgab: 
So that's the backbend part, that's the Ruby part, that's on the server? 
How do you write the client? Does it provide a client, in JavaScript? 

[16:08] timigod: 
Oh no, you don't need to. 
You use Resque like entirely in your Rails backend application and then you can expose, so what I did, it was just a simple endpoint, <q>move images</q> and someone can just create it and make a request. 
What you can do actually is sort of give parameters of this, but it forgets the external something like that, yeah, there's no frontend stuff to be done, because you know Rails is in Node or JavaScript, so everything is done asynchronously, so there's no need to monitor asynchronous versus stuff like that. 
And Resque does the clients as well. 

[16:54] szabgab: 
Okay, great, any other gems you would like to mention? 

[17:03] timigod: 
There are a couple. 
There's [API Pagination](https://github.com/davidcelis/api-pagination), makes it easy to do pagination for API, it's very straightforward. 

And [SearchKick](https://github.com/ankane/searchkick), is an abstraction for [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html) and it's awesome. 
So you make search in your app work even easier than it once did. 

[17:23] szabgab: 
So I guess you have used all of these, right? 

[17:27] timigod: 
All of them. 

[17:28] szabgab: 
What kind of applications have you built with these? 

[17:32] timigod: 
Okay, all kinds. 
I've build chat bots, APIs for chat bots, I've built regular CREP apps to store computers or people, and then you need to search, with pagination. 
You need to have some currency process. I've done, there's one I did for a client, it had to do with text messaging. 
You...basically you can fulfil orders with text messaging, so I added a bit to do a lot of things. 
All kinds, it varies wildly. 

[18:25] szabgab: 
Okay, great. 
So let's get back to the open source part, especially one thing that I wanted to ask that I wonder if someone wants to start contributing to open source, what would you suggest to this person? 
How to get started? 

[18:51] timigod: 
Well, usually, initially it's one thing, because I've always wanted to make a contribution to some haystack but it just felt very daunting. 
Some people who create open source projects actually tag some of their issues as for beginners, which helps, so you can go and solve those beginner issues. 
There's always a small thing that you can do, it might be a typo, it might be to just to make a method or a function look nicer. 
There's always something you can run. 
Once you start with that small thing, you'll become more confident and if you'll just refactor a class and it looks neater and the MLD requisite prerequisites, you'll become more competent at that. 
<q>Maybe I do know something, maybe I can do this,</q> and you'll be able to. 
But you'll have to...it's better if you're doing it on projects you actually want to use, and you like. 
Because that way, fixing those things would affect your own applications that you're building and there's more on the line, so there's more motivation to fix those things. 

[20:12] szabgab: 
So then you have the selfish motivation that you also mentioned earlier. 
I want this to be working better, right? 

Okay, thank you very much, I think we can get to the end of this interview. 
Do you have any other issues you wanted to mention that we have skipped over, forgotten? 

[20:42] timigod: 
I guess the only thing I didn't talk about were my blogs. 
And I wanted to mention how open source allows you to write a tutorial and then write some projects and just share it. 
So I have two, I have one [HelloSails](https://hellosails.com/) to come, entirely dedicated to building stuff with Sails, so a lot of time when I do tutorials teaching how to do stuff, I put up the code and the requisite tree, and if helps because not only does it help people who are trying to learn, but it helps me. 
Because I make mistakes and people who read my tutorial who know about one part of it more than I do, are just...have an opposite issue, or fix it. 
Make it correct. 
So it's better for everybody, it's better for all the newbies learning, it's better for me, I won't make the mistake again, it's better for them, so the HelloSail's one and the other one is JumpsSoCool. 

JumpsSoCool is quite weird because it doesn't have any particular theme, I'm just teaching how to build anything I've built before. 
So if I built a voice-activated home automation motor, I write really long tutorials on how to...which there's one series like that going on. 
I just write anything I've built, maybe because I do a lot of experiments and they never see the light of day. 
They're never public. 
So I figure that'd be a good way to show it off and to teach people how to do them. And get some much-needed help. 

[22:20] szabgab: 
That's excellent. 
I really also like to write articles, mostly because I'm learning a lot from these. 
In many cases, if you write software, then you think that you know something and then when you have to explain it, you find that, <q>Oh, I didn't know this and this and this!</q> 

[22:41] timigod:  
Yeah, it's amazing, people are so different and it opens up your mind. 
You think you've covered, in fact there are some things that, just by being a different person, you'd be more concerned about and it's amazing that everybody can work on something at the same time at different, I can't find the language. 
I really like the idea of collaboration and opening people's minds to see things. 
And again, the main thing is you can't do it all alone, which is why we have so many different kinds of developers. 

We have frontend and backend. 

We have people like me, who sort of do everything, but the frontend is my weakest aspect, I don't think I'm every going to be a full, really good frontend developer. 
But my experience in doing all of these things is different from the experience of someone doing only frontend. I'm doing backend and all of us kind of learn from each other. 
It's amazing. 

[23:57] szabgab: 
Yeah, right, and that was an excellent conversation, I think. 
And thank you for coming on the show and I think we can try to think of a couple of other projects later on and talk about those. 
A couple of months from now, or so? Okay, great. 

[24:16] timigod: 
Yeah, cool. 

[24:19] szabgab: 
So thank you very much, bye bye. 

[24:20] timigod: 
Yeah, very cool. I don't know how to pronounce your name, I meant to ask? 

[24:24] szabgab: 
Gabor, Gabor Szabo. 

[24:29] timigod: 
Okay, Szabo, cool also, nice to meet you Gabor. 

[24:31] szabgab:  
Thank you.

[/transcript]

