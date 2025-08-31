---
title: "CMOS #9: Ire Aderinokun - Khaled Bot, Can I Use Embed, Formhack"
timestamp: 2016-09-21T08:01:01
tags:
  - podcast
  - CSS
  - HTML
  - JavaScript
  - Nigeria
description: "Interview with Ire Aderinokun about Khaled Bot, the Can I Use Embed, and Forhack a configurable form reset."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-9-ire-aderinokun.mp3
  size: 21405046
  time: 23:45
img: /img/cmos/ire_aderinokun.jpg
alt: Ire Aderinokun
published: true
author: szabgab
archive: true
---


Interview with [Ire Aderinokun](http://ireaderinokun.com/) about
[Khaled Bot](http://khaledbot.com/) a Slack-bot,
[The (Unofficial) CanIUse Embed](http://caniuse.bitsofco.de/),
and [Formhack](http://formhack.io/) a configurable form reset.

In which I've also learned what are CSS resets and heared about progressive web apps.


{% youtube id="W5gy7EMe7LM" file="cmos-9-ire-aderinokun" %}

<podcast>

<div id="person">
  <h2>Ire Aderinokun</h2>
  <ul>
    <li>[Ire Aderinokun](http://ireaderinokun.com/)</li>
    <li>[GitHub](https://github.com/ireade)</li>
    <li>[Twitter: @ireaderinokun](https://twitter.com/ireaderinokun)</li>
    <li>[Blog: bits of code](https://bitsofco.de/)</li>
    <li>[Medium @ireade](https://medium.com/@ireade)</li>
    <li>[LinkedIN](https://www.linkedin.com/in/iaderinokun)</li>
  </ul>
</div>

<div id="links">
  <h2>Links</h2>
  <ul>
    <li>[NeoPets](http://www.neopets.com/)</li>
    <li>[Big Cabal Media](http://www.bigcabal.com/)</li>
    <li>[Tech Cabal](http://techcabal.com/)</li>
    <li>[Zikoko](http://zikoko.com/)</li>
    <li>[BuzzFeed](https://www.buzzfeed.com/)</li>
    <li>[Pidgin](https://en.wikipedia.org/wiki/West_African_Pidgin_English)</li>
    <li>[Slack](https://slack.com/)</li>
    <li>[DJ Khaled](https://en.wikipedia.org/wiki/DJ_Khaled)</li>
    <li>[Lorem Khaled Ipsum](http://khaledipsum.com/)</li>
    <li>[Khaled Bot](http://khaledbot.com/)</li>
    <li>[KhaledBot at GitHub](https://github.com/ireade/khaledbot)</li>
    <li>[Bootstrap](http://getbootstrap.com/)</li>
    <li>[The (Unofficial) CanIUse Embed](http://caniuse.bitsofco.de/)</li>
    <li>[Can I use](http://caniuse.com/)</li>
    <li>[Can I Use embed at GitHub](https://github.com/ireade/caniuse-embed)</li>
    <li>[Formhack](http://formhack.io/)</li>
    <li>[Formhack at GiHub](https://github.com/ireade/formhack)</li>
    <li>[Offline FX at GitHub](https://github.com/ireade/OfflineFX-Codelab)</li>
  </ul>
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [ireade guest1 Ire Aderinokun]

[00:03] szabgab: Hello there, this is CMOS, the Code Maven Open Source podcast and interview series. 
I'm your host, Gabor Szabo, and with me is [Ire Aderinokun](http://ireaderinokun.com/), have I pronounced it correctly?

[00:19] ireade: Yes, that's quite good. 
So my name is Ire Aderinokun.

[00:24] szabgab: Okay, so it's really nice to have you on the show, on the podcast, and to see you in the video. 
How's everything over there?

[00:34] ireade: Thank you, thanks for having me. 
So I'm in Nigeria at the moment, in Lagos, so it's morning and I'm just starting my day.

[00:43] szabgab: That's great. 
I understand that you are a front-end developer and a designer, mainly. Can you tell me a little bit about how you got involved in this, how you got started?

[00:57] ireade: Yes, so my coming in to this kind of line of work is probably a bit different to how other people did it, because I actually studied psychology for my undergraduate degree, and then law for my masters, so I did something completely different to programming. 

But I got interested in this when I was a lot younger, so maybe when I was about 13, 14. I used to play this online game which is called [NeoPets](http://www.neopets.com/), I think a lot of people use to play it as well, so I'm not the only one. 
But it was just kind of like an online role-playing game in a way, and as part of the game you could do little bits of HTML and you could create these pages, so you could style them a bit differently. 
So that's kind of how I got started with it, that's how I was introduced to the concept of making websites or doing things like that. 
So that's how I got started and then, over time, I found that I was really interested in doing this, so on and off, I would make websites for my friends and family. 
And then more recently, after I graduated from my masters, I decided this was actually something that I want to do, not just as a hobby but as a career.

So I decided that I would just go for it and see how it worked out. 
Luckily it worked out well because I'm still doing it and I don't have to go back to law school.

[02:29] szabgab: So have you graduated law school or ..?

[02:33] ireade: Yes, I graduated almost two years ago now.

[02:37] szabgab: So does either of these, law school or learning psychology, any of these have an impact on your work or ..?

[02:48] ireade: I don't think it has an impact very directly but it's helped me in the soft-skills aspects, I think. 
So for example, for law, I learned how to write well and articulate what I'm trying to explain, how I'm trying to explain things to people, so whenever I write things, like articles for my blog, I think that my background in law really helps me try to develop my writing skills. 
And psychology, I think it helps in user-experience design a lot, because it really allows me to have a high level of empathy for people and think about how they're experiencing something. 
So I think it helps in that aspect. 
But generally, it's more impacted my soft skills in this job rather than actually learning how to code.

[03:46] szabgab: Yeah, well I guess the actual code is not, there is the psychology of the computer, of course, but it's more of understanding how people might use your website, of course, so there might be a connection between [UI](https://en.wikipedia.org/wiki/User_experience_design) and psychology?

[04:10] ireade: Yeah, I think so, because it's all about trying to understand other people, and psychology is also about trying to understand other people, so they really merge in that aspect, yes.

[04:23] szabgab: So, these days when you work, do you work for a company or are you freelancer or what kind..?

[04:30] ireade: Yeah, so I work for a company based here in Nigeria, they're called [Big Cabal](http://www.bigcabal.com/) and it's a media company. 
So at the moment, they have two publications, one is called [Tech Cabal](http://techcabal.com/), which is the biggest news tech site in Nigeria. 
And the second one is called [Zikoko](http://zikoko.com/), and it's kind of more entertainment. 
It's like [BuzzFeed](https://www.buzzfeed.com/), but for Nigerian or African audiences in general.

[04:59] szabgab: And are these websites in English?

[05:03] ireade: Yes, it's in English.

[05:05] szabgab: Okay, so there is a large, I think I understand that in Nigeria the common language is English, but there are lots of other languages? 
And do most of the people speak English?

[05:19] ireade: Yes, you find that a lot of people speak English because there are many, many different tribes in Nigeria and each of these tribes, they have their own language. 
So the common language that you would probably expect that most people would be able to speak is English or some variation of English. 
It's called [Pidgin](https://en.wikipedia.org/wiki/West_African_Pidgin_English), which is a little bit more low level, I guess, version of English. 
So you could probably at least expect that people would be able to speak that in addition to their own native language.

[05:51] szabgab: I understand. 
Any other countries, you said it's not only for Nigeria, these websites, or at least one of them, but for more of African countries, so they all too have relatively good English?

[06:07] ireade: We're trying to break out into other African countries as well, but obviously because we're based here, then Nigeria is our first audience. 
But we're also trying to break out into neighboring countries like Ghana, also places like Kenya, and just trying to break out as much as possible into markets where people are more online, so soon we'll hopefully be across the whole of Africa.

[06:32] szabgab: Yeah, that's definitely interesting. 
So you explained a little bit about how you got into computers and design and building websites, but how did you get from there to building stuff which is open source?

[06:51] ireade: I think it's kind of to do with the way I got into this field to begin with. 
So because it was a hobby for myself rather than a job, I've always been working on side-projects and things, all of this time, so it just seemed like something natural to develop into making things open source. 
So whenever I would work on something that I just thought was fun or interesting, I always find it really helpful to make it open source and see what other people think. 

Because that's kind of how I learned myself, by looking at what other people had done, people putting their code online and making things open source so other people can learn from it. 
So as much as possible, whenever I do something, I always try to give back in that way because it was so important, it was such an important part to me learning, that I try to contribute as well. 
And sometimes it's just a silly project that I work on, so it's not even something that I would make money off of, so it's just kind of fun to show people, <q>Oh, this is how I made this funny Slack bots or something like that.</q>

[08:03] szabgab: Okay, so what would be the most interesting project that you, I don't know, that made you the happiest to work on, these open source..?

[08:12] ireade: Made me the happiest? 

Well, that's a difficult question! I worked on a bunch of different things, so different things kind of hit different things for me as well, but I think one of the most fun things that I worked on was the Slack bot, which is called [Khaled Bot](http://khaledbot.com/). 
So I think awhile ago, there was kind of a [DJ Khaled](https://en.wikipedia.org/wiki/DJ_Khaled) phase, when people were making things to do with DJ Khaled, and I think I saw someone had made sort of a [Lorem Ipsum version of DJ Khaled](http://khaledipsum.com/). 
It just kind of brought the idea to me because I was also playing around with Slack bots, to make a [DJ Khaled Slack bot](http://khaledbot.com/), so that was really funny for me to do. 

I was personally cracking up to myself while I was making  it, while I was testing it, and seeing how it works, that was really fun to make.  
So I just made this bot that pretends to be DJ Khaled, so you can talk to it and then it will say things like <q>Major Key</q> and all of that. 
So that was really fun and I think a lot of people enjoyed it as well, so that was fun for me, probably one of the most fun things. 

Because a lot of my other projects, not all of them are just random, fun things. 
Some of them are actual utility, so they're less funny but probably more useful, because I don't think this Khaled bot is very useful!

[09:41] szabgab: So how can people meet this Khaled bot? 
Is it running somewhere now, or is it something that you download and start running for yourself, or how does it work?

[09:51] ireade: Yeah,  you can go to [Khaledbot.com](http://khaledbot.com/), so that's another one of my obsessions, buying domain names for a lot of these silly projects. 
So if you go to khaledbot.com, you'll see instructions for how to install it, also you can have it hosted, I use this hosting provider which is called Deep Blue and it's free so you can use by yourself. 
Or you can also just download the source and then you can run it locally yourself, and maybe make some changes if you want to add things, so you can do that. 
So you can just add it to your Slack team and whenever you're having conversations, you can just involve DJ Khaled into it.

[10:32] szabgab: Okay, especially I guess when there's some tense situations maybe, then you can just ask Khaled bot to lighten up?

[10:42] ireade: Yeah, one of my favorite features that I added, kind of for this purpose, was if you are just in a private conversation with the Khaled bot, you can just say, <q>Okay, just go and send something, go and talk to this person.</q> 
So maybe if someone is having an argument, you can privately just say, <q>Okay, go and just send a key to this person.</q> 
And then in the middle of maybe a heated argument, DJ Khaled would just pop up and just say something, so I guess that's a good utility for the bots.

[11:10] szabgab: Okay, so we made it useful now! 
Good.

[11:13] ireade: Yeah, exactly.

[11:15] szabgab: Okay, so what other projects? 
There's this <a href="http://caniuse.com/"><q>Can I use?</q></a> project, something like that, right? 
That's on your website?

[11:25] ireade: Yeah, so this is probably one of the biggest things I've worked on, because it did take a long time for me to do. 
But because I write a blog, it's called [Bits of Code](https://bitsofco.de/), and I write weekly articles about, for example, development. 

So obviously, when I'm writing about things like CSS features or JavaScript features you come across, you always want to know whether there's support for these features across all the various browsers. 
So probably the most popular website for this is this website, called <a href="http://caniuse.com/"><q>Can I Use?</q></a> and they actually have their data open source, so they have an API where you can just connect to and just get all the data. 

So I had the idea of creating an embeddable widget of the information, so whenever I'm writing a blog post, if I'm talking about Viewport units or CSS variables, I could just drop in the embed, so people could, while they're reading, just see what the support is for this feature at the moment. 
So I created that, it's probably one of the biggest things that I've created by myself because I learned a lot, I learned a lot about it because I don't think I'm that amazing at JavaScript but it's through working on things like this that you develop your skills, so it taught me a lot. 

And so I put it up, I think you can go to [CanIUse.bitsofco.de](http://caniuse.bitsofco.de/) or if you just Google <q>Can I Use Embed</q> it should show up somewhere. 
So you just have this little widget that you can embed in your blog post or wherever, and you can see the support for something like CSS, JavaScript, HTML features.

[13:12] szabgab: So it can actually tell, it can easily tell what kind of, if a certain feature, so which browser supports a certain feature that you're talking about, right?

[13:23] ireade: Yeah, exactly. 

It has something that kind of looks like a table, and it has all the major browsers, and then you can just say that you want to see what the feature support is for the current versions of each browser. 
Or you can say you want to see what will be in the future or the past. 
And then you just drop that there and then it's responsive, so it will look nice on your site.

[13:47] szabgab: Okay, and if it's embedded, then the other blogs that use this, you actually know what blogs are using this, right? 
Because you have it in your own log?

[14:00] ireade: Yeah, I haven't done much tracking actually, but occasionally I do see, I think I do have some analytics on it. 
Or sometimes I just see, maybe from reading an article and someone has used it, and then it's surprising to me, because I'm reading an article and someone has embedded it there and it's kind of like, <q>Oh, that's cool!</q>

[14:21] szabgab: Yeah, I guess it's a really good thing when you do some work and then suddenly you encounter that someone is using it.

[14:30] ireade: Exactly, because it's something that takes so much time and I feel like maybe I might be the only one that uses it. 
But for me it was worth it because I knew it was something that I wanted, so even if I would be the only person that uses it, it would still be useful. 
But it's also good to know that something that I spent time doing, that other people find it useful.

[14:54] szabgab: Okay, and is there actually any work that needs to be done on any of these projects? 
Or are they finished and there's no on-going maintenance?

[15:06] ireade: For the most parts, they are done. 
I do have a lot of ideas for how to make it better, and I think, I mean I did this almost six months ago, so I feel like if I went back and looked at the code, I probably could make a lot of improvements on it now. 

But for the Embed, in particular, there are some things I want to do. 
For example, because it's an iframe, you can't really use it in GitHub READMEs, and that's something that some people have requested, <q>How can we use it for that?</q> 
So I had this idea of making it like a canvas thing, so people can just download it as an image as well. 
So that's something that's been on my to-do list for awhile, and I hope to have that feature out soon, if I have some time. 
But if anyone wants to help me out with it, that'd be great as well, because it's open source, people can contribute as well. 
I'll be happy with that.

[16:07] szabgab: Okay, I guess it's in your [GitHub repository](https://github.com/ireade), right?

[16:10] ireade: Yeah, exactly.

[16:11] szabgab: Okay, so there's also a third project, [Formhack](http://formhack.io/), right? 
That's its name?

[16:18] ireade: Yes, so Formhack is a hackable sass-based form reset. 
So this is probably, it is actually, one of the first things that I created that was open source. So what it is, is a reset for forms.

[16:37] szabgab: Okay, wait a second. 
I looked at my website and you probably know that I have no idea about web design and it's hard for me, so what is a form reset? 
What is a reset?

[16:48] ireade: Yeah, let me try. 
So when you are creating forms in HTML, forms and everything looks different in different browsers. 
So if I just put an input element that says <q>Okay, I want the user to be able to input text here.</q> 
If I just drop that into the page, it's going to look different between different browsers. 

So a reset, a CSS reset, is basically something that you add to try to normalize the way things look across different browsers. 
Because by default, different browsers may add specific CSS rules to specific elements on the page, so you want to add something at the very beginning of your CSS to just say <q>Make sure everything is the same.</q>

So forms in particular are quite difficult, because the different browsers, they have a lot more heavy influence on the way these things look, so form elements tend to look much more different between different browsers, more than other elements on the page. 
I wanted to create a reset for forms that was also configurable, so instead of just saying <q>Make sure everything is this width, or has no margins, or no paddings, or something like that,</q> it's something that you can actually configure. 
 As you're doing the resets, you're also defining what you want it to look like as well. 
So instead of just a basic reset, it's just something that you can, as you're doing the reset, you can style it the way you want it to be. 
That's basically what it is.

[18:34] szabgab: So, just to understand, I'm using Bootstrap, is it something that can work with Bootstrap, or these frameworks, or is it something that you would use, if you don't use any of these frameworks?

[18:50] ireade: It's something that you would use if you don't use them. 

Because, so for Bootstrap, they've already defined what the styles are going to look like. 
So whereas, what this is, is something where you want to define what you want things to look like. 
In Bootstrap, you can tell like buttons always have a certain look, or all these elements have a certain look, but with this, it's kind of for you to say what you want it to look like. 

So it's more easy to change things using this, rather than using something like Bootstrap, where all the things are already predefined for you. 
Whereas, this gives you the opportunity to make changes much more easily without having to write out the CSS for everything always from scratch.

[19:33] szabgab: And do you have any idea how many people use this? 
Or how many websites? 
Do you have any feedback ..?

[19:40] ireade: I don't know how many people use it, because it's something that you just include in your projects, when you probably minify your CSS. 
I'd probably be able to tell. 
But it has almost 300 stars on GitHub now, so I guess that's how many people like it, I don't know how many people use it.

[20:05] szabgab: Yeah, I guess it's usually a lot more are using it than people just clicking on that is an effort that not many people make, and there are not that many people on GitHub either, just using stuff from there. 
Yeah, that's really nice and do you have more work on that, too?

[20:26] ireade: Not really, I think that has probably cooled down in terms of things that need to be done. 
I think, if people want more features, that's something that can be added. 
But for the moment, there's not really anything that needs to be fixed, it's more really just kind of enhancements.

[20:46] szabgab: Nice. 
What other plans do you have? 
Do you have any specific project plans, something else?

[20:53] ireade: That I'm working on right now? 

Lately I've been doing a bunch of work with progressive web apps, actually. 
So I've been playing around with how to create them and things like that. 
And I think about a month ago, I was giving a talk about progressive web apps and I created this project, which is called [Offline FX](https://github.com/ireade/OfflineFX-Codelab), so it's basically an FX exchange-rate app, but it's a progressive web app, obviously. 

So I've been working on that and that's been really interesting. 
I demoed how I made it into a progressive web app, so I put the source for that on my GitHub as well, so you can see how you can take a web application and convert it to a progressive web application.

[21:42] szabgab: That's cool. 

Okay, it was really very nice to talk to you and very educational about all these projects. 
Do you think there are any other subjects that we haven't touched, that you would like to talk about? 
Or anything you haven't mentioned?

[22:01] ireade: You can check out my websites, or actually if you can check out my blog, it's called [Bits of Code](https://bitsofco.de/), like I mentioned. 
I'm sure there's a bunch of stuff I've done, because I sometimes just feel like working on something, and just staying and just build something, and I'll usually write about it on my blog. 
So if you are interested in open source, or just learning about front-end development things, you should definitely check it out. 
I write an article once a week and sometimes I talk about projects I'm working on, or sometimes I just write articles on particular HTML, CSS, and JavaScript things. 
I try to break things down that are probably, seem like they are very complex, but just the process of breaking it down and explaining exactly how things work, so that's what I do with that. 
You can check that out.

[22:53] szabgab: That's great, thank you. 
Any shout-out to anyone, before we finish the podcast?

[23:06] ireade: Okay, shout-out to everyone who follows me on [Twitter](https://twitter.com/ireaderinokun). 
I'm also quite active on Twitter, so you can always ask me questions, and it's a good place to interact with, not just me, but I think a lot of people in this field tend to interact on Twitter. 
It's also just a good place to ask questions to people.

[23:28] szabgab: Yeah, I've noticed that. 
I follow you and I see you talk about a lot of interesting stuff, yeah. 
I really thank you for coming on the show, it was really great, and I hope to have you in a future episode again.

[23:41] ireade: Thank you.

[23:42] szabgab: Okay, bye bye.

[23:44] ireade: Okay, bye!

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
