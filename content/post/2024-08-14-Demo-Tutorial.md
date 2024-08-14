---
title:  Demo Tutorial for the STELLA Evaluation Infrastructure.
categories: [blog]
tags: [STELLA, living labs, tutorial]
excerpt_separator: <!--more-->
date: "2022-08-14"
draft: true
---

# Demo Tutorial for the STELLA Evaluation Infrastructure
In this demo, we’ll explore the STELLA evaluation infrastructure, designed to assess various retrieval systems in a live, online environment. This tutorial provides a technical overview covering the setup, configuration, and operation of the STELLA infrastructure. You’ll learn how to interact with the system components, including the STELLA Server, STELLA App, experimental search systems, and a rudimentary search interface that simulates a search portal for testing.

<!--more-->

This tutorial can give you an idea of the project's current state or help you start setting up the infrastructure for your search portal. It follows the workflow outlined in our second community workshop, with [slides](https://docs.google.com/presentation/d/1kpPAxCjyb8PVbI5sLIJ0nyz0nv8XWUO8j3B-SsxJz_U/edit?usp=sharing) and a [video](https://www.youtube.com/watch?v=48mZSEDVJaU) recording of the demo available online. The code is hosted on [GitHub](https://github.com/stella-project), using a pre-release of the second version on demo branches. The STELLA stack is built with Docker and Python (Flask) and has been tested on Ubuntu and MacOS. A Docker installation is required for this tutorial. 

STELLA is composed of several key components:

- **STELLA Server:** Orchestrates systems and experiments, handling system registrations and collecting interaction results.
- **STELLA App:** Acts as the intermediary, performing system selection and interleaving of search results.
- **Experimental Systems:** Custom systems that should be compared within the infrastructure.
- **Search Interface:** A basic UI to mimic the functionality of a search portal for testing purposes.

These components work together, enabling researchers to evaluate different retrieval systems in a realistic environment.

Please note that STELLA is a work in progress. For the latest developments, you can follow the project’s [GitHub repositories](https://github.com/stella-project) and track ongoing issues. We welcome feature requests and feedback from the community, as it helps us improve and shape the infrastructure to better meet your needs.


## Setting Up the Infrastructure
To begin with STELLA, we need to set up the infrastructure by cloning the necessary repositories, downloading data, and starting the relevant services. Follow these steps to get everything up and running:


### Clone the Repositories
This step involves cloning the core components of STELLA from GitHub, including the STELLA App, STELLA Server, and STELLA Search. These repositories contain the necessary code to run the STELLA infrastructure.


Clone the STELLA App repository: 
```bash
git clone -b demo https://github.com/stella-project/stella-app
```

Clone the STELLA Server repository:
```bash
git clone -b demo https://github.com/stella-project/stella-server
```

Clone the STELLA Search repository:
```bash
git clone -b demo https://github.com/stella-project/stella-search
```


### Download the Data
Next we will download and prepare the GESIS search data, which serves as the dataset for the demo. This data will be copied into specific directories within the STELLA Search and STELLA App repositories.

The dataset can be downloaded from [this link](https://th-koeln.sciebo.de/s/OBm0NLEwz1RYl9N?path=%2F).

To extract the archive we can call the following command:
    
```bash
tar -xf ~/Downloads/gesis-search.tar
```
    
After that we copy the data to the appropriate directories:
```bash
cp gesis-search/documents/publication.jsonl stella-search/data/index cp -r gesis-search stella-app/data
```
        

### Start the STELLA Search Dummy UI
This step launches a basic search interface for STELLA using Docker. The dummy UI simulates a search portal and allows you to perform simple searches and interact with the results.

We can start the service with this command after navigating to the `stella-search` directory:
        
```bash
cd stella-search 
```
```bash
docker compose up -d
```
        
The STELLA Search interface will now be available at [localhost:8888](http://localhost:8888).



### Pull an Experimental System
Finally we clone the STELLA template for an experimental system. This system can be used as a startingpoint to implement your experimental systems into the STELLA infrastructure.

```bash
git clone https://github.com/stella-project/stella-micro-template
```



## 1. Experimental System Integration
This phase focuses on the integration of an experimental system that will be compared to the current baseline system. It can be a new recommendation or ranking system, or an enhancement of an existing system with varied parameters. The process involves setting up and registering the experimental system within the STELLA infrastructure. This section of the tutorial corresponds to the first two steps in the linked slides.


First we launch the STELLA Server that is used to orchistrate the experimental systems. Before we can use the experimental system we need to register it to STELLA using the server. We navigate to the `stella-server` directory and launch the service:
```bash
cd stella-server
docker compose up
```

Before we can use the STELLA Server we need to initialize the database with some dummy data to simulate a demo environment.
```bash
docker exec -it stella-server-web-1 flask seed-db
```

Now we can register the experimental system. The server is available at [localhost:8000](http://localhost:8000). We can log in with the default credentials (experimenter@stella-project.org / pass) to manage system configurations. Under the `systems` tab, we can register the experimental system by providing the system name and the GitHub repository URL. For example, we can register the ranking system `gesis_rank_pyserini` with the URL https://github.com/stella-project/gesis_rank_pyserini and the recommendation system `gesis_rec_pyterrier` with the URL https://github.com/stella-project/gesis_rec_pyterrier. These systems will now show up in the list of registered systems in the STELLA Server, can be activated and will be used for the next build of the STELLA App.

To verify that the systems are correctly registered, we can check the systems table of the STELLA Server database.




## 2. Integrating the Experimental System into STELLA
This section details the steps required to fully integrate experimental systems into the STELLA infrastructure. It covers logging into the STELLA Server as an administrator to activate systems, updating the STELLA App, launching and initializing the STELLA App, and indexing data for all systems to prepare them for searching.

### Activation and Updating
First, we will log into the STELLA Server as an administrator to activate the newly registered experimental systems, using the credentials (admin@stella-project.org / pass). On the *systems* subpage we can activate the systems we would like to include in the next experiments. Through the *administration* site, we can update the STELLA App. This generates a docker compose file that can be used to rebuild the STELLA App inclunding all updated systems. Alternatively we can manually create a docer compose file with the experimental systems. 

### Building and Initializing STELLA App
Now we can launch the STELLA App, which serves as the intermediary between the experimental systems, the production systems, and the search site. We start the service by navigating to the STELLA App directory and running `docker compose up`. 

```bash
cd stella-app
docker compose up
```

Once the service is up, initialize the app by seeding the database with demo data, which will create all necessary tables and populate them with the users and demo systems:

```bash
docker exec -it stella-app-web-1 flask seed-db
```

### Data Indexing for Systems
With the systems active and the app running, the final step is to prepare the systems for searching by indexing the downloaded data. Access the STELLA App user interface at [localhost:8080](localhost:8080) and initiate the indexing process for all systems through the UI. This step is crucial as it allows the experimental systems to perform searches based on the latest available data. After that, the experimental systems are fully integrated and ready for live testing within the STELLA infrastructure.

### Using the STELLA Search Interface
Finally, all components should be set up and ready for interaction. Now we can conduct a search query and analyze the results. This step involves using the STELLA Search interface, monitoring system interactions, verifying data logging, and investigating the feedback.

We can access the STELLA Search interface which should be available at [localhost:8888](http://localhost:8888) to perform a search. We can put in any query and inspect the result page as well as the document pages. All interactions will be logged for our analysis.

- **Observing System Responses:** As queries are inputted, we can observe how the STELLA App requests and compiles rankings from the experimental and production systems in the docker logs of the STELLA App. 

- **User Interaction with Results:** By clicking on a search result we can view the document's details page, which also includes recommendations for related documents.

- **Checking the Database:** The logs will be saved to the STELLA App database where we can verify that rankings and session data are properly recorded.


### Data Transfer to the STELLA Server
The logged interactions will be automatically transferred to the STELLA Server at regular intervals. A rudimentary dashboard displays the results and a json download is available.


## Conclusion
Through this tutorial, we have explored the steps necessary to set up, integrate, and interact with the STELLA evaluation infrastructure. From cloning the necessary repositories and initializing the system to conducting real search queries and analyzing the outcomes, we've covered a pathway to understand and engage with STELLA. 

For ongoing developments and further details, continue to follow the STELLA project on GitHub and contribute your insights and feature requests to enhance this evolving infrastructure. We would be happy to welcome you at our next community workshop, where you can connect with other users and developers to share experiences and learn more about the future of STELLA.

*Jüri Keller for the STELLA team, August 14 2024.*

