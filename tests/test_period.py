import unittest
from datetime import date

from ..models import Period


class TestPeriod(unittest.TestCase):
    def assert_date(self, period, year, month, day):
        self.assertEqual(period.date.day, day)
        self.assertEqual(period.date.month, month)
        self.assertEqual(period.date.year, year)

    def test_period(self):
        period = Period(date(2000, 1, 1), days=2)
        self.assert_date(period, 2000, 1, 1)
        assert period.days == 2
        assert period.weeks == 0
        assert period.months == 0
        assert period.years == 0

        period = period.increment()
        self.assert_date(period, 2000, 1, 3)
        assert period.days == 2
        assert period.weeks == 0
        assert period.months == 0
        assert period.years == 0

    def test_period_days(self):
        period = Period(date(2000, 1, 27), days=2).increment()
        self.assert_date(period, 2000, 1, 29)

        period = period.increment()
        self.assert_date(period, 2000, 1, 31)

        period = period.increment()
        self.assert_date(period, 2000, 2, 2)

        period = Period(date(2000, 1, 30), days=2).increment()
        self.assert_date(period, 2000, 2, 1)

    def test_period_weeks(self):
        period = Period(date(2000, 1, 27), weeks=1).increment()
        self.assert_date(period, 2000, 2, 3)

        period = period.increment()
        self.assert_date(period, 2000, 2, 10)

        period = period.increment()
        self.assert_date(period, 2000, 2, 17)

        period = period.increment()
        self.assert_date(period, 2000, 2, 24)

        period = period.increment()
        self.assert_date(period, 2000, 3, 2)

        # leap year
        period = Period(date(2001, 2, 24), weeks=1).increment()
        self.assert_date(period, 2001, 3, 3)

    def test_period_months(self):
        period = Period(date(2000, 1, 27), months=1).increment()
        self.assert_date(period, 2000, 2, 27)

        period = Period(date(2000, 1, 29), months=1).increment()
        self.assert_date(period, 2000, 2, 29)

        period = Period(date(2001, 1, 29), months=1).increment()
        self.assert_date(period, 2001, 2, 28)

        period = Period(date(2001, 1, 1), months=1).increment()
        self.assert_date(period, 2001, 2, 1)

        period = Period(date(2001, 8, 31), months=1).increment()
        self.assert_date(period, 2001, 9, 30)
