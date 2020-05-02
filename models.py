"""
Datatypes
"""
from datetime import date, timedelta
from calendar import monthrange

class Bill:
    def __init__(self, name, amount, period):
        self.name = name
        self.amount = amount
        self.period = period

    def next(self):
        self.period = self.period.increment()
        return self.period.date

    def transaction(self):
        current_transaction = Transaction(self.period.date, self)
        self.next()
        return current_transaction


class Balance:
    def __init__(self, _date, amount):
        self.date = _date
        self.amount = amount


class Period():
    def __init__(self, _date, days=0, weeks=0, months=0, years=0):
        assert _date
        self.date = _date
        self.days = days
        self.weeks = weeks
        self.months = months
        self.years = years

    @staticmethod
    def add_months(sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day, monthrange(year,month)[1])
        return date(year, month, day)

    def increment(self):
        date_incr = self.date + timedelta(days=self.days, weeks=self.weeks + self.years * 52)
        date_incr = self.add_months(date_incr, self.months)
        return Period(date_incr,
                      days=self.days,
                      weeks=self.weeks,
                      months=self.months,
                      years=self.years)


class Transaction():
    def __init__(self, _date, bill):
        self.date = _date
        self.bill = bill


Income = Bill
