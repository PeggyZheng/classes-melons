"""This file should have our melon-type classes in it."""

class Melons(object):
    # def __init__(self,:
    #     self.species = species
    #     self.color = color
    #     self.shape = shape
    #     self.origin = origin
    #     self.seasons = seasons

    def get_base_price(self):
        """Calculate price, given a number of melons ordered."""

        self.base_price = 5  
        if self.species == "Casabas" or self.species == "Ogens":
            self.base_price += 1
        if self.origin == True:
            self.base_price *= 1.5
        if self.shape == "square":
            self.base_price *= 2
        return self.base_price

    def get_total_price(self, qty):
        if self.species == "Watermelon" and qty >= 3:
            return self.get_base_price() * qty * 0.75
        elif self.species == "Cantaloupe" and qty >= 5:
            return self.get_base_price() * qty * 0.5
        else:
            return self.get_base_price() * qty

#         return total


class Watermelon(Melons):
    species = "Watermelon"
    color = "green"
    origin = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
   

class Cantaloupe(Melons):
    species = "Cantaloupe"
    color = "tan"
    origin = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']


class Casabas(Melons):
    species = "Casabas"
    color = "green"
    origin = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']


class Sharlyn(Melons):
    species = "Sharlyn"
    color = "tan"
    origin = True
    shape = 'natural'
    seasons = ['Summer']

    
        
class Santa_Claus(Melons):
    species = "Santa_Claus"
    color = "green"
    origin = True
    shape = 'natural'
    seasons = ['Spring', 'Winter']

    

class Christmas(Melons):
    species =  "Christmas"
    color = "green"
    origin = False
    shape = 'natural'
    seasons = ['Spring', 'Winter']

    

class Horned_Melon(Melons):
    species =  "Horned_Melon"
    color = "yellow"
    origin = True
    shape = 'natural'
    seasons = ['Summer']

    

class Xigua(Melons):
    species =  "Xigua"
    color = "black"
    origin = True
    shape = 'square'
    seasons = ['Summer']

    

class Ogens(Melons):
    species =  "Ogens"
    color = "tan"
    origin = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    


        

w = Xigua()
print w.get_total_price(2)
print w.get_total_price(6)
