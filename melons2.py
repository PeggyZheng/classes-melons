"""This file should have our melon-type classes in it."""

class Melons(object):

    def get_base_price(self):
        """Calculate price, given a number of melons ordered."""
        try:   
            self.base_price = 5  
            if self.species == "Casabas" or self.species == "Ogens":
                self.base_price += 1
            if self.origin == True:
                self.base_price *= 1.5
            if self.shape == "square":
                self.base_price *= 2
            return self.base_price

        except AttributeError
            print "These are not melons!"

    def get_total_price(self, qty):
        
        try:
            if self.species == "Watermelon" and qty >= 3:
                return self.get_base_price() * qty * 0.75
            elif self.species == "Cantaloupe" and qty >= 5:
                return self.get_base_price() * qty * 0.5
            else:
                return self.get_base_price() * qty

        except AttributeError:
            print "These are not melons!"

#         return total
m = Melons()
print m.get_total_price(2)

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

    
        
class SantaClaus(Melons):
    species = "SantaClaus"
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

    

class HornedMelon(Melons):
    species =  "HornedMelon"
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
