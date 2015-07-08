"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    # species = "Watermelon"
    # color = "green"
    # imported = False
    # shape = 'natural'
    # seasons = ['Fall', 'Summer']
    def __init__(self, species, color, shape, origin, seasons):
        self.species = species
        self.color = color
        self.shape = shape
        self.origin = origin
        self.seasons = seasons


    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0   # TODO, calculate the real amount!
        self.base_price = 5
        if self.species == "Casabas" or self.species == "Ogens":
            self.base_price += 1
        if self.origin == True:
            self.base_price *= 1.5
        if self.shape == "square":
            self.base_price *= 2

        if self.species == "Watermelon" and qty >= 3:
            total += self.base_price * qty * 0.75
        elif self.species == "Cantaloupe" and qty >= 5:
            total += self.base_price * qty * 0.5
        else:
            total += self.base_price * qty
        

        return total