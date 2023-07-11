#!/usr/bin/env python3

# Script Name:                  Ops401d8 Day 2
# Author:                       Your Name: Nick Van Noort
# Date of latest revision:      07/11/2023
# Purpose:                      

# import library

import time
from datetime import datetime
from ping3 import ping, verbose_ping

# Print currnet time and date
now = datetime.now()
print("Current date and time")
print (str(now))

# Transmit a single ICMP (ping)

ping = os.system("ping 8.8.8.8")
print(ping)

# The IP to ping
ip = '8.8.8.8'

while True:
    try:
        # Ping the IP
        delay = ping(ip)

        # Check the response
        if delay is not None:
            status = 'Network Active'
        else:
            status = 'Network Failure'
        
        # Print the timestamp, status, and IP
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} {status} to {ip}')

        # Sleep for two seconds
        time.sleep(2)
    

# end 