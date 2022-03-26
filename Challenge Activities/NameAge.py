"""
Created by: Kyle Reddoch
Email: kyle.reddoch@snhu.edu
Class: IT-140
Professor: Malcolm Wabara
"""

# Imports class date from module datetime
from datetime import date

# Create variables for user inputs of name, age, and year
name = input("What is your name?")
age = int(input("How old are you?"))
year = date.today().year - age

# Using the variables, prints out the users name and the year they were born.
print("Hello " + name + "!" + " You were born in " + str(year) + ".")
