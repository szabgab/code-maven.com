---
title: "CMOS #3: Joel Berger on Mojolicious"
timestamp: 2016-09-01T14:08:03
tags:
  - podcast
  - Perl
  - Mojolicious
  - USA
description: "Interview with Joel Berger one of the core developers of Mojolicious, the Perl-base web framework with rainbows and unicorns."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-3-joel-berger-mojolicious.mp3
  size: 23645783
  time: 26:37
img: /img/cmos/joel_berger.jpg
alt: Joel Berger
published: true
author: szabgab
archive: true
---


Mojolicious is a modern, non-blocking Web framework in Perl.
Joel Berger member of the development team talks about the project
and on how to get started with it.


{% youtube id="O7JGQqCUOJM" file="cmos-3-joel-berger-mojolicious.mp4" %}

<podcast>

<div id="person">
## Joel Berger
* [Joel Berger](http://blogs.perl.org/users/joel_berger/)
* [PAUSE](https://metacpan.org/author/JBERGER)
* [@joelaberger](https://twitter.com/joelaberger)
* [GitHub](https://github.com/jberger)
</div>

<div id="links">
## Links
* [Mojolicious](http://mojolicious.org/)
* [mojolicio.us](http://mojolicio.us/)
* [Joel's PDF Thesis](https://archive.org/details/ultrafast_electron_microscopes_berger_phd_thesis.pdf)
* [Physics::UEMColumn, the basis of the thesis](https://metacpan.org/pod/Physics::UEMColumn)
* [Modeling Physical Systems with Modern Object Oriented Perl - YAPC::NA 2012](https://www.youtube.com/watch?v=YnW1hTVQYfA)
* [United States budget sequestration in 2013](https://en.wikipedia.org/wiki/United_States_budget_sequestration_in_2013#Impact_on_research_funding) (sequester) 
* [Chicago Perl Mongers](http://chicago.pm.org/)
* [ServerCentral](https://www.servercentral.com/)
* [Node.JS](https://nodejs.org/)
* [POE](https://metacpan.org/pod/POE)
* [AnyEvent](https://metacpan.org/pod/AnyEvent)
* [Sebastian Riedel (project leader)](http://blog.kraih.com/)
* [Mojo::Pg](https://metacpan.org/pod/Mojo::Pg) Mojolicious and PostgreSQL
* [Abhijit Menon-Sen (crab)](http://toroid.org)
* [DBI](https://metacpan.org/pod/DBI)
* [DBD::Pg](https://metacpan.org/pod/DBD::Pg)
* [Mojolicious::Plugin::ForkCall](https://metacpan.org/pod/Mojolicious::Plugin::ForkCall) aka. [Mojo::IOLoop::ForkCall](https://metacpan.org/pod/Mojo::IOLoop::ForkCall)
* [Jan Henning Thorsen](http://thorsen.pm/)
* [Mojo::IOLoop::ReadWriteFork](https://metacpan.org/pod/Mojo::IOLoop::ReadWriteFork)
* [(Bash) Windows Subsystem for Linux](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux)
* [CPAN](http://www.cpan.org/)
* [Jason Crome on Perl Dancer 2](/cmos-1-jason-crome-perl-dancer2)
* [Carton](https://metacpan.org/pod/Carton)
* [Mojolicius Wiki](https://github.com/kraih/mojo/wiki)
* [Marcus Ramberg](http://marcus.nordaaker.com/)
* [Slack](https://slack.com/)
* [Convos](https://convos.by/)
* [Oetiker Partner AG](http://www.oetiker.ch/en/oss/projects/)
* [Tobias Oetiker](https://github.com/oetiker)
* [Telenor](http://www.telenor.com/)
* [mail.ru](https://mail.ru/)
* [Craigslist](https://www.craigslist.org/)
* [Glen Hinkle (tempire)](http://tempi.re/)
* [Mojocasts](http://mojocasts.com/e1)
* [Mojocast Errata](https://github.com/kraih/mojo/wiki#screencasts)
* [Websockets](https://en.wikipedia.org/wiki/WebSocket)
* [PSGI](http://plackperl.org/)
* [morbo](https://metacpan.org/pod/distribution/Mojolicious/script/morbo)
* [Hypnotoad](http://mojolicious.org/perldoc/Mojo/Server/Hypnotoad)
* [Starman](https://metacpan.org/pod/Starman)
* [Test::Mojo](https://metacpan.org/pod/Test::Mojo)
* [Test::Mojo::Role::PSGI](https://metacpan.org/pod/Test::Mojo::Role::PSGI)
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [jberger guest1 Joel Berger]

  [0:00] szabgab:
    Hello there!  This is Gabor again with the CMOS, Code Maven open source podcast and screencast and with me is Joel Berger.  Hi Joel!

  [0:14] jberger:
    Hi!  Good to see you, Gabor.

  [0:16] szabgab:
    Good to see you too.  And to those who are listening to this podcast, good to hear you too.  Anyway, welcome to the show.  We are going to talk about Mojolicious, the Perl based web framework but before we get there, let us talk a little about you.  Tell me a little bit about your background and how did you get into programming and how did you get into using Mojolicious.

  [0:41] jberger:
    Alright, sure.  Well, I actually have a PhD in physics and in my research I was doing some modeling of electron microscopes and I decided I needed to do some programming to do this and I already had a little bit of Perl work from doing some text processing and of course how does everyone start with Perl, right?  There is a value and needs a regex for that, right?

But I had learned some Perl.  And so, I started making big models for these electrons and learned quite a bit of programming that way.  And eventually once I got my PhD, it happened that the US had its a sequester, if you have heard this term.

Basically where the government decided that in order to cut the budgets they were going to do some sort of a deal where they would all cut the budgets at the same time but they all excluded their favorite things.  So, science got cut more than the rest and it was very hard for scientists.  So, luckily I had quite a bit of Perl programming by this point because of all that modeling I was doing and I asked around at my local Perl mongers, Chicago Perl mongers where I am still quite active and they found me a job in the programming world and I have been programming ever since, mostly in Perl and now I am lucky enough to actually be working in Mojolicious shop here in Chicago.

It is called Server Central, we do server hosting and whatever but we are doing a lot of our back-end work now in Mojolicious as well as some other languages.  The other groups are using some other languages but of course the group that I am in hired me because they were doing Mojolicious already.  It is been a lot of fun working there.

  [2:29] szabgab:
    Can you tell a little more about what kind of things do you do with Mojolicious?  I mean, back-end programming, Web-hosting company.

  [2:38] jberger:
    We are writing a server deployment system where the idea is that for our own internal use it is going to look like cloud provisioning, a cloud server provisioning like you have a Linode or any other well-known hosting companies, you can click a button and it gives you a new server, but our company is actual physical servers. 

  So, we are writing software and an API and all this to actually spin up real physical servers in that sort of same convenient way and that will help us respond more when a new client will come to us and say "Hey, we need 50 new servers."  We will not need to take all the humans out to the racks and get them installing operating systems and all that.  We are going to have API calls and all that other fancy stuff too so that they can provision operating systems and set up networks and such all through the web frontend and that will all run through Mojolicious and we have actually got a fair amount of working ready.  So, it is a very exciting project.

  [3:37] szabgab:
    So, this a web application basically, just an internal one, right?

  [3:42] jberger:
    Yes but it is got many components because of course we have backside networks that we do not want the frontend to have access to because of course you would not want the security implications of allowing the frontend have access to your servers backends.  That is just terrifying.  So, we have all kinds of isolation there too.  So, there are some issues of proxying and all that other things.  And of course Mojolicious does that quite well too.

  [4:09] szabgab:
    So, you like Mojolicious and you liked it before you started with this company, right?

  [4:18] jberger:
    Yes, yes.  Actually even while I was still a graduate student I was starting to get into web programming just for my own fun and I happened upon my Mojolicious more or less by accident.

I think as many people do, you sort of pick your first web framework because you have heard of it and the thing that really kept me were some of the features that I am sure we will get to describe later but specifically the asynchronous stuff, really played with my brain in the right way.  I really enjoyed working on non-blocking code.

  [4:54] szabgab:
    Non-blocking like in Ajax, like in Node.

  [5:00] jberger:
    Like in Node, yeah.  And actually that is a great way to segue into talking a little bit about Mojo.  I like to describe Mojolicious as sort of a Node JS like framework for Perl.  Node is built on a reactive event-loop and so is Mojolicious.

    So, all of the incoming calls, outgoing calls are all event based, but that also lets you have the freedom to do things like asynchronous database queries or responding by web sockets or all kinds of other things you cannot do when you have to do a procedural request response platform.

And because Perl did not have a framework built on a non-blocking event loop like that, it was rather difficult to write a web application in that way.  It was not impossible.  You could use POE or you could use AnyEvent to write this but you had to be a little closer to the event loop than most people would like to be in.  So, when you build a web framework on top of it, it isolates you from that.
You can do a lot more.
It feels more like regular programming for the most part as much as non-blocking ever can do that.

  [6:16] szabgab:
    Yeah that is what I wanted to ask you because my feeling, coming from the blocking world or growing up in that, writing non-blocking code like Node is a little strange and things that seem straightforward, or were straightforward...

  [6:39] jberger:
    If you do very complex things, there is really no way to avoid that, but for the most part if you really are just doing say make a non-blocking web database request or maybe you make a request to another web service in a non-blocking way, the way that you then call back to your original client is very natural and you do not have to worry about it too much.

   Of course if you start doing things like making 12 calls, three different services and you can do them in batches of whatever, it gets complex of course but you do not need to start at that level.

   And actually I should say here a lot of people come to us and say "Oh, it is most Mojolicious but I am afraid of it because it is non-blocking. That scares me." You do not need to do anything non-blocking.  It works just fine as a blocking framework.  Still there is parts that are reacting in the background but you do not have to think about that at all if you do not want to.

  [7:32] szabgab:
    And if you start out that way, if you start with the blocking way which I see most of the people are familiar with, can you switch over to the non-blocking mode or how difficult it is?

  [7:43] jberger:
  Of course.

  The only thing that becomes a little bit difficult is if you have got very long running processes that you have started.  Because you have now blocked the loop, the next iterations of the loop also were blocked.

  It is a tricky question, right?  In a normal web app you will have no problem going to sort of not-blocking incrementally.  The bigger problem is you have got sort of gigantic database queries that take minutes to complete or other crazy things but usually anything where you have not had to extend the client's timeout, you probably would be fine anyway because only the client will timeout first anyway.

  [8:36] szabgab:
    Yeah.  I mean, I saw all kinds of solutions for this problem when you have a long query and then the client keeps asking "Are you ready yet?, Are you ready yet?" and really strange solutions.  So, you say that with Mojolicious you can solve it much easier?

  [8:56] jberger:
    Well, you can.  So, there are several ways around this.

    First of all you can do sort of, well, that is the easiest way and particularly if you are using one of the..
    So, Mojolicious project has spawned a couple of sort of spin-off projects that wrap databases in a more asynchronous way.  The primary one is Postgres.

    Our project founder Sebastian Riedel has really taken on to Postgres lately and actually one of other core members Abhijit Menon-Sen, I hope I am saying that right, is Crab on IRC, that is a lot easier to say, is also on the Postgres development team.  So, that is a really cool crossover we have there. 

   When we have questions about PostgreS, we can just call over Crab and say "Hey, this thing is confusing us" and he can help us out but we have a wrapper. It is still just using DBI and DBD::PG but it provides you a non-blocking interface and when you do that, you have got this query that is going to take 5 minutes to run and assuming you have set up all your timeouts correctly, you can keep serving other clients while that query is running. 

   And when the query is completed and it starts sending you data back, then you can respond to that client.  That is the easiest way to do it.  If you cannot do that for some reason and if you are not using a database that has a reactive or a non-blocking client, then you can do several different sorts of forking where you fork after getting the request, do your computation in some other process and then you pipe the results back to your original server.

   And we have plug-ins for that too. I have written one called [Mojolicious::Plugin::ForkCall](https://metacpan.org/pod/Mojolicious::Plugin::ForkCall)
It is actually [Mojo::IOLoop::ForkCall](https://metacpan.org/pod/Mojo::IOLoop::ForkCall) too, but do not worry about that.

And Jan Henning Thorsen, another of the Mojo core developers has one called [Mojo::IOLoop::ReadWriteFork](https://metacpan.org/pod/Mojo::IOLoop::ReadWriteFork).
 You can actually interact with your forked process.  You can send it data over a pipe and it thinks that it is standard input and you can send data back over it.  So, that is where we are doing really long running things where you want to monitor some process or whatever.  So, there are plenty of options for what we call unblocking code and they all work fairly well with a slight asterisk around Windows of course because forking and piping and things do not work so well on Windows.

  Actually with the new Windows subsystem for Linux which is the real name, people have been calling Bash on windows, it is really called WSL or Windows Subsystem for Linux is we have actually had some fairly good reports of Mojolicious. The corner cases that Windows did not work as well are working quite nicely on Windows Subsystem for Linux.  So, we are very excited about that.

  [12:02] szabgab:
    I see.  So, besides this non-blocking mode, what else would you say as the killer feature of Mojolicious?  Why would someone pick Mojolicious?

  [12:18] jberger:
    So, I think the biggest thing is API consistency, right?

    We are very used to in the Perl world taking pieces from all over different parts of CPAN and each one presents a slightly different interface and we are very used to that and let us not think that that is a bad thing, but Mojolicious was designed really to work together with itself quite well.

    You can of course use whichever modules you want but if you use the tools that come with it and it comes with a lot of built-in tools like a DOM parser and JSON parser and. I am sure I am going to forget everything because I am on the spot here, but it comes with lots of batteries included and the really nice thing as you get to use them more and more is that they were all designed with the same API in mind and consistency is always a key for us.

    I already watched your first video with Jason Chrome from the Dancer group and I think I probably ought to comment that for a lot of the people in the Perl world we value stability over everything else and I think it would be wrong to not say that Mojolicious takes a slightly different approach to this.  We have a very defined breakage policy where we can at specific times break backwards compatibility and we have done that more in the past then we have lately but we have done quite a bit and the point has been it allows us to keep making the framework more and more consistent and if we need to change a thing that would change that consistency, we can change at other places too and the code as a result has now gotten to be very lean and very easily read while still providing really consistent API.  And as it turns out, after a while of iterating like that we have not actually broken much lately.  So, Mojo got this reputation for "Oh, you know, you have to be very careful about your dependencies" and we will probably never say that it is never going to change again but it is gotten quite stable lately and quite beautiful as a result of our willingness to iterate on it.

  [14:35] szabgab:
    So, if you had these changes earlier, not recently but earlier, these breaking changes, how did people used Mojolicious manage?  Do you have some process of upgrading?

  [14:50] jberger:
    First of all, we recommend Carton very heavily.  As you are developing, we recommend that you use Carton and pin your dependency of Mojolicious so that you know exactly where you have developed and which version you should use.

    We also have then a porting document that we try to keep up-to-date whenever we make a breaking change.  It says "This thing has changed.  Use this one instead."   It is in the wiki and for the most part, especially since say about 5.0, we are now into the 7.0 series, the changes have been mostly semantic.  You change name here or there, a few behaviors have gone away but for the most part it is been fairly easy. Oh, you used to use this. Use that instead.  Not too many things have really just plain out gone away. 

  [15:44] szabgab:
    I see.  Okay, do you know any projects that were written in Mojolicious either open source or those that are, I mean, besides the company where you work?

  [15:55] jberger:
    Yeah.  Actually, I know that a lot of .. First of all, the big one that we are always kind of proud of is Jan Henning Thorsen and Marcus Romberg wrote an IRC client in Mojolicious and it is easy to compare it now, now that a lot of people have seen Slack.

     It feels a lot like Slack.  Its IRC in the browser.  You can pull it up on your phone or you can pull it up on your desktop or your laptop and it is all the same connection because you are hosting it in one place and it behaves then as a web server that you can connect to and type into.
     The web is convos.by if you want to look at that and they have a little demo there and actually it is kind of fun to mention now that they have just done a huge rewrite and it is about to be released for the 1.0 version which should be a lot easier to install.  That was a little bit hard to install which was a big problem.

   Also, I know Tobi Oetiker, I hope I am it right.  Tools are starting to be written into Mojolicious which is quite fun for us to see people doing server administration using Mojolicious based tools.  Kind of interesting thing, I did not expect to see but it was fun to see happen.

    As far as websites, first of all, we have lists of people who are using the Mojolicious on our wiki and even some user quotes about it.  I know for some reason Norway has a huge user base of Mojolicious.  So, I know Telenor is using it for some things and there is a travel service out there that Jan Henning is actually moving to.  I know they are using it.  I wish I knew the name.  I do not off the top of my head.

    We have some bigger sites.  I do not know if I am supposed to say.  I think I am allowed to say that we know that mail.ru which is in the Alexa Top 50 actually uses Mojolicious, not for all of their sites but I think as they go, they are coding more and more to it.  We were only just allowed to share that recently.  So, that is kind of fun for us to say. 

   I have a nod and a wink that told me that there is some Mojo being used at Craigslist. I hope I am right in saying that but that is kind of fun for us too.  And plenty other smaller sites that you can see if you go to our Wiki and see the listings.

  [18:28] szabgab:
    If you are going to your Wiki, where do people go if they want to learn Mojolicious and they want to start using it.

  [18:40] jberger:
    That is a great question.  We have our website.  It is Mojolicious.org or you can do the sort of more fun Mojolicio.us so it just looks like Mojolicious but Mojolicious.org is easier to say.  And from there you can see the front page, kind of a pretty page.  You can get documentation there and then you can get links then from there to the GitHub as well.  The wiki is then through GitHub.  It is a GitHub wiki.

    We have an IRC channel, IRC.perl.org #mojo and we are quite friendly.  So, we try to be at least.  If it is not, come tell me and I will help you out.  I am your guy. 

    So, we do most of our communication through IRC.  A lot of development is through IRC.  We are very proud it.  If you come into the IRC and find a bug, we often have it fixed within minutes and released.  Because we have kept the code base very clean over this time, we can react to issues very quickly.

    I think you will remember back when there is that bug was found in Bugzilla about the code interpolation, the privilege escalation, the same thing that everyone has did you get a list of parameters thing.

  [20:09] szabgab:
    Something about CGI, I think.

  [20:11] jberger:
    Yeah and most web frameworks copied that API. So, most web frameworks had that same kind of, I should not say it is a vulnerability, it was a way that a user might accidentally write their code badly and because of the way that CGI had developed that API and we all copied allowed users to write insecure code and we put out a fix to that that very evening which was kind of fun for us to say "You know you what?  No, we will not let you write this unsafe code anymore.  We are stopping it tonight."

  So, we are very proud of our ability to respond very quickly especially to security bugs which have been few.

  [20:53] szabgab:
    So, any screencast or other resources?

  [21:01] jberger:
    One of our core members Glen Hinkle who goes by Tempire has a series of Mojocasts.  They are getting a little bit older unfortunately but for the most part they are pretty good. We have a list of errata as well on the wiki.

    I should probably help him link that into the website.  Unfortunately, Glenn has spent more of his time in iOS development lately.  So, although he is still around if we ever need to call me in for a for a group chat, he will be there but he has not had as quite as much time to spend on the Perl side but his is podcasts are amazing.

     I believe it is Mojocasts.com but let me just quickly Yes, Mojocasts.com.  I was worried if it was .org or something but Mojocasts.com.  It is really good.  And there are a few things that have changed since then we have noted that on the wiki as well.

  [21:56] szabgab:
    Good.  Just one thing, going back before we are closing here, you mentioned CGI lately and CGI sort of has a bad name especially because it is old and it is rather slow when you are running CGI. So, I wonder when you are running Mojolicious, do you run it as a CGI script or ... ?

  [22:18] jberger:
    Ah, good point.

    No, it is not a CGI script although it can actually run under a CGI server. If you have like a shared hosting or some old servers, you can still run Mojolicious under a CGI environment and it will work correctly.
    You cannot use web sockets or anything because of course CGI has no way to know how to do that.  And I also should say that if you are using a PSGI server which is fine, you can do that as well.  Mojolicious will run as a PSGI server but again does not have the web sockets because you need to have the event loop in the server level in order for that to work.

   So, to say that then we do bundle our own web servers in with distribution.  We have a few of them.  We have a basic Damon that is very capable and we have a script called Morbo which is nice because as you develop, it will notice that you have saved files and made changes and it will restart the server for you which is quite nice.  And then we have a much more capable production server called Hypnotoad and Hypnotoad is basically equivalent to the PSGI server Starman if you are aware Starman, same sort of pre-forking architecture.

   It has one extra little feature of hot deployment.  So, if you say I have made all these changes I would like to release a new server or on post production, however you want to call this, and you do not want to have to bring your site down, you can actually tell Hypnotoad to start the new server and as the old clients keep being served by that old server, new requests will go to the new server and they never miss a beat.

   You can upgrade Mojolicious.  You can upgrade your site.  You can even upgrade your Perl while doing that.  So, it is really quite interesting.

   And then I should also say for all that capability, Mojolicious is still quite small.  It something about 8,400 lines of code and as its kind of famously known, it has no non-core dependencies but can use CPAN modules for extra behavior like IO::Socket::SSL for SSL connections and all kinds of other things if you want to use CPAN modules but it does not need them.  So, it is very easy to install.  And it is got 11,000 or so tests.  So, it has more tests than lines of code.  So, you can be reasonably sure that we have been careful about what we are doing.  And all that installs in less than a minute. So, if you are coming from my platform where it was hard to install, Mojolicious might be for you too.

  [24:59] szabgab:
    That is really nice.  So, thank you for coming to the show and sharing all this information.  I wonder if you have anything else, a shout-out or something that you would like to add that I failed to ask.

  [25:16] jberger:
    Great. It feels like I should, should not I?  

  [25:19] szabgab:
    It is not a requirement.

  [25:23] jberger:
    No, I would just say give it a look, come by the IRC channel.

    Actually, I think I could say one of the things I particularly like about Mojolicious is there is a test framework called Test::Mojo. It comes in the distribution but I really like how it works and I would encourage people that if you had a hard time testing your web application before, even if it is not a Mojolicious application, you can use Test::Mojo with a plug-in that I have written and I am sure if we give some links here, I can give a link to it but using that Test Mojo and the plug-in that I have written, you can use it to test any other PSGI application as well and it can be very nice to have the expressive nature of Test Mojo for any website you have developed.  So, I would give that a look too.

  [26:15] szabgab:
    Yeah.  I will add it to the show notes and the links.

  [26:18] jberger:
    Okay.

  [26:19] szabgab:
    Great.  So, thank you very much and I hope that in a few months or when there is a new release we can return to this conversation and see what changed and how to update it.

  [26:33] jberger:
    Will do.

  [26:33] szabgab:
    Thank you very much.  Bye, bye.

  [26:35] jberger:
    Yup.  Thank you.

[/transcript]

<!--

## Technical info

Recorded on 24 August 2016 with "Ecamm Network Call Recorder for Skype v2.6.1" using the following settings:

<pre>
QuickTime Options:
  Audio Encoding: Uncompressed
  Video Quality: Normal
  Video Image Size: 854 x 480 (Wide)
  Video Frame Rate: Medium

Recoding Option:
  Record Video: Multi-track
</pre>

By the end of the recording the noise from the ventillator of my computer became pretty disturbing.

-->
