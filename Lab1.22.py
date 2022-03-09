# Creates variables for user inputs
age = int(input())
weight = int(input())
heart_rate = int(input())
time = int(input())

# Calculates calories based on user inputs and creates variable
calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368

# Outputs calories burned to two decimal points
print('Calories: {:.2f} calories'.format(calories))
