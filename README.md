# Calculate Future Cash Flow
This project is a tiny command-line script that generates a text table representing future bank transactions to
help folks reason about their future cash flow.

## Configuration
Copy `config.py.sample` to `config.py` and edit it to reflect your bank account balance and your recurring income and bills.

### Examples
#### Bank Account Balance
Bank account balance of $10,000 on May 2nd, 2020.
```
balance = Balance(date(2020, 5, 2), 10000)
```
#### Income
Paycheck every month, starting May 1st, 2020.
```
Income('Paycheck', 2000, Period(date(2020, 5, 1), months=1)),
```
Paycheck every 2 weeks
```
Income('Paycheck', 2000, Period(date(2020, 5, 1), weeks=2)),
```

#### Bills
Rent is $2000 due on the first of every month
```
Bill('Rent', -2000, Period(date(2020, 1, 1), months=1)),
```

Yearly travel around Christmas gets reserved in October
```
Bill('Christmas Trip', -2000, Period(date(2020, 10, 1), years=1)),
```
