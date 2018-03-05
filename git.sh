#!/usr/bin/env bash



git clone https://github.com/$USERNAME/$REPO_NAME

git status  # Do this EARLY and OFTEN. Red = bad, fix it!
git add foo.txt  # Add the file foo.txt to the staging area (green).
git add bar/  # Add the folder bar/ (and all its contents).
git commit -m 'Add foo and bar.'  # Commit all staged items.


git remote -v



