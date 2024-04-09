total = 0
count = 0
user_input = int(input("Please enter a number (or enter -1 to exit): "))

while user_input != -1:
    total += user_input
    count += 1

    user_input = int(input("Please enter a number (or enter -1 to exit): "))

    if user_input == -1:
        print(total)
        break

if count > 0:
    average = total / count
    print("Average of the numbers entered is: ", average)

else:
    print("No number was entered.")