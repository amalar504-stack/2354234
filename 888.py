import turtle
import random

turtle = turtle.Turtle()
turtle.speed(0)

colors = ["red", "green", "blue", "yellow", "purple", "orange"]

for i in range(36):
    turtle.color(random.choice(colors))
    
    for j in range(4):
        turtle.forward(100)
        turtle.right(90)
    
    turtle.right(10)

turtle.done()