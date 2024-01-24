# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75181755/function-call-for-pong-game-made-in-python-throwing-attributeerror-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from turtle import Turtle
    _l_(607161)

except ImportError:
    pass
try:
    import random
    _l_(607163)

except ImportError:
    pass

class Ball(_n_(607164, "Turtle", lambda: Turtle)):
    _l_(607231)

    def __init__(self):
        _l_(607191)

        _c_(607167, _a_(607166, _n_(607165, "super", lambda: super)(), "__init__"))
        _l_(607168)
        _n_(607169, "self", lambda: self).ball = _c_(607171, _n_(607170, "Turtle", lambda: Turtle), shape="circle")
        _l_(607172)
        _c_(607176, _a_(607175, _a_(607174, _n_(607173, "self", lambda: self), "ball"), "color"), "white")
        _l_(607177)
        _c_(607181, _a_(607180, _a_(607179, _n_(607178, "self", lambda: self), "ball"), "penup"))
        _l_(607182)
        _c_(607189, _a_(607185, _a_(607184, _n_(607183, "self", lambda: self), "ball"), "setheading"), _c_(607188, _a_(607187, _n_(607186, "random", lambda: random), "randint"), 1, 360))
        _l_(607190)

    def collide(self):
        _l_(607203)

        current_heading = _c_(607195, _a_(607194, _a_(607193, _n_(607192, "self", lambda: self), "ball"), "heading"))
        _l_(607196)
        _c_(607201, _a_(607199, _a_(607198, _n_(607197, "self", lambda: self), "ball"), "setheading"), 180 - _n_(607200, "current_heading", lambda: current_heading))
        _l_(607202)

    def wall(self):
        _l_(607219)

        if _c_(607207, _a_(607206, _a_(607205, _n_(607204, "self", lambda: self), "ball"), "ycor")) == 350 or _c_(607211, _a_(607210, _a_(607209, _n_(607208, "self", lambda: self), "ball"), "ycor")) == -350:
            _l_(607218)

            _c_(607215, _a_(607214, _a_(607213, _n_(607212, "self", lambda: self), "ball"), "collide"))
            _l_(607216)
        else:
            pass
            _l_(607217)

    def move(self):
        _l_(607230)

        _c_(607223, _a_(607222, _a_(607221, _n_(607220, "self", lambda: self), "ball"), "forward"), 5)
        _l_(607224)
        _c_(607228, _a_(607227, _a_(607226, _n_(607225, "self", lambda: self), "ball"), "wall"))
        _l_(607229)