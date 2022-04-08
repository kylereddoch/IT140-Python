user_input = input()
entries = user_input.split(',')
country_capital = {}

for pair in entries:
    split_pair = pair.split(':')
    country_capital[split_pair[0]] = split_pair[1]
    # country_capital is a dictionary, Ex. { 'Germany': 'Berlin', 'France': 'Paris'

del country_capital['Prussia']

print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Spain deleted?', end=' ')
if 'Spain' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Togo deleted?', end=' ')
if 'Togo' in country_capital:
    print('No.')
else:
    print('Yes.')
    