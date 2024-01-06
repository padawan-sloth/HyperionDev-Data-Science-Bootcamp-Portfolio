import math

print("Investment - to calculate the amount of interest you'll earn on your investment") #print statement so user has investment information
print("Bond - to calculate the amount you'll have to pay on a home loan") #print statement so user has bond information
user_input = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ").lower() # get user input for interest or bond. user input need not be case sensitive, so cover all usual posibilites of input. convert to lowe case by adding .lower, when printing

# Create if statement for investment. Cover all usual posibilites of input. Use above formula variables as part of if statements.

if user_input == "investment":

    investment_deposit = float(input("How much are you depositing?: ")) # get user input for amount being deposited (cover decimal numbers as well)
    investment_interest = float(input("What interest rate are you looking for?: ")) #  get user input for interest rate that they're looking for (cover decimal numbers as well)
    time_interest = int(input("How many years do you plan on investing?: ")) # get user input for how many years they want to invest
    interest_type = input("Are you looking for simple interest or compound interest?: ").lower() # get user input on if they want compound or simple interest. convert to lower case by addint .lower when printing
    total_simple_interest = investment_deposit * (1 + (investment_interest/100) * time_interest) # formula for simple interest
    total_compound_interest = investment_deposit * math.pow((1 + (investment_interest/100)),  time_interest) # formula for compound interest - round it up to two decimal places

                #run an if statement for investment types. round it up to 2 decimal places

    if interest_type in ["simple", "simple interest", "simpleinterest"]:
        print(round(total_simple_interest, 2))
    elif interest_type in ["compound", "compound interest", "compoundinterest"]:
        print(round(total_compound_interest, 2))
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")

                #run an elif statement for the bond. round it up to 2 decimal places

elif user_input == "bond":
    
    house_value = int(input("What is the present value of the house?: "))
    bond_interest = int(input("What is the interest rate?: "))
    bond_repayment = int(input("How many months do you plan to take to repay the bond?: "))
    repayment = (bond_interest/100 / 12 * house_value) / (1 - math.pow(1 + ((bond_interest/100) / 12), -bond_repayment))
    
    print(round(repayment, 2), "per month.")

                #run an else statement to end the if statement

else:
    print("Invalid entry. Please enter either 'Investment' or 'Bond'.")