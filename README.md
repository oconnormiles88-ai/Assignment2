# DATA 4000 – Assignment 2: Conditional Logic for Business Decisions

Three Python programs that use `if`, `elif`, and `else` to turn business rules into program logic. No external libraries required.

## How to Run

```
python problem1_discount_eligibility.py
```

## Programs

### Problem 1 – Customer Discount Eligibility
Asks for a purchase amount and membership status (yes/no), then applies the discount rules and prints the discount and final price. Members get 15% off at $100 or more, otherwise 5%. Non-members get 10% off at $150 or more, otherwise no discount.

```
Purchase amount: $150
Are you a member? (yes/no): yes
Discount applied: 15%
Final price: $127.50
```

### Problem 2 – Employee Performance Bonus
Asks for annual salary and performance score (0–100), then prints the bonus percentage and dollar amount. Scores of 90+ earn 20%, 80–89 earn 10%, 70–79 earn 5%, and below 70 earn no bonus.

```
Annual salary: $65000
Performance score (0-100): 85
Performance Bonus: 10%
Bonus Amount: $6,500.00
```

### Problem 3 – Loan Risk Classification
Asks for credit score and annual income, then classifies the applicant. Low Risk needs a score of 720+ **and** income of $60,000+. Medium Risk needs 650+ **and** $40,000+. Everyone else is High Risk.

```
Credit score: 700
Annual income: $50000
Loan Risk Category: Medium Risk
```

## Assumptions

- Users enter valid numbers. Error handling (try/except) hasn't been covered yet, so text like "abc" will crash the program.
- Membership input is case-insensitive and ignores extra spaces ("YES", " no " both work). Anything other than yes/no prints an error.
- Negative purchase amounts, salaries, and incomes are rejected as invalid.
- Performance scores can be decimals (e.g., 79.5 falls in the 70–79 tier). Scores outside 0–100 are rejected.
- Credit scores must be whole numbers from 300 to 850.