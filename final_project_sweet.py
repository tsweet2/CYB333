import re
import random
import string

#Evaluates the strength of a password and provides feedback for improvement.
def check_password_strength(password):

    strength = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        strength += 1

    # Check for digits
    if not re.search(r'\d', password):
        feedback.append("Password should contain at least one digit.")
    else:
        strength += 1

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        strength += 1

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        strength += 1

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        feedback.append("Password should contain at least one special character.")
    else:
        strength += 1

    # Evaluate strength
    if strength == 5:
        feedback.append("Password is strong.")
    elif strength >= 3:
        feedback.append("Password is moderate.")
    else:
        feedback.append("Password is weak.")

    return feedback

#Generates a strong password with a user inputted length of 8-20 characters.
def generate_strong_password(length):

    if not (8 <= length <= 20):
        raise ValueError("Password length must be between 8 and 20 characters.")

    # Ensure at least one character from each category
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Fill the rest of the password length with random characters from all categories
    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = ''.join(random.choice(all_characters) for _ in range(remaining_length))

    # Combine all characters and shuffle
    password = list(lowercase + uppercase + digit + special + remaining_chars)
    random.shuffle(password)  # Shuffle to ensure randomness
    return ''.join(password)

#Main function to allow the user to either check the strength of a password
#or generate a new strong password.
def main():

    print("Choose an option:")
    print("1. Enter a new password")
    print("2. Generate a strong password")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        password = input("Enter a password to check its strength: ")
    elif choice == '2':
        try:
            length = int(input("Enter desired password length (8-20): "))
            password = generate_strong_password(length)
            print(f"Generated password: {password}")
        except ValueError as e:
            print(e)
            return
    else:
        print("Invalid choice.")
        return

    feedback = check_password_strength(password)
    for comment in feedback:
        print(comment)

if __name__ == "__main__":
    main()
