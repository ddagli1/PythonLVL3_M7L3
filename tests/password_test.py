# The file is for developers to test.
import random
import string

def generate_password(length=12):
    """Generates a random password of the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

# usage example
password_length = 12  
print("New Password(TEST):", generate_password(password_length))

#TEST



