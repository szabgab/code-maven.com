---
title: "Flight ticket vendor for low-cost flights"
timestamp: 2016-09-16T22:30:01
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


Let's create a Web Application for flight ticket vendor as one of the [projects](/exercises).


As a model we can look at some of the features available at [WizzAir](https://wizzair.com/) or
at [Expedia](http://expedia.com/).

## Database:

<ol>
  <li>Airports: Each airport has a code, a city name, a country name, and a timezone represented as the offset from UTC.</li>
  <li>Flights. Each flight has a flight code, a source airport, and a destination airport.
   A departure time (at the timezone of the airport) a length of flight, a price in USD and a number of available seats.
   This number will be 0 in some of the cases.</li>
</ol>

When the user visits the website she needs to select a "From" airport and a "To" airport.
Once a "From" is selected the choices in the destination should be limited
to the cities to which there is a direct flight in the database.

Once the "From" and "To" are selected, the user needs to select a "Departure date" and optionally a "Return date".
When the user clicks on "Search", show the available flights on the given dates.

Provide an option to see the N days. If N=3 show the day before and the day after the selected dates.
If there is a flight but there are no more seats left, show "Sold out".


## Views

<ol>
  <li>Show many dates around the current date, but show only the prices and when the user clicks through,
      only then show the details of the flight.</li>
  <li>Show few dates but also show the details of the flight (departure time, arrival time)</li>
</ol>

## Increase complexity:

* Allow the user to select the number of passangers and show the information using that number. (For now, don't deal with different ages.)
* Each flight has several buckets of seats at different prices.
      Every time we show the cheapest available.<br>
      So for example we assume that every airplane can hold 180 passangers we might have the following buckets:
      60 seats for $80, 50 searts for $140, 40 seats for $200, 20 seats for $300, and 10 seats for $500.<br>
      If 168 seats are taken and the user asks for 3 tickets, show 2 tickets for $300 and one ticket for $500.

## Options:

<ol>
  <li>Show average ticket prices (interesting when not all the tickets are in the same bucket).</li>
  <li>Show total ticket prices for all the passangers.</li>
</ol>

<pre>
From To Date   # Adults # Children (0-17)
Round Trip / One Way / Multiple Destination
(Each flight has a From, To, Date)

Direct flights
Flights with 1  or 2 (or more?) stops.
Data from multiple Airlines
</pre>

## Sample Data

There are several organizations that provide real flight data via an API. These could be used
for getting real data.

* [QPX Express API](https://developers.google.com/qpx-express/)
* [SkyScanner](http://business.skyscanner.net/)
* [Sabre](https://developer.sabre.com/)

I've also started to put together some random data that could be loaded in a database and used:

{% include file="examples/data/airports.csv" %}

{% include file="examples/data/flights.csv" %}

