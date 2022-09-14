#!/usr/bin/python3

# Script: Ops 301 Class 12 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 14SEP2022      
# Purpose: Psutil fetches the following information:
    # Time spent by normal processes executing in user mode
    # Time spent by processes executing in kernel mode
    # Time when system was idle
    # Time spent by priority processes executing in user mode
    # Time spent waiting for I/O to complete.
    # Time spent for servicing hardware interrupts
    # Time spent for servicing software interrupts
    # Time spent by other operating systems running in a virtualized environment
    # Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

# Prerequisites:
    # Install pip in Linux machine with: sudo apt install python3-pip
    # Install psutil in Linux machine with: python3 -m pip install psutil

# Import psutil
import psutil

# Main
print(psutil.cpu_times())
print(psutil.cpu_freq())
print(psutil.net_io_counters())

# End