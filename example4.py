""" Class declaration """
class Cat():
    def __init__(self,myName,myColor,myAge):
        self.__name = myName
        self.__color = myColor
        self.__age = myAge
   
    """ Getters methods """ 

    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color

    def getAge(self):
        return self.__age

    def setColor (self, newColor):
        self.__color = newColor

    def birthday (self):
        self.__age = self.__age + 1

    def sayHello (self):
        print('Hello, my name is',self.getName(), 'and i am', self.getAge(), 'year(s) old.')

""" Objects cat1 and cat2 of class Cat are being instantiated """
cat1 = Cat('Speed', 'yellow', 1)
cat1.sayHello()
cat1.__age = cat1.__age + 1
cat1.sayHello()