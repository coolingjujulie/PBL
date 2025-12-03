from abc import ABC, abstractmethod
""" Declaration of the abstract class Animal """
class Animal(ABC):
    def __init__(self,myName,myColor):
        self.name = myName
        self.color = myColor    

    @abstractmethod
    def makeNoise(self):
        pass

    @abstractmethod
    def eat (self):
        pass

    def sayHello(self):
        print('My name is',self.name, 'and my color is',self.color)

""" Subclass declaration: class Cat inherits from class Animal """
class Cat(Animal):
    def __init__(self,myName,myColor):
        super().__init__(myName,myColor)
        self.numberOfMice = 0

    def eat(self):
        self.numberOfMice = self.numberOfMice + 1
    
    def sayHello(self):
        super().sayHello()
        print('I am a cat and i have eaten',self.numberOfMice,'mouse')

    def makeNoise(self):
        print ('Miau! Miau!')

""" Declaration of the World class """
class World ():
    def __init__(self):
        self.cat1 = Cat('Felix','white')
        self.cat2 = Cat('Speed','black')

    def act(self):
        self.cat1.eat()
        self.cat1.sayHello()
        self.cat1.makeNoise()
        self.cat2.eat()
        self.cat2.sayHello()
        self.cat2.makeNoise()     

""" Object earth of class World is being instantiated """
earth = World()
earth.act()