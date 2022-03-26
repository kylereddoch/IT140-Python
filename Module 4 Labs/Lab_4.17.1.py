word = ""

while True:
    user_text = input().split()
    word = user_text[0]
    if word == 'quit':
        break

    number = user_text[1]
    print('Eating {} {} a day keeps the doctor away.'.format(number, word))
