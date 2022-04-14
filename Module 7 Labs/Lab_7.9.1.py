file = input() #user file input
with open(file) as f: #open file
    data = f.readlines()
dict_info = {}
for i in range(0, len(data)-1, 2):
    season = int(data[i].strip())
    name = data[i+1].strip()
    if season in dict_info:
        dict_info[season].append(name)
    else:
        dict_info[season] = [name]

#OUTPUT KEYS
keys = list(dict_info.keys()) #will list the dictionary keys
keys.sort() #will sort the keys from min to max
with open('output_keys.txt', 'w') as f:
    for key in keys:
        names = '; '.join(name for name in dict_info[key]) #will print the name with number
        f.write(str(key)+': '+names+"\n")
names = [] #Dictionary value
for item in dict_info: #will add name to dict
    for name in dict_info[item]:
        names.append(name)

#OUTPUT TITTLE
names.sort() #sort names from min to max
with open('output_titles.txt', 'w') as f: #open the file
    for name in names: #will write name plus a new line
        f.write(name+'\n')
