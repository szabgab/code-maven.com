---
title: "Run only one instance of a Ruby program at the same time - self locking"
timestamp: 2015-11-23T23:00:01
tags:
  - open
  - flock
  - $PROGRAM_NAME
  - LOCK_EX
  - File::LOCK_NB
  - $$
published: true
books:
  - ruby
author: szabgab
archive: true
---


There are cases when you'd like to make sure the same script cannot be run twice at the same time.
Maybe because it generates a lot of load on the server, or because it uses some other scarce resource.

Maybe you are test-driving a drone, and there is only one drone.


This is a sample script that use `flock` on the script being executed in order to make
sure there are no two proccess running at the same time.

## Non-blocking version

`$PROGRAM_NAME` is a variable Ruby provides us and it has the filename of the current script in it.
We open that file for reading and then we use the `flock` method of the File class to try to put an
exclusive lock `LOCK_EX` on it. We are trying to put this lock on it in a non-blocking way: `LOCK_NB`.

If this is the first instance of the script the `flock` will be successful. It will return `true`
and thus or code can continue printing the current process-id (`$$`) and then going into the real process
which is represented by a call to `sleep` in our code.

If we try to run the same script again, while the first instance is still running (sleeping), then
the `flock` will not succeed. Because we made the call non-blocking it will return immediately with a `false`
value. In that case we complain an exit the script.

{% include file="examples/ruby/only_one_nb.rb" %}

That's it. You can try it by running the script in one terminal and while it is still running,
switching to another terminal and try running it there too. It will return immediately.


## Blocking version

If we omit the `LOCK_NB` from the call to `flock` then the call to `flock`
will wait for the lock to be released by the other process. Once it is done the flock in the second process will
return and that instance will run too.

In this case there is no need for the `if` statement as the `flock` will wait till it can lock.

{% include file="examples/ruby/only_one_blocking.rb" %}

