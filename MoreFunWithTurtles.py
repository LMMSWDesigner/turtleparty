#Fun with Turtles
# by Lincoln Miller
# 7/30/23

import turtle
timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.speed(0)
timmy.penup()
timmy.hideturtle()

def draw_rect(turtle, color, len, wid, x, y, pensize, speed):
    turtle.speed(speed)
    turtle.width(pensize)
    turtle.color(color)
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(2):
      turtle.forward(len)
      turtle.right(90)
      turtle.forward(wid)
      turtle.right(90)
    turtle.penup()

def polygon(turtle, color, numSides, sizeLen, x, y, pensize, speed ):
    turtle.speed(speed)
    turtle.width(pensize)
    turtle.color(color)
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(numSides):
        turtle.forward(sizeLen)
        turtle.left(360 / numSides)
    turtle.penup()

def drawHouse(x, y, size, color):
    polygon(timmy, color, 4, size, x, y-size, 4, 0)
    polygon(timmy, color, 3, size, x, y, 4, 0)

def drawStopsign(x, y, size, color):
    draw_rect(timmy, color, size, size*10, x, y, 1, 0)
    polygon(timmy, color, 8, size*4, x-3*size/2, y, 1, 0)

#draw_rect(timmy, "green", 50, 50, 25, 150, 2, 100)
#draw_rect(timmy, "blue", 80, 100, -125, 150, 4, 500)
drawHouse(0, -50, 50, "red")
drawHouse(-120, -50, 60, "blue")
drawStopsign(-125, 100, 8, "green")
drawStopsign(0, 100, 5, "orange")




turtle.Screen().exitonclick()

