#!/bin/bash

# this script takes an input name for the repo this site will be stored in in GH and then builds the site file system accordingly.
# this is necessary because GH Pages expects the root dir to be one named after the repo, not "/".

read -p "Input the name of the GitHub Repo you would like to store the site tree in: " repo
read -p "What is the path to the root directory of the site generator from the pwd? " genpath

python3 $genpath/src/main.py /$repo/ $genpath
