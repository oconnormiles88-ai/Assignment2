# Problem 1: Customer Discount Eligibility
# Determines a customer's discount based on membership status and purchase amount.


def main():
    # Get user inputs. strip() and lower() let "Yes", " YES ", etc. all work
    purchase_amount = float(input("Purchase amount: $"))
    membership = input("Are you a member? (yes/no): ").strip().lower()

    # Validate inputs before applying any discount rules
    if purchase_amount < 0:
        print("Invalid purchase amount.")
    elif membership != "yes" and membership != "no":
        print("Invalid membership status. Please enter yes or no.")
    else:
        # Members: 15% off at $100 or more, otherwise 5% off
        if membership == "yes":
            if purchase_amount >= 100:
                discount_percent = 15
            else:
                discount_percent = 5
        # Non-members: 10% off at $150 or more, otherwise no discount
        else:
            if purchase_amount >= 150:
                discount_percent = 10
            else:
                discount_percent = 0

        # Convert the percent to a decimal and subtract it from the price
        final_price = purchase_amount * (1 - discount_percent / 100)

        print(f"Discount applied: {discount_percent}%")
        print(f"Final price: ${final_price:,.2f}")


main()