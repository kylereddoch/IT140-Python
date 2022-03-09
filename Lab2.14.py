# Asks user for inputs and creates variables for each input
favorite_color = input('Enter favorite color:\n')
favorite_flower = input('Enter favorite flower:\n')
favorite_number = int(input('Enter favorite number:\n'))

# Prints each input user inputted seperated by a space.
print('You entered:', favorite_color, favorite_flower, favorite_number)

# Creates 2 passwords based on users inputs
password1 = favorite_color + '_' + favorite_flower
password2 = str(favorite_number) + favorite_color + str(favorite_number)

# Prints a password combo
print('\nFirst password:', password1)
# Prints a second password combo
print('Second password:', password2)

# Outputs the length of the two password options
print('\nNumber of characters in', password1 + ':', len(password1))
print('Number of characters in', password2 + ':', len(password2))
