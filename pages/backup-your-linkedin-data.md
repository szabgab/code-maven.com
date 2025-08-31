---
title: "Backup your LinkedIN data!"
timestamp: 2023-01-02T09:00:01
tags:
  - LinkedIn
published: true
author: szabgab
archive: true
show_related: true
---


It's all nice to have all my data in the cloud, but I also like to back it up. In case I get locked out or who knows what happens.

For example, I have a reminder every month to back up my data from LinkedIn. Primarily the list of my connections though now that I am writing this I'll also check how could I backup all my other data from LinkedIn.

This backup is kept in a private git repository on GitHub as well.


## Here is how I do it:

1. Visit [LinkedIn](https://www.linkedin.com/)
1. Click on "Me" (my avatar in the top right corner)
1. Click on [Settings & Privacy](https://www.linkedin.com/mypreferences/d/categories/account)
1. Click on [Data Privacy](https://www.linkedin.com/mypreferences/d/categories/privacy)
1. Click on [Get a copy of your data](https://www.linkedin.com/mypreferences/d/download-my-data)
1. I am mostly interested in <b>Connections</b> so I check that box. You might want others as well.
1. Click on <b>Request Archive</b>

It will take some time for LinkedIn to prepare the zip file, but they will send you an email with a link.

Once I receive that email I click on the link and download the zipfile which is called  something like <b>Basic_LinkedInDataExport_12-05-2022.zip</b>

## Handle the downloaded file

1. cd to the workdir of the git repository where I keep my private data
1. `unzip` the file: <b>unzip ~/Downloads/Basic_LinkedInDataExport_12-05-2022.zip</b>
1. sort the content with <b>sort Connections.csv -o Connections.csv</b>
1. Remove the "empty" rows from the beginning. (For some reason there every time there are a few 10s of rows with only commas. I remove those.
1. Move the line that starts with <b>First Name</b> to the beginning of the file. This is the header of the file that is moved away by the sort.
1. Commit the file to git and push it out.

## Automate this?

I am sure I could automate the process, but I don't think it is worth my time to do so.


