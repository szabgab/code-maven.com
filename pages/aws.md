---
title: "aws - the command line tool for AWS Amazon Web Services"
timestamp: 2018-08-31T08:30:01
tags:
  - aws
  - ec2
  - describe-regions
  - describe-instances
published: true
author: szabgab
archive: true
---


[aws](https://aws.amazon.com/cli/) is a command line interface (CLI) to
the [console](https://console.aws.amazon.com/) of [AWS](https://aws.amazon.com/).



## List of regions

```
aws ec2 describe-regions
aws ec2 describe-regions --output text
aws ec2 describe-regions --query "Regions[*].RegionName" --output text
```


## List of a given tag in a single region

we use the eu-central-1 region here (which is Frankfurt) looking for the values of the "role" tag in every instance.

```
aws ec2 describe-instances --region eu-central-1 --output text

aws ec2 describe-instances --region eu-central-1 --query "Reservations[*].Instances[*].[Tags[?Key=='role'].Value]" --output text

aws ec2 describe-instances --region eu-central-1 --filters "Name=tag:Role,Values=Production" --query "Reservations[*].Instances[*].[ImageId,Tags[*]]"
```


## List of a given tag in every region

```
(for n in $(aws ec2 describe-regions --query "Regions[*].RegionName" --output text); do aws ec2
describe-instances --region $n --query "Reservations[*].Instances[*].[Tags[?Key=='role'].Value]" --output text; done) | sort | uniq
```


## Add / remove tags

```
aws ec2 create-tags --region ap-south-1 --resources i-09c456eacadkahu --tags Key=owner,Value=foobar

aws ec2 delete-tags --region ap-south-1 --resources i-09c456eacadkahdkas --tags Key=Owner

aws ec2 describe-instances --region eu-central-1 --query "Reservations[*].Instances[*].[Tags[?Key=='Name'].Value,InstanceId,State.Name]"
```

