import secrets  # Used for secure password generation
import string
import argparse
from colorama import Fore, Style  # For colorful terminal output

# Password generation function
def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generates a random password with specified criteria.

    Args:
        length (int): Length of the password.
        use_letters (bool): Include letters.
        use_numbers (bool): Include numbers.
        use_symbols (bool): Include special characters.

    Returns:
        str: Generated password or error message.
    """
    if length < 4:  # Validate minimum password length
        print(Fore.RED + "Error: Password length should be at least 4 characters." + Style.RESET_ALL)
        return None

    chars = ''  # Build the character set based on user choices
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:  # Ensure at least one character type is selected
        print(Fore.RED + "Error: Select at least one character type." + Style.RESET_ALL)
        return None

    # Generate a secure password using the secrets module
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password


# Password strength checker
def check_password_strength(password):
    """
    Checks the strength of a password based on its length and character diversity.

    Args:
        password (str): The password to check.

    Returns:
        str: Strength of the password ("Weak", "Moderate", "Strong").
    """
    if not password:  # Handle cases where no password is provided
        return Fore.RED + "Error: No password provided." + Style.RESET_ALL

    length = len(password)
    has_upper = any(char.isupper() for char in password)  # Check for uppercase letters
    has_lower = any(char.islower() for char in password)  # Check for lowercase letters
    has_digit = any(char.isdigit() for char in password)  # Check for digits
    has_special = any(char in string.punctuation for char in password)  # Check for special characters

    # Calculate the strength based on criteria met
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

    # Return the strength level based on the score
    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Moderate"
    else:
        return "Weak"


# Main function with command-line argument handling
def main():
    parser = argparse.ArgumentParser(description="Password Generator")  # Command-line argument parser
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")  # Password length
    parser.add_argument("--no-letters", action="store_true", help="Exclude letters")  # Exclude letters
    parser.add_argument("--no-numbers", action="store_true", help="Exclude numbers")  # Exclude numbers
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")  # Exclude special characters
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of passwords to generate")  # Number of passwords
    parser.add_argument("--save", action="store_true", help="Save the generated passwords to a file")  # Save passwords
    args = parser.parse_args()

    passwords = []  # List to store generated passwords

    for _ in range(args.number):  # Generate the specified number of passwords
        password = generate_password(
            length=args.length,
            use_letters=not args.no_letters,
            use_numbers=not args.no_numbers,
            use_symbols=not args.no_symbols
        )
        
        if password:
            passwords.append(password)
        
            # Display the generated password and its strength
            print(Fore.GREEN + "Generated password: " + Style.RESET_ALL + password)
        
            strength = check_password_strength(password)
            if strength == "Weak":
                print(Fore.RED + f"Password strength: {strength}" + Style.RESET_ALL)
            elif strength == "Moderate":
                print(Fore.YELLOW + f"Password strength: {strength}" + Style.RESET_ALL)
            else:
                print(Fore.BLUE + f"Password strength: {strength}" + Style.RESET_ALL)
        
            print("-" * 20)  # Separator for better readability

    # Save passwords to a file if the user requests it
    if args.save:
        with open("generated_passwords.txt", "w") as f:
            f.write("\n".join(passwords))
        print(Fore.CYAN + "Passwords saved to 'generated_passwords.txt'" + Style.RESET_ALL)


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

