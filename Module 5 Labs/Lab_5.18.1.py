# define swap values function
def swap_values(user_val1=None, user_val2=None):
    swap = user_val1
    user_val1 = user_val2
    user_val2 = swap
    return user_val1, user_val2


if __name__ == '__main__':

    user_val1 = int(input())  # prompt user to input an integer
    user_val2 = int(input())  # prompt user to input an integer

    user_val1, user_val2 = swap_values(user_val1, user_val2)  # recall swap_values function

    print(user_val1, user_val2)  # print output
