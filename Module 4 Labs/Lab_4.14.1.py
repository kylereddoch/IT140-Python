user_text = input()

numOfChars = 0
count = 0
for i in user_text:
    if user_text[count] != ' ' and user_text[count] != '.' and user_text[count] != ',':
        numOfChars += 1
    count += 1
print(numOfChars)
