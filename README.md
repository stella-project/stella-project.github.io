# STELLA Project Website

This repository contains all the necessary files to build the content for the "STELLA - Infrastructures for Living Labs" project website. 


Visit the site at https://stella-project.org


The website is hosted on GitHub Pages, utilizing its build mechanism. To make updates, clone this repository, implement your changes, and push them back to the master branch in the repository.

## Workflow to Update the Website

1. Get current status

     a. by cloning
        
                git clone <url>
                
     b. by pulling 
        
                git pull origin master

1. Perform your changes

1. Run the site locally (see below) to preview the changes and ensure everything works as expected

1. In the Repository: Add and Push changes
    + Add relevant changes to git:

            git add <files>
        
    + Push changes to the remote repository

            git push origin master

### Running the Site Locally


1. Install [Hugo](https://gohugo.io/installation/)


1. Build the site and make it available on a local server

        hugo server

1. Browse to [https://localhost:1313](http://localhost:1313)

## Blog

New blog posts should be placed in the `/contents/post/` directory. The naming scheme is: `yyyy-mm-dd-title.md`.


        
## Updating Publications

~ To be written ~

## Theme

The theme is based on [Hugo Blackburn theme](https://github.com/yoshiharuyamashita/blackburn).


Customizations to the theme should be made in `static/css/my.css`, while content additions go in the respective content markdown files.