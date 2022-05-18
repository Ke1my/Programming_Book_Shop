import unittest

from utils import check_password_weakness

class PasswordTest(unittest.TestCase):
    def test_pass_valid(self):
        cases = [
            "StrongPa44word",
            "AnotherSt0ongPa$$word",
            "paSSw0rd",
            "s1mplePassword",
        ]

        for password in cases:
            self.assertTrue(check_password_weakness(password))
    
    def test_pass_invalid(self):
        cases = [
            "password",
            "pa44",
            "NotEnoughStrong",
            "alm0st_strong",
        ]

        for password in cases:
            self.assertFalse(check_password_weakness(password))
