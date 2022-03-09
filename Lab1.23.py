# Creates variable based on user input
user_int = int(input('Enter integer (32 - 126):\n'))
user_float = float(input('Enter float:\n'))
user_char = input('Enter character:\n')
user_str = input('Enter string:\n')

# Outputs each value on a single line separated by a space
print(user_int, user_float, user_char, user_str)

# Outputs the four values in reverse
print(user_str, user_char, user_float, user_int)

# Converts the integer to a character, and outputs that character
print(user_int, "converted to a character is", chr(user_int))
