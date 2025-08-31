---
title: "CMOS #17: Moyinoluwa Adeyemi creating Android Watch in Yorùbá"
timestamp: 2016-10-21T10:01:01
tags:
  - podcast
  - Android
  - Face recognition
  - Nigeria
description: "Creating Android Watch Face in Yorùbá. Facial recognition API in Android, using landmarks for the facial features, to locate specific parts of the face."
types:
  - interview
  - cmos
mp3:
  file: /media/cmos-17-moyinoluwa-adeyemi.mp3
  size: 19573318
  time: 21:57
#img: /img/cmos/moyinoluwa-adeyemi.jpg
#alt: Moyinoluwa Adeyemi
published: true
author: szabgab
archive: true
---


Interview with [Moyinoluwa Adeyemi](https://twitter.com/moyheen) about her Yorùbá Watch Faces app, available on the Google Play Store for Android phones, and her Face Detector work, now on [GitHub](https://github.com/moyheen/face-detector), but perhaps soon it will be an Android app. Moyinoluwa also tells us about the great developers now available in Nigeria!


{% youtube id="tJt4Dpgql4c" file="cmos-17-moyinoluwa-adeyemi" %}

<podcast>

<div id="person">
  <h2>Moyinoluwa Adeyemi</h2>
  <ul>
    <li>[@moyheen on Twitter](https://twitter.com/moyheen)</li>
    <li>[GitHub](https://github.com/moyheen)</li>
    <li>[LinkedIN](https://ng.linkedin.com/in/moyinoluwa)</li>
    <li>[@moyinoluwa on Medium](https://medium.com/@moyinoluwa)</li>
  </ul>
</div>

<!--
<div id="links">
  <h2>Links - articles about Moyinoluwa Adeyemi</h2>
  <ul>
    <li>[The Female App Developer](http://techherng.com/moyinoluwa-adeyemi/)</li>
    <li><a href= "http://womenofrubies.com/2016/08/10/meetprofile-moyinoluwa-adeyemi-the-woman-who-built-an-android-watch-that-tells-time-in-yoruba/">The Watch that Tells Time in Yorùbá</a></l>
    <li>[Another article about the Yorùbá Watch](http://woman.ng/2016/08/how-moyinoluwa-adeyemi-built-an-android-watch-face-that-tells-time-in-yoruba/)</li>
    <li>[Sunday Adalaja's Blog about the Yorùbá Watch](http://sundayadelajablog.com/nigerians-moyinoluwa-adeyemi-builts-android-watch-tells-time-yoruba/)</li>
    <li>[More about the Yorùbá Watch](http://howafrica.com/this-is-moyinoluwa-adeyemi-the-nigerian-lady-who-builds-watchface-that-tells-time-in-local-dialect-yoruba/)</li>
  </ul>
</div>
-->

<div id="links">
  <h2>Links</h2>
   <ul>
    <li>[The Radar Online Tech Community in Nigeria](http://radar.techcabal.com/)</li>
    <li>[The Yorùbá Language](https://en.wikipedia.org/wiki/Yorùbá_language)</li>
    <li>[Moyinoluwa Adeyemi writes about Machine Learning in Android / Face Detection](https://hackernoon.com/machine-learning-for-android-developers-with-the-mobile-vision-api-part-1-face-detection-e7e24a3e472f)</li>
<!--
    <li>A podcast where [Carina C. Zona interviewed at @codenewbie](http://www.codenewbie.org/podcast/algorithms) starting at 21:00 she talks about racial bias in photographic film in the U.S. in the 1950s and how that carried over into digital photography.</li>
-->
  </ul>
</div>

[transcript]
  [szabgab host1 Gabor Szabo]
  [moyheen guest1 Moyinoluwa Adeyemi]

[00:03] szabgab: 
Hello there, this is CMOS, the Code Maven open source podcast and video interview series, and I'm your host, Gabor Szabo. 
And with me is Moyinoluwa Adeyemi. Hi! 

[00:17] moyheen: Hi! 

[00:18] szabgab: 
Please correct the pronunciation, I'm really bad at this, I think. 

[00:21] moyheen: 
No, it's okay, it's okay, you tried. 

[00:23] szabgab: 
Okay, so welcome to the show. 
It's been some time, I was looking for you actually, I couldn't get a way to contact you. 
I was a little bit afraid of publicly talking on Twitter, so I really thank you for coming on the show. 
I understand that you are from Nigeria, right? 

[00:48] moyheen: 
Yes, I'm from Nigeria. 

[00:50] szabgab: 
So, tell me a little bit about your background. 
How did you get to coding and to open source, and I saw this Google Glasses on you, and quite a few things that I saw a couple of articles. 
So I would like to get some background about you. 

[01:10] moyheen: 
Okay, so I started computer science in the university here and while on campus, I got involved with the Google Developmenter group in my school. 
And that had a couple of experienced students who were developers too, and they tried to bring the rest of us into the field, and that was how I got started with programming seriously. 
And I was interested also in GitHub and I started learning it and from then up to now, it has been about three years of getting into the field and working with it professionally. 
I'm through school now and I'm a full-time Android developer, based on what I picked up back in school. 

[01:56] szabgab: 
Okay, so where do you work now? Are you employed somewhere? 

[02:01] moyheen: 
Yes, I'm employed, I work at [Swifta Systems](http://www.swifta.com/) in Nigeria. I'm an [Android](https://www.android.com/) engineer there. 
And it's like a developer agency, although we started to sell our own products now. 

[02:13] szabgab: 
Okay, so do you...so I understand that most of the things are out-sourcing but you also have your own product now?

[02:22] moyheen: 
Yeah, well we build apps for other companies but we also are starting to have our own product now. 

[02:30] szabgab: 
And are your clients primarily in Nigeria, other African countries? 

[02:34] moyheen: 
Yes, primarily Nigerian, most of them. 

[02:41] szabgab: 
Okay, and your open source world, so when have you started to write open source code? 
Right in the university? 

[02:49] moyheen: 
Well, not really. I...of course everyone has used the open source code from other developers but I think I started that actively after school. 
So I discovered that while programming for Android, sometimes I will need a couple of things, and I'll end up using libraries written by other developers and so after a while, after I got comfortable enough, after my Android developer and I earned a degree, I thought, <q>Why not contribute back to the society.</q> 
And well, I started with a workspace, I contributed, I build a webspace for a tech community in Nigeria and it was well-received, so I thought, why not just continue and build more. 
So most of the time now, when I write articles, I make sure I have source code to go along with it and then I push that to GitHub, hopefully to help somebody, somewhere, sometime. 

[03:46] szabgab: 
So, what is this watch face? I think I understand that it's some kind of a watch, right, I guess, running Android? 

[04:00] moyheen: 
Yeah, well so a watch face is like, it's not exactly exclusive but it's like building exclusively for Android-built devices, just like this tells the time, in realtime. 

[04:14] szabgab: 
Okay, so what...? 

[04:16] moyheen: 
So the open source one I built was an analog one, for [Radar](http://radar.techcabal.com/), a tech community, an online tech community for Nigeria, the biggest actually. 
And well, the notebook kind of looked like a watch already, so I thought, why not just make this into watches. 
And programming for Android is not really common for programmers in this region, so they love excitement. 
So people were excited so then I learned how to get started, which was what's the open source code. 

[04:50] szabgab: 
So do you have an Android watch, using this? 

[04:52] moyheen: 
Yes, I have a model 360, first generation. 

[04:59] szabgab: 
Do a lot of people...I understand that one of them was for the Radar community, right? 
That's the first one and then you created one for speaking [Yorùbá](https://en.wikipedia.org/wiki/Yorùbá_language)? 

[05:13] moyheen: 
Yeah, I did one for speaking in Yorùbá. 

[05:15] szabgab: 
So it does say aloud things, or just...? 

[05:19] moyheen: 
No, no, it just writes, does the time and writes it out on the watch face. 

[05:25] szabgab: 
And are there many people using it? 

[05:29] moyheen: 
Okay, yeah, there's a bit of story around that, because when I first created that, since a lot of people here were not used to Android-web devices, I got a lot of negative feedback. 
I was getting more stars on the Google Play Store, because people did not know how it works. 
They expected it to pop up on their phones. 
So when I discovered that, I went and viewed another application that works on the phone, too. 
So that's the applications now, there's one for the web-device and there's one for the Android phone. 
So even if you don't have an Android web device, you can still tell the time on your phone in Yorùbá. 

[06:06] szabgab: 
Okay, I understand. And are these both open source, the applications? 

[06:11] moyheen: 
No, the Yorùbá one is not open source, although I plan to open source the code, but just the conversion, because I did that myself. 
I talked to a couple of local speakers because I worked with them to get the translation from Yorùbá to what the app needed. 
So translate from realtime into Yorùbá, so I'm going to open source that. 
I've not gotten around to doing that yet but I plan to do that someday. 

[06:41] szabgab: 
Okay, so let me try to understand this. What was the problem? What did you have to translate? I don't understand that part? 
If I understand, you speak English and isn't Yorùbá also your mother tongue? Or...? 

[06:58] moyheen: 
Yeah, so I also speak Yorùbá. 
And what happens is a lot of people don't speak the language any more, and then there's this fear about the language dying off. 
So I thought that was one way the watch face could help, if it could teach, at least people in my age-group, how to speak the language. 
So I take the time in Ekiti states, say it's 5:42, and then I translate it and on the watch face what you see is 5:42 but in Yorùbá, not in English. 

[07:31] szabgab: 
Okay, so you had to translate the time to Yorùbá, that's what you're saying? 

[07:40] moyheen: 
Yes, I had to write algorithms to translate the time. 

[07:43] szabgab: 
Oh, you had to...oh, okay, is it difficult to say it in Yorùbá? Is it very different from English? 
The order of the number, or...?

[07:50] moyheen: 
Yeah, the numbers are different, it's a lot different from English. 
But anyone that  knows how to speak the language, would not have too much of a problem to learn to speak the time with the app. 

[08:06] szabgab: 
So for the one on regular Android phone, do you have a lot of downloads there? 

[08:16] moyheen: 
I have up to 500 downloads now although I am hoping that will sort of increase. I have about 500 downloads. 

[08:29] szabgab: 
Well, it's okay, I have no idea how many people would want to listen to this, or read it in Yorùbá, and have Android phone and know about it, right? 

[08:43] moyheen: 
Yeah, sure. 

[08:45] szabgab: 
How can people know about it? 

[08:48] moyheen: 
About the app? 

[08:49] szabgab: 
Yeah? 

[08:51] moyheen: 
Well, it's on the [Google Play Store](https://play.google.com/store/apps/details?id=com.moyinoluwa.yorubawatchfaces&hl=en), so anybody that wants it can go download it. 
It's still Yorùbá Watch Faces, I don't know if that name is correct since it's more than a watch face now, but it's still called [Yorùbá Watch Faces on Google Play Store](https://play.google.com/store/apps/details?id=com.moyinoluwa.yorubawatchfaces&hl=en). 

[09:12] szabgab: 
Do you have some way to encourage people? 
To let each other know about it? 
So, to create some kind of a way for people to tell about it? 
So otherwise, I mean, how many people would look for it, right? 

[09:31] moyheen: 
Well, not so much for now. 
But at a time you really need it, I don't think you would think of it. 
But we're doing a lot of publicity so anybody I meet, I ask them, <q>Do you have this on your phone?</q> 
If they say no, they are going to download it immediately. 
But I've been doing a lot of word of mouth but I guess I'll have to figure out how to improve that. 
But then it started as a side projects, I didn't go into it thinking I was going to solve this problem, so I'll have to just think about how to promote it. 
How to promote the app. 

[10:09] szabgab: 
Okay, I also saw another article from you. 
I don't know if it has more parts or only the first part, about the [face detection](https://hackernoon.com/machine-learning-for-android-developers-with-the-mobile-vision-api-part-1-face-detection-e7e24a3e472f). 
Tell me about that one, please? 

[10:23] moyheen: 
Yeah, okay, so very recently there was the [Google Launchpad](https://developers.google.com/startups/accelerator/) Summit in Nigeria by the [Google Developer](https://developers.google.com/) developing, and one of the sessions was machine learning with the Google API's methods, and that looks cool. 
After I attended the presentation, I thought it was cool, so I had free time on my hands and decided to check it out. 
It was fine and interesting because at least for the face detection, there are three APIs for mobile developers, and I checked out the face detection, it looked interesting. 
I tried to...I went through the [Codelab by Google](https://codelabs.developers.google.com/), and tried to replicate it and then make it personal. 
I'll build my own thing out of it, when I started learning it, I found how interesting it would be to take images, get them, and then transpose other images on top of them. 
So I thought I'd never read an article about this before, about the official work from Google site, but it's VR that they write about. 

[11:36] szabgab: 
I saw the article, that you had the faces, and then you put eye patches on that? 

[11:43] moyheen: 
Yeah. 

[11:44] szabgab: 
Did you do that programmatically? 
Or did you put it manually and then was using the face recognition to not recognize that there are eye patches there? 

[11:57] moyheen: 
Yeah, so pattern thinks the API helps you to detect landmarks on the face, like the eye, the cheeks, and then the mouth. 
So what I did was I detected the eyes and then I did it programmatically, so I positioned the images relative to the positions of the landmark. 
So it works for any image, but I have not published the app yet, but I expect it to work for any image. 
So once I improve it, and put image where the eyes were, and then puts the eye patch itself. 

[12:30] szabgab: 
And images of a face of someone, right? 

[12:34] moyheen: 
Yes, the face of people. 

[12:36] szabgab: 
Okay, and then what kind of calls do you have like a landmark, get me the left eye or get me the right eye, like this? 

[12:46] moyheen: 
So each eye, I discovered that each of the landmarks have unique numbers, but I don't know what those numbers stand for, but I checked on it and I discovered all the faces had unique numbers that were identical, so the left eye was, I think four, I'd have to check that again, but each of the landmarks had unique numbers so all I did was, if the landmarks type is four, then put this image there. 
If the landmarks type is say five, and then five is the cheek, put another image there. 
So all I did was just detect the landmarks and then put images based on what landmark it was. 

[13:29] szabgab: 
What are your plans with this project? 

[13:34] moyheen: 
Well, like how all my interesting projects start off, I just did this for fun, at least initially, but it might come together in a piece, I don't know yet what...I don't know, I think I'll just keep working with it, I plan to improve it and at least make the code cleaner and follow more practices. 
As of now, I'm currently doing the presentation on the main frame, I plan to move it to the background, create another of that...and I honestly don't know what will come out of this but maybe something more interesting than the Yorùbá, because that also started as an experiment and before I knew it, it became a full app. 

[14:19] szabgab: 
Okay, and I saw that the source code is available on [GitHub](https://github.com/moyheen/face-detector) and is that also an app in the Android store? 

[14:27] moyheen: 
No, no, no, it's not yet. This was just to show what was possible. It's not on the store yet. 

[14:34] szabgab: 
It's a pity, when is it going to be there? 

[14:37] moyheen: 
I'll have to do a lot more work before it can go on there. For now, like I wrote in the article, I didn't follow any best practices. 
I just wanted to show what was possible so I'll have to clean up the code, maybe add a couple of more featurs, because I don't think anybody's going to just download an app that's just putting an eye patch over their left eye? 

[15:02] szabgab: 
Well, you might be surprised! 

[15:06] moyheen: 
Well, and then there were, I noticed a bit of an issue with some of the faces. 
For faces that were facing the camera directly, my face was, I was deleting that picture. 
I didn't have any issues with the image of my face because I was looking directly into the camera. 
But you noticed that some people in the picture had their heads bent and the image wasn't aligned perfectly with the left eye, so I will have to go back and see how I can optimize for that, detect faces that are bent and then try to calculate the positions of the image, based on the face. 
I still have more work to do on that, and then... 

[15:47] szabgab: 
So what about uploading, adding some features to the application that, where people can give you feedback? 
How well it works? 
And then you can upload it to the apps store and tell people, this is for demo and this is for learning it, so don't expect anything, but I need feedback for how it behaves, works for you? 

[16:10] moyheen: 
Okay, I think I'll consider that. I didn't look at it that way. 

[16:16] szabgab: 
So there's a very, I don't know, strange and interesting aspect of this, because when I saw [that article](https://hackernoon.com/machine-learning-for-android-developers-with-the-mobile-vision-api-part-1-face-detection-e7e24a3e472f#.qzflujbdj), and you had this picture with five people, I think, and the landmarks pointed out. 
And obviously all the people were black, and the interesting thing is, just a couple of weeks ago I read an article explaining that most of the photo-recognition software algorithms work much better for light or white faces, than for dark and black. 

(Actually this was a [podcast](http://www.codenewbie.org/podcast/algorithms) where Carina C. Zona, the interviewee, is talking about film development in years past. Starting at 21:00.)

[16:56] moyheen: 
Oh, really? 

[16:58] szabgab: 
Yeah, and it was basically a complaint, that the companies probably, I mean these are all probably U.S.-based companies, and then because of the market, being primarily light or white people, so they hadn't invested enough in the algorithm for black faces. 

[17:23] moyheen: 
Well, this is the first time I'm hearing that actually! 
I expected it to work since they said it worked for all faces, I really wasn't expecting any issues. 

[17:39] szabgab: 
Yeah, I don't know if this software has the same issues or not. 
Or even if any of this whole thing is really true, I haven't really researched it. 
I just read an article about it, like a week or two ago, and well, I was surprised, obviously, a little bit, maybe not too surprised, because I mean, I don't know, these strange things do happen. 
But I was wondering first of all, whether you know about it, apparently you don't. 
And would be interested, if have you tried the software on white people as well? 

[18:26] moyheen: 
Well, I haven't but now that you mention it, maybe I'll go back and do that and edit my article, but I wasn't expecting any issues and I didn't have any real issues with it, it worked as expected. 
And the only places where there were challenges was where some of the heads are bent. 
If you notice the last picture, to the right, the head was a bit bent, so the software didn't pick up the right eye and a couple of other landmarks on the face, but that was practically all the challenge I had with it. 
I'll go look for this article and see what it says. 

[19:02] szabgab: 
I'll try to find it and send it to you, if you don't find it. 
But it's definitely an interesting thing and I would really want to know a little more about it, whether it's improving or it's a non-issue, actually. 

[19:25] moyheen: 
Yeah, I think it is so. 

[19:28] szabgab: 
Okay, great. What other open source projects have you been doing? 

[19:37] moyheen: 
Let's see, I have...well I am practically just starting out seriously with open source and the two you've mentioned have been my biggest so far but I can definitely say, expect more from me because I'll continue trying out new stuff and I'll definitely write about it, and if I write about it, then I'll have to publish the code to GitHub. 
So it's quite new to me but I'll keep pushing out more stuff. 

[20:08] szabgab: 
What would you say to...so these applications, they're primarily your playground, right? 
Do you have...do you expect people to contribute code? 
Or help in any way, in your applications? Or you just want...? 

[20:27] moyheen: 
Yeah, some people have already started helping. 
Someone sent a pull request about two days ago, because I had quoted the positions of the eye patch relative to the eye, and someone sent in some contribution to calculate that position programmatically and I accepted it because it worked fine, so anyone can contribute now, it's free to contribute. 
If you think you have something that can make it work better then I'll be waiting for the pull requests, whenever that comes. 

[21:03] szabgab: 
Great, thank you. 
Before we close this interview, do you have anything else that we haven't discussed that you would like to tell the listeners or the people who are watching it? 

[21:18] moyheen: 
Yeah, well, maybe watch out for developers from Nigeria. 
I know we don't hear a lot about us too often, but there are a lot of good guys here doing good stuff. 

[21:32] szabgab: 
Yeah, actually I have... you are, I think, the fourth from Nigeria that I have interviewed on the podcast and there are really interesting things that all of you have been telling me, so...yes, I agree! 

[21:49] moyheen: 
Yeah, so watch out for us! 

[21:50] szabgab: 
Okay, thank you very much for coming on the show. 

[21:54] moyheen: 
Yeah, thank you for inviting me, it was nice. 

[21:55] szabgab: 
Bye bye. 

[/transcript]

