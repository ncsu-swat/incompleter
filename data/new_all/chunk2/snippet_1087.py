# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35838021/attributeerror-function-object-has-no-attribute-canvas-width
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pedalClass import Pedal
    _l_(441095)

except ImportError:
    pass
try:
    from ballClass import Ball
    _l_(441097)

except ImportError:
    pass
try:
    import bordersClass
    _l_(441099)

except ImportError:
    pass
try:
    from turtle import *
    _l_(441101)

except ImportError:
    pass
try:
    import random
    _l_(441103)

except ImportError:
    pass
try:
    import time
    _l_(441105)

except ImportError:
    pass
try:
    import turtle
    _l_(441107)

except ImportError:
    pass

canvas=_c_(441109, _n_(441108, "getcanvas", lambda: getcanvas))
_l_(441110)
CANVAS_WIDTH = _c_(441113, _a_(441112, _n_(441111, "canvas", lambda: canvas), "winfo_width"))
_l_(441114)
CANVAS_HEIGHT = _c_(441117, _a_(441116, _n_(441115, "canvas", lambda: canvas), "winfo_height"))
_l_(441118)

_c_(441121, _a_(441120, _n_(441119, "turtle", lambda: turtle), "penup"))
_l_(441122)
_c_(441125, _a_(441124, _n_(441123, "turtle", lambda: turtle), "setup"), 800,500)
_l_(441126)
_c_(441129, _a_(441128, _n_(441127, "turtle", lambda: turtle), "ht"))
_l_(441130)
_c_(441133, _a_(441132, _n_(441131, "turtle", lambda: turtle), "bgpic"), 'breakout.gif')
_l_(441134)
TIME_STEP = 30
_l_(441135)
SQUARE_SIZE=20
_l_(441136)


ball1=_c_(441138, _n_(441137, "Ball", lambda: Ball), 1, 0.5, 0, 0)
_l_(441139)
mypad=_c_(441141, _n_(441140, "Pedal", lambda: Pedal), 0.5, 0, -230, 5, 1)
_l_(441142)

def borders(cells):
    _l_(441158)

    global mypad
    _l_(441143)
    width=_c_(441145, _n_(441144, "get_screen_width", lambda: get_screen_width))
    _l_(441146)
    height=_c_(441148, _n_(441147, "get_screen_height", lambda: get_screen_height))
    _l_(441149)
    x=_c_(441152, _a_(441151, _n_(441150, "mypad", lambda: mypad), "xcor"))
    _l_(441153)
    y=_c_(441156, _a_(441155, _n_(441154, "mypad", lambda: mypad), "ycor"))
    _l_(441157)


if (_c_(441161, _a_(441160, _n_(441159, "mypad", lambda: mypad), "xcor")) > _n_(441162, "width", lambda: width)):
    _l_(441170)

    _c_(441168, _a_(441164, _n_(441163, "mypad", lambda: mypad), "set_dx"), -_c_(441167, _a_(441166, _n_(441165, "mypad", lambda: mypad), "get_dx")))
    _l_(441169)
if (_c_(441173, _a_(441172, _n_(441171, "cell", lambda: cell), "ycor")) > _n_(441174, "height", lambda: height)):
    _l_(441182)

    _c_(441180, _a_(441176, _n_(441175, "cell", lambda: cell), "set_dy"), -_c_(441179, _a_(441178, _n_(441177, "cell", lambda: cell), "get_dy")))
    _l_(441181)
if (_c_(441185, _a_(441184, _n_(441183, "mypad", lambda: mypad), "xcor")) < -_n_(441186, "width", lambda: width)):
    _l_(441194)

    _c_(441192, _a_(441188, _n_(441187, "mypad", lambda: mypad), "set_dx"), -_c_(441191, _a_(441190, _n_(441189, "mypad", lambda: mypad), "get_dx")))
    _l_(441193)
if (_c_(441197, _a_(441196, _n_(441195, "cell", lambda: cell), "ycor")) < -_n_(441198, "height", lambda: height)):
    _l_(441206)

    _c_(441204, _a_(441200, _n_(441199, "cell", lambda: cell), "set_dy"), -_c_(441203, _a_(441202, _n_(441201, "cell", lambda: cell), "get_dy")))
    _l_(441205)

def move_pedal(event):
    _l_(441230)

    global mypad
    _l_(441207)
    global CANVAS_WIDTH
    _l_(441208)
    global CANVAS_HEIGHT
    _l_(441209)
    _c_(441220, _a_(441211, _n_(441210, "mypad", lambda: mypad), "goto"), _a_(441213, _n_(441212, "event", lambda: event), "x")-_c_(441216, _a_(441215, _n_(441214, "canvas", lambda: canvas), "winfo_width"))/2, _c_(441219, _a_(441218, _n_(441217, "mypad", lambda: mypad), "ycor")))
    _l_(441221)
    CANVAS_WIDTH = _c_(441224, _a_(441223, _n_(441222, "canvas", lambda: canvas), "winfo_width"))
    _l_(441225)
    CANVAS_HEIGHT = _c_(441228, _a_(441227, _n_(441226, "canvas", lambda: canvas), "winfo_height"))
    _l_(441229)


def move_left(event):
    _l_(441241)

    global mypad
    _l_(441231)
    _c_(441239, _a_(441233, _n_(441232, "mypad", lambda: mypad), "goto"), _a_(441235, _n_(441234, "event", lambda: event), "x")-1, _c_(441238, _a_(441237, _n_(441236, "mypad", lambda: mypad), "ycor")))
    _l_(441240)


def move_right(event):
    _l_(441252)

    global mypad
    _l_(441242)
    _c_(441250, _a_(441244, _n_(441243, "mypad", lambda: mypad), "goto"), _a_(441246, _n_(441245, "event", lambda: event), "x")+1, _c_(441249, _a_(441248, _n_(441247, "mypad", lambda: mypad), "ycor")))
    _l_(441251)


_c_(441256, _a_(441254, _n_(441253, "canvas", lambda: canvas), "bind"), "<Motion>", _n_(441255, "move_pedal", lambda: move_pedal))
_l_(441257)
_c_(441261, _a_(441259, _n_(441258, "canvas", lambda: canvas), "bind"), "<Left>", _n_(441260, "move_left", lambda: move_left))
_l_(441262)
_c_(441266, _a_(441264, _n_(441263, "canvas", lambda: canvas), "bind"), "<Right>", _n_(441265, "move_right", lambda: move_right))
_l_(441267)
_c_(441271, _a_(441270, _c_(441269, _n_(441268, "getscreen", lambda: getscreen)), "listen"))
_l_(441272)


Playing=True
_l_(441273)
while _n_(441274, "Playing", lambda: Playing):
    _l_(441292)

    _c_(441278, _n_(441275, "print", lambda: print), _a_(441277, _n_(441276, "borders", lambda: borders), "CANVAS_WIDTH"))
    _l_(441279)
    _c_(441282, _a_(441281, _n_(441280, "ball1", lambda: ball1), "move"))
    _l_(441283)
    _c_(441286, _a_(441285, _n_(441284, "mypad", lambda: mypad), "borders"))
    _l_(441287)
    _c_(441290, _a_(441289, _n_(441288, "mypad", lambda: mypad), "move_pedal"))
    _l_(441291)
_c_(441295, _a_(441294, _n_(441293, "time", lambda: time), "sleep"), 3)
_l_(441296)