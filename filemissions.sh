#!/bin/bash

# Script: Ops 301 Class 03 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 31AUG2022      
# Purpose: Navigates to dir user inputs and changes all files inside it to the input setting and prints out new contents/permissions of that dir

# Main

# Prompts user for input directory path.
read -p "Welcome to file permission changing application. *WARNING: PLEASE ONLY INPUT USER-CREATED DIR/FILES. FAILURE TO DO SO WILL CAUSE SYSTEM HARM!*
Please input the directory path to the files you would like to change permissions (e.g. /home/name/directory): " input1

# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
read -p "What permissions number would you like to assign? (e.g. 777 to perform a chmod 777): " input2

# Navigates to the directory input by the user and changes all files inside it to the input setting.
cd $input1
sudo chmod -R $input2 $input1

# Prints to the screen the directory contents and the new permissions settings of everything in the directory.
echo "Congratulations! You have changed the permissions to the directory and the associated files! Here are your results. Good-bye!"
sudo ls -l

# End