string_fav = input("Please enter the name of your favourite restaraunt: ")

int_fav = int(input("Please enter your favourite number: "))

print(string_fav)

print(int_fav)

int_string_fav = int(string_fav)
print(int_string_fav) # This does not work as int_string_fav is made up of characters, not integers. Therefore, it cannot be cast as an integer.