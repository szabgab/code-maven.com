This is the source code of the Code-Maven site: http://code-maven.com
===========

Copyright and License
========================

Copyright by Gabor Szabo http://szabgab.com, 2015, 2016. All Rights Reserved.


TRANSCRIPTIONS of the podcasts
==============================
The CMOS podcasts (listed here http://code-maven.com/cmos ) have a transcription.

The format of the transcription looks like this:

```
<transcript>
  <szabgab host1 Gabor Szabo>
  <foobar guest1 Foo Bar>

  <entry 0:00 szabgab>
    Hello!
  </entry>

  <entry 0:25 foobar>
  </entry>

  ....

</transcript>
```

Everything is within the `<transcription></transcription>` tags.
At the beginnig we declare the participants:

  `<szabgab host1 Gabor Szabo>`  declares 'szabgab' nickname is used for the host whose real name is
   'Gabor Szabo'
  `<foobar guest1 Foo Bar>` declares 'foobar' nickanme is used for the guest, whose real name is 'Foo Bar'

Then every time the speaker switches we have an `<entry></entry>` and within that entry
we have the text the person said. When another person starts to speak we create a new
`<entry></entry>` section.

In the opening of each `<entry>` we write the timestamp of when it starts in the podcast
and then the nickname of the person who speaks.


