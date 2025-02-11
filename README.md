# STELLA Project Website

This repository contains all the necessary files to build the content for the "STELLA - Infrastructures for Living Labs" project website. 


Visit the site at https://stella-project.org


The website is hosted on GitHub Pages, utilizing its build mechanism. To make updates, clone this repository, implement your changes, and push them back to the master branch in the repository.


## Clone the Website
If you would like to make changes to the website locally, you need to obtain a copy of it. Therefore, you need to clone this repository and also the Theme in the submodule.
1. Clone the repository:

          git clone <url>

3. Add the submodule:
               
         git submodule update --init --remote


## Update the Website

1. Get current status by pulling 
        
           git pull origin main

1. Perform your changes

1. Run the site locally (see below) to preview the changes and ensure everything works as expected

1. In the Repository: Add and Push changes
    + Add relevant changes to git:

            git add <files>
        
    + Push changes to the remote repository

            git push origin main


## Running the Site Locally

1. Install [Hugo](https://gohugo.io/installation/)


1. Build the site and make it available on a local server

        hugo server

1. Browse to [http://localhost:1313/stella-project.github.io/](http://localhost:1313/stella-project.github.io/)

## Blog

New blog posts should be placed in the `/contents/post/` directory. The naming scheme is: `yyyy-mm-dd-title.md`.


        
## Updating Publications

The publications are updated automatically on each rebuild. Therefore, publication metadata is fetched from [www.bibsonomy.org](www.bibsonomy.org) with the tag `stella`.

## Theme

The theme is based on [Hugo Blackburn theme](https://github.com/yoshiharuyamashita/blackburn).


Customizations to the theme should be made in `static/css/my.css`, while content additions go in the respective content markdown files.
