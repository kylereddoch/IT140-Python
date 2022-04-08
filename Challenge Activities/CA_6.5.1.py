user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

for row in mult_table:
    line = 0
    for num in row:
        if line < len(mult_table) - 1:
            print(num, '| ', end = '')
            line += 1
        else:
            print(num)
