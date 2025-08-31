---
title: "R&D at The Black List"
timestamp: 2019-06-13T07:30:01
tags:
  - R&D
published: true
author: szabgab
archive: true
---


<a id="rnd-logo" href="https://blcklst.com/"><img src="/img/rnd/the-black-list.png" alt="The Black List logo"></a>

<div class="rnd-author">
  <img class="rnd-author-img" src="/img/rnd/dino-simone.png" alt="Dino Simone">
  [Dino Simone](https://www.linkedin.com/in/dinosimone/) - Co-founder and CTO of The Black List.
  <p>
  [The Black List](https://blcklst.com/) is a Los Angeles based screenplay discovery and evaluation platform.
  We're a home to over 60,000 screenwriters and have hosted nearly 70,000 screenplays since our inception in 2012.
</div>


<div class="qa">
  <div class="question">
    What kind of products / services does your company develop / maintain? (web based, mobile, desktop, on-site appliance, embedded, hardware, etc.)
  </div>
  <div class="answer">
Web based.
  </div>
</div>

<div class="qa">
  <div class="question">
    Number of engineers:
  </div>
  <div class="answer">
Total team size is 8 with 2 full stack engineers. We also have hundreds of freelance professional readers who evaluate screenplays using our proprietary routing and queuing technology.
  </div>
</div>


<div class="qa">
  <div class="question">
    Are there any remote engineers? (If yes, how does that work out?)
  </div>
  <div class="answer">
All of engineering work is conducted remotely. We find remote work to be efficient and cost effective. Tools such as <a
href="https://slack.com/">Slack</a> and [Github](https://github.com/) are obviously crucial to being able to collaborate and get work done.
  </div>
</div>

<div class="qa">
  <div class="question">
Are the remote developers in the same time zone? Do you have all your communication asynchronous or do you have on-line meetings? How? How often?
  </div>
  <div class="answer">
Team is geographically dispersed between California, Massachusetts and Vermont.
Developers are on same time zone on the east coast.
We do both scheduled online meetings (once per week) and some asynchronous communication via email / Slack throughout the week.
  </div>
</div>


<div class="qa">
  <div class="question">
    What are the most common tools that engineers use?
  </div>
  <div class="answer">
Our team uses a combination of engineering and communication tools:
    <ul>
      <li>[Vim](https://www.vim.org/) for development</li>
      <li>[AWS CLI](https://aws.amazon.com/cli/)</li>
      <li>[Airbrake](https://airbrake.io/) for error monitoring</li>
      <li>[BrowserStack](https://www.browserstack.com/) for test automation</li>
      <li>[Castle.io](https://castle.io/)</li>
      <li>[Chrome developer tools](https://developers.google.com/web/tools/chrome-devtools/)</li>
      <li>[Kali Linux](https://www.kali.org/) for auditing & vulnerability testing</li>
      <li>[Jira](https://www.atlassian.com/software/jira) for project management and sprints</li>
      <li>Slack / Google Hangouts</li>
    </ul>
  </div>
</div>

<div class="qa">
  <div class="question">
    Which languages do engineers code in?
  </div>
  <div class="answer">
    <ul>
      <li>Mainly modern [Perl](https://www.perl.org/)
               ([Moose](https://perlmaven.com/moose) /
               [Mason](https://metacpan.org/pod/HTML::Mason) /
               [Catalyst](https://perlmaven.com/catalyst))</li>
      <li>[jQuery](https://jquery.com/) and [Foundation](https://foundation.zurb.com/) on the front-end</li>
    </ul>
  </div>
</div>

<div class="qa">
  <div class="question">
    Which operating systems do you use?
  </div>
  <div class="answer">
    <ul>
       <li>AWS Linux</li>
       <li>Kali Linux</li>
       <li>Mac OS</li>
    </ul>
  </div>
</div>

<div class="qa">
  <div class="question">
    Which databases do you use?
  </div>
  <div class="answer">
  <ul>
    <li>[MariaDB](https://mariadb.org/)</li>
    <li>[Memcached](https://memcached.org/)</li>
  </ul>
  </div>
</div>

<div class="qa">
  <div class="question">
    What are the development environments? (OS, editor, Vagrant? Docker?)
  </div>
  <div class="answer">
We have a developer sandbox image that is identical to what we run on production. Individual developers have their own instances running on AWS where they write most of the code in Vim.
  </div>
</div>

<div class="qa">
  <div class="question">
Isn't using AWS for development slow?
  </div>
  <div class="answer">
Not particularly. There is the added step of having to SSH to one's development machine.
Besides that, it's not all that different from developing locally.
The advantage of this for us is being able to develop in an environment we know is identical to what we run on production so there are no surprises.
  </div>
</div>


<div class="qa">
  <div class="question">
    What is the system architecture? (Monolith, Microservices, Mix, etc...?)
  </div>
  <div class="answer">
When we started off, we were definitely a monolith. These days, it's a blend. While the core application is still somewhat of a monolith, we've been migrating to microservices whenever we see it to be appropriate.
  </div>
</div>

<div class="qa">
  <div class="question">
    Do you use "the cloud"? What kind of cloud infrastructure do you use?
  </div>
  <div class="answer">
We originally started in a data center on a single rack server. We migrated to Rackspace after that. While we enjoyed the amazing support provided by Rackspace, we knew that in order to scale we needed the power of AWS. We've been on AWS for a couple of years now.
  </div>
</div>

<div class="qa">
  <div class="question">
    What Agile practices do you employ? (Daily stand-up, Sprints, Retrospectives, ...)
  </div>
  <div class="answer">
We do weekly sprints. Our stand-ups are more like Slack-ups since engineering works remotely. We've taken the best principles of Scrum and adapted for a small team size.
  </div>
</div>

<div class="qa">
  <div class="question">
Could you elaborate the steps you took to introduce Agile principles? What were the obstacles and how did you overcome them?
  </div>
  <div class="answer">
I became a certified ScrumMaster by attending one of the live courses first. This was helpful because I was able to see the challenges that other people were going through and learn from some of the mistakes. We slowly introduced a more minimalist version of it at the Black List. It was fairly easy to implement because of our small size and we continue to use it to this day.
  </div>
</div>

<div class="qa">
  <div class="question">
    What does DevOps mean in your company? (Do you have a dedicated developer experience/developer tools team?)
  </div>
  <div class="answer">
We do not because of our small engineering team size. Engineers are responsible for some of the work that would traditionally be performed by a dedicated devops person.
  </div>
</div>

<div class="qa">
  <div class="question">
    Is anyone on-call? Who? (Developers, DevOps people, ...?)
  </div>
  <div class="answer">
Developers
  </div>
</div>

<div class="qa">
  <div class="question">
    What is the development process like? (The lifecycle of a piece of committed code, branching strategy. How do developers cooperate?)
  </div>
  <div class="answer">
Whether we're fixing a bug or building a new feature, we work within a separate branch. Features are tested on sandbox by a developer working on it and also a dedicated product manager. Once we're satisfied with a new feature, we merge and push it up to production. We push new code frequently and do not follow a specific release schedule.
  </div>
</div>

<div class="qa">
  <div class="question">
If your developers can push all the time to production, what does having sprints provide you?
  </div>
  <div class="answer">
Well, I think there is a myth that in scrum code can only be released at the end of the sprint.
For us, scrum is about commitment to working on certain tasks we can complete in one week's time.
We may or may not be ready to release that product or feature at the end of the week, but at the very least we can get some feedback on its functionality from our product team.
Sprints provide us with focus on rapid incremental development and feedback.
  </div>
</div>

<div class="qa">
  <div class="question">
    Do you practice pair-programming? Mob-programming?
  </div>
  <div class="answer">
We do not at this time.
  </div>
</div>


<div class="qa">
  <div class="question">
    Do you have code reviews? How often? What is code review like?
  </div>
  <div class="answer">
We do code reviews once or twice during the development cycle. This is mainly to ensure we're following best practices and that there are no obvious security vulnerabilities. We perform a code review by logging into a developer's machine and viewing the code directly. In a way, it's a bit like pair-programming without actually sitting next to each other.
  </div>
</div>

<div class="qa">
  <div class="question">
    How is testing done? (Manual QA? What kind of tests do you run? How long does a test cycle take?)
  </div>
  <div class="answer">
We do a lot of manual testing and some automated testing as well. However, we're in the process of expanding our automated testing suite with the help of Browserstack.
  </div>
</div>

<div class="qa">
  <div class="question">
    How is code released / deployed? (How often? Who can do it? Do you have staging environment? Deployment circles?)
  </div>
  <div class="answer">
As mentioned above, our staging consists of individual developer sandboxes that run a production image. We push new features and bug fixes frequently and do not follow any specific deployment schedule.
  </div>
</div>

<div class="qa">
  <div class="question">
    What is an average day-in-the-life of someone on one of the engineering teams?
  </div>
  <div class="answer">
Our focus is on getting work done and not working set hours. I'm very much a fan of David Hansson's ideology here. In engineering at least, I encourage our small team to take ownership of certain products and services. Our end goal is to deliver great products to our user base. If that means going for a run or having some family time during the day, and working in the evening instead, that's entirely fine.
  </div>
</div>

<div class="qa">
  <div class="question">
    Any disaster you could share with us?
  </div>
  <div class="answer">
In the early days, we hosted the site on a single rack server in a Boston data center. This was all we could afford at the time. I remember one night a hard drive crashed and I raced to the data center to replace it. Luckily, it had a RAID setup so no data was lost. However, it quickly made me realize we needed to switch to something more reliable. We moved to Rackspace shortly before a major public launch, and again later to AWS. I still have the old server we originally launched on. Some day when we're further along, I'll turn it on to check out the original site.
  </div>
</div>

<div class="qa">
  <div class="question">
    What was a major problem you as an engineering organization have encountered in the last year and how did you solve it?
  </div>
  <div class="answer">
We've gone through a number of site redesigns to get to the current look and feel. A little over a year ago we, we went through a major site overhaul where were ripped apart a lot of the front-end UI and switched to the Foundation Framework. This was challenging because every page was being rebuilt from scratch essentially. However, we knew it was a necessary move for a cleaner more intuitive UI.
  </div>
</div>

<div class="qa">
  <div class="question">
    What makes your company a special place to be an engineer?
  </div>
  <div class="answer">
One is the flexibility. The other is knowing that the work you do is having such a big impact on the lives of screenwriters all over the world who otherwise would never be able to break into the industry. There are also other perks like being able to attend certain major film festivals and meet interesting people along the way.
  </div>
</div>


