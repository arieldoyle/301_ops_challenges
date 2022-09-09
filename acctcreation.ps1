#!/usr/bin/env powershell -acctcreation.ps1

# Script: Ops 301 Class 08 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 08SEP2022      
# Purpose: Creates a new user in Windows Server AD within PowerShell administrator rights with all attached information (ex used: Franz Fredinand)

# Main

# Creates user
New-ADUser -Name "Franz Ferdinand" -City Springfield -Company "GlobeX USA" Country USA -Department "TPS Reporting Lead" -DisplayName "Frans Fredinand" -EmailAddress fredi@Globexpower.com

# End