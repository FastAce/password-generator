import unittest
from password_generator import generate_password, check_password_strength

class TestPasswordGenerator(unittest.TestCase):
    def test_default_password_length(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_password_length(self):
        password = generate_password(length=16)
        self.assertEqual(len(password), 16)

    def test_no_character_types_selected(self):
        password = generate_password(use_letters=False, use_numbers=False, use_symbols=False)
        self.assertIsNone(password)

    def test_password_strength_weak(self):
        weak_password = "abc"
        self.assertEqual(check_password_strength(weak_password), "Weak")

    def test_password_strength_moderate(self):
        moderate_password = "abc12345"
        self.assertEqual(check_password_strength(moderate_password), "Moderate")

    def test_password_strength_strong(self):
        strong_password = "Abc123!@"
        self.assertEqual(check_password_strength(strong_password), "Strong")

if __name__ == "__main__":
    unittest.main()

