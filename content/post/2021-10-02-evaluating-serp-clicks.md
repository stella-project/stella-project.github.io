---
title:  Evaluating clicks on different SERP elements.
categories: [blog]
tags: [STELLA, living labs, docker, clicks, serp]
excerpt_separator: <!--more-->
date: "2021-10-02"
---
One shortcoming of the previous measures (wins, losses, ties) derived from interleaving experiments is the simplified interpretation of click interactions. By weighting clicks differently, it is possible to account for the meaning of the corresponding elements on the search engine result page (SERP). In this blog post, we share our results on weighting clicks on elements of SERPs differently. 

<!--more-->

We follow [Gingstad et al.’s proposal](https://arxiv.org/abs/2009.11576) of a weighted score based on click events and define the Reward as

<p align="center">
  <img src="/images/reward.png" />
</p>

where 𝑆 denotes the set of all elements on a SERP for which clicks are considered, 𝑤𝑠 denotes the corresponding weight of the SERP element 𝑠 that was clicked, and 𝑐𝑠 denotes the total number of clicks on the SERP element 𝑠. The Normalized Reward is defined as

<p align="center">
  <img src="/images/nreward.png" />
</p>

that is the sum of all weighted clicks on experimental results Reward(exp) normalized by the total Reward given by Reward(exp) + Reward(base). The figure below shows the SERP elements that were logged at LIVIVO and the corresponding weights for our evaluations. 
![docker-vs-precom](/images/click-logs.png)

The figure below shows the CTR of these elements also follows a power-law distribution. Interestingly, the number of clicks is the highest for the Details button and it is followed by the Title and Fulltext click options. In comparison, the other four logged elements receive substantially less clicks.

![docker-vs-precom](/images/click-logs-distribution.png)

The table below shows the total number of clicks on SERP elements for each systems and the Normalized Reward (nReward) resulting from the weighting scheme. We compare the total number of clicks of those (interleaving) experiments in which the experimental and baseline systems delivered results. As it can be seen, comparing systems by clicks on different SERP elements, provides a more diverse analysis. For instance, some of the systems achieve higher numbers of clicks (and CTRs) for some SERP elements in direct comparison to the baseline systems. livivo_rank_pyserini , lemuren_elastic_only got more clicks on the Bookmark element than the baseline system, while all systems achieve lower  numbers of total clicks.

![docker-vs-precom](/images/click-logs-round02.png)

None of the systems could outperform the baseline system in terms of the nReward measure, but in comparison to the Outcome scores, there is a more balanced ratio between the nReward scores that also accounts for the meaning of specific clicks. Likewise, it accounts for clicks even if the experimental system did not “win” in the interleaving experiment. In Table 10 we compare the total number of clicks over multiple sessions. While the Win, Loss, Tie, and Outcome only measure if there have been more clicks in a single experiment, the nReward also considers those clicks that were made in experiments in which the experimental system did not necessarily win.

More details can also be found in the corresponding lab overview: [http://ceur-ws.org/Vol-2936/paper-143.pdf](http://ceur-ws.org/Vol-2936/paper-143.pdf)