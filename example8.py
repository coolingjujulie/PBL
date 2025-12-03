import turtle

# Set up Turtle window
window = turtle.Screen()
window.title("Turtle Graphics")
window.bgcolor("white")

# Example Turtle commands
t = turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.backward(100)

# Close Turtle window on click
window.exitonclick()
