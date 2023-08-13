class Pet:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour