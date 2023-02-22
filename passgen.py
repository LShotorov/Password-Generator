import random
import string

def generate_password(min_length: int, numbers: bool = True, special_characters: bool = True) -> string:
    all_letters = string.ascii_letters
    all_digits = string.digits
    all_special_characters = string.punctuation

    characters = all_letters
    if numbers:
        characters += all_digits
    if special_characters:
        characters += all_special_characters

    password = ""
    criteria = False
    has_number = False
    has_special_character = False

    while not criteria or len(password) < min_length:
        some_character = random.choice(characters)
        password += some_character

        if some_character in all_digits:
            has_number = True
        elif some_character in all_special_characters:
            has_special_character = True

        criteria = True
        if numbers:
            criteria = has_number
        if special_characters:
            criteria = criteria and has_special_character

    return password

number_of_characters = int(input("Enter the MINIMUM length of your password? : "))
numbers = input("Do you want your password to have numbers? (y/n): ").lower()[0] == "y"
special_characters = input("Do you want your password to have special characters? (y/n): ").lower()[0] == "y"
generated_password = generate_password(number_of_characters, numbers, special_characters)

print(f"This is your password: {generated_password}\nPlease keet it safe!")