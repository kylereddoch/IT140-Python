# Creates variable for user inputted value, presumable their full name
full_name = input()

# Splits the input by spaces and creates list with provided input
mod_name = full_name.split(' ')

# Creates a variable for the last name by removing the last item in list
last_name = mod_name.pop(-1)

# Creates a variable for first initial by getting the first character of the first list item
first_initial = mod_name[0][0]

# If the list has more than 2 items, do what's inside if statement
if len(mod_name) >= 2:
    # Creates variable for middle initial from list by getting first character of the second item
    middle_initial = mod_name[1][0]
    # Prints output
    print(f'{last_name}, {first_initial}.{middle_initial}.')
# Else (list has equal to 2 items)
else:
    # Prints output
    print(f'{last_name}, {first_initial}.')
