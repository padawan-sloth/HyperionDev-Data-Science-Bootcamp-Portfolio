user_age = int(input("What is your age? "))
print(user_age)

if user_age >= 65 and user_age <= 100:
    print("Enjoy your retirement!")  

elif user_age > 100:
    print("Sorry, you're dead.")

elif user_age >= 40 and user_age < 65:
    print("You're over the hill.")
  
elif user_age <= 13:
    print("You qualify for the kiddie discount.")

elif user_age == 21:
    print("Congrats on your 21st!")

else:
    print("Age is but a number.")
