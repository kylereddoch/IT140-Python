user_int = int(input('Enter integer (32 - 126):\n'))

# Finish reading other items into variables, then output the four values on a single line separated by a
#  space

user_float = float(input('Enter float:\n'))
user_char = input('Enter character:\n')
user_str = input('Enter string:\n')

print(user_int, user_float, user_char, user_str)

# Output the four values in reverse

print(user_str, user_char, user_float, user_int)

# Convert the integer to a character, and output that character

print(user_int, "converted to a character is", chr(user_int))
