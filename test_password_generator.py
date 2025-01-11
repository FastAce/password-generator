import unittest
from password_generator import generate_password, check_password_strength

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password_default(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_generate_password_custom_length(self):
        password = generate_password(length=16)
        self.assertEqual(len(password), 16)

    def test_generate_password_only_letters(self):
        password = generate_password(use_numbers=False, use_symbols=False)
        self.assertTrue(all(char.isalpha() for char in password))

    def test_generate_password_no_types(self):
        result = generate_password(use_letters=False, use_numbers=False, use_symbols=False)
        self.assertEqual(result, "Error: Select at least one character type.")

    def test_check_password_strength_strong(self):
        password = "Aa1!Aa1!"
        strength = check_password_strength(password)
        self.assertEqual(strength, "Strong")

    def test_check_password_strength_weak(self):
        password = "abc"
        strength = check_password_strength(password)
        self.assertEqual(strength, "Weak")

if __name__ == "__main__":
    unittest.main()

