---
title: "Jenkins triggers: Periodic polling"
timestamp: 2019-12-07T08:30:01
tags:
  - Jenkins
  - triggers
  - pollSCM
published: true
books:
  - jenkins
author: szabgab
archive: true
---


For a Continuous Integration system ideally the Version Control system should trigger the Jenkins jobs when new code was piushed out, but sometimes this is not possible.
The next best thing is to let Jenkins periodically check for anything new.

## Jenkins periodic polling

Check the Version Control System every minute if there were changes since the last time.

```
triggers {
    pollSCM '* * * * *'
}
```


