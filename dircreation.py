#!/usr/bin/env python3

# Script: Ops 301 Class 07 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 07SEP2022      
# Purpose: Generates all directories, sub-directories, and files for a user-provided directory path

# Import libraries
import os

# Declaration of variables

### Read user input here into a variable
path = input('Hello. Welcome to the Directory Services Application. Please input the file path you wish to list: ')

# Declaration of functions
res = []

# Main

### List to sotre file names
for (root, dirs, files) in os.walk(path):
    ### Add a print command here to print ==root==
    print(root)
    ### Add a print command here to print ==dirs==
    print(dirs)
    ### Add a print command here to print ==files==
    print(files)

# End