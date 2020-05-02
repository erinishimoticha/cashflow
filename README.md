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

## Execute the script
```
python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
./run.py
```

Example output
```
(venv) eishimotich-mbp:cashflow eishimoticha$ ./run.py 
starting balance: $10000
Date        Transaction      Transaction Amount    New Balance
----------  -------------  --------------------  -------------
2020-05-15  Paycheck                  $2,000.00     $12,000.00
2020-05-29  Paycheck                  $2,000.00     $14,000.00
2020-06-01  Rent                     -$2,000.00     $12,000.00
2020-06-01  Credit Card              -$1,000.00     $11,000.00
2020-06-12  Paycheck                  $2,000.00     $13,000.00
2020-06-26  Paycheck                  $2,000.00     $15,000.00
2020-07-01  Rent                     -$2,000.00     $13,000.00
2020-07-01  Credit Card              -$1,000.00     $12,000.00
2020-07-10  Paycheck                  $2,000.00     $14,000.00
2020-07-24  Paycheck                  $2,000.00     $16,000.00
```
