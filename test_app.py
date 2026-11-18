import string
import unittest
from app import generate_password


class PasswordTests(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(generate_password(24)), 24)

    def test_required_groups(self):
        password = generate_password(32)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in "!@#$%^&*()-_=+" for c in password))

    def test_letter_only(self):
        password = generate_password(8, False, False)
        self.assertTrue(all(c in string.ascii_letters for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(2)


if __name__ == "__main__":
    unittest.main()
