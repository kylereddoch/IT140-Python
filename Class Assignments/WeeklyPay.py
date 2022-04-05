"""
Problem: A company wants a program that will calculate the weekly paycheck for an employee based on how many hours
they worked. For this company, an employee earns $20 an hour for the first 40 hours that t60hey work. The employee
earns overtime, $30 an hour, for each hour they work above 40 hours.
"""

hours_worked = int(input('Enter number of hours worked:'))

weekly_pay = 0
overtime_pay = 0
overtime_hours = 0

if hours_worked <= 40:
    weekly_pay = hours_worked * 20
else:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * 30
    weekly_pay = (40 * 20) + overtime_pay

final_pay = "${:.0f}".format(weekly_pay)

print('Your weekly pay is ', final_pay)
