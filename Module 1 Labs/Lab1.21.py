# Create variables for two user inputs
user_num = int(input())
x = int(input())

# Creates variable for user first input divided by the second input
user_total = user_num // x

# Creates variables for the total of each division 3 times
result1 = user_total
result2 = user_total // x
result3 = result2 // x

# Outputs the value of the users first input divided by second input 3 times.
print(result1, result2, result3)
