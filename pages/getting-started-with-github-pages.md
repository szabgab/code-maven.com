---
title: "Getting Started with GitHub Pages: with HTML and with Jekyll"
timestamp: 2018-04-23T12:30:01
tags:
  - GitHub
  - Markdown
  - Jekyll
published: true
author: szabgab
archive: true
---


[GitHub](https://github.com/) is the most popular cloud-based hosting service for Open Source projects using Git.
They also offer a service called [GitHub Pages](https://pages.github.com/) with which you can easily build and host a static web site on their servers. Free of charge.

The site is going to be static from the point of view of the server, but you can include any JavaScript code and build a whole client-side application on that site.

By default GitHub provides you with a subdomain in the **github.io** domain, but you can also map a domain name or a hostname you own.

It is a perfect solution for software developers who want to show their work and make themselves look more attractive to prospective employers. It is also a fun way to experiment with front-end development.


## GitHub Pages writing HTML


1. If you don't have one yet, create an account on [GitHub](https://github.com/)
1. On GitHub create a repository on GitHub called USERNAME.github.io with your USERNAME. As my username is **szabgab**, I've creted a repository called [szabgab.github.io](https://github.com/szabgab/szabgab.github.io/)
1. Create a file called index.html in the repository with some HTML content. It can be as simple as **&lt;h1&gt;Hello World&lt;/h1&gt;** You can either clone the repository to your local disk and then push it out or you can create the file using the online editor of GitHub
1. Once the index.html is in your GitHub repository the page will be shown at the URL USERNAME.github.io. For me it is  [szabgab.github.io](https://szabgab.github.io/). Note: there might be up to **10 minutes delay** between you submitting the changes till they appear on the web site. So be patient. There is no process log, but if there is a major error you'll get an e-mail notification.


Once you created one html page you can add more content to this page, you can improve the HTML and add some CSS to enhance the look of it.

You can also add more html pages.

Soon, however, you'll recognice that if you'd like to have all the pages look the same you'll need to copy and paste all the HTML around your content and that's not easy.

## GitHub Pages using Jekyll

This is where static site-generators, such as [Jekyll](https://jekyllrb.com/) can be useful. You create a single HTML template file and for each page you put the content in a separate .md file using [Markdown](https://daringfireball.net/projects/markdown/syntax) format.
Then, you run the static site-generator that will combine the content of each Markdown file with the template and generate an HTML page.

Even better, you don't have to run the site-generator yourself as GitHub will run it on your behalf.


1. Assuming you already have GitHub pages set up with HTML files as explained above.
1. Assuming you don't have an about.html yet, create a file called about.md with some Markdown in it. e.g **# About me**
1. Save that md file in the same GitHub repository. After a few minutes you will be able to visit your GitHub page adding the name of the file to the end of the request (without the .md) and you'll see the content of your page converted into HTML.
1. For example the [about.md](https://github.com/szabgab/szabgab.github.io/blob/master/about.md) in my repository is converted to [szabgab.github.io/about](https://szabgab.github.io/about). One warning though: if you already have an .html file with the same name, that will take precedence and you'll spend hours trying to understand why the content of your .md file does not show up. It happened to me. Don't fall in the same trap.
1. At this point I'd convert all the .html files to .md files in my repository though you might be wondering where are you going to put your HTML template.


## HTML templates for Jekyll

When I started to create my GitHub pages I did not have any HTML and creating a nice design was not my forte. This probably won't change any time soon so even if you read this years after I've written it this is still probbaly true.

When we start using .md files instead of .html file and let GitHub run Jekyll and convert them to HTML pages, it, I mean Jekyll, will use some very simple HTML template. You can create your own templates, but before doing that try one of the [Jekyll themes GitHub pages already support](https://pages.github.com/themes/).

In your Git repository create a file called **_config.yml** with the following content: **theme: jekyll-theme-cayman**. That will enable the Cayman theme. Once the file reaches GitHub, that is.

There are lots of other ways to improve your site. For now just get started and start writing some content.

## Linking to my sites

Oh and don't forget to include a link to my [Perl Tutorial](https://perlmaven.com/perl-tutorial) or to the [Code Maven](https://code-maven.com/) site. Those links will get me some extra points at the various search engines. In Markdown you can create a link by writing [Perl Tutorial](https://perlmaven.com/perl-tutorial).

