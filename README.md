# Password Generator

A simple Python password generator that creates secure and customizable passwords.

## Features

- Generate random passwords with customizable length
- Include or exclude letters, numbers, and special characters
- Secure random generation using Python's built-in libraries
- Save generated passwords to a file (`--save` option).
- Colorful terminal output for better readability.
- Easy to use and integrate into other projects

## Requirements

- Python 3.x
- Additional package:
  - [Colorama](https://pypi.org/project/colorama/)

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

## Example Commands 
Generate a 16-character password:
```bash
python password_generator.py --length 16
```
Generate 5 passwords without special characters (not recommended, just for the example):
```bash
python password_generator.py --length 16 --number 5 --no-symbols
```
Save generated passwords to a file:
```bash
python password_generator.py --length 16 --number 5 --save
```

## Import in your own project:
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

### Reporting Issues
If you encounter any bugs, issues, or have feature requests:
- Open an issue on [GitHub](https://github.com/FastAce/password-generator/issues) with detailed information.

### Submitting Code
If you’d like to contribute code, follow these steps:

1. **Fork the Repository**:
   - Go to the repository page on GitHub and click "Fork".

2. **Clone Your Fork**:
   - Clone your forked repository to your local machine:
     ```bash
     git clone https://github.com/<your-username>/password-generator.git
     ```

3. **Create a Branch**:
   - Create a new branch for your feature or fix:
     ```bash
     git checkout -b feature/your-feature-name
     ```

4. **Make Changes**:
   - Edit the code and commit your changes:
     ```bash
     git add .
     git commit -m "Description of the changes"
     ```

5. **Push Your Branch**:
   - Push the branch to your fork:
     ```bash
     git push origin feature/your-feature-name
     ```

6. **Submit a Pull Request**:
   - Go to the original repository on GitHub and click "New Pull Request".
   - Describe your changes and submit the PR.

### Guidelines
- Ensure your code follows PEP 8 guidelines (Python's style guide).
- Write meaningful commit messages.
- Include tests for any new functionality.

## License

This project is open source and available under the [MIT License](LICENSE).
