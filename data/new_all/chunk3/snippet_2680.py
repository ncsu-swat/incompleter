# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67042983/typeerror-init-missing-1-required-positional-argument-sage
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Studentclass import Student
    _l_(567612)

except ImportError:
    pass
try:
    from Courseclass import Course
    _l_(567614)

except ImportError:
    pass

class Marks(_n_(567615, "Student", lambda: Student), _n_(567616, "Course", lambda: Course)):
    _l_(567637)

    def __init__(self, Sid,Cid, Mark):
        _l_(567626)

        _c_(567621, _a_(567618, _n_(567617, "super", lambda: super)(), "__init__"), _n_(567619, "Sid", lambda: Sid),_n_(567620, "Cid", lambda: Cid))#Error line 7, in __init__ super().__init__(Sid,Cid) TypeError: __init__() missing 1 required positional argument: 'Sage'#
        _l_(567622)#Error line 7, in __init__ super().__init__(Sid,Cid) TypeError: __init__() missing 1 required positional argument: 'Sage'#
        _n_(567623, "self", lambda: self).Mark = _n_(567624, "Mark", lambda: Mark)
        _l_(567625)

    def __repr__(self):
        _l_(567636)

        aux = _c_(567634, _a_(567627, '({},{},{})', "format"), _a_(567629, _n_(567628, "self", lambda: self), "Sid"), _a_(567631, _n_(567630, "self", lambda: self), "Cid"), _a_(567633, _n_(567632, "self", lambda: self), "Mark"))
        _l_(567635)
        return aux