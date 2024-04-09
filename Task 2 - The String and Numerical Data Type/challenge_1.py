import math

a = int(input("Please enter the length of side a of a triangle: "))
b = int(input("Please enter the length of side b of a traingle: "))
c = int(input("Please enter the length of side c of a triangle: "))

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(area)