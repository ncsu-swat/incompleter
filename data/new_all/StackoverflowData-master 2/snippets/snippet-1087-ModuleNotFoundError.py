#Source: https://stackoverflow.com/questions/35838021/attributeerror-function-object-has-no-attribute-canvas-width
from pedalClass import Pedal
from ballClass import Ball
import bordersClass
from turtle import *
import random
import time
import turtle

canvas=getcanvas()
CANVAS_WIDTH = canvas.winfo_width()
CANVAS_HEIGHT = canvas.winfo_height()

turtle.penup()
turtle.setup(800,500)
turtle.ht()
turtle.bgpic('breakout.gif')
TIME_STEP = 30
SQUARE_SIZE=20


ball1=Ball(1, 0.5, 0, 0)
mypad=Pedal(0.5, 0, -230, 5, 1)

def borders(cells):
    global mypad
    width=get_screen_width()
    height=get_screen_height()
    x=mypad.xcor()
    y=mypad.ycor()


if (mypad.xcor() > width):
    mypad.set_dx(-mypad.get_dx())
if (cell.ycor() > height):
    cell.set_dy(-cell.get_dy())
if (mypad.xcor() < -width):
    mypad.set_dx(-mypad.get_dx())
if (cell.ycor() < -height):
    cell.set_dy(-cell.get_dy())

def move_pedal(event):
    global mypad
    global CANVAS_WIDTH
    global CANVAS_HEIGHT
    mypad.goto(event.x-canvas.winfo_width()/2, mypad.ycor())
    CANVAS_WIDTH = canvas.winfo_width()
    CANVAS_HEIGHT = canvas.winfo_height()


def move_left(event):
    global mypad
    mypad.goto(event.x-1, mypad.ycor())


def move_right(event):
    global mypad
    mypad.goto(event.x+1, mypad.ycor())


canvas.bind("<Motion>", move_pedal)
canvas.bind("<Left>", move_left)
canvas.bind("<Right>", move_right)
getscreen().listen()


Playing=True
while Playing:
    print(borders.CANVAS_WIDTH)
    ball1.move()
    mypad.borders()
    mypad.move_pedal()
time.sleep(3)