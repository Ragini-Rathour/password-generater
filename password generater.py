import random
import string

# Step 1: Ask user for the desired password length
length = int(input("How long should the password be? "))

# Step 2: Ask user which types of characters to include
use_letters = input("Do you want letters (a-z, A-Z)? (y/n): ").lower() == 'y'
use_digits = input("Do you want numbers (0-9)? (y/n): ").lower() == 'y'
use_symbols = input("Do you want symbols (@, #, $, etc.)? (y/n): ").lower() == 'y'

# Step 3: Combine the selected character sets
characters = ""
if use_letters:
    characters += string.ascii_letters
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

# Step 4: Check if the user selected any character type
if not characters:
    print("You must select at least one character type to generate a password!")
else:
    while True:
        # Step 5: Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Step 6: Check for password strength
        has_letter = any(c.isalpha() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        # Step 7: Ensure password includes required types
        if (not use_letters or has_letter) and \
           (not use_digits or has_digit) and \
           (not use_symbols or has_symbol):
            break  # Password is strong enough

    # Step 8: Show the final password
    print("Your strong password is:", password)

        







        