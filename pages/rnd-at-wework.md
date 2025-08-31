---
title: "R&D at WeWork"
timestamp: 2018-07-08T08:00:01
tags:
  - R&D
published: true
author: szabgab
archive: true
---


<a id="rnd-logo" href="https://www.wework.com/"><img src="/img/rnd/wework.png" alt="WeWork logo"></a>

<div class="rnd-author">
  <img class="rnd-author-img" src="/img/rnd/yonatan-bergman.png" alt="Yonatan Bergman">
  [Yonatan Bergman](https://www.linkedin.com/in/yonbergman/) Senior Director Of Engineering at [WeWork](https://www.wework.com/) leading the Tel Aviv, Israel office of WeWork.
Yonatan is an experienced software engineer and manager with an eye for design and a passion for building great products and teams. Focused on consistently improving and nurturing team culture, productivity, technical excellence, as well as empowering those around him. [GitHub](https://github.com/yonbergman) Twitter: [@yonbergman](https://twitter.com/yonbergman).
</div>



<div class="qa">
  <div class="question">
    What kind products / services does your company develop / maintain? (web based, on-site appliance, hardware, etc.)
  </div>
  <div class="answer">
    We build a whole array of products/api/services that help WeWork scale and provide a holistic experience for our members. The majority are cloud hosted web services/Interfaces, mobile applications and some hardware.

    We build the software the creates the OS to run the company of the future. Everything from streamlining construction and real-estate deals, operating our sales and marketing flows. All the way to sensor networks that give you insights into space utilization,  a mobile app that behaves as a remote control to the building from meeting rooms, guest registration and a console that let's help community managers foster culture inside existing companies and locations. 
  </div>
</div>

<div class="qa">
  <div class="question">
    Number of engineers: 
  </div>
  <div class="answer">
    Today we have about 180 engineers around the world, 60 of them are here in Tel Aviv
  </div>
</div>


<div class="qa">
  <div class="question">
    Are there any remote engineers? (If yes, how does that work out?)
  </div>
  <div class="answer">
    We don't have remote engineers or teams but we are dispersed across 5 R&D centers. New York, Tel Aviv, San Fransisco, Shanghai, and Singapore.
  </div>
</div>

<div class="qa">
  <div class="question">
    How much interaction is among the people in different locations vs. inside a single office?
  </div>
  <div class="answer">
It really depends on the group. We strive for all our first level teams (aka squads) to be fully co-located. Meaning that
everyone engineering, product, design all sit in the same physical location, in most cases even right next to each other. As
you go up our org chart the groups become more distributed.
This leads to a lot of interaction amongst the people in your squad that are in your office, for groups that share missions
across offices they have more need to collaborate via email, Slack and video conferences.
We also have guilds and other structures to increase interaction in one office outside of the squad structure.
  </div>
</div>

<div class="qa">
  <div class="question">
     What are quads and guilds?
  </div>
  <div class="answer">
    Squads are our first level team, smallest multi-discipline team. Usually 8-12 people including engineers, product managers and designers.
    Guilds are a-formal groups of interest around technical and non-technical topics like React, Databases or API design.
  </div>
</div>


<div class="qa">
  <div class="question">
    What are the most common tools that engineers use?
  </div>
  <div class="answer">
    Not sure how to answer this one ;)

    We have over 30 teams across the world working on very different applications and in many different languages, I don't think we have something that we can call a common tool.
  </div>
</div>

<div class="qa">
  <div class="question">
    Which languages do engineers code in?
  </div>
  <div class="answer">
    Because we build and maintain an eco-system of about a 100 services we have a lot of languages depending on the application and the use case.
    We have Ruby on Rails, Java/Kotlin, Go, Scala, Python, and NodeJS on the backend. We're predominantly doing React on the web but we do have some BackboneJS and Angular. Mobile is mostly native (Swift and Java). 
  </div>
</div>

<div class="qa">
  <div class="question">
    Which operating systems do you use?
  </div>
  <div class="answer">
    Most of our engineers develop on OSX and our services are deployed on multiple OSes.
  </div>
</div>

<div class="qa">
  <div class="question">
    Which databases do you use?
  </div>
  <div class="answer">
    Mostly relational databases like PostgreSQL, we do have Redis and Elasticsearch for some use cases and Redshift as our DW.
  </div>
</div>

<div class="qa">
  <div class="question">
    What is the system architecture? (Monolith, Microservices, Mix, etc…?)
  </div>
  <div class="answer">
    We have a few monoliths in our architecture but we're moving towards a world where it's mostly well organized services - some people would call this Microservices :)
  </div>
</div>

<div class="qa">
  <div class="question">
    What kind of cloud infrastructure do you use?
  </div>
  <div class="answer">
    Mix of cloud providers based on our needs.
  </div>
</div>

<div class="qa">
  <div class="question">
    What Agile practices do you employ? (Daily stand-up, Sprints, Retrospectives, ...)
  </div>
  <div class="answer">
    It mostly depends on the team to choose, but the vast majority do hold major practices of some variation of
    agile/scrum/kanban. Including daily stand-ups, weekly grooming sessions as part of sprints (we mostly adhere to 2 week
    sprints, but again depending on the team). As far as I know most of the teams do hold retros too.
  </div>
</div>

<div class="qa">
  <div class="question">
    What does DevOps mean in your company? (Do you have a dedicated developer experience/developer tools team?)
  </div>
  <div class="answer">
    DevOps is part of the responsibility of the squad, you develop the code, you deploy and monitor it too :)
    "You break it you fix it" mentality.
     We do have a dedicated foundations team that leads strategy, tooling and training in the world of Devops.
  </div>
</div>

<div class="qa">
  <div class="question">
    Is anyone on-call? Who? (Developers, DevOps people, ...?)
  </div>
  <div class="answer">
    Depends on the system and the team, but developers are on-call for their own systems.
  </div>
</div>

<div class="qa">
  <div class="question">
    What is the development process like? (The lifecycle of a piece of committed code, branching strategy)
  </div>
  <div class="answer">
     Every change into our master branch goes through dedicated feature/fix branches that get merged in after they get reviewed
using GitHub pull request feature. During that time the code goes through our CI which usually means testing it, linting it
and any other automation that we have set up for that system.
  </div>
</div>

<div class="qa">
  <div class="question">
    Do you do pair-programming?
  </div>
  <div class="answer">
    We support pair-programming including certain offices having dedicated pair-programming stations, but like most other places
    I don't think we actually do it that often.
  </div>
</div>


<div class="qa">
  <div class="question">
    Do you do code reviews? How often? What is code review like?
  </div>
  <div class="answer">
    We love code reviews, each piece of code that reaches production usually sees two other sets of eyes. We've been very strict
    about integrating tools like linters into our CI process to decrease the effect of bike-shedding during CRs. Everyone does
    CRs to everyone and it's absolutely crucial for us since we hold an inner-sourcing model where any team can contribute code
    to any system.
  </div>
</div>

<div class="qa">
  <div class="question">
    How is testing done? (Manual QA? What kind of tests are run? How long does a test cycle run?)
  </div>
  <div class="answer">
   We try to avoid manual QA as much as possible. We aim at the bottom of the testing pyramid with a majority for unit and regression testing and a bit ui testing where relevant. Testing cycles take from a few minutes to an hour depending on the project.
  </div>
</div>

<div class="qa">
  <div class="question">
    How is code released / deployed? (How often? Who can do it? Do you have staging environment? Deployment circles?)
  </div>
  <div class="answer">
    Code is deployed on a need to basis. Meaning mostly once or several times a day. We have a staging environment and for majority of projects we spin up an environment per pull request as well.
  </div>
</div>

<div class="qa">
  <div class="question">
    What is an average day-in-the-life of someone on one of the engineering teams?
  </div>
  <div class="answer">
    <ul>
      <li>Come in the morning for the daily standup, on the way there stop at the barista station and pick up your fav coffee.</li>
      <li>Start working on one of the tasks in the sprint, spend some time code reviewing or pairing on someone else tasks.</li>
      <li>Because it's WeWork we usually have some sort of community happy hour for the members of our building that we join.</li>
      <li>An optional guild meeting on some advance technical topic that you can decide to skip if you're too busy.</li>
      <li>Deploy your code from earlier today to production just in time to hop on a call with your colleagues in New York about that design review they're working on.</li>
      <li>Head out for the day 🌔</li>
    </ul>
  </div>
</div>

<div class="qa">
  <div class="question">
    What makes your company a special place to be an engineer?
  </div>
  <div class="answer">
    WeWork is special because on the one hand the company is so big and is doing a lot of things but on the other hand we’re not that many engineers. That means people get to work on a lot of different types of problems and systems in order to deliver value.
  </div>
</div>

<div class="qa">
  <div class="question">
    What was a major problem you as an engineering organization have encountered in the last year and how did you solve it?
  </div>
  <div class="answer">
   When we past a certain threshold of engineers (about a 100) we understood that the engagement model with teams like devops and QA doesn't scale. We shifted the dev platform group from a [service provider organization](/service-provider) to a [strategy and tooling org](/tooling-teams). This was a painful move for us because we haven't yet had the skills embedded in all our squads and we didn't have the self serve infrastructure already in place.
  </div>
</div>

<div class="qa">
  <div class="question">
    Any disaster you could share with us?
  </div>
  <div class="answer">
    About a year ago we onboarded our biggest enterprise client at the time, which included 10's of thousands of employees. Our system for adding new members wasn't equipped to handle that load and the set of services and events that propogated brought our system to a halt. That happened during the busiest day of the month when we onboard all the new members joining WeWork. We quickly scrambled to scale the relevant servers and clean the queues and after about an hour of troubleshooting the issue everything was back to normal. Since then we added [circuit breakers](/circuit-breaker) and reconfigured the onboarding flow sow that it can scale with the number of new users added to the system.
  </div>
</div>

<div class="qa">
  <div class="question">
    What else would you like to tell people interested to the work at WeWork?
  </div>
  <div class="answer">
    If you're looking to experience what it means to be at a true hyper growth company, where your team and group double in size every year, where new projects and business lines start every quarter and where you can have a major impact no matter who you are. If you're looking to join a company that has a net-positive effect on the world and the people in it and if you're looking to join a group of diverse people from different backgrounds, skillsets and experience that love working together - WeWork is the place for you.

The [engineering blog of WeWork](http://engineering.wework.com/) is an excellent place to get more insight.
  </div>
</div>

