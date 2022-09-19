#!/usr/bin/python3

# Script: Ops 301 Class 13 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 15SEP2022 
# Prerequisites:
    # Must install the library requests:
        # python3 -m pip install requests 
        #  pip install inquirer    
# Purpose: 
    # Prompt the user to type a string input as the variable for your destination URL.
    # Prompt the user to select a HTTP Method of the following options: GET / POST / PUT / DELETE / HEAD / PATCH / OPTIONS
    # Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
    # Using the requests library, perform a GET request against your lab web server.
    # For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
    # For the given URL, print response header information to the screen. 

# Import Library
import requests

# Prompts user for website
website = input("Hello. Please input a website URL (ex. https://api.github.com): ")

# Asks the user for HTTP method
method = input("Select an HTTP method:\n GET \n POST \n PUT \n DELETE \n HEAD \n PATCH \n OPTIONS \n")

# if loop to decide what to do with the method input
if method == 'GET':
    action = requests.get
elif method == 'POST':
    action = requests.post
elif method == 'PUT':
    action = requests.put
elif method == 'DELETE':
    action = requests.delete
elif method == 'HEAD':
    action = requests.head
elif method == 'PATCH':
    action = requests.patch
elif method == 'OPTIONS':
    action = requests.options
else:
    print("Invalid input detected. Goodbye.")
    quit()

# Puts action and website together based on next input
response = action(website)

# Runs command based on response if y is input, else it ends
def run_command():
    sendit = input("Please confirm you want to run the command: (y for yes): ")
    
    if sendit == 'y':
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print('The request was successful!')
        elif response.status_code == 307:
            print('The request was re-directed')
        elif response.status_code == 400:
            print('The request was bad')
        elif response.status_code == 403:
            print('The request was unauthorized')
        elif response.status_code == 404:
            print('The request could not be found by the server')
        elif response.status_code == 405:
            print('The request is not allowed')
    else:
            print("Re-run code if you want to do it again.")
            return None

    print('Header information: \n')
    print(response.headers)

# Main
run_command()
# End