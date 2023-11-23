---
title: Code
weight: 3
---
All of the project's code is available open source in the <a href="https://github.com/stella-project/">STELLA GitHub Project</a>. Below you find a short list of the most important repositories:

- The [STELLA server](https://github.com/stella-project/stella-server) is the central instance of the infrastructure. It handles the user administration, provides access to a dashboard, it automatically updates the STELLA app, and it hosts the database with user interaction logs.
- The [STELLA app](https://github.com/stella-project/stella-app) is deployed at sites that want to conduct IR and recommender experiments and evaluate them with user interactions. It is a multi-container application composed of several experimental micro-services that are built with the STELLA micro-template. It provides experimental rankings and recommendations and receives feedback data that will we posted to the STELLA server.
- The [STELLA micro-template](https://github.com/stella-project/stella-micro-template) provides interested experimenters with a template for integrating their ranking and recommendation systems into the STELLA infrastructure. Currently, the infrastructure supports two different types of submission. Experimenters can choose to submit pre-computed runs with TREC run file syntax OR use this repository in order to integrate their system as a micro-service into the STELLA App. In contrast to pre-computed results, these dockerized systems can deliver more comprehensive search result since they are not limited to pre-selected queries or items.

More details can also be found in the [technical documentation](https://stella-project.org/stella-documentation/).