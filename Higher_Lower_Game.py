from random import randint

name = input("What's your name player?")
print("Welcome to the Higher / Lower Game, ", name + "!")

while True:
    lower = int(input("Enter the lower bound number: "))
    upper = int(input("Enter the upper bound number: "))
    if lower < upper:
        break
    print("The lower bound must be less than the higher bound.")

random_int = randint(lower, upper)

user_num = int(input("Awesome! Now guess a number between {} and {}: ".format(lower, upper)))

while random_int != user_num:
    if user_num < random_int:
        print("Sorry, too low. Try again!")
    if user_num > random_int:
        print("Sorry, too high. Try again!")
    user_num = int(input("Guess another number: "))

print("YAY! You guessed it correct.")
