---
title: "R&D at Graduway"
timestamp: 2018-07-12T08:30:01
tags:
  - R&D
published: true
author: szabgab
archive: true
---


[Graduway](https://graduway.com/) a Raanana, Israel based tech company that provides SaaS products aimed at universities, schools, enterprises, and other organizations.

<a id="rnd-logo" href="https://graduway.com/"><img src="/img/rnd/graduway.png" alt="Graduway logo"></a>

<div class="rnd-author">
  <img class="rnd-author-img" src="/img/rnd/antony-gelberg.png" alt="Antony Gelberg">
  [Antony Gelberg](https://www.linkedin.com/in/antgel/) VP R&amp;D. You can also reach him [@antgel](https://twitter.com/antgel).
</div>


<div class="qa">
  <div class="question">
    What kind products / services does your company develop / maintain? (web based, on-site appliance, hardware, etc.)
  </div>
  <div class="answer">
Our main products are Alumni Networking and Mentoring Intelligence, subscription SaaS products aimed at universities, schools, enterprises, and all institutions that wish to foster improved connections between alumni. We are the market leaders with over 600 customers, and we're growing fast.
  </div>
</div>

<div class="qa">
  <div class="question">
    Number of engineers:
  </div>
  <div class="answer">
    12 Full Stack Developers, 3 QA-ers.
  </div>
</div>


<div class="qa">
  <div class="question">
    Are there any remote engineers? (If yes, how does that work out?)
  </div>
  <div class="answer">
We outsource some HTML generation to a company based in Ukraine. It's not ideal, anyone who knows Agile knows how important face-to-face communication is, but we have learnt to work well together, minimizing any potential bottlenecks.

For example, we store the HTML in a separate git repository which means we can use GitHub PRs and Issues to review code and track requests.

We also use an on-site contractor for some DevOps-y work (see below). The challenges there are getting the standard of polish that we would expect internally. It's understandable and natural that we have to work hard to coordinate expectations.
  </div>
</div>


<div class="qa">
  <div class="question">
    What are the most common tools that engineers use?
  </div>
  <div class="answer">
    <ul>
      <li>A standard Microsoft environment e.g. Visual Studio / Visual Studio Code / SSMS.</li>
      <li>Git (from Bash where possible).</li>
      <li>Meld for resolving git conflicts.</li>
      <li>Postman for JSON fun.</li>
      <li>Chrome Developer Tools, an underrated tool under constant development. The Performance and Audit tabs are particularly impressive and under-utilized.</li>
      <li>I'm working hard to install some Linux / bash-fu in the team!</li>
    </ul>

  </div>
</div>

<div class="qa">
  <div class="question">
    Which languages do engineers code in?
  </div>
  <div class="answer">
    Angular / TypeScript for the web frontend, C# for the backend API.
  </div>
</div>

<div class="qa">
  <div class="question">
    Which operating systems do you use?
  </div>
  <div class="answer">
    Due to our .NET Framework legacy, we use Windows. My laptop is currently the only one in the company running Linux. Once we migrate to .NET Core, which seems the sane choice rather than rewriting the backend in Python / Ruby / Node, that will open the door to migrate our servers to Linux.
  </div>
</div>

<div class="qa">
  <div class="question">
    Which databases do you use?
  </div>
  <div class="answer">
    Microsoft SQL Server, more legacy. Long-term, we'd like to move to Postgres.
  </div>
</div>

<div class="qa">
  <div class="question">
    What are the development environments? (OS, editor, Vagrant? Docker?)
  </div>
  <div class="answer">
    See above.
  </div>
</div>

<div class="qa">
  <div class="question">
    What is the system architecture? (Monolith, Microservices, Mix, etc…?)
  </div>
  <div class="answer">
    The backend API is currently built and deployed as one unit. It's important not to over-engineer and pre-optimize. As and when there is a defining business need, we would consider refactoring into microservices. We also don't use containers, and that's totally cool.
  </div>
</div>

<div class="qa">
  <div class="question">
    What kind of cloud infrastructure do you use?
  </div>
  <div class="answer">
    We've been through the three big players, and are about to settle on AWS with the release of our Next-Generation Product.
  </div>
</div>

<div class="qa">
  <div class="question">
    What Agile practices do you employ? (Daily stand-up, Sprints, Retrospectives, ...)
  </div>
  <div class="answer">
These are Scrum practices, and we do them all. When I arrived, we didn't do any, so that was a clear win. Team leaders estimated tasks for engineers, and the focus was on trying to build a perfect architecture rather than to deliver small working increments.

Now, developers are empowered and more connected to the product and business. We run two-week sprints, and take the Retrospective very seriously - it's a crucial part of the process for any team that wants to improve. At first, many people were shy and even afraid to express constructive criticism. But now, the contributions are plentiful, and everyone is enthusiastic to participate. It builds trust and we learn lots.

It's important to note that one can act according to Agile principles, but not “do Agile” - Agile isn't a process. We keep the Agile Manifesto and Principles at the front of our thinking, and implement what we can, where we can.

  </div>
</div>

<div class="qa">
  <div class="question">
    What does DevOps mean in your company? (Do you have a dedicated developer experience/developer tools team?)
  </div>
  <div class="answer">
When I arrived, there was nothing, deploys were manual and a massive drain on resources. Implementing a CI / CD pipeline was one of my first strategic goals. My background is across all areas of computer science, and being no stranger to DevOps, I implemented the first version of the pipeline with support from a contractor. When it goes live in the next few weeks, I don't intend to build a specialist DevOps team.

Why not, you ask? At its heart, DevOps is a culture, not a profession, and I see no reason why “Full Stack” shouldn't include the architecture. It's “just” code, right? So we'll be working as a team to learn about these tools and concepts, and bring them into our day-to-day life. We have a blank slate, and we can afford to be brave.
  </div>
</div>

<div class="qa">
  <div class="question">
    Is anyone on-call? Who? (Developers, DevOps people, ...?)
  </div>
  <div class="answer">
We don't use a formal rotation system like PagerDuty, because we rarely have downtime. If we have ever needed to work through the night, it was before my time. If and when there is an incident, we gather in Rocket.Chat (the open-source Slack clone, highly recommended!) and self-organize to deal with it, with minimum fuss.
  </div>
</div>

<div class="qa">
  <div class="question">
    What is the development process like? (The lifecycle of a piece of committed code, branching strategy)
  </div>
  <div class="answer">
It's pretty simple. We use GitHub (soon to be GitLab? ;) ) as a de facto solution. Work on a feature branch, submit a pull-request, at least one colleague reviews and merges the code to master. We have separate branches for development, QA, and production code, which are roughly aligned with our three Terraform-generated cloud environments.
  </div>
</div>

<div class="qa">
  <div class="question">
    Do you do pair-programming?
  </div>
  <div class="answer">
Almost never. I mention it a lot but we rarely seem to do it in practice. It's a fine balancing act, with business pressures on one side, and long-term professional growth on the other. But communication and support within the team are good, and we do learn from each other.
  </div>
</div>


<div class="qa">
  <div class="question">
    Do you do code reviews? How often? What is code review like?
  </div>
  <div class="answer">
When I arrived, everyone could push anything they wanted to master, and this was a big reason why the quality wasn't as expected. Now, all code is reviewed before hitting master. At first, it was a shock to the system for some of us. But the right kind of developer is not only open to having their code reviewed, they see it as a bonus, a chance to learn something. Same goes for the reviewers, who learn a lot by reading others' code.
  </div>
</div>

<div class="qa">
  <div class="question">
    How is testing done? (Manual QA? What kind of tests are run? How long does a test cycle run?)
  </div>
  <div class="answer">
We have hundreds of unit tests in the backend (xUnit) and end-to-end tests (Protractor). It's a current focus to improve our coverage, and extend the suite to include API / integration tests. We have a manual QA team who check releases, and who are learning how to code automated tests. The current cycle runs in a few minutes, and will run as part of CI / CD when it goes live.
  </div>
</div>

<div class="qa">
  <div class="question">
    How is code released / deployed? (How often? Who can do it? Do you have staging environment? Deployment circles?)
  </div>
  <div class="answer">
As I mentioned above, it's currently manual and painful. We release our legacy (production) product as and when we need to, based on bug fixes. We release our Next-Generation code daily, as an internal preview.

When our CI / CD pipeline goes live, we'll be able to release whenever we want, and we'll be able to do less and less manual QA as we introduce more automation. (A manual QA cycle on the legacy product takes 1-2 days.) Anyone who contributes code and understands the implications will be welcome to deploy to production.
  </div>
</div>

<div class="qa">
  <div class="question">
    What is an average day-in-the-life of someone on one of the engineering teams?
  </div>
  <div class="answer">
   Rock up. Help our self-organizing team deliver working software to our customers. Go home happy.
  </div>
</div>

<div class="qa">
  <div class="question">
    What makes your company a special place to be an engineer?
  </div>
  <div class="answer">
We don't just talk Agile principles, we apply them. We are realists, focused on the customer, yet we keep our standards high under the inevitable pressure of modern business life. We're ambitious but realistic. We don't expect perfection, it doesn't exist, but we are committed to continuous improvement.
  </div>
</div>

<div class="qa">
  <div class="question">
    What was a major problem you as an engineering organization have encountered in the last year and how did you solve it?
  </div>
  <div class="answer">
Development of our Next-Generation product (a ground-up rewrite) wasn't going according to plan. I'd say that implementing Agile principles has turned the project around. We understand our place and responsibility within the organization, and the rest of the company is more engaged with our activities and challenges.
  </div>
</div>

<div class="qa">
  <div class="question">
    Could you elaborate the steps you took to introduce Agile principles? What were the obstacles and how did you overcome them?
  </div>
  <div class="answer">
It's a natural progression, because Agile isn't a formula. If you assess the situation correctly, it's usually pretty clear where to go next. We internalized the basics by reading and discussing the Agile Manifesto and Principles. Israeli R&D tends to move fast, but it pays to take a balanced approach.

By learning from scratch rather than trying to take a shortcut to a fictional Agile / Scrum utopia, we understand why we act in a certain way, rather than acting like robots. It's like learning to fish rather than being given a fish.
  </div>
</div>

<div class="qa">
  <div class="question">
    Any disaster you could share with us?
  </div>
  <div class="answer">
It's hard to forget the 1992 MTV Video Music Awards. At the end of Nirvana's performance, Krist Novoselic threw his bass guitar into the air, failed to catch it, and it smacked him on the head. I've played a bit of bass, they're heavy, I didn't envy him.
  </div>
</div>

