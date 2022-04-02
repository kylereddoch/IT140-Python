def print_popcorn_time(bag_ounces):
    if user_ounces < 3:
        print('Too small')
    elif user_ounces > 10:
        print('Too large')
    else:
        print(6 * user_ounces, 'seconds')
    return bag_ounces


user_ounces = int(input())
print_popcorn_time(user_ounces)
