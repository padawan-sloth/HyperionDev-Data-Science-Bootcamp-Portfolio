rows = 5                                        # establish a variable

for i in range(2 * rows + 1):                   # create for loop that iterates from 0 to 2 x rows. i value will take values from 0 to 2 x rows.
    if i <= rows:                               # if statement to check if i is less than or equal to rows. 
        print('*' * i)                          # prints ascending pattern if i is less than or equal to rows e.g. i = 1, it prints *. i = 2, it prints **, etc.
    else:                                       # else statement when i is greater than rows
        print('*' * (2 * rows - i))             # prints descending pattern. As i increases, the number of '*' will decrease.
