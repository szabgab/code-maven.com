---
title: "Exercise: Compare the Wikipedia translations"
timestamp: 2015-11-16T12:30:01
tags:
  - exercises
  - projects
published: true
books:
  - ruby
  - python
  - javascript
  - php
author: szabgab
archive: true
---


Given an article on the [English Wikipedia](https://en.wikipedia.org/), for example
about [Perl](https://en.wikipedia.org/wiki/Perl),
[Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29),
[Ruby](https://en.wikipedia.org/wiki/Ruby_%28programming_language%29),
[PHP](https://en.wikipedia.org/wiki/PHP), or [JavaScript](https://en.wikipedia.org/wiki/JavaScript),
create a program that will fetch the size of all the translated versions of this article
from every language on Wikipedia.



Depending on the level of investigation you'd like to do you can start implementing right away or you could read one or more
of the <b>hint</b> that explain what you need to fetch.

## Hints

Wikipedia provides an [API to fetch the content of the page](https://www.mediawiki.org/wiki/API:Main_page) in
raw format. It also provide a lot more details about its [API](https://www.mediawiki.org/wiki/Wikibase/API),
including information about [API::Properties](https://www.mediawiki.org/wiki/API:Properties).

The language links are served by [Wikidata](https://www.wikidata.org/).

## Hints

This URL will return the content of the 'Perl' page of the English version of the Wikipedia in JSON format:

```
https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles=Perl
```

This URL will return the list of translated versions of the page with Q-id Q42:

```
https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=sitelinks&ids=Q42
```

Given a title (in this case PHP), the following URL will return the Q-id of the page:

```
https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&format=json&titles=PHP'
```

## Hints

There seem to be 4 types of language links returned from [Wikidata](https://www.wikidata.org/):

Plain Wikipedia links that end in the word 'wiki' such as `itwiki`, `newwiki`, or `pdcwiki`. They
can be 2 or more characters. The real URL is the same without the last 4 characters.

Wikipedia links with underscores such as `zh_yuewiki`, `bat_smgwiki`, or `zh_min_nanwiki`
are quite similar, but we need to replace the underscore `_` characters by dash `-` characters.

[Wikiquote](https://en.wikiquote.org/) links. For exampe `enwikiquote` which map to https://en.wikiquote.org/.

[Wikibook](https://fr.wikibooks.org/) links, such as `frwikibook` which map to https://fr.wikibooks.org/.


## Tools

## Solutions

[wikipedia stats in GitHub](https://github.com/szabgab/wikipedia-stats)


