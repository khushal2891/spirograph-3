import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range(7):
    for colors in ["red","blue","green",'yellow','orange','pink','purple','cyan','magenta','white']:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()
#Khushal
#projectifire