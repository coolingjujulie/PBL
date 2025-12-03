import turtle  
pen = turtle.Turtle() 
  
def square (side) :
    for i in range(4): 
        pen.forward(side) 
        pen.right(90) 

pen.fillcolor("red") 
pen.begin_fill()
square(150) 
pen.end_fill() 
pen.hideturtle()
turtle.done() 
