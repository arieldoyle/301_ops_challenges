#!/usr/bin/python3

# Script: Ops 301 Class 06 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 06SEP2022      
# Purpose: Executes Linux terminal commands from within a python script

# Import OS Library
import os

# Main
# Declare Variable 1
var1 = 'whoami'
print(var1)

# Call Variable 1
os.system(var1)

# Declare Variable 2
var2 = 'ip a'
print(var2)

# Call Variable 2
os.system(var2)

# Declare Variable 3
var3 = 'lshw -short'
print(var3)

# Call Variable 3
os.system(var3)

# End
