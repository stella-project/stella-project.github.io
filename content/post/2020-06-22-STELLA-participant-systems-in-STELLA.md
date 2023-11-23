---
title:  Integrating Participant Systems in STELLA - An Overview
categories: [blog]
tags: [STELLA, living labs, AB-testing, dockerization, search-engine evaluation, live evaluation, docker infrastructure]
excerpt_separator: <!--more-->
date: "2020-06-22"
---
STELLA enables researchers and coders to deploy and evaluate search and recommendation algorithms in a real-world scenario. These so-called "Living Labs" provide a user-focused and thus more realistic evaluation approach.
What are the crucial steps when implementing a participant-system in STELLA?

<!--more-->
First of all, participants need to register and specify which systems they want to implement. With registration, a new GitHub repository for every system will be created automatically. This is your starting point. Now you can develop your code and push changes to your GitHub repository. When time is ready you can activate your system for use in a real-world task.

Docker is a core element of STELLA. Our STELLA application, which handles communication between participant-containers and sites, is a multi-container-application (MCA). This means every participant-system must be deployed as a docker image, which runs as a container inside our STELLA application. This gives you full freedom in choice of programming language and software tools. Your container only has to satisfy the constraints of a predefined REST-API. Moreover a containerized approach enables full reproducibility of the participants systems.
Don't worry: In any case, we will provide you with a fully working template, which will give you an easy start.

![STELLA, general workflow](/images/STELLA_participate_ani.gif)

To connect your system with STELLA, your container has to provide endpoints according to our interface. Most importantly, your system has to implement an indexing-endpoint. This endpoint is called when your system is used for the first time. It builds a search-index from the data provided by the site. For rankings and recommendations, the endpoints differ a little, but the return result is pretty similar. The ranking-endpoint expects a search-query, the recommendation endpoint a document or dataset-id. Both endpoints must return an ordered list of document-ids in JSON format. If you provide these endpoints, your results will be integrated seamlessly into the sites' pages.

How will these results become visible for the site users'? Whenever a user visits a site, a small percentage of visitors (for example, 15%) will get their results through STELLA-framework and not from the site's production-system. The STELLA-framework then picks one of the participant-containers for the time of the website-users' search-session.

Given a ranking or recommendation, sites log interactions (user-feedback) such as clicks, downloads, or dwell times. The STELLA app will temporarily store these relevance indicators and upload them later to a central server. Based on that, we calculate evaluation measures for participant-containers. The evaluation results are aggregated and can be accessed by participants by visiting a dashboard service, which enables a comparison between different retrieval and recommender systems.

Best regards, Your STELLA team