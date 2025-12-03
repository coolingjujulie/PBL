import turtle
# Set up Turtle window
window = turtle.Screen()
window.title("Turtle Graphics")
window.bgcolor("white")

turtle.register_shape("dog.gif")

dog = turtle.Turtle()
dog.shape("dog.gif")
dog.penup()
dog.speed(1)
dog.forward(200)

window.exitonclick()