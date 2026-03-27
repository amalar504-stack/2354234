import turtle

turtle = turtle.Turtle()
turtle.speed(3)

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.color("red")
turtle.begin_fill()

turtle.left(45)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(135)
turtle.forward(100)

turtle.end_fill()

turtle.done()