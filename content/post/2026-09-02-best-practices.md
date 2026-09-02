---
title: STELLA Best Practices released!
categories: [blog]
tags: [STELLA, living labs, documentation, evaluation]
excerpt_separator: <!--more-->
date: "2026-09-02"
---

We have published a new guide on running valid interleaved retrieval experiments with STELLA, from setup through interpretation.

<!--more-->

Interleaving compares two rankers on the same query, user and moment. It is a sensitive measure of ranking quality, but only if the experiment is designed carefully. The guide covers what tends to go wrong:

- How Team Draft Interleaving works and when to prefer it over a classic A/B test
- How to pick a baseline, a single experimental change and a testable hypothesis
- How to avoid presentation, latency and padding biases
- How to plan sample size and duration *before* launch, then avoid peeking at early results
- How to read win rate, significance and whether a statistical win is actually worth shipping

The full guide, including ready-to-use sample-size and significance calculators, is available in the documentation: [https://stella-project.org/stella-documentation/best-practices/](https://stella-project.org/stella-documentation/best-practices/)
