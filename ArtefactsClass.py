import turtle
import random

class Artefacts:
    def __init__(self, color, shape, position):
        self.obj = turtle.Turtle()
        self.obj.shape(shape)
        self.obj.color(color)
        self.obj.penup()
        self.obj.goto(position)
        self.position = position

    def get_position(self):
        return self.position

    def hide(self):
        self.obj.hideturtle()

class Food(Artefacts):
    def __init__(self, color, shape, position):
        super().__init__(color, shape, position)

class Bone(Food):
    def __init__(self, position):
        super().__init__("brown", "images/bone.gif", position)

class Lettuce(Food):
    def __init__(self, position):
        super().__init__("purple", "images/lettuce.gif", position)

class Banana(Food):
    def __init__(self, position):
        super().__init__("yellow", "images/banana.gif", position)

class Carrot(Food):
    def __init__(self, position):
        super().__init__("orange", "images/carrot.gif", position)

class Fence(Artefacts):
    def __init__(self, position):
        super().__init__("gray", "images/barrier.gif", position)  

