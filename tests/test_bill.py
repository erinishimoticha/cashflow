import unittest
from datetime import date

from models import Bill, Period


class TestBill(unittest.TestCase):
    def assert_date(self, bill, year, month, day):
        self.assertEqual(bill.period.date.day, day)
        self.assertEqual(bill.period.date.month, month)
        self.assertEqual(bill.period.date.year, year)

    def test_bill(self):
        bill = Bill(name='rent', amount=2000, period=Period(date(2020, 1, 1), months=1))
        self.assert_date(bill, 2020, 1, 1)
        bill.next()
        self.assert_date(bill, 2020, 2, 1)
        bill.next()
        self.assert_date(bill, 2020, 3, 1)
        bill.next()
        self.assert_date(bill, 2020, 4, 1)
        bill.next()
        self.assert_date(bill, 2020, 5, 1)
        bill.next()
        self.assert_date(bill, 2020, 6, 1)
        bill.next()
        self.assert_date(bill, 2020, 7, 1)
        bill.next()
        self.assert_date(bill, 2020, 8, 1)
        bill.next()
        self.assert_date(bill, 2020, 9, 1)
        bill.next()
        self.assert_date(bill, 2020, 10, 1)
        bill.next()
        self.assert_date(bill, 2020, 11, 1)
        bill.next()
        self.assert_date(bill, 2020, 12, 1)
        bill.next()
        self.assert_date(bill, 2021, 1, 1)
        bill.next()
        self.assert_date(bill, 2021, 2, 1)
        bill.next()
        self.assert_date(bill, 2021, 3, 1)
