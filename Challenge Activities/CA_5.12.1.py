def swap(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list


values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
