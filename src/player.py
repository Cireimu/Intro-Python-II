# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room != None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You can't go that direction.")

    def inventory(self):
        print("You currently possess: ")
        if len(self.items) == 0:
            print('nothing')
        else:
            for item in self.items:
                print(item.name)
