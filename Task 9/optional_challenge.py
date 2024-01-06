# Error 1: Missing colon after the if statement
if x > 5
    print("x is greater than 5")                    # Syntax Error. The colon is missing after the if statement. Colons are used to indicate the start of a block of code for control flow statements.

# Error 2: Using an undefined variable y
print(z)                                            # Name Error. The variable z is not defined before it is used. Python raises a Name Error when trying to access a variable that has not been defined.

# Runtime Error: Division by zero
result = 10 / 0                                     # Zero Division Error. Attempting to divide by zero in line 9, result = 10 / 0. This is a runtime error since division by zero is undefined.

# Logical Error: Incorrect formula for calculating the area of a rectangle
length = 5
width = 3
area = length * length  # Should be length * width
print("Area of the rectangle:", area)               # Logical Error. The formula used to calculate the area of a rectangle is incorrect (area = length * length). It should be area = length * width. This is a logical error as the code will run without any errors, but it will not produce the expected result.
