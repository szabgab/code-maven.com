---
title: "jq"
timestamp: 2018-11-11T11:12:13
tags:
  - jq
  - json
published: true
author: szabgab
archive: true
---


[jq](https://stedolan.github.io/jq/) is the swiss army knife for dealing with JSON files.

Alternatively, you can write your own [JSON beautifier](/json-beautifier) in one line of your facorite languge.


## Fetching a JSON file

Fetching a JSON file is the job of `curl` or similar tools. Here is an example how you might do it:

```
curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer $DO_API_TOKEN" "https://api.digitalocean.com/v2/images?type=distribution" > images.json
```

A few `jq` command that can be used for that file.

```
jq keys images.json

jq .images[].slug images.json

jq .links images.json  | jq keys

jq .images images.json  | jq keys      are all numbers
```


## A sample JSON file

{% include file="examples/data/in.json" %}

Print the whole content of the JSON file in a readable way:

```
jq . in.json
```

Print the top-level keys of the file:

```
jq keys in.json

[
  "abstract",
  "author",
  "generated_by",
  "meta-spec",
  "name",
  "no_index",
  "prereqs"
]
```

<b>The value of a key</b>

The name after the dot.

```
jq .abstract examples/data/in.json
jq .prereqs examples/data/in.json

jq .prereqs.runtime.requires examples/data/in.json
{
  "Code::Explain": "0.02",
  "App::Ack": "0",
  "Archive::Any": "0",
  "Acme::MetaSyntactic": "1.012"
}
```

Element in a list

```
jq .no_index.directory[0] examples/data/in.json
```

## Array as the top level item

If the top level is an array `jq keys data.json` will list the indexes `jq .[0].name data.json` will fetch the "name" field of the first element.

## Generating JSON

```
echo '{}' | jq --arg name 'Foo Bar' --arg email 'foo@bar.com' '.name |= $name | .address |= $email'
```

generates this:

```
{
  "name": "Foo Bar",
  "address": "foo@bar.com"
}
```

## Adding values to JSON

Given a JSON file, eg. `template.json</h2> with the following content:

```
{
    "title": "Example"
}
```

We can add fields to it:

```
jq --arg name 'Foo Bar' --arg email 'foo@bar.com' '.name |= $name | .address |= $email' template.json 
```

The result will look like this:

```
{
  "title": "Example",
  "name": "Foo Bar",
  "address": "foo@bar.com"
}
```


