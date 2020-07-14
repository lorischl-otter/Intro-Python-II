from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Cave Entrance",
                     "North of you, the cave mount beckons.",
                     ["Armor"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["Shield", "Sword"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["Locket"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["A Small Gold Coin"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by earlier adventurers.
The only exit is to the south.""", ["Empty Chest", "Rusty Arrows"])
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(name="Link", location=room['outside'])

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

user_action = input("""Welcome to The Game.
Press any key to begin, or 'q' at any time to exit. """)
# add in sanitization -- strip off whitespace, lowercase, split
print(user_action)
while not user_action == "q":
    print("You are now at the", player.location, "\n")
    print("""Here's what's around:
(you can pick up using 'get' + item name)\n""")
    player.location.show_items()
    user_action = input("Which direction would you like to go? (n,e,s,w) ")

    if user_action[:3] == 'get':
        selected_item = user_action[4:].capitalize()
        if selected_item in player.location.items:
            player.pick_up_item(selected_item)
        else:
            print("""Sorry there's nothing by that name to pick up.
Be sure you're typing 'get item' with the items name""")

    elif user_action[:4] == 'drop':
        selected_item = user_action[5:].capitalize()
        if selected_item in player.items:
            player.drop_item(selected_item)
        else:
            print("Sorry that's not an item you have to drop.")

    elif player.location == room['outside']:
        if user_action == "n":
            player.location = room['foyer']
        else:
            print("Don't you want to go inside?\n")

    elif player.location == room['foyer']:
        if user_action == "n":
            player.location = room['overlook']
        elif user_action == "e":
            player.location = room['narrow']
        elif user_action == "s":
            player.location = room['outside']
        else:
            print("There's no exit that way. Try again.\n")

    elif player.location == room['overlook']:
        if user_action == "s":
            player.location = room['foyer']
        else:
            print("Don't go over the edge!")

    elif player.location == room['narrow']:
        if user_action == "n":
            player.location = room['treasure']
        elif user_action == "w":
            player.location = room['foyer']
        else:
            print("There's nothing in that direction. Try again.\n")

    elif player.location == room['treasure']:
        if user_action == "s":
            player.location = room['narrow']
        else:
            print("Sorry the treasure isn't over there either!")


# figure out text wrap function?
# how to handle non direction inputs
# change so q in the middle doesn't output the print statement?


# other possible structre:
# while true, then ask input
# if command == q, quit
# if in possible directions, check to see if we can go there
# else... do something else

# refactor into classes -- add method to player class
# (try direction)
