# Password Generator

A simple Python password generator that creates secure and customizable passwords.

## Features

- Generate random passwords with customizable length
- Include or exclude letters, numbers, and special characters
- Secure random generation using Python's built-in libraries
- Easy to use and integrate into other projects

## Requirements

- Python 3.x
- No additional packages required

## Installation

```bash
git clone https://github.com/FastAce/password-generator.git
cd password-generator
```

## Usage

Run the script directly:
```bash
python password_generator.py
```

Import in your own project:
```python
from password_generator import generate_password

# Generate a default password (12 characters)
password = generate_password()

# Generate a custom password
password = generate_password(
    length=16,
    use_letters=True,
    use_numbers=True,
    use_symbols=False
)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
