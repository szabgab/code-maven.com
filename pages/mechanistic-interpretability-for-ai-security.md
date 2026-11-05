---
title: Mechanistic interpretability for AI Security
timestamp: 2026-10-26T14:30:01
author: szabgab
published: false
description:
tags:
---

## Description

Large language models are usually tested from the outside, prompt by prompt, and judged by what they say. Mechanistic interpretability takes the opposite stance: it treats a model as an engineered object whose internal computation can be read, decomposed and causally edited. Linear probes recover concepts from activations, steering vectors add or subtract a direction, activation patching swaps one component’s output for another’s, and sparse decompositions split a layer into named features. The central finding of recent years is that behaviours such as refusal, deception and task intent occupy low-dimensional, approximately linear subspaces that are stable across prompts.
For security this cuts both ways. A guardrail that lives in a thin slice of activation space can be measured, and a guardrail that can be measured can be removed, rotated, poisoned or watched. The same instruments therefore equip a white-box red team and a white-box blue team. Offensively, they quantify the work factor of a model’s intrinsic safeguards: how much weight noise, how small an activation push, how shallow an ablation suffices before the model complies with what it would otherwise refuse. Defensively, the same signals become runtime detectors over hidden states and model-diffing tools that reveal what a fine-tune or supply-chain modification changed inside the weights.


## Bio

[Natan Katz](https://www.linkedin.com/in/natan-katz-2936425/) is Co-founder and Chief Scientist of LuminAI Security, an Israeli startup building runtime security for open-weight language models. LuminAI’s approach is grounded in mechanistic interpretability: instead of filtering prompts and outputs, it monitors the model’s internal beahvor as it runs and detects malicious activities and cyber threats from inside the model.

Before LuminAI, Natan led AI technology at Avanan/Check Point, developing ML systems for detecting malicious code, HTML phishing, and network threats. In Web3 security, he has researched ML-based detection of malicious Ethereum transactions and smart-contract vulnerabilities, including LLM-based analysis with CodeLlama and gas-driven detection methods. Earlier, as Principal AI Researcher at NICE, he built AI for fraud-ring detection and voice biometrics. He holds more than 15 patents in applied AI, including graph-neural-network systems for fraud and malicious-code detection, and has represented Israel on an international standardization committee for quantum computing.

Natan trained as a mathematician (Hebrew University, MSc Weizmann Institute) and was a guest scientist in non-linear dynamics at Weizmann and Goethe University Frankfurt.


<a class="button is-primary" href="">register</a>
