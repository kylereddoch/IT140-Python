"""
Name: Kyle Reddoch
Date: 4/4/2022
Class: IT-140
Assignment: Module Six Assignment
Professor: Malcolm Wabara, M.S.
"""

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {
        'name': 'Great Hall', 'south': 'Bedroom',
    },
    'Bedroom': {
        'name': 'Bedroom', 'east': 'Cellar', 'north': 'Great Hall',
    },
    'Cellar': {
        'name': 'Cellar', 'west': 'Bedroom',
    },
    'Exit': {
        'name': 'Exit',
    }
}
directions = ['north', 'south', 'east', 'west']  # List of direction commands
current_room = rooms['Great Hall']  # Starting room

while True:
    # display current location
    print('You are in the {}.'.format(current_room['name']))

    if current_room['name'] == 'Cellar':
        print('Congratulations! You have reached the cellar and won the game!')
        break

    elif current_room['name'] == 'Exit':
        print('You can type "quit" to quit the game.')
        pass

    # get user input
    command = input('\nWhich way do you want to go?')
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print('You are unable to go that way. Go another way')
    # exit command
    elif command == 'exit':
        current_room = rooms['Exit']
    # quit game
    elif command == 'quit':
        print('Thanks for playing!')
        break
    # bad command
    else:
        print('Invalid input. Try again.')
