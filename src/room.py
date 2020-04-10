# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items_in_room = []

    def __str__(self):
        return f"{self.name}\n\n{self.description}"

    def show_items_in_room(self):
        print(f"Items available in {self.name}: ")
        if len(self.items_in_room) == 0:
            print("nothing found...")
        else:
            for item in self.items_in_room:
                print(item.name)
