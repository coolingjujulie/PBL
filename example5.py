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

""" Object cat1 of class Cat is being instantiated """
cat1 = Cat('Speed','white')

""" The method eat will be executed by the object cat1 """
cat1.eat()

""" The method sayHello will be executed by the object cat1 """
cat1.sayHello()

""" The method makeNoise will be executed by the object cat1 """
cat1.makeNoise()