# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, location, items=[]):
        self.name = name
        self.location = location
        self.items = items

    # def try_direction(self, user_action):
    #     attribute = user_action + '_to'

    #     # see if the current room has an attribute
    #     # we can use 'hasattr' (has attribute)
    #     if hasattr(self.location, attribute):
    #         # can use 'getattr' to move to room
    #         self.location = getattr(self.location, attribute)
    #     else:
    #         print("Nothing to find here!")

    def pick_up_item(self, item):
        if len(self.items) <= 3:
            self.items.append(item)
            print(f"""\n\nNOW YOU HAVE THE {item}!
You can drop it at any time by typing 'drop {item}'\n""")
        else:
            print("Sorry you'll have to drop something to pick this up.")

    def drop_item(self, item):
        if len(self.items) > 0:
            self.items.remove(item)
            print(f"YOU HAVE DROPPED THE {item}.")
        else:
            print("You don't have any items to drop!")

# add for player to print what items they have
# def print_items
