user_input = input()
short_names = user_input.split()

short_names[3] = 'Joe'
del short_names[0]

print(short_names)
