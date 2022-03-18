"""
Write a program whose inputs are three integers, and whose output is the smallest of the three values.
"""

# Create variables based on user input
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))

if (a <= b and a <= c):
    print(a, "is the smallest")

elif (b <= a and b <= c):
    print(b, "is the smallest")
else:
    print(c, "is the smallest")
