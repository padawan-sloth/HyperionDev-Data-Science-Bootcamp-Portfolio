user_input = input("Please enter a sentence: ") # Get user input
print(user_input)                               # print user input
str_manip = user_input                          # get user input stored as a variable that can be manipulated

print(len(str_manip))                           # print the length of user input

str_manip_end = str_manip[-1]                   # new variable where the user input indexing starts from the end of the user input
str_manip_end_replace = str_manip.replace(str_manip_end, "@") # variable where the end of the user input is replaced with a "@" sign.
print(str_manip_end_replace)                    # print the variable

str_manip_last_three = str_manip[-1:-4:-1]      # new variable for printing user input backwards, but only for the last three characters.
print(str_manip_last_three)                     # print the variable

str_manip_five = str_manip[:3] + str_manip[-2]  # concatenate the first three characters and the second last character of the input/
print(str_manip_five)                           # print the conatenation
