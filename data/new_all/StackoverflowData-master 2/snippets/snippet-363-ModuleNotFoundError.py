#Source: https://stackoverflow.com/questions/77358866/attributeerror-turtle-object-has-no-attribute-colormode-but-my-code-have
from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.colormode(255)

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  random_colour= (r,g,b)
  return random_color

direction = [0,90,270,180]
turtle.speed(0)
# Remove the `where` variable since it is not used.

# Add a colon (`:`)` after the `for` loop to indicate the beginning of the loop body.
for _ in range(200):
  turtle.color(random_color())
  turtle.forward(30)
  turtle.setheading(random.choice(direction))

# Move the `screen.exitonclick()` function to the end of the code snippet so that the screen does not close until the user clicks it.
screen = Screen()
screen.exitonclick()