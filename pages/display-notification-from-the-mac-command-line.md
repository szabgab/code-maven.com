---
title: "Display notification from the Mac command line"
timestamp: 2018-02-28T10:30:01
tags:
  - Apple
  - Mac
  - osascript
  - display
  - say
published: true
author: szabgab
archive: true
---


Quite often I run some job on the command line that takes a few minutes. Staring at the terminal waiting for the job to finish is not fun.
Switching to check what's on Facebook I end up wasting an hour looking at pictures of cats and dogs. If I am lucky.

I am trying something new now. I'm trying to send myself an alert whenever a task is done. For this to work first I had to find a way to
send a notification from the command line.


## The tools

[osascript](https://ss64.com/osx/osascript.html) is a tool that comes with Mac that can execute code written in AppleScript, JavaScript
and maybe a few other languages. If the previous link stops working typing `man osascript` in the Mac Terminal should give you the explanation.

[AppleScript](https://developer.apple.com/library/content/documentation/AppleScript/Conceptual/AppleScriptLangGuide/) is a scripting language created by Apple. It has a bunch of [commands](https://developer.apple.com/library/content/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html). There are a couple of interesting ones, for example: `display` and `say`.

## display

The `display` command can send a notification to the standard notification system of Mac that will show a pop-up for a few seconds and that can be listed by clicking on the hamburger icon in the top-right corner of the screen (at the right end of the menu bar).

We could write an AppleScript in a file and use osascript to run the file, but osascript can also execute one-liners where all the commands are on the command-line.
That seems to be more useful at this point.

## display hello world

The AppleScript code to send a notification with the text "hello world!" looks like this:

```
display notification "hello world!"
```

In order to run it on the command line we need to wrap that code in single-quotes and use the `-e` flag of `osascript`.

```
osascript -e 'display notification "hello world!"'
```

The result is a pop-up like this that shows up in the top right corner of the screen and disappears after about 3 seconds:

<img src="/img/notification_hello_world.png" alt="Notification" />

You can open the Notification center (the hamburger icon in the top right corner of the screen) that will look something like this: (assuming the only notification
you have is the one we just sent.)

<img src="/img/notification_hello_world_in_list.png" alt="Notification" />

You can clear the list of notifications by clicking on the `x`.

## display notification with title

The default title of the notification was "Script Editor".  We can also set it in the AppleScript command:

```
display notification "hello world!" with title "This is the title"
```

and with `osascript`:

```
osascript -e 'display notification "hello world!" with title "This is the title"'
```

The result is better:

<img src="/img/notification_hello_world_with_title.png" alt="Notification" />

## display notification with subtitle

If we have a title we can also have a subtitle:

The AppleScript command:

```
display notification "hello world!" with title "Greeting" subtitle "More text"
```

With osascript:

```
osascript -e 'display notification "hello world!" with title "Greeting" subtitle "More text"'
```

This is how the result looks like:

![](/img/notification_hello_world_with_subtitle.png)


## display notification and make sound

In addition to the visual notification, the `display` command can also include a sound effect.
The sound can be one of the files in `/System/Library/Sounds` or in `~/Library/Sounds`.

The AppleScript command:

```
display notification "hello world!" with title "Greeting" subtitle "More text" sound name "Submarine"
```

executed by `osascript`:

```
osascript -e 'display notification "hello world!" with title "Greeting" subtitle "More text" sound name "Submarine"'
```

If the name of the sound is incorrect Mac will make an alert sound.

## Longer text

If we try to send a longer text:

```
osascript -e 'display notification "hello world! This is a longer message and we would like to see how is it going to be displayed." with title "Greeting" subtitle "More text"'
```

The pop-up notification will only display the beginning:

![](/img/notification_longer_message.png)

but we can see the full text in the notification center:

![](/img/notification_longer_message_full_text.png)



## display alert with confirmation request

There is another way to create a notification using the `display alert` command. The syntax is a bit different.
The string that comes immediately after the `display alert` is the title and then one can optionally add a `message`
parameter with a longer explanation.

the AppleScript command:

```
display alert "Hello World!" message "longer text can be added in the message field and it will be all shown on the pop-up alert."
```

The `osascript` wrapped command:

```
osascript -e 'display alert "Hello World!" message "longer text can be added in the message field and it will be all shown on the pop-up alert."'
```

The result is a pop-up window in the middle of the screen that also stays there till you click on the OK button.

![](/img/alert_hello_world.png)

The alert won't be recorded in the notification center of your Mac.


## Saying Hello World

Finally there is also the `say` command that can vocalize any text you give to it.

The AppleScript command:

```
say "Hello World!"
```

wrapped in `osascript` on the command line:

```
osascript -e 'say "Hello World!"'
```

This does not have any visual effect, but it is quite surprising when your computer starts to talk to you.


## Execute after the long-running program

The whole article was written because I wanted to get some alert after a long-running program ends.
Here we substitute the long-running program with `sleep 2`. We can then include a call to
`osascript` or even two calls to `osascript` to be executed immediately after the
main command (the sleep 2) ends.

```
sleep 2; osascript -e 'say "Hello World!"'; osascript -e 'display alert "hello world"'
```

I put in two ways of notification so I'll hear some text if I am near the computer but does not watch the screen
and I'll get a pop-up that remains on the screen later. So even if I am out of the room when the process ends,
I'll see the pop-up when I return to my computer.


## Comments

This is brilliant! Just what I was looking for! :)

---

Is there a way to specify a custom icon in the slide out notification? I know other apps have their own custom icons in the notifications side bar on the right of the screen.
---

I don't think it's possible, but please share if you've learned how :)

---
This is so awesome!!
---

Great article. I placed this in an alias to run after long bash processes.

    alias notify='osascript -e "display notification \"done!\""'

---

On Big Sur there is an additional title showing the process that triggered the banner (I guess). For these examples it is always "SCRIPT EDITOR". Any way to remove or customize it?

---

Awesome !

---
I know I am a bit late to the party here but I can only use "with title" or "with icon" and nothing else after either of those. If I try
osascript -e 'display dialog "Hello world!" with title "title" subtitle "subtitle"'
I get the error message
syntax error: A identifier can’t go after this “"”. (-2740)
Basically putting anything after the initial with parameter gives an error. "with subtitle" also gives an error. So I am left using just "with title" or I can use "with icon". Anyone have any ideas why this doesn't work? I am on Big Sur.
---
Instead of using " use '
I hope it will work ^_^

---

Perfect.

---

It would be nice to add an example of sending the notification of the result of another shell command. for example
```
echo "hey"|xargs -I {} osascript -e 'display notification "{}"'
```

---

THANK YOU!


---

In my Xcode it shows failed to display notification.

caused by: script error: osascript: no such component "JavaScript".

Any solution for this?

---

Nice insights. Just a further question: is it possible to detect a notification window in order to trigger an Automator workflow?
Something like:
if window "Hello World" from application System Events exists
...
end if


