# Creates variable based on users input (ex. h Happy)
user_str = input()

# Creates variable by getting the value starting at character count 0 and ending before 1
char = user_str[0:1]
# Creates variable by getting the value starting at character count 2 though end of users input
phrase = user_str[2:]

# Creates variable based on the amount of char in the users input
char_total = phrase.count(char)

# Prints total number of char found in input
print(char_total)
