''' Type your code here. '''
age = int(input())
weight = int(input())
heart_rate = int(input())
time = int(input())

calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368

print('Calories: {:.2f} calories'.format(calories))