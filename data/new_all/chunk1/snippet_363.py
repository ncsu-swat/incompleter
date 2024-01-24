# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77358866/attributeerror-turtle-object-has-no-attribute-colormode-but-my-code-have
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from turtle import Turtle, Screen
  _l_(418924)

except ImportError:
  pass
try:
  import random
  _l_(418926)

except ImportError:
  pass

turtle = _c_(418928, _n_(418927, "Turtle", lambda: Turtle))
_l_(418929)
_c_(418932, _a_(418931, _n_(418930, "turtle", lambda: turtle), "colormode"), 255)
_l_(418933)

def random_color():
  _l_(418952)

  r = _c_(418936, _a_(418935, _n_(418934, "random", lambda: random), "randint"), 0,255)
  _l_(418937)
  g = _c_(418940, _a_(418939, _n_(418938, "random", lambda: random), "randint"), 0,255)
  _l_(418941)
  b = _c_(418944, _a_(418943, _n_(418942, "random", lambda: random), "randint"), 0,255)
  _l_(418945)
  random_colour= (_n_(418946, "r", lambda: r),_n_(418947, "g", lambda: g),_n_(418948, "b", lambda: b))
  _l_(418949)
  aux = _n_(418950, "random_color", lambda: random_color)
  _l_(418951)
  return aux

direction = [0,90,270,180]
_l_(418953)
_c_(418956, _a_(418955, _n_(418954, "turtle", lambda: turtle), "speed"), 0)
_l_(418957)
# Remove the `where` variable since it is not used.

# Add a colon (`:`)` after the `for` loop to indicate the beginning of the loop body.
for _ in _c_(418959, _n_(418958, "range", lambda: range), 200):
  _l_(418978)

  _c_(418964, _a_(418961, _n_(418960, "turtle", lambda: turtle), "color"), _c_(418963, _n_(418962, "random_color", lambda: random_color)))
  _l_(418965)
  _c_(418968, _a_(418967, _n_(418966, "turtle", lambda: turtle), "forward"), 30)
  _l_(418969)
  _c_(418976, _a_(418971, _n_(418970, "turtle", lambda: turtle), "setheading"), _c_(418975, _a_(418973, _n_(418972, "random", lambda: random), "choice"), _n_(418974, "direction", lambda: direction)))
  _l_(418977)

# Move the `screen.exitonclick()` function to the end of the code snippet so that the screen does not close until the user clicks it.
screen = _c_(418980, _n_(418979, "Screen", lambda: Screen))
_l_(418981)
_c_(418984, _a_(418983, _n_(418982, "screen", lambda: screen), "exitonclick"))
_l_(418985)