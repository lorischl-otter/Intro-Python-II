# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    """
    Takes name and description of room.
    """
    def __init__(self, name, desc, items=[]):
        self.name = name
        self.desc = desc
        self.items = items

    def __str__(self):
        return f"{self.name}. {self.desc}"

    def show_items(self):
        for i in self.items:
            print(f"{i}")
        print()

# add for when items dropped or added to a room
    # def remove_item(self, item):
    # def add_item(self, item):
