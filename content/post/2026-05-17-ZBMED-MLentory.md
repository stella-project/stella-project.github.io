---
title: "STELLA meets MLentory: Evaluating Search for Machine Learning Models"
categories: [blog]
tags: [STELLA, living labs, model registry, machine learning]
excerpt_separator: <!--more-->
date: "2026-05-17"
draft: false
---

[MLentory](https://mlentory.zbmed.de/), developed by [ZB MED](https://www.zbmed.de/) as part of [NFDI4DS](https://www.nfdi4datascience.de/), brings together machine learning model metadata from platforms such as Hugging Face, OpenML and AI4Life into a unified discovery portal. As a relatively new registry, MLentory faces a familiar challenge: without years of interaction data, it is difficult to know whether search rankings actually reflect what users find relevant. To better understand how search rankings perform in practice, MLentory has now been integrated with the STELLA evaluation framework, enabling live evaluation of lexical and semantic search approaches directly within the portal.

<!--more-->

## Why search matters

Most users do not browse an entire model registry that they search. Queries range from short entity-style lookups (“BERT”, “Llama”) to intent-driven descriptions (“models for image segmentation in microscopy” or "biomedical embedding models"). 

To keep the interface compact and easy to navigate, MLentory displays only a subset of metadata fields for each result card in the search page. Behind the scenes, however, the retrieval system considers substantially richer metadata, including descriptions, tasks, keywords and additional contextual information when determining rankings. As a result, the quality of the ranking algorithm plays a central role in helping users discover relevant models efficiently.

This is especially important in machine learning registries, where users often search conceptually rather than by exact identifiers. Two models may solve very similar tasks while sharing little vocabulary, making retrieval quality far more challenging than simple keyword matching.


Search rankings in MLentory for biomedical language model queries. 


{{<fluid_img class="post-image" src="/images/mlentory.png">}}


## Two search systems under comparison

MLentory’s **baseline** search uses Elasticsearch over harmonized metadata including model names, descriptions, tasks, keywords and authors. Depending on the query, the backend distinguishes between entity-oriented searches (for example, model name lookups such as “BERT”) and broader semantic-style searches across descriptive metadata.

Alongside this baseline system, an experimental vector-based semantic search approach is also being evaluated. Instead of relying only on lexical overlap, models and queries are embedded into a shared vector space so that semantically related queries and models can match even when they use different terminology.

## Evaluating search in practice

The [STELLA](https://stella-project.org/) allows different retrieval strategies to be evaluated directly within the live MLentory portal. Researchers continue using the same familiar interface, while behind the scenes STELLA interleaves results from multiple search systems and learns from user interactions such as clicks.

This allows MLentory to continuously improve retrieval quality based on real user behavior rather than offline benchmarks alone, while demonstrating how STELLA can support domain-specific discovery systems where ranking quality directly impacts usability and discoverability.
