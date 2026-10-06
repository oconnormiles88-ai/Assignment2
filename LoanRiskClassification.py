# Problem 3: Loan Risk Classification
# Classifies a loan applicant as Low, Medium, or High risk based on
# credit score and annual income.


def main():
    # Get user inputs. Credit scores are whole numbers, income can have cents
    credit_score = int(input("Credit score: "))
    annual_income = float(input("Annual income: $"))

    # Validate inputs first (credit scores range from 300 to 850)
    if credit_score < 300 or credit_score > 850:
        print("Invalid credit score. Please enter a number from 300 to 850.")
    elif annual_income < 0:
        print("Invalid income.")
    else:
        # Check the strictest category first. Both conditions must be true
        # ("and"), so a high score alone isn't enough without the income
        if credit_score >= 720 and annual_income >= 60_000:
            risk_category = "Low Risk"
        elif credit_score >= 650 and annual_income >= 40_000:
            risk_category = "Medium Risk"
        # Anyone who fails both checks above falls here
        else:
            risk_category = "High Risk"

        print(f"Loan Risk Category: {risk_category}")


main()