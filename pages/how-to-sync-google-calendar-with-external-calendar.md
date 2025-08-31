---
title: "How to sync Google calendar with an external calendar?"
timestamp: 2020-07-29T10:30:01
tags:
  - Google
  - Calendar
description: "Sometimes an external calendar is changed but your Google calendar does not reflect the change. How to convince it to sync?"
published: true
author: szabgab
archive: true
show_related: true
---


TL;DR add  <b>?answer=42</b> to the end of the URL of your external calendar.

I use various services where I schedule meetings. For example I use [italki](https://www.italki.com/i/EFbbfc)
to have Spanish classes with native speakers from Spain and Latin-America. (BTW It is awesome, try it!)

The offer a link that provides an [ICS or iCal](https://en.wikipedia.org/wiki/ICalendar) with my own schedule.
The links looks like this:  https://www.italki.com/calendar/ASGSAGGFADS/ics


I can go to my Google Calendar an under "Other Calendars" I can add it "From URL".

Google will automatically sync from this external calendar and show the events on your Calendar.
You can even set the color so it will stand our from all of your other tasks. (I set it to red.)

The problem is that Google syncs the calendar on its own schedule and I have no control over the sync-ing
so often I scheduled a meeting but it took hour or maybe even days till it showed up in my Google calendar.

Recently it seemed to have totally stopped sync-ing. I think it happened after I have rescheduled one of my
Italki appointments.

As I cannot tell Google to sync I needed another way of triggering the update. But there is non.

I even tried to remove and add again the same calendar. It did not make a difference either.

It might have worked if I waited a few minutes after I removed the old calendar, but who has the patience for that.

So in the end I replace my URL with something that has a query parameter at the end. Anything could do I used this:

<b>?cache=no20200729</b>

just so it will remind me the date I set it. At another time I might need to change the value to trigger another new sync.

So the new URL looks like this:

<b>https://www.italki.com/calendar/ASGSAGGFADS/ics?cache=no20200729</b>

I got the new events immediately

