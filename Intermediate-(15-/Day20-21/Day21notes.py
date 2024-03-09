#Looking at class inheritance

#The following code shows inheritance of animal to fish, the fish has attributes and methods inherited from animal
#but has a few unique attributes and methods

class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print('Inhale, exhale')

class Fish(Animal):
    def __init__(self):
        super().__init__() #With initialisaiton, super().__init__() initialises from the super class (Animal) This is reccommended but not needed
    
    def breathe(self):
        super().breathe() #Calls method of .breathe() within super class
        print('bubbles')
    
    def swim(self):
        print('Swim swim')

joseph = Animal()
isaac = Fish()

joseph.breathe()
isaac.breathe()