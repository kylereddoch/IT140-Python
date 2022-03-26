word = input()
password = ''

for char in word:
    if char == 'i':
        password += '!'
    elif char == 'a':
        password +='@'
    elif char == 'm':
        password +='M'
    elif char == 'B':
        password +='8'
    elif char == 'o':
        password +='.'
    else:
        password += char
print(password, end='q*s\n')
