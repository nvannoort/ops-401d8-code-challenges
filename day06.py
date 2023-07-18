#!/usr/bin/python3

# Import libraries

from cryptography.fernet import Fernet

# Declare funcation

# Function that handles key generation
def write_key():

    # Generate a key and it into a file
    key = Fernet.generate_key()
    print(key)
    
    # Saving key into file
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the generated key so we can use it to encrypt and decrypt
def load_key():

    # Returns the key from the key.key file
    return open("key.key", "rb").read()

# Main

# Generate and write the new key
write_key()

# Load the generated key
key = load_key()
print("Key is " + str(key.decode('utf-8')))

# Encrypt a message

# Message to be encrypted
message = "THIS is TOP SECERT!!".encode() 

print("Plaintext massage is " + str(message.decode('utf-8'))) 

# Do the encryption - Initializes the Fernet moodule and names is f
f = Fernet(key)

# Encrypt the message
encrypted_message = f.encrypt(message)

# Print the encrypted messsage
print("The encrypted message is " + encrypted_message.decode('utf-8'))