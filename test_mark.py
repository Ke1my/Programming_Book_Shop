import unittest

from utils import check_mark


class MarkTest(unittest.TestCase):
    def test_name_correct(self):
        cases = [
            "2",
            "5",
            "7",
            "10",
        ]

        for mark in cases:
            self.assertTrue(check_mark(mark))

    def test_email_incorrect(self):
        cases = [
            "адин",
            "два",
            "21",
            ".",
            "4.4",
            "-3",
            ""
        ]

        for mark in cases:
            self.assertFalse(check_mark(mark))