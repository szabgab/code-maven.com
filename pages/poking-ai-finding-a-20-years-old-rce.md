---
title: Poking AI, Finding a 20 years old RCE
timestamp: 2026-11-08T19:30:01
author:
published: true
description:
tags:
---




What happens when you spend half an hour testing an AI model's safety guardrails on offensive security tasks? Sometimes, you accidentally find a critical vulnerability in the backbone of the Perl ecosystem.

In this talk, I'll share the story of how a casual 30-minute experiment testing DeepSeek's rejection rates turned into the discovery of an RCE in PAUSE (the Perl Authors Upload Server) that had been lurking in the codebase for over two decades.

We'll walk through how a quick exploration led to Perl's infamous 2-argument `open()` footgun, how an uploaded archive filename could trigger code execution, and how combining that with a local privilege escalation could have allowed an attacker to poison CPAN package mirrors worldwide. We'll also chat about the role of LLMs in vulnerability hunting today—where they excel, where they stumble, and how casual curiosity can still yield major security findings.


## Bio

[Imre Rad](https://www.linkedin.com/in/imre-rad-2358749b/) has spent over a decade in IT security across offensive operations, defensive engineering, and software development. Having coded heavily in Perl back when it was popular, they bring a strong historical lens to security research alongside extensive experience in vulnerability programs—both as an active bug bounty hunter and as a program lead for a major enterprise VRP. Today, they handle security for a fast-growing AI startup, while spending their little spare private capacity on security again.

## Length

30 min


## Other titles:

* Breaking CPAN: Inside the PAUSE RCE

<a class="button is-primary" href="https://luma.com/8h4kzkwo">register</a>
