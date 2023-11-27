---
title:  STELLA - A Primer on our Infrastructure
categories: [blog]
tags: [STELLA, living labs, AB-testing, dockerization, search-engine evaluation, live evaluation, docker infrastructure]
excerpt_separator: <!--more-->
date: "2020-05-08"
---
In academia, we often rely on standard test collections with static relevance judgments that somewhat abstract away the specific information need of single users. Thus, evaluating search engine algorithms with real-world users is a desiderata. Finally, we want to know how users can benefit from innovative search engines. The STELLA project tries to bridge this gap with the help of an innovative infrastructure that makes it possible to evaluate experimental search algorithms in live environments. In this post we want to outline the general idea of our infrastructure.

<!--more-->

Our early adopters - academic search engines - open their backends for researchers to deploy search algorithms, such that we expose the search results to site visitors. Therefore, the researchers prepare their systems in accordance with a defined project structure and upload them upon completion of the development process. The STELLA infrastructure will then automatically transfer the uploaded system to the sites where they can be queried. By Observation of the available feedback, it is possible to gain insights on the overall performance of the systems and adapt them to specific user needs.

{{<fluid_img class="post-image" src="/images/figure_stella.png">}}

This means, if you provide us with your system, we will handle the rest and ultimately have the system evaluated on real-world user feedback!

This blog post is the beginning of an upcoming series of posts in which we will outline STELLA and its components, features and partners.

Best regards, Your STELLA team