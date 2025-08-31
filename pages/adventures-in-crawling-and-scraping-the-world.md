---
title: "Adventure in crawling and scraping the World"
timestamp: 2015-10-04T11:30:01
tags:
  - Mechanize
published: true
books:
  - perl
  - python
  - ruby
  - javascript
  - nodejs
author: szabgab
archive: true
---


While the two words `crawling` and `scraping` are usually interchangeable - at least when we are talking about the web -
they still might have sime slightly different meaning.  Crawling usually refers to the acto of going from page to page, traversing one or more sites.
Scraping on the other hand usually refers to analyzing one or a very limited set of pages.

Or maybe I am just making up this distinction. Who knows what other means by these words?


`bots`, `robots`, `web spiders` usually refer to the software that does the `crawling` or `scraping`

## Tasks

The most simple task is to download a given URL.

Then if the returned thing is an HTML page, we can 

Dowload images.

Download certain files. (Images would be of course one of the possibilites, but you might want to download all the JavaScript files,
or all the movies, or ...)


## Problems encountered

<b>Exclusion</b> There are part of web site you do not want to crawl. Either because you are not
interested, or because you would like to be a good citizen and abide by the requets of the site own
as expressed in the `robots.txt` file.
`robots.txt` is a file that describes the preferences of the site owner regarding which bot
can visit which areas of the web site.

<b>Depth</b> - how many clicks from the starting page do you want to crawl?

<b>Simultaneous pages</b> - On one hand dowloading the pages one after the other might take a lot of time.
on the other hand downloading 100 pages at the same time from the same server might get you banned from that site.
You need to find the right balance.

<b>Pause between pages</b> to further ease on the load we generate on the server we might want to pause between downloading pages
from the same server.

<b>Starting URLs</b> Some way to describe more than one starting URLs.

<b>Loops</b> Avoiding the repeated download of he same page.

<b>Terms of Service</b> some web site might have some legal document describing what you are entitled to crawl and what you can do with the
data you've downloaded. For example displaying the same content on another site as it was on the original site
is usually not one of the thing you should do.

Handling JavaScript on the web site. Crawling web sites 

Handling parameters in the URLs. http://examples.org/  http://examples.org/?id=42 Are these the same pages? When encountering the latter, should we just remove
the part after the ? mark?

Handling buttons. Should the crawler click on buttons as well, or only on links?

Handling forms. Should our crawler fill forms and click on submit buttons? What values should it fill in?

Cross links: When we would like to crawl one or more specific site we have to make sure linke that lead outside of this
cluster are not followed. OTOH we would want to allow following the links between the sites of the pre-defined list of URLs.

www and without wwww.  There are still some sites that server the same content from both www.example.com and example.com instead of
redirecting one to the other. We have to decide if we would like to treat these two as different site or if we would like to crawl only
one of them. What will we do if there is a link from one of the sites to the other one, or from some other page from the cluster
we are indexing. Will we then replace one of the URLs by the other pretend that they actually redirect?
In other wods if we decided to index example.com but then there is a link leading to http://www.example.com/abc  shall we actually try to
fetch http://example.com/abc instead?

## Tools of the trade


<h3>JavaScript / NodeJS</h3>

* [http](https://nodejs.org/api/http.html) (see how to [build a crawler in NodeJS](/building-a-crawler-in-nodejs))
* [node-crawler](https://github.com/sylvinus/node-crawler)
* [node-jsdom](https://www.npmjs.com/package/node-jsdom)
* [node-crawler-cheerio](https://github.com/virushuo/node-crawler-cheerio)
* [PhantomJS](http://phantomjs.org/)

<h3>Python</h3>

* [urllib](https://docs.python.org/2/library/urllib.html)
* [urllib2](https://docs.python.org/2/library/urllib2.html)
* [Scrapy](http://scrapy.org/)

<h3>Perl 5</h3>

* [LWP::Simple](https://metacpan.org/pod/LWP::Simple)
* [LWP::UserAgent](https://metacpan.org/pod/LWP::UserAgent)
* [WWW::Mechanize](https://metacpan.org/pod/WWW::Mechanize)
* [WWW::Spyder](https://metacpan.org/pod/WWW::Spyder)
* [WWW::Crawler::Lite](https://metacpan.org/pod/WWW::Crawler::Lite)
* [WWW::Crawler::Mojo](https://metacpan.org/pod/WWW::Crawler::Mojo)
* [Web::Query](https://metacpan.org/pod/Web::Query)
* [Mojo::UserAgent](https://metacpan.org/pod/Mojo::UserAgent) and [mojo-crawler](http://blogs.perl.org/users/stas/2013/01/web-scraping-with-modern-perl-part-1.html) and [yada-crawler](https://gist.github.com/creaktive/4607326)
* [Scrappy](https://metacpan.org/pod/Scrappy)
* [Web::Scraper](https://metacpan.org/pod/Web::Scraper)
* [Web scraping with HTML::TreeBuilder](https://perlmaven.com/pro/web-scraping-with-html-treebuilder)
* [A Simple way to download many web pages using Perl: LWP::Simple and HTTP::Tiny](https://perlmaven.com/simple-way-to-fetch-many-web-pages)
* [Fetching several web pages in parallel using AnyEvent](https://perlmaven.com/fetching-several-web-pages-in-parallel-using-anyevent)

<h3>Ruby</h3>

  <l">[mechanize](https://rubygems.org/gems/mechanize)
* [excon](https://rubygems.org/gems/excon)
* [httparty](https://rubygems.org/gems/httparty)
* [httpclient](https://www.ruby-toolbox.com/projects/httpclient)
* [curb](https://www.ruby-toolbox.com/projects/curb)
* [Typhoeus](https://www.ruby-toolbox.com/projects/typhoeus)
* [Patron](https://www.ruby-toolbox.com/projects/patron)


## The alternative: Common Crawl

[Common Crawl](http://commoncrawl.org/)

## Books

* [Web Scraping with Python](http://shop.oreilly.com/product/0636920034391.do)
* [Web Client Programming with Perl](http://www.oreilly.com/openbook/webclient/)

## Other

* [Scraping Hub](http://scrapinghub.com/) is scraping as a service.
* [DeepCrawl](https://www.deepcrawl.com/)


