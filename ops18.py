#!/usr/bin/env python3

# Script Name:                  Ops401d8 Day 18
# Author:                       Your Name: Nick Van Noort
# Date of latest revision:      08/2/2023
# Purpose:                      

# import library
import time
from getpass import getpass
import paramiko
from zipfile import zipfile 

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

# Function that attempts to authenticate to an SSH server using a wordlist
def ssh_auth():
    ip = input("Enter the IP address of the SSH server: ")
    username = input("Enter the username: ")
    wordlist = input("Enter the complete filepath to the wordlist: ")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(wordlist, 'r') as file:
        line = file.readline()
        while line:
            password = line.rstrip()
            try:
                ssh.connect(ip, username=username, password=password)
                print(f"Successfully authenticated with password: {password}")
                return
            except paramiko.AuthenticationException:
                pass
            line = file.readline()

    print("Failed to authenticate with any password in the wordlist.")

# Function that tries to open a zip file using a wordlist
def zip_crack():
    zip_path = input("Enter the complete filepath to the zip file: ")
    wordlist = input("Enter the complete filepath to the wordlist: ")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        with open(wordlist, 'r') as file:
            line = file.readline()
            while line:
                password = line.rstrip()
                try:
                    zip_ref.extractall(pwd=bytes(password,'utf-8'))
                    print(f"Successfully extracted zip file with password: {password}")
                    return
                except RuntimeError:
                    pass
                line = file.readline()
            
    print("Failed to extract the zip file with any password in the wordlist.")


# Main
def main():
    print("Select mode:")
    print("1: Offensive; Dictionary Iterator")
    print("2: Defensive; Password Recognized")
    print("3: SSH Authentication")
    print("4: Zip File Cracker")
    mode = input("Enter mode (1, 2, 3, or 4): ")

    if mode == '1':
        iterator()
    elif mode == '2':
        check_password()
    elif mode == '3':
        ssh_auth()
    elif mode == '4':
        zip_crack()
    else:
        print("Invalid selection. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()