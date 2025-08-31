---
title: "Using the Open Weather Map API with curl"
timestamp: 2018-10-26T12:30:01
tags:
  - curl
published: true
author: szabgab
archive: true
---


The [Open Weather Map](https://openweathermap.org/) provides data about the weather. How novel :)

The really cool part is that a large chunk of the data can be received via their [API](https://openweathermap.org/api)
free of charge. Let's see a simple example using their API from a Perl script.


## Get API keys

Though you don't have to pay for the service you need to get an <b>API key</b> to identify your requests. In order to get
an API key you need to register on the [Open Weather Map](https://home.openweathermap.org/) web site and then
you need to visit the [API keys](https://home.openweathermap.org/api_keys) section  of the site. There you can generate
API keys.


Once you have the key you can start reading the documentation of the API and you can start making calls either with your browser
or using something like `curl` on the command line.

For example:

```
curl "https://api.openweathermap.org/data/2.5/weather?q=Budapest&appid=a457e758ed0d9ab3fcc40xxxe&units=metric"
```

has several parts:

<ol>
  <li>The URL itself that leads to the correct end-point of the specific query type.
  <li>`q=Budapest`, the parameter indicating the name of the city for which I am interested in the weather.</li>
  <li>`appid=...` which is the API key generated manually on the web site. In order to use this you'll need to replace the one above with an API key of your own.</li>
  <li>`units=metric` tells the API that instead of the default Kelvin you'd like to get the temperatures in Celsius.</li>
</ol>

The above request returned the following JSON:

```
{
  "coord": {
    "lon": 19.04,
    "lat": 47.5
  },
  "weather": [
    {
      "id": 701,
      "main": "Mist",
      "description": "mist",
      "icon": "50d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 3,
    "pressure": 1016,
    "humidity": 74,
    "temp_min": 3,
    "temp_max": 3
  },
  "visibility": 5000,
  "wind": {
    "speed": 1.5
  },
  "clouds": {
    "all": 75
  },
  "dt": 1518174000,
  "sys": {
    "type": 1,
    "id": 5724,
    "message": 0.0038,
    "country": "HU",
    "sunrise": 1518155907,
    "sunset": 1518191898
  },
  "id": 3054643,
  "name": "Budapest",
  "cod": 200
}
```

I used [jq](https://stedolan.github.io/jq/) to beautify the JSON structure.

You can go on further experiment with the other API end-point, or you can start building
and application using these requests in [Perl](https://perlmaven.com/pro/openweathermap-api-using-perl) or in [Python](/openweathermap-api-using-python).


