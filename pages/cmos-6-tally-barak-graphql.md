---
title: "CMOS #6: Tally Barak on GraphQL"
timestamp: 2016-09-10T11:01:01
description: "Interview with Tally Barak about GrahpQL being the next big protocol after SOAP and REST."
tags:
  - podcast
  - GraphQL
  - Meteor
  - web
  - Israel
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-6-tally-barak-graphql.mp3
  size: 22528898
  time: 25:41
#img: /img/cmos/tally_barak.png
#alt: Tally Barak
published: true
author: szabgab
archive: true
---


Interview with [Tally Barak](http://www.morffy.com) on how a 13 year old girl inspired her to get into programming. Getting back to programming after a 15 year long break. The impact of GitHub and Open Source.

Our main subject however is [GraphQL](http://graphql.org/) being the next big thing after SOAP and REST.


{% youtube id="Bd6A9TdGhm0" file="cmos-6-tally-barak-graphql.mp4" %}

<podcast>

## Tally Barak

* [GitHub](https://github.com/Tallyb)
* [LinkedIN](https://www.linkedin.com/in/tallybarak)
* [@tally_b](https://twitter.com/tally_b)
* [Tally Barak](http://www.morffy.com)

## Links

* [GitHub](http://github.com/)
* [StackOverflow](http://stackoverflow.com/)
* [Magic](https://en.wikipedia.org/wiki/Magic_Software_Enterprises)
* [PowerBuilder](https://en.wikipedia.org/wiki/PowerBuilder)
* [Node](https://nodejs.org/)
* [Angular](https://angularjs.org/)
* [Meteor](https://www.meteor.com/)
* [Angular-Meteor](http://www.angular-meteor.com/)
* [Apollo Server](https://github.com/apollostack/apollo-server)
* [Apollo Stack](http://www.apollostack.com/)
* [GraphQL](http://graphql.org/)
* [awesome-graphql](https://github.com/chentsulin/awesome-graphql)
* [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer)
* [Ajax](https://en.wikipedia.org/wiki/Ajax_(programming))
* [MDG - Meteor Development Group](https://www.meteor.com/company)
* [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping)
* [SOAP](https://en.wikipedia.org/wiki/SOAP)
* [Relay](https://facebook.github.io/relay/)
* [Zero to GraphQL in 30 Minutes – Steven Luscher](https://www.youtube.com/watch?v=UBGzsb2UkeY)
* [Learn GraphQL](https://learngraphql.com/)
* [Postman](https://www.getpostman.com/) in the REST world. [Chrome extension](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en)
* [Dream Factory](https://www.dreamfactory.com/)
* [Lookback](https://lookback.io/)

<!--
cuts: 3:21 14:46 18:45 
-->


## Transcript

[transcript]
  [szabgab host1 Gabor Szabo]
  [tally guest1 Tally Barak]

  [00:02] szabgab: Hi there and welcome to the CMOS, the Code Maven Open Source podcast and interview series, where you can learn about interesting projects in terms of open source projects, from interesting people, who are either using them or contributing to them directly.

I'm your host, Gabor Szabo, and with me is [Tally Barak](http://www.morffy.com). Hi Tally, how are you?

[00:24] tally: Hi, how are you?

[00:25] szabgab:  I'm really happy to have you here, on the show, because we met a couple of times and I've heard a couple of your talks and they were always really interesting. So I'm quite excited to learn a little bit more about you and some projects that you're interested in.

[00:42] tally: Okay, cool.

[00:44] szabgab: Please tell me a little bit of your background, so other people who are either listening or watching this video feed, and don't know about you. How did you get into programming, how did you get to where you are now?

[00:56] tally: Just like those actors and dancers that say, that I didn't pick my profession, the profession picked me, I think I have the same story about programming. I was very young when I was traveling and stopping somewhere, and there was, well I'm not that young, so that was back just when personal computers started, in fact. And I was standing by some girl, girl, important to note, and she wrote two lines of code in Basic, and I still remember this feeling, that I stood there at the age of 13, fascinated by what she did. And that was the moment that I realized, this is what I'm going to do for life.

And it was like that. So it's many, many years now, since I started programming. I did that as a hobby, as a kid, later on as my military service which is compulsory in Israel, later on as my profession. But the interesting twist here is, that along those years, I moved from pure programming into more management, products, other things, consulting for large firms about architecture, all those surrounding areas around programming. For about 15 years, I wasn't really doing pure programming, at the time.

So we are talking about some time back at the end of the millennium, the previous millennium, that I stopped programming. About 2.5 years ago, I got this urge again, to go back to code. A few things have changed, I was doing some other things, and then I realized, <q>Why shouldn't I go back and start doing that?</q> 

I came back to a totally different world, because it was, and especially the two things that are different from 15 or 17 years ago, we can call them [GitHub](http://github.com/) and [StackOverflow](http://stackoverflow.com/). That's the one thing that changed all the  programming experience for everyone, the GitHub with all the open source projects, and StackOverflow with all the questions, that you just post your <q>Guys, guys, I don't know what I'm doing wrong here!</q> and then someone says <q>Oh, no problem,  you are missing a semi-colon</q> or <q>You should just call it A instead of B</q> or something.

For me, that was an amazing experience and one that I said <q>I want to be part of it.</q> And since, which is for some time now, I am asking and answering on StackOverflow and various forums, helping with some open source project, and that sort of things. So yeah, that's how I got here, to be a programmer, female, not so young, which I think is pretty rare. I mean it's not very common for sure, I'm not your typical 25 years old, male.

Yeah, I know you're not 25 as well.

[04:50] szabgab: Yeah, neither I am 25.

[04:51] tally: I just found for the first time.

[04:55] szabgab: Anyway, this is interesting, what you said, because it is a little bit how, on one hand, when someone is growing up, and then the people around that person, see that person always more or less the same, they don't notice how the person changes. Because they are always there, and then someone sees that other person only once a year, or once every 15 years, then you can suddenly change. <q>How did you grow so fast?</q> So you can see the differences, the contrast, in a different way, how the industry has changed, especially open source I guess, but in general, the industry, right?

[05:43] tally: Yeah, when I stopped programming, we barely knew what is web, JavaScript was there to some extent. I think I stopped coding somewhere around 97 or 98, I'm not quite sure about the exact year. So yeah, that's what we're talking about, JavaScript 0.1 or 1 or 2, Windows maybe 95. All the web technologies, everything, that was so uncommon, you would still write in C, C++, I guess, all kind of tools like [PowerBuilder](https://en.wikipedia.org/wiki/PowerBuilder), [Magic](https://en.wikipedia.org/wiki/Magic_Software_Enterprises), you probably know the names, I don't know how many of the people that will listen to this podcast or videocast, will know what we're talking about.

[06:50] szabgab: Yeah. Okay, so what have you been doing in the last 2.5 years, since you came back?

[06:57] tally: Okay, so because I wanted to develop something which is web-based and front end, I started with JavaScript, naturally. So I just worked with it and then a friend of mine told me <q>You should really learn [Node](https://nodejs.org/) and [Angular](https://angularjs.org/), they're cool.</q> And a day later or two days later, I called him back and said <q>What were the names of the things you told me I should learn?</q> Because I couldn't even remember, that was how out-of-touch I was at the time.

So I was mainly doing JavaScript, or maybe I should say just JavaScript, and I started with Angular, which I really like. It was almost like the code generators I had before, because it was so, the first time it let you <q>hide</q> a lot of the complexity, you could just go ahead, write something, and later on understand it. But in parallel, I did a lot of reading, and watching of videos, and YouTube, and going to meet-ups, and learning other things. 

So I also learned about [Meteor](https://www.meteor.com/), which was <q>Yay, I don't really have to write a back end in PHP or something, I can just do it in JavaScript and quickly and I have almost everything already connected.</q> The whole environment, I did in  Meteor, and recently [Angular-Meteor](http://www.angular-meteor.com/) is one of the projects that I'm still quite involved, not so much in the pure development, but a bit of contributing here and there, some documentation, helping people with questions and issues, blogging a bit on it.

Recently, the new thing from Meteor group is [Apollo Server](https://github.com/apollostack/apollo-server), and I got really fascinated, back again. You go to something and you say <q>Wow, that's really nice and cool!,</q> so yeah, GraphQL and Apollo server is my last cool thing and right now I'm doing that as sort of as a hobby, an after hours kind of thing, but I hope it will go to my real-hours thing.

[10:06] szabgab: So when you are in the after hours, do you write open source applications, contribute there, or it's just mostly for your own fun?

[10:15] tally: Right now, it's for fun mainly. I don't think I have had something that I've published, I think that I took some of the things that I did as open source and then used it in a project but it was mainly a high-level. So right now it's still a bit for fun.

[10:43] szabgab: Okay, so we talked about a couple of subjects that we might talk about, because I know that you're quite familiar with quite a few of the subjects that personally at least, I would like to know but I don't. So for example, we talked about [GraphQL](http://graphql.org/), right? And  you said that could be, so what is GraphQL?

[11:06] tally: Okay, what is [GraphQL](http://graphql.org/)? That's an excellent question, GraphQL is in fact, a standard. This is not a software, and that's an interesting thing, because when you think about open source, the first thing that pops to mind is code, pure code. In fact, if you go into GitHub, which is now not the only one but GitHub now is definitely the Mecca of open source, you will find other things apart from pure software. One example for that is GraphQL, which is in fact, a standard. So if you go to the Facebook GraphQL repository on GitHub, you will find specs. And then you will find a lot of other implementations, in different languages, in different servers, starting from JavaScript and going to Go, PHP, and you name it. I don't know if there's a Perl one, but it's up to you to check.

So GraphQL is actually a standard, it is, I don't like to say an evolvement, but more like another tier, on top of [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). I mean, we are all familiar with REST API and [Ajax](https://en.wikipedia.org/wiki/Ajax_(programming)), and how do you send the data back and forth? But it turns out that REST APIs have some great features and great value but some big disadvantages and the main one of them, well, let's say the two main things are performance and documentation. 

Performance is because you are sending one request per resource, normally, and you get it back. So that means if you want a few resources and to get some additional information about each resource, that will require you quite a few roundtrips to the server and if you are doing that from your desktop with your 1GB network connection, then I guess that you're okay. Even if it's 50 or 70 or 20MB connection, but the reality is that most of us use something else for a lot of browsing and it's this big device, which is not that powerful on one side, and usually having a worse internet connection. 

So the main issue here is to say <q>I want to send one request, and get all the data I need at once, because that will be much, much more efficient, especially when I use mobile devices.</q> And GraphQL describes some sort of a standard, it's a middleware that is standing between your client and the server, receives those requests from your client, mobile, or web, or whatever, and does the multiple requests, and then returns one response with all the data. So it actually takes some of the processing that you used to do in the client, for combining data, merging it, and moves it to sort of a server, or middleware. In fact, it's another server.

And the GraphQL is describing the schema, what you should send. The good thing about it is that, that schema is very well-aligned with what is needed in the client, with how you design the user-experience in the client. Now I know it sounds very fluffy, but once you go and look at it on your screen, how you describe it and how you send a query, how it is well-documented, it is very easy to understand. And most people go <q>Wow, that's really what I need!</q> 

I don't know if you are doing demos here, or...?

[16:04] szabgab: Well, I don't know what you would need, I've never tried here. Can you show...?

[16:09] tally: Yeah, we don't really have, maybe I will just post a link to an example, it's actually a tool that is called [GraphiQL](https://github.com/graphql/graphiql). GraphQL, by the way, is a standard that was developed in Facebook when they moved from the web to a native code back in 2012, and recently they open sourced it, so then we see some implementation. One implementation is the one that was done by Facebook itself, they also open sourced the implementation, not just the spec. 

And the Meteor Group, [MDG](https://www.meteor.com/company), actually used this spec and developed their own version of a server, which is JavaScript-based, because that's their expertise, and is called [Apollo Stack](http://www.apollostack.com/), this is what you will see in GitHub, and it has the server-side and the client. 

The main thing about GraphQL is that you describe your schema, you describe how the schema is built, and you use this schema to build all your queries. It's sort of, and I'm very careful here, it's like moving your [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) to half-way through the client. I think that's almost like it, and then you have all your schema defined, but the good thing, this is what as a consultant for large firms, what is really exciting is that you don't have to connect to a single server, you can, in fact, use this middleware to connect to multiple servers if you have in your organization. 

Or even if you are a start-up and you say <q>No, I am not this huge enterprise that has ten thousands of servers</q> but even if you are a start-up, you probably connect to Slack and Stripe, for your payment, and some other services that you use, instead of developing them. Maybe you have payment, maybe you have something else for your billing, and the accounts' management, and that sort of thing, so you probably have some integration that you need to take care of.

Go ahead, check it out, because it's really, really interesting and I believe it's going to be extremely popular in the coming years, look at it as sort of some evolution. First we had [SOAP](https://en.wikipedia.org/wiki/SOAP), and most people love SOAP today, just as long as it's in the shower, and not in the code. And then we had REST, which solved some of the problems that SOAP had. And I think the next step is GraphQL.

[19:36] szabgab: Interesting, so if I understand then, basically, wait a second. So the implementation that Facebook provides, it's written in PHP, so it's only the back end part, or...?

[19:51] tally: The implementation that Facebook provides, I think I heard it was in PHP, which makes sense. I wouldn't bet a large sum on that, because I never looked at it. So Facebook provided a PHP implementation for the server and then they provided the client-side as well, that allows you to quickly use the schema and this is called [Relay](https://facebook.github.io/relay/), this is the part that I know better. I think the implementation of the server is just called GraphQL Server but I'm not 100% sure about that.

And another implementation now is the Meteor, which is JavaScript, but a lot of other implementations, and there's actually a really great talk of a Facebook guy, which suddenly I don't remember his name, but he was doing [three implementations of GraphQL in 30 minutes](https://www.youtube.com/watch?v=UBGzsb2UkeY) talk and it was 30 minutes, so he did Python, PHP maybe, and JavaScript. I'm sure about the Python and the JavaScript, I'll have to double-check the third one. So it's GraphQL in 30 minutes, something, so check it out in YouTube, it's incredible, especially this tri-lingual guy. Just you know, in 30 minutes, write in three different coding languages, that's impressive.

[21:42] szabgab: Okay, so how do you get started with GraphQL? What is the minimum thing that I need to do, to have something working?

[21:54] tally: Have something working, is probably... well, the first resource that you should go to is something called [LearnGraphQL.com](https://learngraphql.com/) and this is JavaScript-based but is, in fact, a great tutorial for seven or eight lessons, with questions and with tests. It's one of the best resources I've seen and it will tell you, through understanding, what is GraphQL to start with. It lets you play with [GraphiQL](https://github.com/graphql/graphiql), which is the user-interface for it. Sort of if you want the [Postman](https://www.getpostman.com/) for GraphQL, we'll take the equivalent in the REST world.

And then, to set up a server, it's actually pretty easy. I mean, you can take the Apollo server, which is open sourced, as I said, and implement it, but there is another cool thing which is about two companies, which are providing now GraphQL as a back-end service, similar to [Lookback](https://lookback.io/) or [Dream Factory](https://www.dreamfactory.com/), that provides you a full back end without you needing to develop anything. So they did the assembly, they're providing GraphQL with a database. So assuming you go to a database that is local, they have two different approaches. One is giving you all the surrounding services, the other is more focused on database. We'll put them in the notes, one of them is GraphQL and the other is [GraphCool](https://graph.cool/). If you want to find more about that, there's a GitHub repository which is called [awesome-graphql](https://github.com/chentsulin/awesome-graphql), and it has all the resources, just like the Awesome, everything that they are doing there.

We talked about what's in GitHub, apart from just pure code. So that's another example, we have books, I think the second most-popular GitHub repository is in fact, books. And we have all the Awesome-something repository, which gives you the main resources that you can see on different environments, so there's also an awesome-graphql there, so you can go and check it out, and there you will see also the provider, the GraphCool and the other two, that I don't remember.

[24:49] szabgab: Well, that's interesting, certainly

[24:50] tally: That's a start.

[24:52] szabgab: Yes, it's a start, and we are quite getting close to the end of our time for this interview. So I wanted to really thank you for coming on the show and I was wondering if you have anything else you would like to add that I haven't asked you? Or if you have a shout-out to some people, or...?

[25:15] tally: I didn't think about that! No, I mean, GraphQL is really cool, you should go and check it out. That will be my very simple shout-out.

[25:26] szabgab: Okay, all right, again thank you very much for coming on the show.

[25:28] tally: Thank you! It was fun.

[25:30] szabgab: And I really hope that we'll get back to talk about some other subject, because I really enjoy the way you present things.

[25:37] tally: Thank you.

[25:39] szabgab: Thank you very much, bye bye.

[25:39] tally: Bye.

[/transcript]

<!--

## Technical info

Recorded on 9 September 2016 with "Ecamm Network Call Recorder for Skype v2.6.1" using the following settings:

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
