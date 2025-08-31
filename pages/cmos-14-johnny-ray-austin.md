---
title: "CMOS #14: Johnny Ray Austin - Mo - Django - VueJS"
timestamp: 2016-10-06T19:01:01
tags:
  - podcast
  - Django
  - VueJS
  - web
  - USA
description: "Interview with Johnny Ray Austin about the Mo project for creating Django based projects and VueJS for front-end development."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-14-johnny-ray-austin.mp3
  size: 20580712
  time: 20:49
img: /img/cmos/johnn-ray-austin.jpg
alt: Johnny Ray Austin
published: true
author: szabgab
archive: true
---


Interview with [Johnny Ray Austin](https://johnnyray.me/) about how he changed his major from aerospace engineering to computer science and found the field he loves! He's now the Director of Technology at <b>ISL</b> (formerly called iStrategy Labs), which does a lot of social media AOR (agency of record), website design/development, applications, and content work. The ISL Mo project, available on their [GitHub](https://github.com/istrategylabs), includes skeletons for static, Django, and Node.js website deployments, to allow developers to get up and running in minutes, with a framework that complies with current best standards.


{% youtube id="6j4tUUwOU3w" file="cmos-14-johnny-ray-austin" %}

<podcast>

<div id="person">
  <h2>Johnny Ray Austin</h2>
  <ul>
    <li>[Johnny Ray Austin](https://johnnyray.me/)</li>
    <li>[Twitter: @recursivefunk](https://twitter.com/recursivefunk)</li>
    <li>Director of Technology at [ISL](https://isl.co/) [@istrategylabs](https://twitter.com/istrategylabs)</li>
    <li>[Blog](https://medium.com/@recursivefunk)</li>
    <li>[GitHub](https://github.com/recursivefunk)</li>
    <li>[iStrategyLabs’ Johnny Ray Austin almost became an aerospace engineer](http://technical.ly/dc/2016/08/08/johnny-ray-austin/)</li>
  </ul>
</div>

<div id="links">
  <h2>Links</h2>
  <ul>
    <li>[ISL GitHub repo](https://github.com/istrategylabs)</li>
    <li>[mo-static](https://github.com/istrategylabs/mo-static)</li>
    <li>[mo-django](https://github.com/istrategylabs/mo-django)</li>
    <li>[mo-node](https://github.com/istrategylabs/mo-node)</li>
    <li>[Vue.js](https://vuejs.org/)</li>
    <li>[ember.js](http://emberjs.com/)</li>
    <li>[Django](https://www.djangoproject.com/)</li>
    <li>[cookiecutter](https://github.com/audreyr/cookiecutter)</li>
  </ul>
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [jra guest1 Johnny Ray Austin]

  [00:02] szabgab: 
Hello there,  you're listening to the CMOS, to the Code Maven open source podcast and video interview series, I'm your host, Gabor Szabo, and with me is [Johnny Ray Austin](https://johnnyray.me/). 
Hi Johnny!

[00:13] jra: 
Hey, how's it going?

[00:14] szabgab: 
I'm really fine and really happy to have you finally on the show.

[00:21] jra: 
Well, I went on vacation, so...

[00:22] szabgab: 
Oh, that's good, I hope you enjoyed it. 
I see you are at work, right now?

[00:27] jra: 
Yeah, I'm in the office today, I know we initially talked about me being at home but I decided to come into the office today, so that's why the interesting background is there, with the ceiling and stuff.

[00:37] szabgab: 
Yeah, well I think it's much better than my usual storage room and whatever background I have, wherever I find some space to record these shows. 
So anyway, tell me a little bit about your background, how did you get into computing and what kind of stuff you do?

[00:57] jra: 
Sure, so I work at [ISL](https://isl.co/), which is a digital agency in Washington, D.C. 
I work there as the Director of Technology. 
As far as how I got into tech, I guess it goes back to high school, a bit. 
I mean, this was late 90s sort of timeframe, and so Internet was around but it wasn't as prevalent in people's homes and whatnot. 
So it was really just starting to take off and that kind of brought me into college, where, you know, the exposure was a lot more prevalent at that point. 
Actually I started off majoring in aerospace engineering, didn't really like it as much as I thought I would. 

And it was completely random, it was towards the end of the second semester, and I knew I had to change my major, and I didn't know what. 
And one of my roommate's friends was in there, and I was like, <q>So, what are you majoring in?</q> 
And he was like, <q>Oh, computer science.</q> 
And I was just like, <q>Well, how do you like it?</q> 
And he was like, <q>It's cool.</q> 
And so I changed my major to computer science, turns out I loved it. So yeah, I've been doing that ever since. 
Wrote my first program at 19 years old, got my first job at Lockheed Martin here in D.C. 
Did the contracting stuff for a little while, then I went to the start-up side of the house, [EverFi](http://everfi.com/) here in D.C. and after I left there, came on here to [ISL](https://isl.co/), and been doing that ever since.

[02:21] szabgab: 
Nice, so are you a programmer at ISL, or project manager, or Director, I think you wrote?

[02:28] jra: 
Yes, as Technology Director, I'm both at this point. 
There's still a significant part of my day, I do spend writing code. 
It's more and more internal tooling, a lot of my efforts are geared towards making other developers, who are working on client projects, more productive. 
So, and we'll talk about this in a second, but you know a [bunch of our open source stuff](https://github.com/istrategylabs) that I contribute to, and also some of the infrastructure stuff. 
But when I'm not doing that stuff, then it is more the technical project management, making sure that developers have everything they need in order to be productive. 
Dealing with client requirements, working closely with our strategy team, which is sort of our version of project managers, to make sure that everyone involved, all the stakeholders, have a good understanding of the technical requirements and any challenges that we may face. 
Things like that.

[03:24] szabgab: 
So this ISL, I looked at the website, and it has all kinds of really nice pictures. 
But really, different things, very different things. 

[03:33] jra: 
Yeah, right, right. 
Yeah, so I mean, I guess the way we used to describe ourselves is an agency that sort of tries to bridge the gap between the physical and the digital world.  
So if you look through the website, you'll see things like, we call them experiments, or stunts, where we will basically take a concept that involves a physical aspect, like for instance the [Nickelodeon SpongeBob project](https://isl.co/case-studies/spongebob-skill-crane/), which basically involved a physical skill crane device that we built up, that was Internet connected, this was a couple of years ago. 
And basically that tied into a game on Facebook which people can login to and play. 
And it was a competition to see, I think it was who can burst the most bubbles or something crazy like that. 
And then whoever would win a round of the game, would actually win control of the skill crane, and you would be able to control it via the web browser, using a virtual representation of the skill crane. 
So kind of move it around, left and right, up and down, or whatnot. 
But it would actually control the physical crane that was situated in a warehouse or something like that. 
And then whatever you were able to pull out, I think you actually won that prize or something. 

So that's like the sort of thing we're famous for, but other than those type of things, we do traditional web application development, websites, we do a lot of social AOR (social media agency of record) work and things like that, content production.

[05:05] szabgab: 
So this project you mentioned, the Mo project?

[05:11] jra: 
Yes, so Mo is essentially a family of projects, so working at an agency is a bit different than a product company, so we're fortunate in that we get to try things over and over and over again. 
We launch a project and then it goes away. 
So then we get to start over. 
And then we immediately get to take all of the lessons learned from the previous project and immediately apply it to the next thing. 
And so the Mo projects are basically the living manifestation of all those lessons that we've learned. 
We're primarily a [Django](https://www.djangoproject.com/) shop and so all the projects that we built in Django and whatnot have a lot of common aspects to them, as you would expect, with models and stuff like that. 

So [Mo-Django](https://github.com/istrategylabs/mo-django) has all of that starter-code in there. 
But it's open source, anyone can clone the repo and start your own project, there's nothing, there's not much that's very specific to ISL. 

There's very little code that would actually identify it as an ISL project, so the same goes for [Mo-Static](https://github.com/istrategylabs/mo-static), which is a project that helps you build static sites really quickly and supports all of the latest and greatest fancy stuff, you know, [ES6](https://es6.io/) modules and all of the syntax associated with that. 

I'm using [Browserify](http://browserify.org/) for bundling, I'm thinking about switching that to [Webpack](https://webpack.github.io/) at some point in the future. 
And there's a flag on there to enable the use of [Vue.js](https://vuejs.org/), that's our official front-end framework that we utilize here. 

And also, finally there's [Mo-Node](https://github.com/istrategylabs/mo-node), which we don't use as much these days, but from time to time we do utilize [Node.js](https://nodejs.org/) as a platform as well. 
And when we do, we'll go to Mo-Node to start those projects.

[07:06] szabgab: 
So if I understand correctly, then Mo is a project starter? 
So if you want a Django project, which in case someone does not know, Django is a development framework in Python, then you can either use the native tools of Django to start it, and then you would get some kind of a skeleton.

[07:29] jra: 
Right, so this is all using a project, I don't know if you've ever heard of [Cookiecutter](https://github.com/audreyr/cookiecutter)? 
Very similar to [Yeoman](http://yeoman.io/) but Cookiecutter basically allows you to templatize the creation of files and directories and stuff like that, so under the covers, it's using Cookiecutter to generate a Django-ready project for you. 
So all of your initial files for models and the project name and domains, it's tied to [Heroku](https://www.heroku.com/) as well. 
Heroku configurations and stuff like that is instantly generated for you, and the idea is you can get started quickly. 
I mean, from clone to running on port 8000, depending on your Internet connection, probably only takes about two to three minutes. 
It's basically, like I said, it's the accumulations of all the solutions to problems we've faced in the past, particularly with getting started and having flexibility to do stuff.

[08:26] szabgab: 
Okay, and the other two. 
The one that is generating static, that doesn't generate any Django thing, right? 
It's just the static?

[08:35] jra: 
Right, yeah, it's just focused on static websites, essentially everything so the build step basically just pre-processes all your source files and then dumps it in your public directory. 
And you can go in there and start a static webserver and then it will just serve all the files as-is.

[08:56] szabgab: 
And then the third one, without Django, it would just create a Node.js-based one?

[09:03] jra: 
Yeah, it's just a Node app.

[09:04] szabgab: 
So, even with Django, but even with smaller frameworks, I have a feeling that you have a long learning curve? 
So it might create a lot of really nice things, this skeleton, or whatever you call it, but then, I mean at least personally, I feel lost. 
So where do you get started there? 
How do you deal with that?

[09:33] jra: 
Yeah, so, I think if you'd look at it you'd find that there isn't as much in there as you think. 
So it's a skeleton as the starter, it's not about giving you a whole lot of stuff. 
It's about giving you the right stuff to get started. 
We've actually gone through several iterations, long before it was called the Mo projects, they were called the Scale projects, that's sort of the precursor, and it was closed source. 
So what the Mo projects are, and the problems we faced with the Scale projects, was just as you said, there was a lot of stuff in there and it was really hard for someone to just walk into those projects and be able to know where everything was and what was going on. 

The idea is, if you're already a Django developer, even a fairly new Django developer, you can generate a Mo-Django project and just know where everything is. 
We don't deviate, really at all, from industry best practices. 
That was a really big thing as well, we didn't want to have all this custom directory structure stuff going on, we really tried to keep in middle-of-the-road so that anyone, who has done any Django development in the past, can come onboard and get started. 
And that was really important because of onboarding, typically our onboarding process would involve, when we did the Scale stuff, basically going through all of these Scale projects, and walking people through them, what was in there, and what wasn't, and how you configure them and all this other stuff, which just, essentially wasted a lot of people's time. 
People who are JavaScript developers and do front-end should be able to come into Mo-Static and just get started. 
People who are Django developers should be able to come into Mo-Django and just get started. 
So that's kind of what we kept in mind.

[11:18] szabgab: 
So how many people, do you think, are using these tools? 
Do you have any information about that?

[11:25] jra: 
Don't have a whole lot of information about that. 
I did use Mo-Static, so from time to time, I do teach a JavaScript course for [General Assembly](https://generalassemb.ly/) here in D.C. and for a bunch of the students in there, I was actively using Mo-Static as a tool for them. 
So I know a bunch of people there were and still are using it. 
But honestly we don't have any really hard numbers. 
The projects are fairly new. 
They've only been open for a few months now so you're still going to see a whole lot of activity, particularly around the Mo-Django stuff, as we mature these projects. 
But they're, we use them for client-facing projects all the time. 
And so, they're definitely production-ready, but I don't have any real hard numbers for you right now.

[12:08] szabgab: 
Okay, and do you have contributors, outside contributors, not from ISL?

[12:15] jra: 
I think there have been like just a handful of contributors, particularly around the Django stuff, not so much the Node stuff, we use that less and less, so it has the least bit of activity of all the projects. 
But I think the Django stuff has the most contributors outside of ISL, but I think it's only actually a handful of people at this point, so shameless plug, looking for contributors. 
So head to the [iStrategyLabs](https://github.com/istrategylabs), that's our old name, GitHub and just look at [Mo-Django](https://github.com/istrategylabs/mo-django) and [Mo-Static](https://github.com/istrategylabs/mo-static), and you'll find the projects there.

[12:47] szabgab: 
So...okay, now you're looking for people to help you, but why have you open sourced it, in the first place? 
Is this the first open source project from ISL?

[12:59] jra: 
No, it's not the first. 
It's sort of the first suite of projects that we're actively pushing. 
They're open because they can be open. 
Like I said, this isn't a bunch of ISL secret sauce stuff in here, these are tools that allow us to be productive and do our jobs well. 
And if we're finding good ways to create tools to allow ourselves to be productive, we want to make sure we give that back to the community as well, depending on, you know, regardless of how many people actually use them, we consume open source projects all the time. 
And so we felt that it was right, that if we have anything that we can contribute back to the community, then we feel like we have a duty to do so. 
So just the fact that they can be open source is reason enough for us to just open source them. 

[13:58] szabgab: 
Okay, so Django and then Vue.js, right? 
That's...

[14:05] jra: 
Yeah, so Vue.js is not ours, obviously. 
It's a framework that is comparable to [React](https://en.wikipedia.org/wiki/React_(JavaScript_library)), which is a lot more popular. 
So traditionally, we've been an [AngularJS](https://angularjs.org/) shop, Angular 1.x, and as of a couple of months ago, we've officially made the switch from AnglularJS to Vue.js, as our go-to framework for our front-end development. 
And there are a lot of reasons for that. 

If you look on the [ISL blog](https://isl.co/blog/), I wrote a post about some of the reasons we switched over. 
But essentially, anyone who's ever done any AngularJS development, I personally like the framework, but there's a lot there. 
You know, it's an all or nothing sort of thing. 
Once you bring in AngularJS, then it's an AngularJS application, no matter what, there's no getting around the framework. 
And the more you fight it, the more difficult it becomes. 
There are a lot of concepts and a lot of baggage and a lot of learning, a big learning curve that has to be overcome, in order to become really productive in AngularJS outside the context of just the basics. 
All these things about services and factories and constants and then directives are themselves, you know, a bunch of concepts. 
And so particularly when we talk about bringing on junior developers, and getting them up to speed, it was quite a lift. 

Vue.js, on the other hand, focuses on just the view layer of building user-interfaces, which is what we really needed. 
And there are very few concepts, and new concepts, to actually learn. 
It's dealing mainly with components and state data in your application. 
And that's really it, everything else is just an outcry from that. 
The documentation is really stellar, so it makes it really easy for fairly inexperienced people to come up to speed on how to use the framework and also we have people on our team who, their previous job, were designers. 
So they haven't been developers for very long, so a lot of those concepts aren't as firm with them as they may be with some of the more seasoned developers. 
So the fact that they're able to come onboard, go to the documentation, take about 30 minutes, and walk away and say, <q>Hey, I think I have a really good handle on this stuff,</q> is really important for us as a company in terms of productivity.

[16:41] szabgab: 
So do you...have you looked at Angular 2 since then?

[16:47] jra: 
I've looked at it. 
I haven't done anything with it. 
It does seem interesting, so before we switched to Vue.js, we did some investigation. 
This was back when Angular 2 was sort of still in active development. 
So we looked at Angular 2 briefly, we looked at React as well, we actually did a project with React, to try it out. 
We looked at [Ember.js](http://emberjs.com/), and a couple of other frameworks that escape my mind so far. 
And there were pros and cons to everything. 
Ember was really structured in how it approached web development, very opinionated, it's a framework like Angular 1.x, but it had a little bit more maturity to it. 
And the fact that it was compatible with the [JSON API spec](http://jsonapi.org/), out of the box, was really, really great because that's a spec that we've adopted for all of our APIs. 
So that was a big benefit there. 
React was very, very, very close to Vue.js, in its view of the world, and its approach to components. 
And even as we talk, there converging in terms of functionality and whatnot with their release of Vue.js 2.0. 
And honestly, the only thing that kept us from moving towards React was [JSX](https://jsx.github.io/) is sort of a hot topic in that world, and a couple people, including myself, weren't really crazy about having the mark-up that closely tied to the JavaScript. 
I know there are advantages to it and people have written some really good arguments for it, but you know, it just didn't seem conducive of the type of software we were trying to build. 
And so we ultimately decided to go with Vue.js, for that reason, and also the documentation is really, really great. 
And coming from AngularJS 1.x where the documentation was...

[18:41] szabgab: 
Yeah, we got disconnected. 
Sorry, we got for a couple of seconds, disconnected. 
So you said about AngularJS where the documentation is...? 
Was good or bad? 
That's where we got disconnected.

[18:59] jra: 
Yeah, so I was just contrasting the Vue.js documentation with the Angular 1.x documentation. 
And one of the reasons why I love the documentation with Vue.js so much is because it's so much better than Angular 1.x documentation. 
I don't know, it's clearly generated from the code-base and whatnot, but that doesn't always translate well to communicating with humans, I guess. 

[19:32] szabgab: 
Great, I think we are just running out of time, so that's great, I mean, I personally learned quite a few things here and I'm really glad that you talked about them. 
So let's wrap this up now, and there were a couple of other subjects that you mentioned that we might talk about later, and I definitely want to see, a couple of months from now, if you're still using Vue.js or if you've changed to something else. 
And see the reason, because that kind of change is really interesting and see the reasoning behind that. 
So do you have anything else that you wanted to mention maybe, and to have a shoutout to some people or projects?

[20:19] jra: 
Yeah, so I'll just say, first of all, thanks for having me on. 
As far as a shoutout, I'll should out ISL. 
Go to [ISL.co](https://isl.co/), check us out. 
We have some really cool work, we have a couple positions open, so check us out there. 
Follow me on Twitter, [@recursivefunk](https://twitter.com/recursivefunk), that's funk with a k, not a c. 
Yeah, that's it.

[20:42] szabgab: 
So thank you very much for coming on the show and see you later! 
Bye bye.

[20:47] jra: 
Thank you, bye.

[/transcript]

