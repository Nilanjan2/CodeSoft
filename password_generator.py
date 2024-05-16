#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

def generate_password(length):
    if length < 1:
        print("Error: Password length should be at least 1")
        return None
    
    # Define the character sets for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special_characters = '@$'
    
    # Combine all character sets
    all_characters = lowercase + uppercase + special_characters
    
    # Generate the password using random.choice
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    if password:
        print(f"Generated password: {password}")

# Run the main function
if __name__ == "__main__":
    main()






















