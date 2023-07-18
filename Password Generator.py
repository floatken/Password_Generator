import random
import string

def generate_password(length, lowercase, uppercase, numbers, symbol):
    characters = ""
    if lowercase:
        characters += string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if symbol:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected. Please choose at least one."
    
    password = "".join(random.choice(characters) for i in range(length))
    return password

print("This is Ken's random password generator.")
while True:
    length = int(input("Length of password (Input number of characters): "))
    
    while length < 6:
        print("Length too short!")
        length = int(input("Input again: "))
                  
    lowercase = input("Include lowercase letters in password? y/n: ").lower() == "y"
    uppercase = input("Include uppercase letters in password? y/n: ").lower() == "y"
    numbers = input("Include numbers in password? y/n: ").lower() == "y"
    symbol = input("Include symbols in password? y/n: ").lower() == "y"

    password = generate_password(length, lowercase, uppercase, numbers, symbol)
    print("Password:", password)
