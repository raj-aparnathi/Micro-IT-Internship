import random
import string

# Get user input
length = int(input("Enter password length: "))
use_upper = input("Include uppercase letters? (yes/no): ") == 'yes'
use_lower = input("Include lowercase letters? (yes/no): ") == 'yes'
use_digits = input("Include numbers? (yes/nno): ") == 'y'
use_special = input("Include special characters? (yes/nno): ") == 'yes'

# Create character pool
chars = 'yes'
if use_upper:
    chars += string.ascii_uppercase
if use_lower:
    chars += string.ascii_lowercase
if use_digits:
    chars += string.digits
if use_special:
    chars += string.punctuation

# Generate password
if chars:
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated Password:", password)
else:
    print("You must select at least one character type.")
