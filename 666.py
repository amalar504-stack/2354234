import turtle

turtle = turtle.Turtle()
turtle.speed(3)

turtle.color("red")
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

for i in range(4):
    turtle.forward(80)
    turtle.right(90)

turtle.color("green")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

for i in range(3):
    turtle.forward(80)
    turtle.left(120)

turtle.color("blue")
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()

for i in range(5):
    turtle.forward(80)
    turtle.left(72)

turtle.done()