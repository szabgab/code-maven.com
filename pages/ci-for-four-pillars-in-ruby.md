---
title: "A JavaScript bug and GitHub Workflow CI for the four-pillars Ruby gem"
timestamp: 2022-12-17T18:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


I thought I'd like to try another Ruby Gem today and went back to the [Ruby Digger](https://ruby-digger.code-maven.com/). I noticed that the gems are not listed in the order they were released. I think I already noticed this earlier, but did not deal with it. Now it really bothered me. I looked at the code and as I remembered, I have sorted the entries. So how come they are not sorted on the web site.


First I  tried it locally. I ran the code that generates the HTML page and then opened the HTML file in my browser. The order was as I expected.

So how come it works correctly on my computer but incorrectly when it is on the GitHub Pages server.

This was really annoying.

I added some debugging code to print the version number of Ruby. As much as it did not seem reasonable I was desperate. I thought maybe we have some version difference and that causes the problem. I also added some code to print the dates to the screen while the HTML file is being generated.

I pushed out the code and after a few seconds looked at the results.

The version number was similar and the dates were printed in the correctly sorted order on the screen. So how come they are not sorted on the web site.

<b>Then I saw it</b>

When I refreshed the page it showed up properly and then there was a blink and the order was gone.

That's when I realized the HTML table is configured s a sortable table. I looked at the code and it was sorted by the wrong column.

I think I copied the code for this from the [CPAN Digger](https://cpan-digger.perlmaven.com/), but we have different columns here so the code was sorting according to the names of the authors. Oh oh.

It did not happen when I looked at the HTML file on my computer as I was loading a plain file and it could not load the JavaScript that triggered the sorting.

I fixed the JavaScript code, well, update the configuration to point to the right column. This fixed the issue, but then I started to think, why do we even need to let the user sort the table? So I turned off the sorting.

Phew, that was a stupid bug.

## four-pillars in Ruby

A class which tells fortune by [Four Pillar astrology](https://en.wikipedia.org/wiki/Four_Pillars_of_Destiny).

It is a very simple Gem without any dependencies and some plain tests. It was easy to configure so I configured both a Docker container based job and a job that runs on the 3 different operating systems.

[Pull-Request](https://github.com/lumbermill/four-pillars/pull/1)

## GitHub Actions configuration file

{% include file="examples/ruby/four-pillars/ci.yml" %}

## Conclusion

Even Chinese Astrology can be tested.
