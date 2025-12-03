import turtle
import random

speed = int(2) 
# The Animal class represents a generic animal in the race.
# It includes basic attributes and methods that all animals will share.
class Animal:
    def __init__(self, shape, color, start_pos):
        # Initialize a turtle object to represent the animal on the screen.
        self.turtle = turtle.Turtle()
        self.turtle.shape(shape)  # Set the shape of the turtle to represent the animal.
        self.turtle.color(color)
        self.turtle.width(5)  # Set the color of the turtle.
        self.turtle.penup()  # Lift the pen so the turtle does not draw on the screen.
        self.turtle.goto(start_pos)  # Move the turtle to the starting position.
        self.speed = speed  # Initialize the speed of the animal.
        self.last_color = "white"  # Track the last terrain color the animal was on.
        self.base_speed = speed  # guardar velocidad original
        self.power_end_time = float('inf')
        self.power_active = False



    # Method to move the animal forward based on its speed.
    def move(self, track):
        self.turtle.forward(self.speed)
        self.check_area(track)  # Check the terrain under the animal and adjust speed if needed.

    # Method to get the current position of the animal.
    def get_position(self):
        return self.turtle.xcor(), self.turtle.ycor()

    # Method to double the speed of the animal, used when the animal finds food.
    def double_speed(self):
        self.power_active = True
        self.speed *= 2

    def divide_speed(self):
        self.power_active = True
        self.speed /= 2

    def restore_speed(self):
        self.power_active = False
        self.speed = self.base_speed

    def nerf_speed(self):
        self.power_active = True
        self.speed *= 0.8

    # Method to check the terrain color under the animal and adjust speed accordingly.
    def check_area(self, track):
        if self.power_active:
            return
        current_x = self.turtle.xcor()  # Get the current x-coordinate of the turtle.
        current_color = track.get_color_under_turtle(current_x)  # Get the color of the track under the turtle.
        #print(current_color)  # Print the current color for debugging purposes.
        if current_color != self.last_color:  # If the terrain color has changed,
            self.adjust_speed(current_color)  # Adjust the speed based on the new terrain color.
            self.last_color = current_color  # Update the last color to the new terrain color.

    # Placeholder method to adjust speed based on the terrain color.
    def adjust_speed(self, color):
        pass

# The Dog class represents a dog in the race.
# It inherits from the Animal class and can have additional or overridden methods.
class Dog(Animal):
    def __init__(self, start_pos):
        super().__init__("images/dog/dog.gif", "brown", start_pos)  # Initialize with a dog shape and brown color.
        #self.turtle.pendown()
        self.frames = [
        "images/dog/dog1.gif",
        "images/dog/dog2.gif",
        "images/dog/dog3.gif",
        "images/dog/dog4.gif",
        "images/dog/dog5.gif"
        ]
        self.current_frame = 0
        super().__init__(self.frames[0], "white", start_pos)  # Prime

    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.turtle.shape(self.frames[self.current_frame])
        turtle.ontimer(self.animate, 120)  # Cambiar imagen cada 120 ms

    # Placeholder method to adjust speed based on the terrain color.
    def adjust_speed(self, color):
        if color == "light green":  # bosque
            self.speed = speed * 1.0
        elif color == "light blue":   # agua
            self.speed = speed * 0.7
        else:          # pista normal
            self.speed = speed * 1.6





class Rabbit(Animal):
    def __init__(self, start_pos):
        super().__init__("images/rabbit/rabbit.gif", "grey", start_pos)  # Initialize with a dog shape and brown color.
        #self.turtle.pendown()

        self.frames = [
        "images/rabbit/rabbit1.gif",
        "images/rabbit/rabbit2.gif",
        "images/rabbit/rabbit3.gif",
        "images/rabbit/rabbit4.gif",
        "images/rabbit/rabbit5.gif"
        ]
        self.current_frame = 0
        super().__init__(self.frames[0], "green", start_pos)  # Prime

    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.turtle.shape(self.frames[self.current_frame])
        turtle.ontimer(self.animate, 120)  # Cambiar imagen cada 120 ms

    def adjust_speed(self, color):
        if color == "light green":    
            self.speed = speed * 1.7
        elif color == "light blue":   
            self.speed = speed * 0.6
        else:        
            self.speed = speed * 1.2


# The TurtleRacer class represents a turtle in the race.
# It inherits from the Animal class and overrides the adjust_speed method.
class TurtleRacer(Animal):
    def __init__(self, start_pos):
        super().__init__("images/turtle/turtle.gif", "green", start_pos)  # Initialize with a turtle shape and green color.
    
        self.frames = [
        "images/turtle/turtle1.gif",
        "images/turtle/turtle2.gif",
        "images/turtle/turtle3.gif",
        "images/turtle/turtle4.gif",
        "images/turtle/turtle5.gif"
        ]
        self.current_frame = 0
        super().__init__(self.frames[0], "green", start_pos)  

    # Method to adjust the speed of the turtle based on the terrain color.
    def adjust_speed(self, color):
        if color == "light blue":     # agua
            self.speed = speed * 2.0
        elif color == "light green":  # bosque
            self.speed = speed * 0.9
        else:        # tierra
            self.speed = speed * 0.5
    
    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.turtle.shape(self.frames[self.current_frame])
        turtle.ontimer(self.animate, 120)  # Cambiar imagen cada 120 ms


# The Monkey class represents a monkey in the race.
# It inherits from the Animal class and overrides the adjust_speed method.
class Monkey(Animal):
    def __init__(self, start_pos):
        super().__init__("images/monkey/monkey.gif", "orange", start_pos)  # Initialize with a monkey shape and orange color.
        #self.turtle.pendown() # para ver la linea 
        self.frames = [
        "images/monkey/monkey1.gif",
        "images/monkey/monkey2.gif",
        "images/monkey/monkey3.gif",
        "images/monkey/monkey4.gif",
        "images/monkey/monkey5.gif"
        ]
        self.current_frame = 0
        super().__init__(self.frames[0], "green", start_pos)  # Prime


    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.turtle.shape(self.frames[self.current_frame])
        turtle.ontimer(self.animate, 120)  # Cambiar imagen cada 120 ms

    def adjust_speed(self, color):
        if color == "light green":    # bosque
            self.speed = speed * 1.8
        elif color == "light blue":   # agua
            self.speed = speed * 0.6
        else:        # tierra
            self.speed = speed * 0.9

class Bird(Animal):
    def __init__(self, start_pos):
        super().__init__("images/bird/bird.gif", "blue", start_pos)  # Initialize with a monkey shape and orange color.
        self.frames = [
        "images/bird/bird1.gif",
        "images/bird/bird2.gif",
        "images/bird/bird3.gif",
        "images/bird/bird4.gif",
        "images/bird/bird5.gif"
        ]
        self.current_frame = 0
        super().__init__(self.frames[0], "green", start_pos)  # Prime
    
    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.turtle.shape(self.frames[self.current_frame])
        turtle.ontimer(self.animate, 120)  # Cambiar imagen cada 120 ms

    def adjust_speed(self, color):
        self
