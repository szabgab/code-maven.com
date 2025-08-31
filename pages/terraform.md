---
title: "Terraform"
timestamp: 2019-01-01T07:30:06
tags:
  - Terraform
published: true
author: szabgab
archive: true
---


This post isn't really finished, but one day it might be useful.


infrastructure as code
HashiCorp Terraform

{% include file="examples/terraform/1/main.tf" %}

```
terraform init
terraform apply
```


{% include file="examples/terraform/2/main.tf" %}

{% include file="examples/terraform/count/main.tf" %}


links

https://www.terraform.io/docs/configuration-0-11/interpolation.html#math

https://www.terraform.io/docs/configuration/resources.html




{% include file="examples/terraform/google/main.tf" %}

{% include file="examples/terraform/google/startup.sh" %}

{% include file="examples/terraform/google/dev.tfvars" %}
