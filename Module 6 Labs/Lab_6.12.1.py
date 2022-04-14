data = input().split()

total = 0
largest = 0

for num in data:
    num = int(num)
    total += num

    if largest == 0 or num > largest:
        largest = num

print(total // len(data), largest)
