# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentroom, inventory = []):
        self.name = name
        self.currentroom = currentroom
        self.inventory = inventory

    def __str__(self):
        return f'{self.name}, {self.currentroom}'

