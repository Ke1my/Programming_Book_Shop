import unittest

from utils import check_username


class UserTest(unittest.TestCase):
    def test_name_correct(self):
        cases = [
            "Никита",
            "Nikita",
            "Тимур",
            "Андрей",
            "Kelmy"
        ]

        for name in cases:
            self.assertTrue(check_username(name))

    def test_email_incorrect(self):
        cases = [
            "mail@mail.ru",
            "Никита1",
            "@",
            ".",
            "ЯПРОСТОПИШУДЛИННОЕСЛОВОЧТОБЫПРОВЕРИТЬСЛИШКОМДЛИННОЕИМЯ",
            "Кельмяшкин Никита",
            "abc@"
        ]

        for name in cases:
            self.assertFalse(check_username(name))