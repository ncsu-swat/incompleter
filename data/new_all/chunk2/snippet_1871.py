# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45908420/python-pygame-attributeerror-int-object-has-no-attribute-draw
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(475239)

except ImportError:
    pass
try:
    import random
    _l_(475241)

except ImportError:
    pass

BLACK = (0, 0, 0)
_l_(475242)
GREEN = (0, 255, 0)
_l_(475243)

class Rectangle():
    _l_(475298)

    def __init__(self):
        _l_(475274)

        _n_(475244, "self", lambda: self).x = _c_(475247, _a_(475246, _n_(475245, "random", lambda: random), "randrange"), 0, 700)
        _l_(475248)
        _n_(475249, "self", lambda: self).y = _c_(475252, _a_(475251, _n_(475250, "random", lambda: random), "randrange"), 0, 500)
        _l_(475253)
        _n_(475254, "self", lambda: self).height = _c_(475257, _a_(475256, _n_(475255, "random", lambda: random), "randrange"), 20, 70)
        _l_(475258)
        _n_(475259, "self", lambda: self).width = _c_(475262, _a_(475261, _n_(475260, "random", lambda: random), "randrange"), 20, 70)
        _l_(475263)
        _n_(475264, "self", lambda: self).change_x = _c_(475267, _a_(475266, _n_(475265, "random", lambda: random), "randrange"), -3, 3)
        _l_(475268)
        _n_(475269, "self", lambda: self).change_y = _c_(475272, _a_(475271, _n_(475270, "random", lambda: random), "randrange"), -3, 3)
        _l_(475273)

    def move(self):
        _l_(475281)

        _n_(475275, "self", lambda: self).x += _n_(475276, "self", lambda: self).change_x
        _l_(475277)
        _n_(475278, "self", lambda: self).y += _n_(475279, "self", lambda: self).change_y
        _l_(475280)

    def draw(self):
        _l_(475297)

        _c_(475295, _a_(475284, _a_(475283, _n_(475282, "pygame", lambda: pygame), "draw"), "rect"), _n_(475285, "screen", lambda: screen), _n_(475286, "GREEN", lambda: GREEN), [_a_(475288, _n_(475287, "self", lambda: self), "x"), _a_(475290, _n_(475289, "self", lambda: self), "y"), _a_(475292, _n_(475291, "self", lambda: self), "width"), _a_(475294, _n_(475293, "self", lambda: self), "height")])
        _l_(475296)

my_list = []
_l_(475299)

for number in _c_(475301, _n_(475300, "range", lambda: range), 10):
    _l_(475310)

    my_object = _c_(475303, _n_(475302, "Rectangle", lambda: Rectangle))
    _l_(475304)
    _c_(475308, _a_(475306, _n_(475305, "my_list", lambda: my_list), "append"), _n_(475307, "my_object", lambda: my_object))
    _l_(475309)

_c_(475313, _a_(475312, _n_(475311, "pygame", lambda: pygame), "init"))
_l_(475314)

screen = _c_(475318, _a_(475317, _a_(475316, _n_(475315, "pygame", lambda: pygame), "display"), "set_mode"), (700, 500))  
_l_(475319)  
done = False
_l_(475320)
clock = _c_(475324, _a_(475323, _a_(475322, _n_(475321, "pygame", lambda: pygame), "time"), "Clock"))
_l_(475325)

while not _n_(475326, "done", lambda: done):
    _l_(475366)

    for event in _c_(475330, _a_(475329, _a_(475328, _n_(475327, "pygame", lambda: pygame), "event"), "get")):
        _l_(475337)

        if _a_(475332, _n_(475331, "event", lambda: event), "type") == _a_(475334, _n_(475333, "pygame", lambda: pygame), "QUIT"):
            _l_(475336)

            done = True
            _l_(475335)

    _c_(475341, _a_(475339, _n_(475338, "screen", lambda: screen), "fill"), _n_(475340, "BLACK", lambda: BLACK))
    _l_(475342)

    for i in _c_(475347, _n_(475343, "range", lambda: range), _c_(475346, _n_(475344, "len", lambda: len), _n_(475345, "my_list", lambda: my_list))):
        _l_(475356)

        _c_(475350, _a_(475349, _n_(475348, "number", lambda: number), "draw"))
        _l_(475351)
        _c_(475354, _a_(475353, _n_(475352, "number", lambda: number), "move"))
        _l_(475355)

    _c_(475360, _a_(475359, _a_(475358, _n_(475357, "pygame", lambda: pygame), "display"), "flip"))
    _l_(475361)
    _c_(475364, _a_(475363, _n_(475362, "clock", lambda: clock), "tick"), 60)
    _l_(475365)

_c_(475369, _a_(475368, _n_(475367, "pygame", lambda: pygame), "quit"))
_l_(475370)