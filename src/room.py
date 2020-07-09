# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap


class Room():
    """
    Takes name and description of room.
    """
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"{self.name}. {self.desc}"
