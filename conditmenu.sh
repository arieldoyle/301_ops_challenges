#!/bin/bash

# Script: Ops 301 Class 04 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 01SEP2022      
# Purpose: Menu system with options that do different things and does not end until the user selects exit

# Main

# Greets user, prompts them, and reads input

PS3="Hi there. Welcome to the menu at the start of your choices here in linuc. Please select one of the following menu options: "

select number in Print_Hello_World Ping_Loopback Print_IP_Information Exit 
do 
    case $number in
        Print_Hello_World) 
        echo "----------------------------"
        echo "Hello World"
        echo "----------------------------"
        ;;
        Ping_Loopback)
        echo "----------------------------"
        echo "Here is your loopback ping: "
        ping -c 5 127.0.0.1
        echo "----------------------------"
        ;;
        Print_IP_Information)
        echo "----------------------------"
        echo "Here is your computer's IP informaion: "
        echo "----------------------------"
        ifconfig
        ;;
        Exit)
        echo "----------------------------"
        echo "Goodbye! Thanks for stopping in!"
        exit

    esac
done

# End