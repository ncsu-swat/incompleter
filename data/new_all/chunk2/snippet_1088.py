# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35838021/attributeerror-function-object-has-no-attribute-canvas-width
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from turtle import *
    _l_(432665)

except ImportError:
    pass
canvas=_c_(432667, _n_(432666, "getcanvas", lambda: getcanvas)) # the canvas is the area that the turtle is moving (the white background)
_l_(432668) # the canvas is the area that the turtle is moving (the white background)
CANVAS_WIDTH = _c_(432671, _a_(432670, _n_(432669, "canvas", lambda: canvas), "winfo_width")) # here we get canvas(screen) width
_l_(432672) # here we get canvas(screen) width
CANVAS_HEIGHT = _c_(432675, _a_(432674, _n_(432673, "canvas", lambda: canvas), "winfo_height")) # here we get the canvas(screen)height
_l_(432676) # here we get the canvas(screen)height
def get_screen_width():
    _l_(432682)

    global CANVAS_WIDTH
    _l_(432677)
    aux = _c_(432680, _n_(432678, "int", lambda: int), _n_(432679, "CANVAS_WIDTH", lambda: CANVAS_WIDTH)/2-10)
    _l_(432681)
    return aux

# This function returns the height of the screen
def get_screen_height():
    _l_(432688)

    global CANVAS_HEIGHT
    _l_(432683)
    aux = _c_(432686, _n_(432684, "int", lambda: int), _n_(432685, "CANVAS_HEIGHT", lambda: CANVAS_HEIGHT)/2-5)
    _l_(432687)
    return aux