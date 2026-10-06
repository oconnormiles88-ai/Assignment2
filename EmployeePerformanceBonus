# Problem 2: Employee Performance Bonus
# Calculates an employee's annual bonus based on their performance score.


def main():
    # Get user inputs. float() allows decimals like 65000.50 or 85.5
    annual_salary = float(input("Annual salary: $"))
    performance_score = float(input("Performance score (0-100): "))

    # Validate inputs before applying any bonus rules
    if annual_salary < 0:
        print("Invalid salary.")
    elif performance_score < 0 or performance_score > 100:
        print("Invalid score. Please enter a number from 0 to 100.")
    else:
        # Check from the highest tier down. Each elif only runs if the
        # ones above it were false, so "score >= 80" here means 80-89
        if performance_score >= 90:
            bonus_percent = 20
        elif performance_score >= 80:
            bonus_percent = 10
        elif performance_score >= 70:
            bonus_percent = 5
        else:
            bonus_percent = 0

        # Convert the percent to a decimal and multiply by salary
        bonus_amount = annual_salary * (bonus_percent / 100)

        print(f"Performance Bonus: {bonus_percent}%")
        print(f"Bonus Amount: ${bonus_amount:,.2f}")


main()