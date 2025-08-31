---
title: "CMOS #15: Prosper Otemuyiwa - Laravel"
timestamp: 2016-10-07T21:01:01
tags:
  - podcast
  - Laravel
  - web
  - Hackathon
  - Nigeria
description: "Prosper Otemuyiwa"
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-15-prosper-otemuyiwa.mp3
  size: 25462851
  time: 27:37
#img: /img/cmos/prosper-otemuyiwa.jpg
#alt: Prosper Otemuyiwa
published: true
author: szabgab
archive: true
---


Interview with [Prosper Otemuyiwa](http://goodheads.io/) from Nigeria about [Laravel](https://laravel.com), being a GDE and a lot of other things.


<podcast>

<div id="person">
  <h2>Prosper Otemuyiwa</h2>
  <ul>
    <li>[GoodHeads](http://goodheads.io/)</li>
    <li>[Twitter: @unicodeveloper](https://twitter.com/unicodeveloper)</li>
    <li>[GitHub](https://github.com/unicodeveloper)</li>
  </ul>
</div>

<div id="links">
  <h2>Links</h2>
  <ul>
    <li>[Google Developer Expert](https://developers.google.com/experts/)</li>
    <li>[National Youth Service Corps (NYSC)](https://en.wikipedia.org/wiki/National_Youth_Service_Corps)</li>
    <li>[Igbo language](https://en.wikipedia.org/wiki/Igbo_language)</li>
    <li>[Andela](https://andela.com/)</li>
    <li>[awesome-opensource-apps](https://github.com/unicodeveloper/awesome-opensource-apps)</li>
    <li>[Laravel](https://laravel.com/)</li>
    <li>[Laravel Forge](https://forge.laravel.com/)</li>
    <li>[Envoy](https://laravel.com/docs/envoy)</li>
    <li>[Laracast](https://laracasts.com/)</li>
    <li>[Jeffrey Way](https://twitter.com/jeffrey_way)</li>
    <li>[Railscasts](http://railscasts.com/)</li>
    <li>[laravel-paystack](https://github.com/unicodeveloper/laravel-paystack)</li>
    <li>[laravel-emoji](https://github.com/unicodeveloper/laravel-emoji)</li>
    <li>[laravel-mentions](https://github.com/unicodeveloper/laravel-mentions)</li>
    <li>[laravel-hackathon-starter](https://github.com/unicodeveloper/laravel-hackathon-starter)</li>
    <li>[jwt-for-babies](https://github.com/unicodeveloper/jwt-for-babies)</li>
    <li>[es6-for-babies](https://github.com/unicodeveloper/es6-for-babies)</li>
    <li>[auth0 jwt](https://auth0.com/docs/jwt)</li>
  </ul>
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [unicodeveloper guest1 Prosper Otemuyiwa]

[00:02] szabgab: 
Hello there, this is the CMOS, the Code Maven open source podcast and this time, it's only a podcast, not a video. 
This is your host, Gabor Szabo, and with me is [Prosper Otemuyiwa](http://goodheads.io/). 
Hello Prosper!

[00:17] unicodeveloper: 
Hi Gabor!

[00:18] szabgab: 
How are you?

[00:19] unicodeveloper: 
I'm fine, how are you doing?

[00:21] szabgab: 
I'm really good. 
I'm a little bit sad that we couldn't manage to set up the video properly this time, but I hope the listeners will forgive us this time.

[00:33] unicodeveloper: 
I hope they do.

[00:35] szabgab: 
So, let's talk about one thing that we talked about a little bit earlier, about your handle, the <q>[Unicodeveloper](https://twitter.com/unicodeveloper).</q>

[00:45] unicodeveloper: 
Oh, okay, so how that came about, actually very funny. 
Back in college, somebody called me <q>Unicode</q>, you know when he entered my room. 
Because a lot of people come to my room to look for programming solutions, to ask me how they could go on, creating apps and stuff, back in the university. 
So he called me Unicode, it sounded nice. I also got to to intern at a place just immediately I was done with school.
And my boss there, too, was calling me Unicode. 
So I was, <q>Okay.</q> 
So I wanted to create a Twitter handle, no actually I had a Twitter handle, and I was trying to revamp it. 
I was trying to get the new handle to become much more active on stuff. 
So I just said, <q>Okay, let me combine Unicode and Developer. 
And to become [Unicodeveloper](https://twitter.com/unicodeveloper).</q> And it sounded like a good name to me then, so I just said, <q>Okay, let me use it.</q> 
And here we are today!

[01:39] szabgab: 
Great, so I understand that you recently became a [Google Developer Expert](https://developers.google.com/experts/)? 
Is that right?

[01:48] unicodeveloper: 
Yes, that's actually very true.

[01:50] szabgab: 
So tell me, your original story, from the beginning until the point where you become a GDE?

[01:58] unicodeveloper: 
Wow...oh my God...well, okay, so I guess I'll start from when I was in university. 
So I graduated from the university three years ago. 
And yes, so in Nigeria, we have a compulsory one-year service program, where you have to serve the government. 
So I went for that, I finished in 2014...

[02:28] szabgab: 
What is this? 
What is this program, the one year?

[02:31] unicodeveloper: 
It is called [National Youth Service Corps](https://en.wikipedia.org/wiki/National_Youth_Service_Corps), NYSC, so you'll be transported on other states for one year, to just work for the government. 
And they give you some peanuts, small amount of money, to survive. 
So it's almost like..

[02:49] szabgab:  
Why is that?

[02:51] unicodeveloper: 
They said it's the first time, people from different regions, so I really don't know if they use the same purpose, but back when it was created it was because the people from the west were so different from the people from the north, there was no collaboration. 
So they wanted collaboration between people, so that's how the program came about. 
To transform, on the path of the nation, that's where you get to know new people and you interact with people from different culture, people can bond and become friends and good things can come out of that. 
So that was the purpose of the program, I guess.

[03:27] szabgab: 
So do you think that it worked for you? 
Have you met a lot of different people, from different...?

[03:33] unicodeveloper: 
When I was transported east, so I met some new people but, to be true, I still met a lot of people from my own culture, from Lagos or hereabouts. 
So I really don't know but I really loved it during my time, because I got to learn new things, I got to learn the language they were speaking there, which is [Igbo](https://en.wikipedia.org/wiki/Igbo_language), Igbo language. 
And what else...I think it was cool for me but for some other people, it was not really that good. 
Some people were angry, trying it for one year. 
But for me, it was kind of a nice experience.

[4:14] szabgab: OK.

[4:16] unicodeveloper:
Yeah, so after my youth service, I joined an organization called [Andela](https://andela.com/). 
Andela was barely started, so I joined an organization called Andela where I started working as a technical trainer. 
So if you don't know Andela, a little context. 
Andela is the company that Mark Zuckerberg and Google Ventures invested in some 24 million dollars. 
It was on the news. 
And Mark Zuckerberg came to Africa recently and that was one of the places he came to check out. 
So that's a little context about Andela. 

So back then, Andela was just starting up, so nobody knew about Andela like that, it was just starting up. 
So I joined, as a technical trainer and I guess a lot of things happened there. 
A lot of things, the mission of Andela is actually to train people in Africa to become world-class software engineers, so that they can just outsource those developers to companies in the U.S. 
Because a lot of companies in the U.S. were finding it difficult to get affordable developers since the market was saturated, because a developer in the U.S. was very expensive, so if you have brains in Africa, you could hire a developer from Africa at the much lower cost. 
And see the same output you get by hiring a developer from the U.S. 
So that was the purpose. 

So we're training these guys in the art of software development, a lot of that. 
So that was where I became very active in open source. 
I started my open source bouts in Andela. 
I always dreamed my evangelizing in Andela, I was always trying to inspire people to be world-class, to know the new processes in world software development, to test their code, I was really big on open source projects and I was also speaking at events. 
I was organizing meet-ups, I was just trying to bring the Nigerian developer community to a place where people outside of Africa can look at Nigerian community and say <q>Wow, these guys have a handful of very good, awesome developers. 
These guys have the community, these guys are good.</q> 
We needed the credibility, so that was just my focus and apparently, I guess I did well. And someone nominated me to be a Google Developer Expert. 
And I went through all the interviews, apparently I also did well, so here we are. I'm now a Google Developer Expert.

[06:39] szabgab: 
So congratulations!

[06:43] unicodeveloper: 
Thank you very much.

[06:44] szabgab: 
Back to Andela a little bit. 
Is it only working in Nigeria? 
Or does it have operations in other countries in Africa?

[06:54] unicodeveloper: 
Yes, so Andela started in Lagos, so Andela is in currently Lagos. 
Andela is in Kenya, I think they have plans of moving to South Africa, I'm not really sure about that for now. 
Then they also have offices in the U.S. 
They have an office in the U.S., yes, so that is how Andela is right now.

[07:15] szabgab: 
Good, but still there are a lot of other countries in Africa, so do you have connections in other countries, as well? 
Personally, or...?

[07:27] unicodeveloper: 
For Andela or for me?

[07:27] szabgab: 
No, for you, personally, within the high-tech community especially?

[07:33] unicodeveloper: 
Okay, yes, so I have a lot of developer friends in Kenya. 
I also have some developer friends from Uganda, from Ghana, and so my goal is to get to a lot of those other African countries and organize meet-ups and conferences. 
But right now, I think I'm organizing my own life. 
Like on Twitter, so I make a lot of noise on Twitter about development and being a world-class developer. 
So I have a lot of people that follow me from those countries. 
So from Ethiopia, from Kenya, from Ghana, from Zimbabwe, from Uganda, and I've just been to a few of those countries, like Kenya and Tanzania. 
I am hoping to go to Ghana this month and then I will start trying to plan my trips to get to see developers in these other countries.

[08:34] szabgab: 
Interesting, okay...so open source? 
You do all kinds of open source projects. 
There's one, it's actually not a project I think, it's the [awesome-opensource-apps](https://github.com/unicodeveloper/awesome-opensource-apps)? 
I think that's a repository that you maintain, right?

[08:52] unicodeveloper: 
Yes, yes, I do. 
Awesome-opensource-apps is a... so, one of the things I observed when I was in Andela, was I discovered that when people get into programming for the first time, they learn the fundamentals of programming. 
They learn operators, they learn functions, they learn return types, now those are the basics of programming, right? 
Now how do you transition from learning the basics of programming to building a full-fledged app, okay? 
So you come and you say <q>Oh, I'm going to use HTTL and CSS with these.</q> 
Or there's a database that maintains this information. 
Or, okay there's this, oh that's wrong. 
How do you put all these resources together, how do you put all this stuff together? How do you get to do push notifications? How do you get to understand how programmer workers work? 
How do you get to understand how to do this work? 
All of those complex processes, so I just looked and I was always on GitHub, so I discovered, <q>Oh, we already have open source apps.</q> 
We have other things existing that people just...developers just found it in their minds to put it online for people to look at the code. 

So I was, <q>Oh, if you could have a place where you could find different open source in different languages or different frameworks so that somebody that's past the level of trying to understand the basics, can just jump into that app, look at the features it implements, look at how it's been implemented online, then learn from it, and go ahead and implement it in your project.</q> 
So that's how the Awesome-opensource-apps came to be and currently I discovered a lot of people are finding it very useful. 
I mean it has about 250 stars already and a lot of people are contributing to it. 

[10:41] szabgab: 
So it's a list of projects, right? 

[10:44] unicodeveloper: 
Yes, it's a list of open source projects.

[10:46] szabgab:  
Okay, and are these projects...are these web applications, or other things as well?

[10:52] unicodeveloper: 
Yeah, they are mostly web applications, so I added a section of interest especially for mobile apps, so I'm hoping to get more mobile apps there also.

[11:04] szabgab: 
And are these applications things that you usually download and run by yourself, or are these websites that are live websites that you can...?

[11:19] unicodeveloper: 
So, 90% of them are live. 
They're live and you can still also download and install on your own local machine.

[11:30] szabgab: 
Okay, but they are actual websites doing something already. 
So most of the people would only contribute and then hopefully get into the real website?

[11:41] unicodeveloper: 
Yes, exactly. So yes, you can actually contribute to get mention to the real web app or websites, and you'll see it start working.

[11:50] szabgab: 
Yeah, I did something like this, only for the Perl community. 
It was a really, really small list of applications. But I definitely will look at your list and maybe I'll send a couple of pull requests, so you include...

[12:05] unicodeveloper: 
That would be totally awesome! 
I'm open, I'm very open to these words.

[12:09] szabgab: 
Good, but you, if I'm not mistaken, you're mostly a...so you do a lot of PHP, right?

[12:18] unicodeveloper: 
Yes, I do a lot of PHP. 
Also [Laravel](https://laravel.com/), which is the PHP framework. 
If it were more recently, I would do a lot of JavaScript because the way the world is structured now, JavaScript is the most popular language and it's used everywhere. 
So you can't run away from it. 
So now I'm doing React, I'm doing Angular, I'm doing Angular 2, stuff like that.

[12:44] szabgab: 
Okay, but can we talk about Laravel a little bit? 
Can you explain what is it? I know the name, mostly..?

[12:52] unicodeveloper: 
So Laravel is an open source framework, that's built on PHP, so Laravel currently, quote me anywhere, currently Laravel is the best PHP framework to use to build web applications because a lot of things are taken care of for you. 
Like you have built-in authentication system, you have a very bubbly Laravel community, you have a lot of Laravel packages, that you can just plug into your application and within a couple of hours you have a fully-functional web app. 
And it's just awesome, the community is great. So that's one thing I love about Laravel.

[13:32] szabgab: 
Okay, what kind of applications are being built with Laravel?

[13:39] unicodeveloper: 
Well, virtually any type of web application. If you want to build a content-management system, if you want to build a build system. 
For example, [Laravel Forge](https://forge.laravel.com/) is a system that you can use to deploy applications that were produced by the criteria of Laravel. And you use Laravel to build it. 
You can also build [Envoy](https://laravel.com/docs/envoy). Envoy is a system that you can also use for deployments. 
Deployments with no downtime. And you can build any type of web application you want to build with Laravel, any type basically.

[14:11] szabgab: 
Okay, so how would you get started with Laravel? If someone wants to learn it?

[14:19] unicodeveloper: 
Oh, so I got into Laravel in 2014, so I joined just before I started the one-year program that I told you about. 
I joined a company called Cart, that was the name of it, I was dealing with market PCs and stores. 
So we were meant to rebuild the platform, using Laravel. 
And there's not a lot of difference between Ruby and Laravel, so that was the best option. 
So we had to start researching about how to build an application in Laravel. 
So that's how I came across Laravel and since then, Laravel has got in my heart. 
Oh my god, I just love Laravel.

[14:59] szabgab: 
Okay, that's great. 
Actually there is a dog behind you somewhere, we can hear it. 

Anyway, what I actually wanted to ask you, is how do people get into Laravel today? 
So if someone wants to start using it, what would you suggest to do?

[15:22] unicodeveloper: What would I suggest for...? 
I didn't get that.

[15:24] szabgab: 
If I wanted to start to use Laravel, to build a web application, where would you suggest me to go?

[15:35] unicodeveloper: 
I would suggest you to go to [Laracasts](https://laracasts.com/). 
Laracasts is the website that is build by [Jeffrey Way](https://twitter.com/jeffrey_way), Jeffrey Way is one of the very popular PHP guys, he did a lot at Tuts+. 
He also has written a lot of articles in different publications in the world and is the best teacher I've ever come across. 
So if you want to do stuff in Laravel, make sure you create an account on Laracasts.com.

[16:01] szabgab: 
I guess there are screencasts, right?

[16:04] unicodeveloper:  
Exactly, there's a screencast. 
I don't know if you know of [Railscasts](http://railscasts.com/), so it's something similar to Railscasts but this one is for Laravel and it's awesome. 
Very awesome!

[16:13] szabgab: 
Okay, that's great. 
You have a couple of Laravel related, I don't know if these are extensions, plug-ins, on [your GitHub](https://github.com/unicodeveloper)?

[16:23] unicodeveloper: 
Yes, I have a couple of Laravel packages that I built, at least 11 or 12 of them, at least.

[16:32] szabgab: Give me the highlights?

[16:36] unicodeveloper: 
Okay, so I have one I built for a payment company in Niger, [Paystack](https://github.com/unicodeveloper/laravel-paystack). 
So I did Laravel-Paystack, so if you're trying to integrate a pay-system into your application, you can use it. 

Then I also did [Laravel-Emojis](https://github.com/unicodeveloper/laravel-emoji), Laravel-Emojis is just a Laravel package that can help you with using different types of emojis in your applications, so you want to build an application that has emojis, you can use Laravel-Emojis because it has the expressive methods, like I used to call emojis.  
You can also dump an emoji down with another name, and all of that. 

And you also have [Laravel-Mentions](https://github.com/unicodeveloper/laravel-mentions), so Laravel-Mentions is a package that helps you to be able to do the type of mentioning you do on Facebook. 
So on Facebook you do <q>@Prosper,</q> it brings the dropdown, I mean once you are on @, it brings the dropdown of the potential people you are trying to mention. 
So with that package, it's a good application, a Laravel application, that package was done in PHP and JavaScript. 
So once you do the @ and connect it to your database, it brings suggestions once you put the first character, it will bring suggestions of the person you're trying to mention easily. 
So you don't have to swear at it. 
And this is the package for that. 

Then, I think one of the most popular ones I did, was the [Laravel-Hackathon-Starter](https://github.com/unicodeveloper/laravel-hackathon-starter), so I don't know if I should call that one a package or a build app. 
It's more of a boiler-plate tool.
So for people who want to build web applications, very fast, you don't want to think about it, think about adding emojis or use this API, it just gets the boilerplates. 
So the boilerplate has integration with several internet providers, it has integration with about 80 APIs from Slack, API from Clockwork, to LinkedIN, different levels of API that you need. Message API, all of that. 
All of that, in just one piece. 
So what I was really thinking about is really people who want to be MVPs. And people that find themselves in hackathons. In hackathons you don't have time, you just want to build your products. 
So if you want to build in Laravel, you can just use my boilerplates, everything is set up for you from the authentication to the social media login to all the APIs you need to use, at least 18 of them. 
So you can choose from, you can just filter them out and before you know it, your hackathon app is ready. 
So and I also thought, <q>Oh, this can just work for every piece, not just hackathons.</q> 
And it's funny how I put it out there and within a week, it became very popular, got a lot of stars, the PHP editor of Sitepoint got to know about it. 
Got it evangelized, people found it very useful.

[19:21] szabgab: 
Okay, do you still work on these projects? 
Or are they finished?

[19:28] unicodeveloper: 
So, I've not touched it in awhile. 
The last time I touched it was about five months ago, so I'm planning on doing a re-fashion on two of the projects. 
Also, upgrade to Laravel 5.3 and also add, I have some ideas of some awesome stuff I want to add to the projects, so I'm just thinking around it and I'm going to start on the re-fashion very soon. 
It's going to be great, it's going to be awesome.

[19:49] szabgab: 
Okay, looking forward to it. 
Maybe I'll learn a little about Laravel and see, it's interesting actually to build these case-studies, so when you have a...you learn a new framework and then you need to try it out, then usually it's better to do something, I think, that you already know the business behind, so you already understand that part and you don't have to figure out that part as well.

[20:18] unicodeveloper: 
Exactly, exactly, totally makes sense.

[20:21] szabgab: 
Okay, so as an ending of this podcast, what are your plans, open-sourcewise or workwise?

[20:35] unicodeveloper: 
Okay, so I...oh my God, I have a lot of plans! 
I am very much a community person so I...it's a passion for me to see upcoming developers grow from this stage where they knew nothing, where they are looking like Jon Snow, to this stage where they become Jon Skeet. 
Like they become a programming badass. 
So I'm always thinking about projects, open source projects, and also articles on software that I can write. 

That can make people easily understand some concepts so there are some concepts in programming that people just have few ideas about, normally indexed, so right now I'm trying to work on a series called <q>For Babies.</q> 
So I want to do <q>Laravel for Babies,</q> 
I want to do <q>SQL for Babies,</q> [JWT-for-Babies](https://github.com/unicodeveloper/jwt-for-babies), nobody knows about that yet. I just put, okay I told one person. 
So if you go to my GitHub, you'll see I created some repos, [es6-for-babies](https://github.com/unicodeveloper/es6-for-babies), I'm trying to work on that series. 
And I want to...it's going to be like an open source book. 
In a way, if you really don't understand this concept, you can just jump in and to give you a very bare, basic explanation of what you need to know. That's within five minutes or ten minutes of getting on, you'll be understanding the concepts that are really very difficult, for a long time. 

So that is my plan right now, and I would like to write more articles, write more tutorials, I'm also working on building an application platform right now, where I can do a lot of screencasts for people to learn how to build popular clones, using Laravel to build those clones. 
So you can build a clone of AirBnB, build a clone of Facebook, a lot of that. 
And I'll go through the process from scratch to finish. 

So those are the ideas I have around in my head right now. 
Also, for example, I work on [Auth0](https://auth0.com/), we just released a handbook called the JWT Handbook, where you can learn all about JWT web cookies, it's good that I was also part of the people, I did code-samples for the book and did some edits and the book is out there now, so anybody that wants to know about JWT, you can go to [Auth0 website](https://auth0.com/docs/jwt) and also just download the book. 

So those are the things I've been working on and thinking about right now concerning the open source community. 
Recently also, my friend and I, Kristen, she is from an Angular community here in Nigeria, so we plan to do talks around Angular 2, and all of that. So those are my ideas.

[23:33] szabgab: 
Interesting, most of your open source projects are generic, can be used by anyone, anywhere in the world. 
But the community part, I guess, it's more focused on Nigerians or Africans in general? 
When you are thinking about things that you are planning to do, or anything, what kind of people do you have in your mind?

[23:59] unicodeveloper: 
So first of all I have Nigerians in my mind, because I'm a Nigerian. 
I was born here and I schooled here, I was brought up here. So no foreign education of any type, everything was in Nigeria here and I still stay in Nigeria, too. 
Any time I'm trying to build something, any time I'm trying to organize an event or meet-up, the first things I think about is Nigeria. 
I cannot think about other parts of the world. 

So for example, just two weeks ago, I was in Kenya for the [DevCraft Conference](http://dev-craft.co.ke/), I talked about it so a lot of people know about it. 
A lot of people came for the session I presented, so I also travel frequently to other African countries to speak. 
But that just started, I haven't come very far with that, but I know very soon I'm going to be doing a lot of that, more often.

[24:55] szabgab: 
Okay, good. I think I ran out of these questions now, even though I think I have quite a few more. 
But I guess I'll keep them for a follow-up session. Hopefully in a couple of weeks from now, or months. 
What do you say?

[25:13] unicodeveloper: 
Okay, yeah, that would be great.

[25:17] szabgab: 
Okay, so thank you very much for coming on the show, do you have anything additional that you wanted to say or ..?

[25:29] unicodeveloper: 
Well, I think everything I need to say is just for developers out there. 
I just like to tell developers that you can be a better developer if you start thinking about building tools for other developers. 
It has a way of expanding your way of thinking. 
That it's a different ball game when you're building applications for clients or for the general populace and it's a different way of building for other developers. 
Now building for developers, now it's for people who are very smart, smart people like you, so when you're building things for them, you think about a lot of things. 
Okay, what about this situation, what about this situation, what if the developer decides to do something like this? 

It has a way of expanding your horizon and you learn a lot, you get to learn very fast. 
So people constantly ask me how I've been able to learn a lot within the few years I've been developing, or how I became a Google Developer Expert, or how I have done all these open source projects. It's because I decided to start building tools for all of us. 
So it's helped me, it opened my horizon. 
I saw very popular developers, I started looking at their code, I looked at how they...actually I was stalking these guys, stalking them, to understand their thought process. To understand how they do things, I look at their code. 
I try to duplicate it, I try to see. 
So every time I go somewhere, every time I'm eating, anything I'm doing, I'm always thinking about how I can put it to an open source project. 
If I'm drinking beer today, I'm thinking of how I can turn that beer into an open source project. 
So it has affected my thinking, it also helps me grow as a developer. So I guess that's my advice, that is what I have to say right now.

[27:15] szabgab: 
That's excellent advice, excellent advice, thank you. And thank you again for coming on the show and I hope to see you, and I hope to have a video next time.

[27:26] unicodeveloper: 
Yeah, that would be great, me too, I really want to have a video, it would be awesome to see my face and know my lips are moving.

[27:34] szabgab: 
Okay, bye bye.

[27:37] unicodeveloper: 
All right, thank you, bye.

[/transcript]


<!--

## Technical info

Recorded on 7 October 2016 with "Ecamm Network Call Recorder for Skype v2.6.1" using the following settings:

<pre>
QuickTime Options:
  Audio Encoding: Uncompressed

Recoding Option:
  Record Video: Audio only
</pre>

-->
