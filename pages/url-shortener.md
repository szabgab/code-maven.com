---
title: "URL Shortener"
timestamp: 2015-11-17T15:00:01
tags:
  - exercises
  - projects
published: true
author: szabgab
archive: true
---


The value of the URL shorteners is far bigger than having a short URL.
They can provide excellent information about clicks leaving your site,
for example to affiliates, or clicks in your newsletter.

A long long time ago, many years before bitly and similar services came on the scene I've built a site
called exitlog. It was a simple url shortener, but I have not understood the business behind it and
abandoned it.

Now, as an execise, let's create a URL shortener.


See other [projects and exercises](/exercises)

Before going out and building the application itself, let's describe how should it work:

## Public URL shortener

A public URL shortener would work like this:

<ol>
  <li>A random visitor arrives to the main page. Pastes a URL, receives a short URL on our site.  e.g. http://exitlog.org/r/xY30pQ</li>
  <li>If a request for that "short" URL arrives, it is redirected to the original URL.</li>
  <li>If the same random visitor arrives again, she can list her previously shortened URLs. (This tricky. How can we know this the same person?)</li>
  <li>User can create an account and log in.</li>
  <li>All the previously remembered shortenings are now associated with her account.</li>
  <li>If logged-in user shortens the URLs those are saved associated to her account.</li>
  <li>A logged in user can see statistics on the clicks of her short URLs.</li>
</ol>

## Implementation

<ol>
  <li>
    <ul>
      <li>Show a a page with a text-box and a submit button.</li>
      <li>When submitted the URL is saved in the database, a string is generated.
          The string has 6 characters of a-zA-Z0-9, the same bitly uses.
          (this provides (26+26+10)**6 = 62**6 = 56,800,235,584 possibilities)
          Quite enough.
          In Perl [Short::URL](https://metacpan.org/pod/Short::URL) might be used.
          A random generator might also work, and checking if the value already exists,
          then either generating a new random string or increasing the one found till the first one which
          is not in use.
          </li>
      <li>Save both of them in a database: url, short-url</li>
    </ul>
  <li>Given a short-url, check the database and send the redirection.</li> 
  <li>Create a session (set a cookie). From now on, when a new url is shortened add the session-id next to the url, short-url pair in the database.</li>
  <li>Have a special request that will fetch all the url, short pairs of the currens session id and list them.</li>
  <li>Show a link to "create account" and a link to "login"</li>
  <li>Create account:
    <ul>
      <li>Fields: username, email, password (twice)</li>
      <li>Check if the username is valid and unique (in its lower case version)</li>
      <li>Check if the e-mail is unique and valied (In Perl use [Email::Valid](https://metacpan.org/pod/Email::Valid))  (At this point we don't verify the e-mail)</li>
      <li>Check if the passwords match.</li>
      <li>Save the username, email, and the hashed password in the database.</li>
      <li>Once this was submitted the user is now "logged in" display a link to "log out".</li>
      <li>Save "logged in" in the session object on the server.</li>
      <li>Save the user_id in the session object on the server.</li>
      <li>If "log out" is clicked then remove the "logged in" from the session object.</li>
    </ul>
  </li>
  <li>Login page:
    <ul>
      <li>Fields: username, password</li>
      <li>Check if username is in the database and validate if the new password matches the old one.</li>
      <li>If yes, then save the user_id in the session object, save "logged_in" in the session object and change the display to show the logout link.</li>
      <li>If not, then show 'invalid login'.</li>
    </ul>
  </li>
  <li>Retreive all the entries with the session id of this user, remove the session id, from the rows and add the user_id. (is it really good to remove the sid?)</li>
  <li>When pasting a new url, check if the user is logged in. If she is get the user_id from the session object and use that to save the new url,short-url pair.</li>
  <li>Change how URLs are shortened: Save the IP, of the shortener, and the time when it was done.</li>
  <li>Map the IP to a location (country) and save that too.</li>
  <li>When a short URL is accessed, save the time, requested IP (=> country), OS/browers etc.</li>
  <li>When the logged-in user wants to see stats:
    <ul>
      <li>For each URL, show the number of clicks.</li>
      <li>Show graph of clicks in the last hour/day/week</li>
      <li>Show the country distribution of links.</li>
    </ul>
  </li>
</ol>


## Private URL shortener

A private URL shortener is part of an already existing website with users on it.
Only designated users can create new short URLs and only special users
can see the statitics, but they can see the statistics of all the shortened URLs.
e.g. http://exitlog.org/private

Describe this later.

