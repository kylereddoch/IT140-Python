import math
"""
Requirements:
Output the user's input. (2 pts)
Output the input squared and cubed. Hint: Compute squared as user_num * user_num. (2 pts)
Get a second user input into user_num2, and output the sum and product. (1 pt)
"""

"""
Example:
Enter integer:
4
You entered: 4
4 squared is 16 
And 4 cubed is 64 !!
Enter another integer:
5
4 + 5 is 9
4 * 5 is 20
"""

user_num = int(input('Enter integer:\n'))

# Type your code here

print("You entered:", user_num)

user_total = user_num * user_num
print(user_num, "squared is", user_total)

user_cubed = math.pow(user_num, 3)
user_num_cubed = math.trunc(user_cubed)
print("And", user_num, "cubed is", user_num_cubed, "!!")

user_num2 = int(input('Enter another integer:\n'))
print(user_num2)

user_sum = user_num + user_num2
print(user_num, "+", user_num2, "is", user_sum)

user_prod = user_num * user_num2
print(user_num, "*", user_num2, "is", user_prod)
