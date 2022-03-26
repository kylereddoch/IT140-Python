user_score = 0
simon_pattern = input()
user_pattern = input()

for i in simon_pattern:
    if user_pattern[user_score] == simon_pattern[user_score]:
        user_score += 1
    else:
        break

print('User score:', user_score)
