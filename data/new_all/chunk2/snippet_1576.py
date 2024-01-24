# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75543849/python-typeerror-init-takes-1-positional-argument-but-4-were-given-pro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Student:
    _l_(428375)

    def __init__(self, name,age,subject):
        _l_(428368)

        _n_(428359, "self", lambda: self).name = _n_(428360, "name", lambda: name)
        _l_(428361)
        _n_(428362, "self", lambda: self).age = _n_(428363, "age", lambda: age)
        _l_(428364)
        _n_(428365, "self", lambda: self).subject = _n_(428366, "subject", lambda: subject)
        _l_(428367)

    def subjchoosen(self):
        _l_(428374)

        _c_(428372, _n_(428369, "print", lambda: print), "The subject choosen is",_a_(428371, _n_(428370, "self", lambda: self), "subject") )
        _l_(428373)

class Science(_n_(428376, "Student", lambda: Student)):
    _l_(428389)

    def __init__(self):
        _l_(428388)

        _c_(428382, _a_(428378, _n_(428377, "super", lambda: super)(), "__init__"), _n_(428379, "name", lambda: name), _n_(428380, "age", lambda: age),_n_(428381, "subject", lambda: subject))
        _l_(428383)
        _c_(428386, _a_(428385, _n_(428384, "super", lambda: super)(), "subjchoosen"))
        _l_(428387)

name = "Test"
_l_(428390)
age = 12
_l_(428391)
subject = "Science"
_l_(428392)
Sc=_c_(428397, _n_(428393, "Science", lambda: Science), _n_(428394, "name", lambda: name),_n_(428395, "age", lambda: age),_n_(428396, "subject", lambda: subject))
_l_(428398)