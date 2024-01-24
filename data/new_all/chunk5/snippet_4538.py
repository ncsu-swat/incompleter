# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55944944/attempting-to-inherit-variable-from-parent-class-nameerror-name-r-is-not-def
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Circle(_n_(653508, "Point", lambda: Point)):
    _l_(653513)


    def __init__(self, r):
        _l_(653512)

        _n_(653509, "self", lambda: self).r = _n_(653510, "r", lambda: r)
        _l_(653511)

class Cylinder(_n_(653514, "Circle", lambda: Circle)):
    _l_(653525)


    def __init__(self,h):
        _l_(653524)

        _c_(653519, _a_(653516, _n_(653515, "Circle", lambda: Circle), "__init__"), _n_(653517, "self", lambda: self),_n_(653518, "r", lambda: r))
        _l_(653520)
        _n_(653521, "self", lambda: self).h = _n_(653522, "h", lambda: h)
        _l_(653523)