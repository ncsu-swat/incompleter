# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62148821/overwriting-init-in-python-typeerror-init-takes-1-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class A:
    _l_(539361)

    x = 0
    _l_(539334)

    def __init__(self, a, b):
        _l_(539343)

        _n_(539335, "self", lambda: self).a = _n_(539336, "a", lambda: a)
        _l_(539337)
        _n_(539338, "self", lambda: self).b = _n_(539339, "b", lambda: b)
        _l_(539340)
        _n_(539341, "A", lambda: A).x += 1
        _l_(539342)

    def __init__(self):
        _l_(539346)

        _n_(539344, "A", lambda: A).x += 1
        _l_(539345)

    def displayCount(self):
        _l_(539352)

        _c_(539350, _n_(539347, "print", lambda: print), 'Count : %d' % _a_(539349, _n_(539348, "A", lambda: A), "x"))
        _l_(539351)

    def display(self):
        _l_(539360)

        _c_(539358, _n_(539353, "print", lambda: print), 'a :', _a_(539355, _n_(539354, "self", lambda: self), "a"), ' b :', _a_(539357, _n_(539356, "self", lambda: self), "b"))
        _l_(539359)

a1 = _c_(539363, _n_(539362, "A", lambda: A), 'George', 25000)
_l_(539364)
a2 = _c_(539366, _n_(539365, "A", lambda: A), 'John', 30000)
_l_(539367)
a3 = _c_(539369, _n_(539368, "A", lambda: A))
_l_(539370)
_c_(539373, _a_(539372, _n_(539371, "a1", lambda: a1), "display"))
_l_(539374)
_c_(539377, _a_(539376, _n_(539375, "a2", lambda: a2), "display"))
_l_(539378)
_c_(539382, _n_(539379, "print", lambda: print), _a_(539381, _n_(539380, "A", lambda: A), "x"))
_l_(539383)