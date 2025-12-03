""" Superclass declaration"""
class Animal():
    def __init__(self,myName,myColor):
        self.name = myName
        self.color = myColor

    def sayHello (self):
        print('Hello, my name is',self.name, 'my color is',self.color)

""" Subclass declaration: class Cat inherits from class Animal """
class Cat(Animal):
    def __init__(self,myName,myColor):
        super().__init__(myName,myColor)
        self.numberOfMice = 0

    def eatOneMouse(self):
        self.numberOfMice = self.numberOfMice + 1

""" Objects cat1 and cat2 of class Cat are being instantiated """
cat1 = Cat('Speed','white')
cat2 = Cat('Elliot','yellow')

""" The method sayHello will be executed by the object cat1 """
cat1.sayHello()

""" The method sayHello will be executed by the object cat2 """
cat2.sayHello()