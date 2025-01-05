
import random
import string
import argparse
from colorama import Fore, Style

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generates a random password with specified criteria
    
    Args:
        length (int): Length of the password
        use_letters (bool): Include letters
        use_numbers (bool): Include numbers
        use_symbols (bool): Include special characters
    
    Returns:
        str: Generated password
    """
    # Define possible characters
    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    # Check if at least one character type is selected
    if not chars:
        return "Error: Select at least one character type"

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# New Feature: Password Strength Checker
def check_password_strength(password):
    """
    Checks the strength of a password based on length and character diversity.
    """
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Moderate"
    else:
        return "Weak" 

def main():
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("--no-letters", action="store_true", help="Exclude letters")
    parser.add_argument("--no-numbers", action="store_true", help="Exclude numbers")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of passwords to generate")
    parser.add_argument("--save", action="store_true", help="Save generated passwords to a file")
    args = parser.parse_args()

    for _ in range(args.number):
        password = generate_password(
            length=args.length,
            use_letters=not args.no_letters,
            use_numbers=not args.no_numbers,
            use_symbols=not args.no_symbols
        )
        print(Fore.GREEN + "Generated password: " + Style.RESET_ALL + password)
        print(Fore.BLUE + f"Password strength: {check_password_strength(password)}" + Style.RESET_ALL)
        print("-" * 20)

        # Save password to file if --save is used
        if args.save:
            with open("generated_passwords.txt", "a") as file:
                file.write(password + "\n")

if __name__ == "__main__":
    main()
