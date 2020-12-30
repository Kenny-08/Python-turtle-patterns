import turtle
import math

point = turtle.Turtle()
point.getscreen().bgcolor("black")
point.pencolor("white")
point.speed(0)
point.penup()

point.pendown()
point.pensize(1)
point.color("yellow","blue")
# colour=["violet","indigo","blue","green","yellow",'orange',"red"]
for i in range(500):
    # point.color(colour[int(i/7)%7])
    point.circle(30,140)
    point.forward(i)
    # point.left(math.sqrt(i))
turtle.done()




