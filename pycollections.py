#!/usr/bin/python3

# Script: Ops 301 Class 09 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 09SEP2022      
# Purpose: 
    # Assigns a variable a list of ten strings
    # Prints the fourth element of the list
    # Prints the sixth-tenth element of the list
    # Changes the value of the seventh element to "onion"

# Assigns a variable a list of ten strings
shoppinglist = ["strawberries", "cucumbers", "cat food", "bananas", "mango", "Hendrick's gin", "lemons", "limes", "Schweppes tonic", "kabobs"]

# Main
# Prints regular shopping list
print("Your Shopping List:")
print(shoppinglist)

# Prints the fourth element of the list
print("The 4th item on your shopping list:")
print(shoppinglist[3])

# Prints the sixth-tenth element of the list
print("The 6th through 10th item on your shopping list:")
print(shoppinglist[5:11])

# Changes the value of the seventh element to "onion"
print("The 7th item on your shopping list has changed from lemons to onions!")
shoppinglist[6]= "onions"

# Prints out new shopping list items
print("Here is your new shopping list:")
print(shoppinglist)

# End
