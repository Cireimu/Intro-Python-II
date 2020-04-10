from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons. To the south you smell something foul.",),

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

    'underground_passage': Room("Underground passage", """You find yourself in a passage within the depths. 
From the north you can see light creeping through the ceiling above a flight of stairs, 
from the east you feel a warmed breeze, carrying an odd smell."""),

    'musty_cell': Room("Musty cell", """You enter an old feeling cell, 
filled with tools from a time long before, smelling of something nastolgic yet foul. 
From the west you can barely see a part of light coming from far over above. 
To the south you see a trail of muddied footsteps."""),

    'crawlspace': Room("Crawlspace", """After lowering yourself to the ground and slowly moving through a narrow space,
     you realize you've stumbled upon what's reffered to as a 'crawl space'."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].s_to = room['underground_passage']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declares all items
stone = Item("stone", "hard, cold and versatile")
dull_blade = Item("dull blade", "a well worn blade, good for many tasks")
old_coins = Item(
    "coins", "currency of a bygone era, not much value to be found...")
cloth = Item("cloth", "just a clump of cloth, good for many uses")
sharp_blade = Item("sharp blade", "a barely used blade, sharper than most...")
old_map = Item(
    "map", "a piece of parchment, could be useful to navigate... ")

# Links Items to rooms
room['outside'].items_in_room.append(stone)
room['foyer'].items_in_room.append(old_map)
room['overlook'].items_in_room.append(dull_blade)
room['narrow'].items_in_room.append(cloth)
room['treasure'].items_in_room.append(old_coins)
room['treasure'].items_in_room.append(sharp_blade)

# Functions

valid_directions = ('n', 's', 'e', 'w')
text_wrapper = textwrap.TextWrapper(width=100)
command_list = {
    'n': 'move north',
    's': 'move south',
    'e': 'move east',
    'w': 'move west',
    'i': 'open inventory',
    'q': 'quit game',
    'get (item name)': 'takes item from room',
    'take (item name': 'takes item from room',
    'drop (item name)': 'drops item back into the room',
    'show': 'shows all items in a room'
}


def two_words(string):
    if len(string.split()) == 1:
        return False
    elif len(string.split()) == 2:
        return string.split()
    else:
        return "Unknown command"


def command_guide():
    for key, value in command_list.items():
        print(f"{key}: {value}")


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("What's your name? "), room["outside"])

print(f"Welcome, {player.name}")
print(
    "Some basic commands: [h] view all commands  [q] exit the game ")
print(player.current_room)
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

while True:
    cmd = input("=> ").lower()
    if two_words(cmd) == False:
        if cmd == "q":
            print("Thanks for playing!")
            quit()
        elif cmd in valid_directions:
            player.move(cmd)
        elif cmd == "i":
            player.inventory()
        elif cmd == 'h':
            command_guide()
        elif cmd == "show":
            player.current_room.show_items_in_room()
        else:
            print("Unknown command")

    else:
        verb = two_words(cmd)[0]
        item_object = two_words(cmd)[1]

        if verb == "get" or "take":
            room_item = [
                item for item in player.current_room.items_in_room if item.name == item_object]

            if len(room_item) > 0:
                player.current_room.items_in_room.remove(room_item[0])
                player.items.append(room_item[0])
                room_item[0].on_take()
            else:
                print(f"{item_object} is not available in this room")

        elif verb == "inspect":
            inspect_item = [
                item for item in player.items if item.name == item_object]
            if len(inspect_item) > 0:
                inspect_item[0].on_inspect()
            else:
                print(f"You don't appear to possess a {item_object}")

        elif verb == "drop":
            inventory_item = [
                item for item in player.items if item.name == item_object]

            if len(inventory_item) > 0:
                player.current_room.items_in_room.append(inventory_item[0])
                player.items.remove(inventory_item[0])
                inventory_item[0].on_drop()
            else:
                print(
                    f"You can't drop {item_object} because you don't have it in your inventory")

        else:
            print("Unkown command")
