import turtle
import random
# The RaceTrack class sets up and manages the race track where the animals will compete.
class RaceTrack:
    def __init__(self, width, height):
        # Initialize the screen for the race.
        self.screen = turtle.Screen()
        self.screen.title("Race Game")
        self.screen.bgpic("images/fondo.gif")
        self.screen.setup(width=width, height=height)
        # Initialize the turtle that will draw the track.
        self.track = turtle.Turtle()
        self.track.speed(0)
        # Store the width and height of the track.
        self.width = width
        self.height = height
         # List to keep track of different areas on the track.
        self.areas = []

# Method to draw a colored area on the track.
    def draw_area(self, color, start_x, area_width):
        self.track.penup()
        self.track.goto(start_x, self.height // 2)
        self.track.pendown()
        self.track.color(color)
        self.track.begin_fill()
        for _ in range(2):
            self.track.forward(area_width)
            self.track.right(90)
            self.track.forward(self.height)
            self.track.right(90)
        self.track.end_fill()
        self.areas.append((start_x, start_x + area_width, color))

# Method to draw lanes and boundaries for the race.
    def draw_lanes(self):
        self.track.penup()
        self.track.goto(-self.width // 2 - 5, self.height // 2 + 5)
        self.track.pendown()
        self.track.color("black")
        self.track.width(5)  # Set the pen width to 5 pixels
        self.track.forward(self.width + 5)
        self.track.right(90)
        self.track.forward(self.height + 5)
        self.track.right(90)
        self.track.forward(self.width + 5)
        self.track.right(90)
        self.track.forward(self.height + 5)
        self.track.right(90)
        self.track.pen(pensize=2, pencolor='gold')
        lane_height = self.height / 5
        y = self.height / 2 - lane_height

        for _ in range(4):   
            self.track.penup()
            self.track.goto(-self.width // 2, y)
            self.track.pendown()
            self.track.forward(self.width)
            y -= lane_height
        self.track.hideturtle()


    # Method to create random colored areas on the track.
    def create_random_areas(self, num_areas, colors):
        used_positions = []
        start_x = -self.width // 2 + 50
        end_x = self.width // 2 - 50
        available_width = end_x - start_x
    
        min_area_width = 50
        max_area_width = 400
        remaining_width = available_width - num_areas * min_area_width
    
        for _ in range(num_areas):
            area_width = min_area_width + random.randint(0, remaining_width // num_areas)
            remaining_width -= (area_width - min_area_width)
        
            if used_positions:
                start_x = used_positions[-1][1]+random.randint(1,100)
            end_area_x = start_x + area_width
        
            color = random.choice(colors)
            self.draw_area(color, start_x, area_width)
            used_positions.append((start_x, end_area_x))


    def get_color_under_turtle(self, x):
        for area_start, area_end, color in self.areas:
            if area_start < x < area_end:
                return color
        return "white"
    
    def create_finish_line(self):
        self.track.penup()
        self.track.goto(475,-160)
        self.track.pendown()
        self.track.color("red")
        self.track.left(90)
        self.track.width(5)  
        self.track.forward(self.height)


