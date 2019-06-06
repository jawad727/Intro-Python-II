from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Link items

lawnmower = Item('lawnmower', 'a device for cutting grass')
sword = Item('sword', 'weapon with a long metal blade')
fidgetSpinner = Item('fidget-spinner', 'an item used to spin..')
lamp = Item('lamp', 'a device for giving light')
spoon = Item('spoon', 'a device used to eat food')
bow = Item('bow', 'a weapon used to shoot arrows')
arrows = Item('arrows', '5x arrows')
gold = Item('gold', 'in game currency')
diamond = Item('diamond', 'in game currency')


room['outside'].items = [lawnmower.name]
room['foyer'].items = [sword.name, fidgetSpinner.name]
room['overlook'].items = [lamp.name, spoon.name, bow.name]
room['narrow'].items = [arrows.name]
room['treasure'].items = [gold.name, diamond.name]


# Main

# Make a new player object that is currently in the 'outside' room.

playa = Player('Randy' , room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# selection = None
# while selection != 'q':
#     selection = input(f"Your Location is {room['outside']}: ")
#     try: 
#         selection = str(selection)
#         if playa.currentroom == 'outside' and selection == 'n':
#             playa.currentroom = room['outside'].n_to
#     except ValueError:
#         print("Please enter your choice as a number.")


selection = None
while selection != 'q':
    print(f'\nYour Name: {playa.name}\nYour Inventory: {playa.inventory}\n')
    selection = input(f"Your Location is {playa.currentroom}\n")
    
    if playa.currentroom == room['outside'] and selection == 'n':
        playa.currentroom = room['outside'].n_to
    elif playa.currentroom == room['outside'] and selection in room['outside'].items:
        playa.inventory.append(selection)
        room['outside'].items.remove(selection)
        print(f'\n***{selection} has been added to your inventory***')

    elif playa.currentroom == room['foyer'] and selection == 'n':
        playa.currentroom = room['foyer'].n_to
    elif playa.currentroom == room['foyer'] and selection == 'e':
        playa.currentroom = room['foyer'].e_to
    elif playa.currentroom == room['foyer'] and selection == 's':
        playa.currentroom = room['foyer'].s_to

    elif playa.currentroom == room['overlook'] and selection == 's':
        playa.currentroom = room['overlook'].s_to

    elif playa.currentroom == room['narrow'] and selection == 'w':
        playa.currentroom = room['narrow'].w_to
    elif playa.currentroom == room['narrow'] and selection == 'n':
        playa.currentroom = room['narrow'].n_to

    elif playa.currentroom == room['treasure'] and selection == 's':
        playa.currentroom = room['treasure'].s_to
    elif selection == 'q':
        print('\nThanks for playing!')
    else:
        print('\nPlease choose a valid direction\n')
    