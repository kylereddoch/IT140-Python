# define exact change function
def exact_change(user_total):
    num_dollars = user_total // 100  # convert to dollars
    user_total %= 100  # get remainder after conversion
    num_quarters = user_total // 25  # convert to quarters
    user_total %= 25  # get remainder after conversion
    num_dimes = user_total // 10  # convert to dimes
    user_total %= 10  # get remainder after conversion
    num_nickels = user_total // 5  # convert to nickels
    user_total %= 5  # get remainder after conversion
    num_pennies = user_total
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_val = int(input())  # prompt user to input an integer
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(
        input_val)  # recall exact_change function

    # define output statements to output number of exact_change variables:
    # num_dollars, num_quarters, num_dimes, num_nickels, num_pennies
    if input_val <= 0:  # if amount is zero
        print('no change')  # print output

    else:
        if num_dollars > 1:  # if number of dollars is greater than one
            print('%d dollars' % num_dollars)  # print number of dollars
        elif num_dollars == 1:  # if number of dollars equal 1
            print('%d dollar' % num_dollars)  # print dollar in singular

        if num_quarters > 1:  # if number of quarters is greater than one
            print('%d quarters' % num_quarters)  # print number of quarters
        elif num_quarters == 1:  # if number of quarters equal 1
            print('%d quarter' % num_quarters)  # print quarter in singular

        if num_dimes > 1:  # if number of dimes is greater than one
            print('%d dimes' % num_dimes)  # print number of dimes
        elif num_dimes == 1:  # if number of dimes equal 1
            print('%d dime' % num_dimes)  # print dime in singular

        if num_nickels > 1:  # if number of nickels is greater than one
            print('%d nickels' % num_nickels)  # print number of nickels
        elif num_nickels == 1:  # if number of nickels equal 1
            print('%d nickel' % num_nickels)  # print nickel in singular

        if num_pennies > 1:  # if number pennies is greater than one
            print('%d pennies' % num_pennies)  # print number of pennies
        elif num_pennies == 1:  # if number of pennies equal 1
            print('%d penny' % num_pennies)  # print penny in singular
            