#!/usr/bin/env python3

# Script Name:                  Ops401d8 Day 16
# Author:                       Your Name: Nick Van Noort
# Date of latest revision:      07/31/2023
# Purpose:                      

# import library
import time
from getpass import getpass

# Declare functions

# Function that iterates over the wordlist file
def iterator():
    filepath = input("Enter the complete filepath to the wordlist: ")

    with open(filepath, 'r') as file:
        line = file.readline()

        # Loop
        while line:
            line = line.rstrip()
            word = line
            print(word)
            time.sleep(1)
            line = file.readline()

# Function that checks passwords
def check_password():
    user_password = getpass("Please enter the password you want to check: ")
    user_wordlist = input("Enter the complete filepath to the wordlist: ")

    print(f"Checking password against the words in '{user_wordlist}', just a moment. ")
    
    with open(user_wordlist, 'r') as file:
        line = file.readline()
        while line:
            word = line.rstrip()
            if user_password == word:
                print("Your password was found in the wordlist!")
                return
            line = file.readline()

    print("Your password was not found in the wordlist.")

# Main
def main():
    print("Select mode:")
    print("1: Offensive; Dictionary Iterator")
    print("2: Defensive; Password Recognized")
    mode = input("Enter mode (1 or 2): ")

    if mode == '1':
        iterator()
    elif mode == '2':
        check_password()
    else:
        print("Invalid selection. Please enter 1 or 2.")

if __name__ == "__main__":
    main()


# End