---
title: "Linking RubyGems to GitHub or other VCS"
timestamp: 2015-12-06T23:30:01
tags:
  - RubyGems
published: true
books:
  - ruby
author: szabgab
archive: true
---


Having a [Public Version Control system](/public-version-control-for-open-source-projects) for your project is 
quite important, make it easy for people to find it. RubyGems makes it very easy.


Since the release of version 2 of RubyGems we can add any field to the metadata key.

In order to include the `source_code_uri` key add the following to the `gempspec` file of your project
replacing the the URL with the one that matches your project.

```ruby
  gem.metadata = {
    "source_code_uri" => "https://github.com/username/project",
  }
```

Some people put the URL of their GitHub Repository in the `gem.homepage` fields.
That's ok, but it would be prefereble to also put it in the `source_code_uri` field.

