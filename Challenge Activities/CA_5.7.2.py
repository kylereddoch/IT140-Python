def shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print('Too few.')
    elif num_cycles > 4:
        print('Too many.')
    else:
        for num_cycles in range(1, num_cycles + 1):
            print(num_cycles, ': Lather and rinse.')
        print('Done.')
    return num_cycles


user_cycles = int(input())
shampoo_instructions(user_cycles)
