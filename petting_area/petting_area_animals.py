# import the python datetime module to help us create a timestamp
from datetime import date


class Llama:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f"{self.name} is a {self.species}"


class Donkey:

    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f"{self.name} is a {self.species}"


class Goat:

    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f"{self.name} is a {self.species}"


class Pig:

    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f"{self.name} is a {self.species}"


class Chicken:

    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
