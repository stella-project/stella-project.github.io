#!/usr/bin/env python3

# Kudos to Jannik Molter (@jmolter)
# Minor modification by @neumannm to reduce unnecessary line breaks between tags
# More modifications by @jueri to get rid of additional packages
import urllib.request
import os
import re

dirPath = "static/publications/"
os.makedirs(dirPath, exist_ok=True)

tag = "stella"
base = "https://www.bibsonomy.org/layout/publist-year-en/user/irgroup_thkoeln"

# get list of publications of the group with given tag
url = base + "/" + tag + "?resourcetype=publication&items=500&duplicates=merged"
page = urllib.request.urlopen(url).read()

with open(dirPath + tag + ".html", mode="wb") as localfile:
    localfile.write(page)
