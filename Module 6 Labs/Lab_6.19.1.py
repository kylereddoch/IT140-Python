input_list = input().split()
keys = input_list[0::2]
sentence = input().split()
sentence2 = []

for i in sentence:
    if i in keys:
        sentence2.append(input_list[input_list.index(i)+1])
    else:
        sentence2.append(i)

for x in sentence2:
    if sentence2.index(x) == len(sentence2)-1:
        print(x)
    else:
        print (x, end = ' ')
    