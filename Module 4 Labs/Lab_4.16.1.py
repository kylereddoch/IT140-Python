triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

for i in range (triangle_height):
    print(' '.join(triangle_char * (i + 1)) + ' ')
