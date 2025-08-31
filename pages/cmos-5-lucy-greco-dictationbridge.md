---
title: "CMOS #5 Lucy Greco - DictationBridge - helping the visually impaired"
timestamp: 2016-09-08T19:01:01
tags:
  - podcast
  - a11y
  - accessibility
  - USA
description: "Interview with Lucy Greco about accessibility in general and about DictationBridge that connects screen readers and speech-input software."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-5-lucy-greco-dictationbridge.mp3
  size: 70780017
  time: 29:31
published: true
author: szabgab
#img: /img/cmos/lucy_greco.jpeg
#alt: Lucy Greco
archive: true
---


Interview with Lucy Greco about [DictationBridge](http://dictationbridge.com/)
an Open Source tool to connect screen readers and speech-input software to
help the blind and visually impaired.

We also talked a lot about accesibility in general and accessibility of web sites in specific.


<podcast>

## Lucy Greco

* [Lucy Greco](http://accessaces.com/)
* [Lucy at DictationBridge](http://dictationbridge.com/author/lucy/)
* [@accessaces](https://twitter.com/accessaces)
* [LinkedIN](https://www.linkedin.com/in/lucy-greco-968b491)

## Links

* [DictationBridge](http://dictationbridge.com/)
* [Screen reader](https://en.wikipedia.org/wiki/Screen_reader)
* [NVDA - NonVisual Desktop Access](http://www.nvaccess.org/)
* [W3C Web accessibility guidelines](https://www.w3.org/standards/webdesign/accessibility)
* [Chrome Accessibility Developer Tools](https://chrome.google.com/webstore/detail/accessibility-developer-t/fpkknkljclfencbdbgkenhalefipecmb?hl=en)
* [WebAIM - WAVE Chrome Extension](http://wave.webaim.org/extension/)
* [Tenon](https://tenon.io/)
* [Dragon Accessibility Solutions](http://www.nuance.com/dragon/accessibility-solutions/index.htm)
* [DictationBridge on GitHub](https://github.com/dictationbridge)
* [Berkeley Web Access site](https://webaccess.berkeley.edu/) maintained by Lucy


## Transcript

[transcript]
  [szabgab host1 Gabor Szabo]
  [lucy guest1 Lucy Greco]
  [screenreader guest2 Screen Reader]

[00:02] szabgab: Hello there! You are listening to the CMOS, the Code Maven Open Source podcast,  you're hearing your host, Gabor Szabo, and with me is [Lucy Greco](http://accessaces.com/), and we are going to talk about the DictationBridge project. Hello, Lucy.

[00:21] lucy: Good morning, how are you?

[00:23] szabgab: I'm really great, thank you. How are you?

[00:26] lucy: I'm excellent, thank you. I'm excited to be on the show with you.

[00:32] szabgab: Before we go on, I want to, the first thing I want to is ask about you and how did you get into the project and how did you get into computing, in general, but before that, the people who are listening to this podcast, and maybe watching the video interview, might wonder why this time we don't have a video feed and what's special in this interview, and the main fact is that you don't see, you're blind.

[01:07] lucy: Correct, yes, I'm totally blind, I've been blind since birth, and I use computers with something called a [screen reader](https://en.wikipedia.org/wiki/Screen_reader), which your audience may not be familiar with, so screen reader is the generic term for a piece of software, used by a person who's blind or visually-impaired, to access information on the computer screen. 

It doesn't just read text, it reads things like buttons, controls, menus. It gives me the ability to say <q>Bring me to the menubar and read the items on the menu.</q> It gives me the ability to move through a screen and find and discover things like buttons, controls, edit-fields, and hear text as I'm typing it, or be able to navigate an interface on a computer as effectively as a person who can just look at it and point at it with their mouse, I can actually give one of many, many commands to do any of the things I need to do, to be as effective as a sighted person on a computer.

[02:19] szabgab: Right, so as I understand it, the screen reader is only reading the text and you are still typing, and I guess you don't move the mouse, do you?

[02:29] lucy: Correct, no I don't use a mouse and so, but I mean, it reads everything. So if there's a button or a graphic, and the graphic has a proper label, it will tell me what the graphic label is. A button, it will tell me that it is a button and it will let me click the button, if I need to. I'm  talking about an image of a button on a screen. It will let me make selections from lists, there's a lot more to it than text, there is actually software called text readers, that only read the text. 

This is a much more powerful thing and the one I'm using is actually an open source screen reader called [NVDA](http://www.nvaccess.org/), which stands for Non-Visual Display Access, and it's been around for about ten years and it's a really fantastic screen reader. I'd say right now it's probably one of the best ones on the market if not the best one on the market.

[03:24] szabgab: Including the commercial, or the paying project, or..?

[03:30] lucy: Exactly, I mean, more and more people are turning to NVDA as their screen reader, when they're having problems on websites, when they're having problems with applications, and NVDA is coded expertly enough and very, very effective, so places where other screen readers have problems, NVDA can actually excel, and that's because it's a very standard-based piece of software, so they work to the standards, they code to recognize the standards and understand content that is created to standards, where the other screen readers take workarounds and basically break the standards, in very many cases, is what they do. But NVDA is, if your code follows standards, NVDA will read it. If your code is bad, NVDA will do its best, but tends to do a better job than most of the other screen readers, at least under my opinion.

[04:35] szabgab: Yeah, actually that's something that I wanted to ask you, much later in the podcast, later in the interview, but if you've already mentioned it, so I have been creating a lot of websites, and there is always this, in the back of my mind, but it's not further, that when I create a website, I should invest in making it screen-reader friendly, is that the right term?

[05:05] lucy: [Accessible](https://www.w3.org/standards/webdesign/accessibility) is the term we use. 

[05:07] screenreader: 22 minutes remaining, ten, if you need to continue using your computer, either plug in your computer, or shut it down.

[05:16] lucy: Sorry about that.

[05:18] szabgab: So now we are hearing the screen reader, right?

[05:20] lucy: Now we were just hearing the screen reader, correct, and it's because I moved my arm and knocked the plug out of the wall, for my computer.

[05:27] szabgab: Okay.

[05:28] lucy: Okay, we're back to normal, it's all plugged-in again. Okay, so yes, the term is accessible, for what you should be doing with a website, and that's because there are many other disabilities that web-accessible or accessible websites should be working with. So, for example, say a person has limited use of their hands, and they can't move with a mouse, say the only thing they can do it hit the Tab key on the keyboard, or hit one key at a time on the keyboard, with something called a head stick or a mouth stick, and that is literally, a head stick is something that's mounted to their forehead and they literally push buttons on the keyboard by tapping with that stick. A mouth stick is the same thing, except that instead of being mounted on their forehead, it's something that they're holding between their lips, and so by making websites accessible, you're actually allowing them, people who are blind and visually-impaired, people who may have no ability to type, people who are using speech-input only, can actually negotiate your websites and work through your websites, much more effectively. 

And the way to do this is by following the [W3C Standards](https://www.w3.org/standards/techs/wcag#w3c_all). W3C web-accessibility guidelines 2.0AA is an international standard that, if you follow the rules within there, and if you follow the guidelines and best practices, your website will be much more effective for everyone. Not only for people with disabilities, but we find that when a website actually is accessible to  persons with disabilities, it's actually more usable for everyone. When you start getting to fancy widgets and fancy divs, that you're using custom code that's not really good, pure HTML5, you end up making something that might be a little hard for the person with the disability and also we find that the average human being has problems with them, as well. That's my push for standards.

[07:50] szabgab: Yeah, yeah, okay. Are there tools, checking for this specific part of the standard?

[07:58] lucy: There's lots of really good tools, lots of really good free tools, Chrome has an [accessibility toolbar](https://chrome.google.com/webstore/detail/accessibility-developer-t/fpkknkljclfencbdbgkenhalefipecmb?hl=en), that is really quite good. It's very effective, very thorough toolbar. It has, for example, in it, a really nice color-checker that can do things like check your contrast and make sure your contrast meets minimum standards. It has the ability to check and make sure that your graphics all have labels on them and that your buttons actually all have proper labels on them, your form-fields are labeled properly. 

There's one called the [WebAIM toolbar](http://wave.webaim.org/extension/) and [WebAIM](http://webaim.org/), which stands for Web Accessibility In Mind, is a fantastic tool. It also runs in Chrome, I think currently the FireFox version is not there yet, I think they have some problems with the FireFox version but it's supposed to be back any day now. 

There's just hundreds of tools out there on the internet. All you have to do is look for web accessibility and you will find tons of pages, start with the W3C and work your way through, they have actually a list of tools. A majority of these tools are free, so they're things that you can incorporate into your workflow for free. 

One of my favorites is a tool called [Tenon](https://tenon.io/), it's actually a very, very powerful tool and incorporates into many, many, I would almost say all, development environments and it's an API that you can actually push, that will, as you're writing your code and testing your code, it will test your code on the fly. It's probably one of the most-effective ones for checking for accessibility of your code. It's not free, it allows, I think, a certain number of pages per month for free, and then you can subscribe to actually get more.

[10:04] szabgab: Okay, so let's get back to the main topic, or..?

[10:12] lucy: You might end up with more than one bit of content for this.

[10:17] szabgab: It's definitely interesting.

[10:19] lucy: So I'm here today to talk about our project, [DictationBridge](http://dictationbridge.com/). DictationBridge is something that's dear to my heart. Myself and another gentleman, who both have problems typing, because we've both been using computers for far too many years, and as a blind person who uses a computer, all we do is type. We don't do mousing, like we said before, and I've been using computers since 1985, probably upwards of ten to fifteen hours a day. 

My hands are getting old and getting sore, and can't take that kind of pressure any more, so I've turned to dictation, probably about 2000, and I've tried various different pieces of software to use dictation, ViaVoice when it was first available, [Dragon NaturallySpeaking](http://http://www.nuance.com/dragon/index.htm) in every single one of its versions, I think I've paid for every single version of Dragon since version two. 

And the problem is, is speech-dictation software doesn't communicate well with the screen reader. As the dictation software is placing the text on the screen, the screen-reader software isn't seeing it appear on the screen, so I could dictate and the text was there, but I had no way of knowing what the text it was typing, unless I went back and reviewed it, with my keyboard. So a bit of a contradiction, that you dictate to remove, or at least lessen, the amount of keyboarding that you're doing, by having to go back and review it, and go through it word-by-word or character-by-character, I'm actually typing just as much as I would have if I'd typed it to begin with. Now the problem with that is, dictation software's not perfect, I don't know if you've, you've probably had problems using your phone, dictating something and the wrong words come out.

[12:29] szabgab: Yeah, I've never ever tried it, because I was always afraid it won't understand me properly.

[12:35] lucy: It's pretty bad stuff, I mean, I've had some really offensive things come out of dictation myself, which we really worry about. So if I emailed something without confirming that what I had dictated was correct, we would be in serious, serious trouble.

[12:55] szabgab: Right, I can  understand this.

[12:58] lucy: And when it comes to using something like Dragon on the computer, if you don't fix the mistakes it makes, it's a learning algorithm, and the recognition can actually get worse if you don't fix it. So you could dictate something like <q>I live in a house</q> and it would say <q>I live in a mouse.</q> And if you don't fix the word <q>mouse</q> to <q>house,</q> it would actually get worse and worse, and eventually one out of every five words would be recognized instead of four out of every five words being recognized. It degenerates very, very quickly. 

When I used to teach people how to use dictation software, I would tell them it takes a long time, up to three to four weeks, to get a really good voice profile. It's better today, dictation software is much better than that. But it can take you as little as an hour to break a voice profile by not correcting it. I mean it just disintegrates very rapidly. It's really a very serious thing, so you can't be dictating unless you can recognize what the problems are and fix them immediately.

[14:16] szabgab: So how does the [DictationBridge](http://dictationbridge.com/) solve this problem?

[14:19] lucy: So what DictationBridge is, is at the core is a DLL that one of our engineers has developed that captures the text that's being dictated, before it's actually typed to the screen, and speaks it to us. It does actually let it be typed to the screen immediately, but it speaks the text that is being captured, and echoes it back to me, so that I can hear that a mistake was made, and then I can use the Dragon correction facilities to fix that problem, or the Microsoft Speech correction facilities to fix that problem, and tell it <q>No, I didn't mean a mouse, I meant house</q> and it would go ahead and fix that, and help me at least maintain a good voice profile. 

One of the other things that DictationBridge does is, both Dragon and Microsoft Speech, which we're working with both of those, have terrible interfaces. The screen reader can't actually grasp a lot of the information in those interfaces, for example, the Microsoft Speech dictation correction-window is a floating window that the screen reader couldn't actually grasp and figure out where it is on the screen, because it's not really there in a focusable place. And of course, if you try to focus in that window, the window goes away. So we've got some coding that will actually tell the screen reader where that window is, it will read the information in that window, and it will let us control the window and keep it on the screen. So it's not only giving us the echo back but it's giving us the ability to use the tools in an accessible way.

[15:59] szabgab: Yeah, so if I understand then, the speech-recognition software understands more or less what you say, then it goes actually to the DictationBridge, then it echoes back to you?

[16:14] lucy: Exactly.

[16:16] szabgab: And then when once you approve it, right, then it goes to the actual text?

[16:22] lucy: It actually goes to the text immediately, it just captures it on the way. So as it's going across the Bridge, the Bridge will echo it back. And it lets it go back to the screen, because that way, if you want to just make a correction by typing something, you can. And it's just basically providing a Bridge, that traps the information that's going across, speaks it back to you, and then lets it go on its merry path, but lets you fix it very easily, very effectively, from there.

[16:52] szabgab: Okay.

[16:52] lucy: Would you like to have a demo?

[16:55] szabgab: Yeah, let's have a demo.

[16:57] lucy: All right, so I'm going to be using Dragon, so give me one second here. 

Wake up. 

This is a demonstration.

[17:07] screenreader: This is a demonstration

[17:09] lucy: of how DictationBridge will echo my text.

[17:12] screenreader: of how DictationBridge will echo my text.

[17:15] lucy: If my voice profile is

[17:17] screenreader: If my voice profile is

[17:19] lucy: working well, the words will all appear correctly.

[17:22] screenreader: working well, the words will all appear correctly.

[17:25] lucy: So far, I haven't heard any mistakes

[17:27] screenreader: So far, I haven't heard any mistakes

[17:31] lucy: you will note that

[17:33] screenreader: you will note that

[17:34] lucy: when I use the words <q>wake up</q>

[17:36] screenreader: when I use the words <q>wake up</q>

[17:38] lucy: the microphone did not actually echo back.

[17:41] screenreader: the microphone did not actually echo back.

[17:44] lucy: That is one of the up-coming features

[17:47] screenreader: That is one of the up-coming features

[17:49] lucy: of our product. 

[17:51] screenreader: of our product.

[17:52] lucy: Period. Go to sleep. 

So I'm still using the beta version of the software and we haven't actually fully-implemented all the features we want. I turned the microphone off, so we can talk again. 

[18:06] szabgab: Okay, it's like having another person listening in to our conversation.

[18:12] lucy: Exactly, it really is, isn't it? So we want things, like a person to be able to know what state that the microphone is in, I've used speech dictation for years and I can't tell you how many times I've had phone calls transcribed, because I forgot to turn the microphone off, when I picked up the phone.

[18:30] szabgab: Oops.

[18:32] lucy: Only my side, luckily. 

So the goal of our project was to make a product like this, that has all the features we want, but we're really a grassroots group that believe in free software, so what we want is our product to be fully free for everyone and anyone to use. 

And typically, people who are blind and visually-impaired, don't have a lot of money. There's some massive statistics around the world that say things like 70% of the population who are blind and visually-impaired are unemployed. So buying expensive software, which screen readers typically are, they're about $1,100 for the leading screen reader on the market, and buying dictation software, like Dragon NaturallySpeaking, for another, say $200, that's a major investment for someone who might be on Social Security or might have some form of limited income, or no income. They can't be spending that much money to be able to be using a computer and in this day and age, you pretty much need a computer to get a job. 

So the goal of our project team was to make sure that a person who is blind or visually-impaired, could have access to dictation with the free screen reader, and using something as basic as Microsoft Speech recognition. So you could go out and buy-

[20:10] szabgab: Which is, if I am, just a second, I understand that it is free?

[20:14] lucy: It is free, it's completely free. It's shipped with every version of Windows since Vista. I wouldn't use it in Vista, I would only use it in Windows 7 and above, but it is completely free.

[20:25] szabgab: As in, free beer?

[20:28] lucy: As in free beer, exactly.

[20:31] szabgab: Once you paid for the Microsoft Windows, okay?

[20:32] lucy: Yeah, exactly, exactly. You have to pay for the glass, but once you get the glass, the beer keeps flowing.

[20:40] szabgab: Okay.

[20:44] lucy: So a person could get a fairly inexpensive laptop, say a $200-$300 netbook, running even something as old as Windows 7, and be able to dictate, using our Bridge and Microsoft Speech recognition and NVDA, the free screen reader. So that's pretty critical, and pretty important, when we think about third-world countries, African countries, where we've got poverty and we've got people with disabilities, those people with disabilities end up being marginalized and side-lined. 

So we wanted people who are poor to be able to use a computer, and learn how to use a computer, and access it, and if they didn't have the use of their hands, then they should be able to dictate. And that's the goal of our project.

[21:38] szabgab: Okay, so actually I wanted to ask about all these technologies. How much, how language-dependent are they? Is there any dependency on being in English?

[21:51] lucy: The screen reader has, I believe, 80 languages that are supported and they have a very good localization process so if there's a language that it currently doesn't support, they have a mechanism with which somebody can localize the screen reader very quickly and very effectively. Microsoft Speech recognition, I believe, works in 40 different languages; Dragon NaturallySpeaking has a large list of supported languages. 

So, no it's not limited to that. It is limited that you need to have a fairly high-end, well not actually even in this day and age, you could use a netbook. You could use a fairly low-end netbook. Anything over a 1.9 GHz processor, and that's even a single-core, will work. You do need to have about 4 gigs of memory, maybe 8 is better, but I have used this on a fairly low-end netbook and it works for me.

[22:57] szabgab: Okay, tell me a little bit about the project, about the development part, before we finish this conversation.

[23:08] lucy: So the really interesting thing about our team, is that we have only one sighted person on the entire team and she's doing the finances, and that's it. 

We have totally blind developers doing some of the coding, our primary lead-developer is low-vision. There's eight of us on the team and we have three developers currently, no sorry, four developers working on the project, out of the eight of us. 

And each person has a bit of responsibility for a different part of the code, so we wanted to make sure that we didn't only support the one screen reader, the free screen reader, we wanted to support all screen readers. So each developer has a screen reader that they've been assigned to work with and I'm not a coder myself, but it's really interesting, it has to do with some very low system hooks. Very few coders in the world actually have the skill-set to do system-hooking that will do things like capture the text from dictation, going to, basically they're having to intercept text between three applications and make sure that the right information is captured, doing things like re-mapping keystrokes to voice-commands is also very complex. 

So we've got some very good programmers and they are all contributing to this project. We did crowdfunding and the crowdfunding is paying for their time, because we don't believe that blind people should be forced to make things for themselves and do it for free. We wanted to actually pay them for their work. So we used crowdfunding to pay for their work but the product itself will be free. I'm not the best person to talk to about the coding but maybe you could have another episode with one of our developers, once the project is done.

[25:06] szabgab: Yeah, that could be interesting, but I actually wanted to ask you if people can, what kind of help can you get from other people? How can other people help you?

[25:19] lucy: Oh, we have a [GitHub repository](https://github.com/dictationbridge), we are on GitHub, DictationBridge is on GitHub. I'm sorry, I don't have the URL but I can actually give that to you so you can put that in the notes later. 

And this is fully, anybody can fork the code, anybody can re-contribute back. This is a full free software but it is also very open to anybody contributing, in fact we are always looking for people who would be interested in helping with it. 

The primary code for NVDA, for example, is in Python, but we have some C++ components, we have some system-hooking and DLLs. I've had a couple of people look at the source code and they say it is actually very easy to get in and look at the source code and understand and comprehend it. 

One of the things we find critical in the project is that we want anybody to be able to create a patch to this, improve it, and then contribute it back. It could be a person who's blind or vision-impaired, or be it a person who's just a coder who wants to contribute to bettering a product, so that everybody's experience is better.

[26:44] szabgab: Okay, anything else that you would like to say to the listeners of this?

[26:54] lucy: If you are a coder interested in doing something that's unique, we welcome your contributions, we welcome you, keep an eye on our website, keep an eye on our GitHub repository, let us know how you think you could help, and we're open to contributions. We want this project to continue on into the future. We have a specific feature-set that we're looking at for our 1.0, once we're finished 1.0, we're working on the plans for how we're going to do this in the future.

[27:31] szabgab: Do you know the timeline for that? Do you have a schedule for..?

[27:37] lucy: Since we're all working on our own time, even our developers are only spending their weekends, we refuse to release a date for release.

[27:45] szabgab: Yeah, okay, fair enough.

[27:48] lucy: We had a massive block about a month ago actually, we've only been working on the code for about two months, but we had a big block that caused a two to three week delay when we were trying to capture text in browsers. We couldn't get Dragon to echo back the text within browsers, it didn't matter which browser it was. 

It turns out that Dragon uses a special plug-in to send text to browsers and we had to figure out how to intercept that plug-in and capture the text from that, and that was a real road-block, it pushed us back quite a few weeks. 

So we're not setting any dates for anyone right now. But definitely keep an eye on the [DictationBridge](http://dictationbridge.com/) website and who knows, maybe we'll do another funding program in the future, we want this thing to go.

[28:43] szabgab: Yeah, yeah, it was really interesting to hear about this and I hope that we can continue talking as well, so to bring you back later in another episode and see, or hear at least, how the project progressed and what's the status, and how else people can help, not necessarily just with this project, but in general with accessibility.

[29:12] lucy: Thank you, I'd love to talk to you more about that. My profession is an accessability consultant, so that's why I got off on the tangent there, you kind of got me on my favorite topic.

[29:25] szabgab: Okay.

[29:25] lucy: All right.

[29:26] szabgab: So thank you very much, and bye bye.

[29:29] lucy: Thank you, take care, bye bye.

[/transcript]

<!--

## Technical info

Recorded on 3 September 2016 with "Ecamm Network Call Recorder for Skype v2.6.1" using the following settings:

<pre>
QuickTime Options:
  Audio Encoding: Uncompressed

Recoding Option:
  Record Video: None
</pre>

The recording stopped twice due to network failure but my son managed to stich them together.
-->
