import random
import string

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

def main():
    # Example usage
    print("Password Generator")
    print("-" * 20)
    
    password = generate_password()
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
