import turtle
import math
draw = turtle.Turtle()
draw.getscreen().bgcolor("black")
draw.speed(0)
draw.color("yellow")
color = ["#8f00ff", "#4b0082", "#0000ff", "#00ff00", "#ffff00", "#ff7f00", "#ff0000"]

for i in range(500):
    draw.pencolor(color[(int(i/30))%7])
    for j in range(4):
        draw.forward(i)
        draw.right(90)
    draw.left(4)
turtle.done()

# Commenting out the rainbow colours and just keeping the yellow colour looks beautiful too