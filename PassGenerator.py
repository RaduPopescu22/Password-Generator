print(f"{'*' * 20} WELCOME TO THE PASSWORD GENERATOR {'*' * 20}\n \n")

import random
# Password choice conditions
weak_condition = ("tortoise", "olive", "engine", "squirrel", "monument", "hatchback", "string", "radiator", "basketball")
medium_condition = "abcdefghijklmnopqrstuvwxyz1234567890"
strong_condition = f"{medium_condition}!@#$%^&*"

# Getting the difficulty
pass_diff = input("Please choose a password difficulty (weak, medium, strong): ")
while pass_diff.lower() not in ["weak","medium","strong"]:
    pass_diff = input("Please choose a password difficulty (weak, medium, strong): ")

# Weak password
def get_weak_diff():
    return weak_condition[random.randint(1,(len(weak_condition)-1))]

# Medium password
def get_medium_diff():
    medium_pass = []
    # Getting first 5 characters as letters
    for letters in range(5):
        medium_pass.append(random.choice(medium_condition[0:25]))
    # Turning first character into uppercase
    medium_pass[0] = medium_pass[0].upper()
    # Getting the last two characters which will be numbers
    for numbers in range(2):
        medium_pass.append(random.choice(medium_condition[26:len(medium_condition)-1]))
    # Getting the end result
    medium_pass = "".join(medium_pass)
    return medium_pass

# Strong password 
def get_strong_diff():
    # Getting 12 mixed characters for the sequence (letters, numbers, symbols)
    while True:
        strong_pass = []
        numbers = []
        for element in range(12):
            strong_pass.append(random.choice(strong_condition))
        # Checking if the sequence has at least two numbers, if not, generating a whole other sequence
        for number in strong_pass:
            if number.isnumeric():
                numbers.append(number)
        if len(numbers) >= 2:
            break
    # Iterating over the generated password once every two steps in order to turn any letter character into an uppercase to increase pass strength 
    for char in range(0,len(strong_pass)-1,2):
        letter = strong_pass[char]
        # Checking if the character is a letter and turning it into uppercase
        if letter in medium_condition[0:25]:
            strong_pass[char] = strong_pass[char].upper()
    # Getting the end result
    strong_pass = "".join(strong_pass)
    return strong_pass


# Assigning the generator to it's respective difficulty
def get_pass(difficulty):
    if difficulty == "weak":
        return get_weak_diff()
    elif difficulty == "medium":
        return get_medium_diff()
    else:
        return get_strong_diff()


generated_pass = get_pass(pass_diff)

# Outputing the generated pass
print(f"Your generated password is: {generated_pass}")




