import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

password_length = int(input("Enter the length of the password you want : "))   # Set the desired password length
print(f"Generated Password :{generate_password(password_length)}")
