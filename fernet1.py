from cryptography.fernet import Fernet
import os

# This function generates a new secret key, then writes it to a file for later use
def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()  # Generate a fresh key
    with open("secret.key", "wb") as key_file:  # Open the key file in write-binary mode
        key_file.write(key)  # Write the key to the file


# This function opens the secret key file and reads the key for use in encryption/decryption
def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()  # Open the file in read-binary mode and read the key


# This function takes a message and a key, then returns the encrypted message
def encrypt_message(message: str, key: str) -> str:
    """
    Encrypts a message
    """
    encoded_message = message.encode()  # Encode the message into bytes
    f = Fernet(key)  # Instantiate the Fernet class with the key
    return f.encrypt(encoded_message)  # Encrypt the encoded message


# This function takes an encrypted message and a key, then returns the decrypted message
def decrypt_message(encrypted_message: str, key: str) -> str:
    """
    Decrypts an encrypted message
    """
    f = Fernet(key)  # Instantiate the Fernet class with the key
    return f.decrypt(encrypted_message).decode()  # Decrypt the encrypted message and decode it into string


# This function takes a file name and a key, reads the file, encrypts its data, then writes the encrypted data back to the file
def encrypt_file(file_name: str, key: str):
    """
    Encrypts a file
    """
    with open(file_name, 'rb') as file:  # Open the file in read-binary mode
        file_data = file.read()  # Read the file's data

    fernet = Fernet(key)  # Instantiate the Fernet class with the key
    encrypted_data = fernet.encrypt(file_data)  # Encrypt the file's data

    with open(file_name, 'wb') as file:  # Open the file in write-binary mode
        file.write(encrypted_data)  # Write the encrypted data back to the file


# This function takes a file name and a key, reads the file, decrypts its data, then writes the decrypted data back to the file
def decrypt_file(file_name: str, key: str):
    """
    Decrypts an encrypted file
    """
    with open(file_name, 'rb') as file:  # Open the file in read-binary mode
        encrypted_data = file.read()  # Read the encrypted data from the file

    fernet = Fernet(key)  # Instantiate the Fernet class with the key
    decrypted_data = fernet.decrypt(encrypted_data)  # Decrypt the encrypted data

    with open(file_name, 'wb') as file:  # Open the file in write-binary mode
        file.write(decrypted_data)  # Write the decrypted data back to the file


# The main function that prompts the user to select a mode, then performs the appropriate action
def main():
    generate_key()  # Generate a new key
    key = load_key()  # Load the key

    # Ask the user to select a mode
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n"))

    if mode in [1, 2]:  # If the user selected a file operation
        file_path = input("Enter the path of the file: ")  # Ask the user for the file path

        if mode == 1:  # If the user selected file encryption
            encrypt_file(file_path, key)  # Encrypt the file
            print(f"File at {file_path} has been encrypted successfully.")  # Notify the user of success
        elif mode == 2:  # If the user selected file decryption
            decrypt_file(file_path, key)  # Decrypt the file
            print(f"File at {file_path} has been decrypted successfully.")  # Notify the user of success

    elif mode in [3, 4]:  # If the user selected a message operation
        message = input("Enter your message: ")  # Ask the user for the message

        if mode == 3:  # If the user selected message encryption
            encrypted_message = encrypt_message(message, key)  # Encrypt the message
            print(f"Encrypted message is: {encrypted_message}")  # Print the encrypted message
        elif mode == 4:  # If the user selected message decryption
            decrypted_message = decrypt_message(message, key)  # Decrypt the message
            print(f"Decrypted message is: {decrypted_message}")  # Print the decrypted message


# If this script is run (instead of imported), call the main function
if __name__ == "__main__":
    main()
