import math

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

user_input = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ").lower()
investment_deposit = float(input("How much are you depositing?: "))
investment_interest = float(input("What interest rate are you looking for?: "))
time_interest = int(input("How many years do you plan on investing?: "))
interest_type = input("Are you looking for simple interest or compound interest?: ").lower()

total_simple_interest = investment_deposit * (1 + (investment_interest/100) * time_interest)
total_compound_interest = investment_deposit * math.pow((1 + (investment_interest/100)), time_interest)

house_value = int(input("What is the present value of the house?: "))
bond_interest = float(input("What is the interest rate?: "))
bond_repayment = int(input("How many months do you plan to take to repay the bond?: "))

# Create if statement for investment.
if user_input in ["investment", "bond"]:
    if interest_type in ["simple", "simple interest", "simpleinterest"]:
        print(round(total_simple_interest, 2))
    elif interest_type in ["compound", "compound interest", "compoundinterest"]:
        print(round(total_compound_interest, 2))
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")

# as per the code, simple interest for 1000 at 8% interest for 20 years is 2600. compound interest for 1000 at 8% is 4660.96, to two decimal places.

elif user_input == "bond":
    monthly_interest_rate = bond_interest / 100 / 12
    monthly_repayment = house_value * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, bond_repayment)) / (math.pow(1 + monthly_interest_rate, bond_repayment) - 1)
    print(round(monthly_repayment, 2))
else:
    print("Invalid entry. Please enter either 'Investment' or 'Bond'.")
