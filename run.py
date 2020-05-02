#!/usr/bin/env python3.7
"""
Given a set of recurring transactions, generate a the future balances.
"""
from datetime import date
from tabulate import tabulate
import locale

from config import balance, bills


locale.setlocale(locale.LC_ALL, '')
TO_DATE = date(2021, 12, 31)
transactions = []
rows = []
headers = ['Date', 'Transaction', 'Transaction Amount', 'New Balance']


for bill in bills:
    transaction = bill.transaction()

    while transaction.date < TO_DATE:
        if transaction.date > balance.date:
            transactions.append(transaction)

        transaction = bill.transaction()

transactions.sort(key=lambda x: x.date)

print(f'starting balance: ${balance}')
for transaction in transactions:
    balance.amount += transaction.bill.amount
    rows.append([
        str(transaction.date),
        transaction.bill.name,
        locale.currency(transaction.bill.amount, grouping=True),
        locale.currency(balance.amount, grouping=True)
    ])

print(tabulate(rows, headers=headers, colalign=('left', 'left', 'right', 'right')))
