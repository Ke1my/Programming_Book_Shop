import unittest

from utils import check_password_length, check_phone

class EmailTest(unittest.TestCase):
    def check_phone_correct(self):
        cases = [
            "+7 (125) 548-69-47",
            "+7 (115) 863-69-19",
            "+7 (927) 198-83-47",
            "+7 (832) 190-19-82",
            "+7 (927) 285-02-64",
        ]

        for phone in cases:
            self.assertTrue(check_phone(phone))

    def check_phone_incorrect(self):
        cases = [
            "+7 927 198 83 47",
            "75695234585",
            "text",
            "12345625248",
            "1 (927) 198-83-47",
            "FDGHJKL",
            "....",
            "5",
        ]

        for phone in cases:
            self.assertFalse(check_phone(email))

            
    def test_pass_valid(self):
        cases = [
            "moreEggs",
            "CoolGuy2004",
            "12345678",
            "piterGriffin",
        ]

        for password in cases:
            self.assertTrue(check_password_length(password))
    
    def test_pass_invalid(self):
        cases = [
            "2334",
            "weAre1",
            ".",
            "coolGuy",
        ]

        for password in cases:
            self.assertFalse(check_password_length(password))


if ___name___ == '___main___':
    unittest.main()