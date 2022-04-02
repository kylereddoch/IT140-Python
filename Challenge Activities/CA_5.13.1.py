def number_of_pennies(dollars=0, pennies=0):
    number_of_pennies = (dollars * 100) + pennies
    return number_of_pennies


print(number_of_pennies(int(input()), int(input())))  # Both dollars and pennies
print(number_of_pennies(int(input())))  # Dollars only
