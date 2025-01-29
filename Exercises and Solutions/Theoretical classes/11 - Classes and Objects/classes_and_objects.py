class SomeClass:
    
    def __init__ (self, a):
        pass

class tuple_with_b:
    def __init__(self, name="", age = 0):
        pass

class Person:

    def __init__ (self):
        self.dead = False
        self.energy = 0
        self.rested = 0

    def eat (self):
        self.energy = 100
    
    def sleep (self):
        self.rested = 100
    
    def live (self):
        while not (self.dead):
            self.eat ()
            self.sleep ()

    def die (self):
        self.dead = True

class Child:

    def __init__ (self):
        super.__init__()
        self.happy = True
    
    def play (self):
        self.happy = True
    
    def live (self):
        while not self.dead:
            self.eat ()
            self.sleep ()
            self.play ()
