#Get user input for name, age, house number and street name.
#Use int for numerical inputs
#When printing sentence, concatenate the int inputs to str.

user_name = input("Please enter your full name: ")
user_age = int(input("Please enter your age: "))
user_house_number = int(input("Please enter your house number: "))
user_street_name = input("Please enter your street name: ")
print("This is " + user_name + ". He is " + str(user_age) + " years old and lives at house number " + str(user_house_number) + " on " + user_street_name + ".")
