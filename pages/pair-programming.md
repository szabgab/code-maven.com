---
title: "Pair Programming"
timestamp: 2017-04-20T14:30:01
tags:
  - Agile
  - XP
published: true
author: szabgab
archive: true
---


[Pair programming](https://en.wikipedia.org/wiki/Pair_programming) is one of the key elements of [Exrteme Programming](https://en.wikipedia.org/wiki/Extreme_programming). It is an [agile software development technique](https://en.wikipedia.org/wiki/Agile_software_development) in which two programmers work together at one workstation.

In this article we'll see some explanation on why it is good and how to do it. You'll also see information on how to do it locally and remotely.

Finally this also includes the description of the Pair Programming workshops I run.


## Advantages of Pair Programming

* Better software through faster feedback
* Better problem solving.
* Improved software quality - less bugs - cheaper software.
* Improved knowledge sharing. (The vacation of the leaving of one person will have smaller impact the knowladge of the company)
* Faster learning. (Of new techniques and of the code-base itself.)
* Higher job satisfaction (better team morale).
* It is Fun

## Disadvantages of Pair Programming

* At first it might be difficult to convince management that you are not wasting time.
* Pair programming is exhausting. Plan for breaks! Even with breaks you will not be able to sustain it for 8-9 hours every day.
* Personal hygiene is even more important than when you "just" work in the same office.

## Related articles

* [Research complied on Pair Programming by Laurie Williams](https://collaboration.csc.ncsu.edu/laurie/Papers/ESE%20WilliamsPairProgramming_V2.pdf)
* [The Cost of Bugs: Why You Can’t Ignore Software Testing](https://xbsoftware.com/blog/cost-bugs-software-testing/) (A nice graph showing the relation of time passed since bug introduced vs. cost of fixing the bug.
* [Defect Prevention: Reducing Costs and Enhancing Quality](https://www.isixsigma.com/industries/software-it/defect-prevention-reducing-costs-and-enhancing-quality/) - explaining that finding bugs later costs a lot more than finding bugs during development. Some research is included.
* [Pair Programing by Thomas Sundberg](https://thomassundberg.wordpress.com/2012/06/15/pair-programing/) actually this article on [Pair Programing](http://www.thinkcode.se/blog/2012/06/15/pair-programing).
* [Remote Pair Practice by Code Cop](http://blog.code-cop.org/2012/08/remote-pair-practice.html)
* [Pair Programming Illuminated](https://www.google.com/search?q=pair+programming+illuminated) (book)
* [I Have Pair Programmed for 27,000 Hours: Ask Me Anything!](https://www.youtube.com/watch?v=rIcUXcyC6BA) (30 min video)
* [Want to be a developer? You should probably be Pair Programming.](https://medium.freecodecamp.org/want-to-be-a-developer-you-should-probably-be-pair-programming-2c6ec12c4866) (an explanation with some strange imagery)
* [Sam Livingston-Gray gSchool talk: Tools for Pair Programming (remote or otherwise)](https://www.youtube.com/watch?v=W_hsEi_UZHE) (45 min video)
* [Thomas Sundberg "(Remote) Pair programming"](https://www.youtube.com/watch?v=Yq1qgWvSIdI) (45 min video)
* <a href="https://medium.com/@jdxcode/how-to-pair-program-d6741077e513"">How to Pair Program</a>
* [Effective Navigation in Pair Programming](https://www.thoughtworks.com/insights/blog/effective-navigation-in-pair-programming)
* [5 Rules of Pair Programming Etiquette](https://blog.rapid7.com/2017/01/27/5-rules-of-pair-programming-etiquette/)
* [How To: Get the Most Out of Pair Programming](https://www.coursereport.com/blog/how-to-get-the-most-out-of-pair-programming)
* [XP - Pair Programming](http://www.extremeprogramming.org/rules/pair.html)
* [How to Pair Program](https://www.wikihow.com/Pair-Program)
* [Pair Programming](https://medium.com/@fagnerbrack/pair-programming-8cfbf2dc4d00) a 4-part series of articles

<h3>Cockburn , Laurie Williams: XP 2000 pair programming</h3>
* 15% more time
* 15% less bugs
* [The Costs and Benefits of Pair Programming (2000) ](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.26.9064)


## Pair Programming Workshops

These workshops are organized in Israel via the [Code Mavens](https://www.meetup.com/Code-Mavens/) Meetup group.

In these workshop we provide an opportunity to experiment with Pair Programming without the pressure and fear involved in production code.  

You already know how to program alone. You can do that as much as you like at work or at home. Here we try something else.

We would like to learn from each other something we can rarely do in a company where everyone is responsible for their own code. And no, code reviews as they are done in most places usually don't help that much. 

In this workshop our primary objective is to experience how pair programming works and to experiment with various setups. You are going to work in pairs. We will start with the driver navigator approach with 5 min per rotation. Each pair can then adjust as they feel right. The point of the session is to learn what works for you. The navigator driver technique means in each pair one person will be the navigator who thinks about the big picture and who tell the driver what to write. Then, after a few minutes of work the two people will switch task.
There will be questions for example what to do if one person is familiar with a module/library that could help in your work and other one not. For how long will you stop to explain the benefits of that library? How much time will you spend teaching the other person. These issues and the way you handle them is part of the experiment. Different pairs will reach different conclusions.

A the beginning of the workshop you will get a project to work on. Your task will be to try to impement the project along with tests as you feel fit.

At the end of the workshop we will have a retrospective in which every person will be able to tell what was their experience. What would they change in the process and in the workshop to make it better for them.

A few things to remember.
You will be working much closer to another person. Make sure this does not cause any unpleasant feeling.
You will work on a single computer. The owner of the computer will be much more comfortable with the keyboard of that computer and the tools ans the setting will reflect the preferences of that person. Make sure this does not impide on the work done by the other person. ( as much as you might love and know vim, don't force the other person to use it when it is their turn to drive. On the other hand you can use this opportunity to show why do you love your editor.
Make sure both of you can comfortably see the code. This means the fonts are large enough for both people and the color scheme works for both person. Some people are used to dark background others prefer white background. Some people are color blind and it is hard for them to see specific colors. Be prepared to change font size and the color of your editor. 
Be flexible and be patient with each other.
In every cycle the navigator is expected to do most of the talking, but the driver should also be able to voice their opinion. They are also encouraged to say what they are writing.
If you really cannot work on each others environment you could try to switch computers when you switch roles. For this youll need to be able to rapidly transfer the files you are working on from one syatem to another. Git and github can be used for that.

Also remember that in a single 2 hour session you wont really learn pair programing. It takes several such sessions till you start feeling the positive impact of it. This workshop is there to allow you to taste it and to get started with it.
Working with a person you don't know much have both advantages and disadvantages. Try to see the bright side of it.

<h3>Audience</h3>

Both students and experienced developers are welcome!

<h3>Objectives</h3>

The primary objective of this session is to let you experiment with Pair Programming. To let you learn from each other without the pressure and fear involved in production code.

<h3>Process</h3>

* At the beginning of the workshop you'll get an explanation about Pair Programming and our process
* Then you'll get a task that you can implement in a few hours of work.
* We will also arrange that each one of you will have a pair to work with.
* Then you'll do the work in pairs.
* At the end we'll have a review of the results.

## Pairing process

If you already have a person you'd like to work with that's fine.
Otherwise we have two strategies:

* We will group the people by programming language they'd like to use. Then within each group we might(!) arrange for proficiency in that languages and we'll try to put together people who are close to each other in term of proficiency.
* Random pairing process: We'll put the names on pieces of paper. Put them in a hat and pull the names for the pairs from there.

<h3>Development Methodology</h3>

You are recommended to use TDD - Test Driven Development. You'll get help if you don't know how to start.

<h3>Development Languages</h3>

You can use any language you'd like, but you need to find a pair who will want to use the same language. The best would be if posted the language of your preference as a comment to this announcement and see if others respond. In any case I'd glad to see developers in the following languages join us:

* JavaScript
* Perl
* Python

<h3>Spoken Languages</h3>

There will be a short presentation in Hebrew which can be switched to English if some people have hard time understanding Hebrew.
The pairs can speak whatever language they both know. Hebrew, English, Arabic, Russian, Hungarian...

<h3>Patterns for working in pairs</h3>

* Driver - Navigator
* Driver - Observer (aka Teacher - Observer)
* Joint  discussion  and  brainstorming - typist

In the Driver-Navigator pattern one person, the Driver, writes the code. The other person, the Navigator, tells the driver what to write.  The Navigator explains the task at the highest possible abstraction that matches the knowledge and experience level of the driver.

In the Driver-Observer pattern the Driver writes the code and articulates and explains what is being done. The Observer watches to learn and to find issues with the code. The Observer is free to ask questions.

<h3>Patterns for switching roles</h3>

* Time based (Pomodoro) e.g. every 5, 15, or 25 minutes.
* Ping-Pong: frequent role changing
* Ping-Pong: A: Test, B: implement, refactor, test for next task.
* Ping-Pong: Change after every implemented method
* Far sight navigator: Navigator is looking ahead, planning. They don't switch very often
* Silent: the pairs don't speak. One implements test, other implements the code.

We are going to experiment with the Driver-Navigator method starting with 5 min rotations. In this method one person is the driver who writes the code. The other person is the Navigator who tells the driver what to write.

The navigator explains the task at the highest possible abstraction that matches the knowledge and experience level of the driver.

As time progresses you will pay attention how you work and you can adjust.
The critical part is that you both pay attention.

<h3>Requirements</h3>

You bring your own computer. (In the end we'll need one computer per pair, but you might be switching computer as well.

You will work very closely with another person. Please take extra care of your <b>Personal hygiene</b>. Bring some chewing gums if necessary.

<h3>Expectations</h3>

Pair programming might not be good for everyone and even people who eventually start likeing it might not work well with evey potential pair.

In addition, in order to be good at pair programming one needs to work that way for many hours.
A single workshop of 2-4 hours will only give you a taste.
In order to really see the benefit most people have to practice it during several 2-4 hours long sessions.

<h3>Retrospective</h3>

At the end of the session we are going to have a retrospective. This is 10 min session in which every one can tell us about their experience. What did they learn. How would they improve the pairing and the whole workshop.

<h3>Tools for local pairing</h3>

* One computer to be used by both people.
* If your setup is very different (OS, editor, etc.) it might be easier to use a Git repository to pass the code back-and-forth and switch computers when switching driver.


## Tools for remote pairing


* Network connection
* Shared coding environment
* Person-to-Person communication (video, audio, text)

* Multi-user editors (Cloud9, SubEthaEdit)
* Screen sharing (VNC, Skype, JoinMe, iChat)
* Terminal: (SSH and tmux or screen)
* one dev hosts on their machine or all devs SSH to a shared server
* [Teamviewer](https://www.teamviewer.com/)

The setup of Sam Livingston-Gray:

* Network layer: SSH over Hamachi
* Code: wemux + vim [ls-pair](https://github.com/livingsocial/ls-pair)
* For pairing: FaceTime in iPad (built-in mic and speaker)
* For meetings of pairs with n > 2: Google Hangout (external mic and speaker, plus $3 Shush.app for push-to-talk)

## Coding Dojo

Some generic ideas for tasks (or Katas)

* From scratch given the full task up-front.
* Where the task is given step by step.
* Give an existing applications that needs refactoring.
* Where the tests already exist, the participants only need to implement the code.
* Project that depends on one language only.
* Project that depends on multiple languages.

[Exercises and task](/exercises) to do in a Coding Dojo.

