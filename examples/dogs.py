'''dogs module. Contains classes for Dog, BorderCollie, Husky.'''
class Dog:
    '''Dog Class'''
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def play(self):
        return "Rooof!"
    def __str__(self):
        return "Dog with color %s and age %s" % (self.color, self.age)

class BorderCollie(Dog):
    '''Border Collie class'''
    def __init__(self, color="black/white", age=1, name="Border Collie"):
        Dog.__init__(self, color, age)
        self.name = name
    def play(self):
        return "Tilts head sideways"

class Husky(Dog):
    '''Husky class'''
    def __init__(self, color="all white", age=1, name="Husky"):
        Dog.__init__(self, color, age)
        self.name = name
    def play(self):
        return "Jumps up and down"
