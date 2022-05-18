import unittest

from utils import check_email

class EmailTest(unittest.TestCase):
    def test_email_correct(self):
        cases = [
            "very1fake@example.com",
            "abc.def@example.com",
            "example@sub.mail.com",
        ]

        for email in cases:
            self.assertTrue(check_email(email))
    
    def test_email_incorrect(self):
        cases = [
            "@mail.ru",
            "wrong@mail.",
            "@",
            ".",
            "abc@mail..com",
            "abc/def@mail.com",
            "abc_def@example.com",
            "abc-xyz@sub.example.com",
            "abc@"
        ]

        for email in cases:
            self.assertFalse(check_email(email))
