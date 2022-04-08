user_input = input()
test_grades = list(map(int, user_input.split()))  # test_grades is an integer list of test scores

sum_extra = -999  # Initialize 0 before your loop

extra = []

for i in test_grades:
    if i > 100:
        i -= 100
        extra.append(i)
    continue

sum_extra = sum(extra)

print('Sum extra:', sum_extra)
