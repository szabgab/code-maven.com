---
title: "CMOS #2: Sawyer X on Perl 5"
timestamp: 2016-08-24T18:08:03
tags:
  - podcast
  - Perl
  - Perl 5
  - The Netherlands
  - Israel
description: "Interview with Sawyer, the current Pumpkin of Perl 5 about his job herding the cats called Perl 5 Porters."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-2-sawyer-perl5.mp3
  size: 13049856
  time: 24:35
#img: /img/cmos/sawyer-lowres.jpg
#alt: Sawyer
published: true
author: szabgab
archive: true
---


Interview with Sawyer X, the current Pumpkin of Perl 5 about the Perl 5 Porters and the programming language in general. He also explains the difference between Amsterdam.pm and AmsterdamX.pm.


{% youtube id="FRWaO2GpA7g" file="cmos-2-sawyer-perl5.mp4" %}

<podcast>

## Sawyer X

* [Sawyer X blog](http://blogs.perl.org/users/sawyer_x/)
* [PAUSE](https://metacpan.org/author/XSAWYERX)
* [@PerlSawyer](https://twitter.com/PerlSawyer)
* [GitHub](https://github.com/xsawyerx)

## Links

* [Booking.com](http://booking.com/)
* [Amsterdam.pm](http://perl.nl/amsterdam/)
* [AmsterdamX.pm](http://amsterdamx.pm.org/)
* [Perl 5 Porters mailing list](https://lists.perl.org/list/perl5-porters.html)
* [perl 5 summary](https://lists.perl.org/list/perl5-summary.html)
* [Twitter @perl5summaries](https://twitter.com/perl5summaries)
* [Sawyer at blogs.perl.org](http://blogs.perl.org/users/sawyer_x/)
* [rt.perl.org](http://rt.perl.org/)

## Transcript

[transcript]
  [szabgab host1 Gabor Szabo]
  [sawyer guest1 Sawyer]

  [0:00] szabgab:
    Hello!

    This is Gabor Szabo from the Code-Maven podcast and screencast and video interviews. With me is [Sawyer](http://blogs.perl.org/users/sawyer_x/) who is current Pumpkin of Perl 5 and we are going to talk about Perl, the language and the compiler.

    Hi Sawyer.

  [0:25] sawyer:
    Hey!

  [0:27] szabgab:
    Please introduce yourself and tell me about you. A little background about yourself and how did you became a Pumpkin? What is a Pumpkin?

  [0:38] sawyer:
   Okay, let's try. A little bit about myself first. I started with Pascal and Assembly and C. Also a bit of C++. At some point, after a friend recommended and suggested at high school, I've started playing with Perl.

   I started learning the language which the basics was fun. I've learned it in one night, like at 4 am, it was a lot of fun. Then I've started writing some code, doing different stuff. I think the first thing I wrote was actually a program that downloaded all of the comics of a certain comics strip that I liked, and put them in nice directories, because the Internet was not very fast and I wanted to download all of them and then read them at home.

  I've started attending the Tel Aviv Perl Mongers group, TelAviv.pm, which you organized. I gave a few talks there and eventually someone, you, convinced me to go to FOSDEM and YAPC::EU, where FOSDEM is the Open Source conference in Belgium, and YAPC is the European Perl Conference, and you suggested I give a talk there.

  I remember we had a discussion about this where you said "Go ahead" and I said "No way" and you said "go ahead" and I said "no way",  and we did it back-and-forth a few times, until I said "fine, I'll go whatever". 

  It was a lot of fun and I just kept giving talks and I've started to be more and more active in different projects. I became mainly active in the Dancer web framework which I started using for a personal project and slowly I had more and more interest in it, and became the maintainer of it, and we grew a nice community around that.

		  When I moved to The Netherlands where I live right now to work at [Booking.com](http://booking.com/) I created another group. We already had [Amsterdam.pm](http://perl.nl/amsterdam/) which is a Dutch Perl Mongers group and I founded the [AmsterdamX.pm](http://amsterdamx.pm.org/) which is not X for Sawyer X, but it is X for [expat](https://en.wikipedia.org/wiki/Expatriate). I really have to stress that. AmsterdamE is not as AmsterdamX for expats and the idea is that it is much more comfortable for people who don't speak Dutch and the timing is different and it is a bit different.
  We found it to be more successful because we had a little participation from expats. We have a large group of people doing Perl in Amsterdam and in the area but they would not go to the Perl Monger's meetings so I started that group. 

  This year Ricardo Signes who was the Perl Pumpkin for the last few year stepped down from that role and I took over it. Mainly passed on from him, less of a "I fought him for it," and that takes most of my time nowedays. I still do a lot of conferences. This month I think I'll be at 3 conferences and along with that Dancer which I am still active in and, of course, work. That's basically my time nowadays.

  The Perl Pumpkin. I don't know if I have a good story for it. I was always interested in internals of Perl, it is written in C and.

  [4:11] szabgab:
    What is a Perl Pumpkin?

  [4:13] sawyer:
    So yeah. The Perl Pumpkin is basically the project manager for the Perl 5 language.

    I was always interested in the internals. I came from C which is what Perl is written in. It is very sophisticated C and I never got to those levels, but I was always interested in that I was always trying to keep track of what's going on in the language itself. You know, the underpinning of what we know as the Perl syntax and how that works and optimizations there. Lexing, parsing all that stuff is very fascinating but the mailing list for that is just too much.

   I don't know if you have ever read the [Perl 5 Porters mailing list](https://lists.perl.org/list/perl5-porters.html). The group that maintains Perl is the Perl 5 porters and the name P5P is the name of either the group or the list, of course.

   The list is very hard to follow because it is basically an amalgamation of several different communication channels. So there is the tickets, and there is the discussion, and then there are some summaries that are sent there for some commits. At least there used to be.
    It could be a lot of different stuff and they could be all combined into one list, which is what P5P reads and writes to. It was just too much to keep track.

    So I started summarizing them. So now I read them every day and then at the end of the week or at the beginning of the week I publish a summary of it that you can read on the list or on a different list that's called [perl 5 summary](https://lists.perl.org/list/perl5-summary.html), that's just for summaries, or on [Twitter](https://twitter.com/perl5summaries) and
also on [blogs.perl.org](http://blogs.perl.org/users/sawyer_x/).

   So I became active in the core group mainly following discussions. Giving notes here and there, getting more interested in the internals. I was always very active in the community prospective of Perl and I was always wondering about the direction and the vision of Perl and where to move forward with it. Specifically Perl 5.

   So when Ricardo decided to step down, he was looking at what kind of people can fill the void, and could take on this role. I was nominated by someone from the core developers. It was discussed internally and a decision was made that I'd do it appropriately, which hopefully I would. So basically what it means... 

  [6:40] szabgab:
    So you are the Pumpkin now.

  [6:42] sawyer:
    Yeah, I know. I am still trying to do it right, because I am always worried that I am not doing it appropriately. People think that ...

  [6:54] szabgab:
    What are you doing?

  [6:56] sawyer:
    No one really knows what the Perl Pumpkin does. What it basically means is that I help with discussions and I try to kind of navigate discussions towards actual actions, rather than just [bikeshedding](https://en.wiktionary.org/wiki/bikeshedding).

    Once in a while there are conflicting ideas, one person implements things, I think it should be this way, and another person says, it should be done that way, and there they just reach a point where they just disagree and they cannot resolve it. Then I come in and I make a decision, Okay, we are taking this approach because of A, B, and C. The thing is that I don't know all of the technical details that a lot of the bright people there do know, so I mostly listen a lot and then talk to people, oftentimes off the list to get more information, and then I can make decisions.

   So actually a lot of my work is not done on the mailing list. You won't see me as much as other people, mostly I talk to people outside the mailing list to get a better understanding of topics before I respond. So my response is usually at the end saying, "Yes."  Or I don't know, what about this direction?  So that's kind what the Perl Pumpkin does. 

  [8:10] szabgab:
    What does Perl do?
 
  [8:11] sawyer:
    Well, Perl allows you to run Perl code, basically.

    I think it would the biggest value of it.  It would be hard to run Perl code without it, but,
    I mean there are a few other interpreters for Perl 5, and you could use them. They are either forks or they have limited capability in comparision, so the cannonical implementation of Perl 5, which has the larges group of developers that are committed to it, including grant money and sponsorhip money, is Perl 5 Porters and what we call Perl. 

    But jokes aside, Perl is a language that can solve a lot of different problems.
    It has a multi-paradigm programming perspective. So you can writen in procedural, you can write in Object Oriented, you can write in purely functional, you can write in so many different ways, so you can apply it to so many different technologies.

    Because it has a good coupling with C, using the XS layer and FFI if you want it, it allows you to interact with C or with C++ code fairly easily and interact with Perl.
    So you can speed up parts of it or combine with libraries etc.
    So it is very high level. It is hyper-dynamic, which is a term that I really enjoy using for that perspective, and it has a lot of really cool features under the hood.

    I use it to solve most of the problems that I have.

  [9:49] szabgab:
    So, what would you say to people who had experience, who knew about Perl maybe 10 or 15 years ago?
    What has changed since then? Has anything changed?

  [10:01] sawyer:
    There are so many things that have changed, both in fixes, in optimizations, in features, there are new syntaxes available. There were a lot of things introduced to solve specific problems and I mean it is very hard to summarize. I tried giving a talk summarizing all the things that have changed since, let's say 5.10 or 5.8 and it's such a long list.
    Let's take two versions back.
    Nowadays Perl is released every few years. Actually released every single year and have a stable release. So let's take just 2. 

  [10:44] szabgab:
    So what version are you at now?

  [10:45] sawyer:
    We are now at version 5.24. Let's take a look at 5.22. It was released on June 1st I think,
    and it included, just to have a few examples, the diamond operator (`&lt;&gt;`that we have for input, now we have a double diamond operator which is much safer. More secure. You have regular expression bounderies for Unicode. So like a lot of people play with Unicode and work with Unicode but we have added several boundaries for spaces, what Unicode considers a word-boundary, what Unicode considers as a sentence-boundaries, like graphme cluster boundaries. If you use Unicode, these are great.
    We have added them last year.

    The regular expression has a strict mode. Unicode 7 was introduced and added last year.
    This year 5.24 already has Unicode 8, and we've already merged Unicode 9, so we'll release it in the next version, which will be 5.26.
    Aliasing by references for example.
    Having const as a subroutine attribute. There are a lot of stuff like that.
    If you have a look at the recent version for example that just released recently.
    It was released in May 9th, 2016 there are a few other stuff.
    So there is Unicode 8 I've already told you about.

    There is also postfix dereferencing. Once of the things pissing people off,
    when you have a very big structure that represents an array, or it can also represent a hash.
    You have to write the entire structure all the way to the last element and then you have to wrap it with a dereferencing in order to got what it references, which is kind of using a pointer and dereferencing a pointer. 
    What happens is that you write all of this forward and then you have to wrap the entire thing.
    Because that's how the wrapping code works. But now we have added syntax to change that to the end.
    These are things that seem simple, but it completely changes the way you write and the way you work, because you only move forward. Which is some of the things people like about functional programming. The way that you move.
    So these actually have a lot of value and this is no longer experimental. You can use this.
    Things like optimizing basic operations. Additions, substractions, multiplications, subroutine calls, you know stuff that people tend to use. All of these have been optimized significantly.

  [13:10] szabgab:
     So you are talking about speed improvements.

  [13:13] sawyer:
     Yes, these would be the optimizations. Subroutine signatures that people really like and use in a lot of other languages we now have, but we are also optimizing it, so the next version will have substantial optimization for subroutine signatures.

     What else?
 
     We are introducing the indented heredocs synatax, a bunch of other languages have it. Now we'll have that too.

     A lot of security-related changes. For example Perl developers familiar the current directory being in what you load when you try to load modules. It also tries the current directory. We are going to remove that. That's a security issue. While people have used it, it is actually very problematic. We realized this and it is going to change in the next version.

  [14:09] szabgab:
     So that can actually break a lot of code out there.

  [14:13] sawyer:
     Well, so one of the things we actually did was release all of the core modules recently, with that removed locally, and we have noticed very little breakage. The only breakage was base.pm which is used by quite a few modules and we are probably going to merge a different implementation that implements the same thing, but in a safer way for base.pm that has a specific usage which is trickier, but we couldn't observe other than the base.pm breakage that was major at all.
     So we are kind of safe with that.

     If your code assumes loading from the current directory, you can just say I'd like from the current directory. That would work just fine. Any code that does that will work just fine. But code that implicitely loaded from the current directory, that is going to be removed. That is a much safer perspecive of this.

     So if you take a few steps back and you look at all this history. What we have added was a lot of syntax, a lot of changes in bug fixex, security, a lot of optimizations.
     We have plugable keywords so you can write an interpreter within the interpreter. Really crazy stuff like that. These are things that keep evolving and changing in the language and you can't really see all of this unless you look at the global picture. The whole picture of it.

  [15:46] szabgab:
    So let's jump to something slightly different. If someone wants to learn Perl or get involved in...
    I mean learn Perl, let's start with that.
    There are two groups here. One is someone who wants to learn Perl, what would you suggest and the other one if someone wants to get involved in developing Perl in helping and further improving the language. So let's start with the...?

  [16:12] sawyer:
    If you don't know Perl and you hear this and you think, "Hey this sounds like an interesting language, maybe I'd like to learn it" then I'd recommend, there are two books that I highly recommend.
    One is Beginning Perl by Ovid, Curtis Poe who goes by Ovid, and the other one is Modern Perl by chromatic. I think these are very very good books that cover the essentials.

    Modern Perl tends to be more succint, but it is very good and Beginning Perl is very thorough and I think Curtis has a very good way of explaining things and they both teach you, not Perl like 10-20 years ago, but Perl that you'd write nowadays, that people would expect you to write, that is proper practices that don't assume on "I know Unix" or don't assume "I came from C" and it is exactly the same.
   give you a very idiomatic and correct way of writing Perl that is extensible and secure and correct and fun. So I really recommend those, if you'd like to learn the language.

   When it comes to how to improve the language itself. So the language breaks down to two parts.
   It breaks down to the core of the language and all of the modules for it.
   The modules for it are written in either C, using a binding loader called XS. It's kind of a glue language between C and Perl, or directly in Perl which we call Pure Perl because it does not have any XS or C.
   And you can write a module that is either in one of them or in both, whatever you want. So a lot of the language extensions are done using modules and the language tries to have a small core that is easily extendable using modules.
   So a lot of things that we assume as the core language are actually just modules that you can open a pull-request for you can contribute you can work on these projects openly and it's a lot of fun and there are project. Examples is the one that I am involved with is Dancer that you could contribute code to and you can join those teams.
   Usually it is a team of people. Sometimes it is a single maintainer. Sometime is one or two maintainers working together and you can always jump in and say hey, I know a little bit of Perl I want to help with this.

   There is also the CPAN Pull-request challenge. The Pull-request challange kind of allows you to get a taste of it, like a tasting menu where every month you get a new module and this module was curated to be both important and used and having issues to work on. So there is a filtering process going on there.  Not just random stuff, because CPAN can take whatever anyone wants to upload. CPAN is where we upload stuff so it contains anything. Some of those no one really uses. Some of those are not very good, but some are very important and used and they get curated and you get every month "hey here is a thing you could work on". You can go and submit a pull-request and talk to the author and it is fantastic.

  Now when it comes to language itself, if you'd like to work on the language, that requires...
  I mean at first I though that it requires learning C like if you want to learn on the language
  then you need to know C. In fact the matter is that the language contains a lot of tooling around it that are part of the language that could use a lot of help. Many of these tools have been written in Perl.  I think the first contribution that I did was remove a core module and put it on CPAN.
   One additional thing that we have now is that we have another module that we are thinking of making available separately from core as well. Because that would allow people to use it without necessarily having to upgrade Perl. That is a contribution I can make knowing any level of C.
   So I've been trying to collect these nowadays. Haven't got very far but I am trying to collect all of these different things that you can do that don't necessarily would require specific C knowledge.
   Now if you do know C you can always take a look at the existing tickets in [rt.perl.org](http://rt.perl.org/) and if there is any ticket there that you want to play with the Perl source is open sourced fully. Free software just clone it from Git. It's also available on a GitHub mirror, an unofficial GitHub mirror. It's available there. You can just submit patches, you can e-mail the mailing list Perl 5 Porters and you can contact us and say "Hey I'd like to work on something, what do you work on?". Or "I'd like to work on this ticket, what can I do?". You can also comment on the tickets themselves. So that ticket and the whole combination of the mailing list, if you comment on the ticket we'll see it and comment onthe ticket back. If you write on the mailing list, everyone else will see it as well. So it all gets combined. So no matter how you access us, no matter how you contact us we'll find it.

 [21:02] szabgab:
   So it either RT, the bug-tracking system, or mailing list, or IRC, I guess.

  [21:09] sawyer:
    Sure, IRC. We are on irc.perl.org #p5p and you can find us. Not everyone is always online, but drop a note and someone will probably respond soon and I think people who come in and just want to play with stuff are really a great resource, they have different perspectives.
    They think from a different angle and it is always interesting to see what people play with. 

 [21:38] szabgab:
  Thank you very much. I wonder if there is any subject that we have not talked about that you'd like to mention here. Shoutout to people.

  [21:53] sawyer:
    I'd shoutout to everyone. It's tricky. Tony Cook and Dave Mitchel have been working a lot on the Perl core as part of their grants and they are doing an amazing work, optimization, a ton of bugfixes, and stuff like that.
    We have one amazing contributor who work tirelessly on pretty much anything and that's Father Chrysostomos. I really like this person. He is a really nice guy.

    And Zefram who is an expert on incredibly detailed technical topics.

    I want to thank Jim Keenan who is a fantastic curator of all the tickes. If you open a ticke he will see it and if you have a test he'll run it and if you have a patch there he'll try to merge it and 
    if its wrong. If it does not pass any kind of policy that we have, then he'll comment with explanations and links. It's just incredible.

    Todd Rinaldo and John Lightsey who worked on the changes to the current directory. They work in the security team at cPanel. And cPanel has like an entire security team that does stuff. They found a slew of these issues and they raised them, they wrote the patches for them. Just fantastic work.
    Matthew Horsfall who is putting the indented heredocs.
    I mean there is a list. I am not gonna be able. I mean if you'r going to have another episode we can sit down and just go.

  [23:22] szabgab:
   We can get back together a couple of month from now and see how things have progressed, and maybe when the next version of Perl is released, we can talk again.

  [23:36] sawyer:
    Yeah absoultely. I think that would be great. It's just there are too many for now.
    Yeah I think very interesting things are happening. I am very happy to see how the group is working together now. And I'd be interested to see where we are going to take this. Because we are already introducing syntax, we are already introducing optimizations, we already introducing lower memory consumptions, the Unicode support that Perl has thanks to Karl Williamson's efforts, these are amazing things and we already have all that going on, so what we are going to be doing now, is a very big and interesting question to me.

  [24:22] szabgab:
    Okay, We'll talk about it later. Thank you for coming on the show.

  [24:26] sawyer:
    Thank you for having me. I blurted out as many things as I can in the least amount of time.

  [24:33] szabgab:
    Thank you very much. Bye bye.

  [24:34] sawyer:
     Yeah. Bye bye.

[/transcript]

<!--

## Technical info

Recorded on 17 August 2016 with "Ecamm Network Call Recorder for Skype v2.6.1" using the following settings:

<pre>
QuickTime Options:
  Audio Encoding: Uncompressed
  Video Quality: High
  Video Image Size: 854 x 480 (Wide)
  Video Frame Rate: Maxium

Recoding Option:
  Record Video: Multi-track
</pre>

There are a couple of places where we had a lot of dropped frames
and by the end of the recording the noise from the ventillator of my computer became pretty disturbing.
-->
