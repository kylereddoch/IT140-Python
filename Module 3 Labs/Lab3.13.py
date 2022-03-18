"""
Write a program with total change amount as an integer input, and output the change using the fewest coins,
one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural
coin names as appropriate, like 1 Penny vs. 2 Pennies.
"""

# Get an integer from user input (the cents)
money = int(input())  # convert input to integer so we can do math

if money <= 0:
    print('No change')

# Variables to hold the number of each coin
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

# noinspection PyRedeclaration
# Conditional statement to determine the amount of dollars.
dollars = money // 100
if dollars > 0 and money > 0:
    money = money - (dollars * 100)
if dollars == 1:
    print(dollars, 'Dollar')
elif dollars > 1:
    print(dollars, 'Dollars')

# Conditional statement to determine the amount of quarters.
quarters = money // 25
if quarters > 0 and money > 0:
    money = money - (quarters * 25)
if quarters == 1:
    print(quarters, 'Quarter')
elif quarters > 1:
    print(quarters, 'Quarters')

# Conditional statement to determine the amount of dimes.
dimes = money // 10
if dimes > 0 and money > 0:
    money = money - (dimes * 10)
if dimes == 1:
    print(dimes, 'Dime')
elif dimes > 1:
    print(dimes, 'Dimes')

# Conditional statement to determine the amount of nickels.
nickels = money // 5
if nickels > 0 and money > 0:
    money = money - (nickels * 5)
if nickels == 1:
    print(nickels, 'Nickel')
elif nickels > 1:
    print(nickels, 'Nickels')

# Conditional statement to determine the amount of pennies.
pennies = money // 1
if pennies > 0 and money > 0:
    money = money - (pennies * 1)
if pennies == 1:
    print(pennies, 'Penny')
elif pennies > 1:
    print(pennies, 'Pennies')
