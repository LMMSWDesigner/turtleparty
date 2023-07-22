# turtle party project 

from turtle import *

color("red")

def polygon(x, y, sides, length):
  penup()
  setpos(x,y)
  pendown()
  for i in range(sides):
    forward(length)
    left(360/sides)
  

start = 0  
size = 120
for j in range(3, 14):
  polygon(50, start, j, size)
  left(360/9)
  size -= 8
