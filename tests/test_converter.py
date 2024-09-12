# tests/test_converter.py

import unittest
import datetime
from persian_datetime_converter.converter import PersianDateConverter


class TestPersianDateConverter(unittest.TestCase):

    def test_gregorian_to_persian(self):
        # Test cases with known Gregorian to Persian conversions
        test_cases = [
            (datetime.datetime(2024, 9, 13), (1403, 6, 23)),  # Known conversion example
            (datetime.datetime(2023, 3, 21), (1402, 1, 1)),  # Start of Persian year
            (datetime.datetime(2022, 3, 20), (1400, 12, 29)),  # End of Persian year
            (datetime.datetime(2000, 1, 1), (1378, 10, 11)),  # Random date in 2000
            (datetime.datetime(1995, 6, 5), (1374, 3, 15)),  # Random date in 1995
        ]

        for gregorian_date, expected_persian_date in test_cases:
            with self.subTest(gregorian_date=gregorian_date):
                persian_date = PersianDateConverter.convert(gregorian_date)
                self.assertEqual(persian_date, expected_persian_date)

    def test_is_leap_gregorian(self):
        # Test the leap year calculation for Gregorian dates
        self.assertTrue(PersianDateConverter.is_leap_gregorian(2024))
        self.assertFalse(PersianDateConverter.is_leap_gregorian(2023))
        self.assertTrue(PersianDateConverter.is_leap_gregorian(2000))
        self.assertFalse(PersianDateConverter.is_leap_gregorian(1900))


if __name__ == '__main__':
    unittest.main()
