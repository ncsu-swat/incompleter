# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61058868/why-am-i-getting-a-nameerror-for-self-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class foo:
    _l_(663809)


    def __init__(self, name):
        _l_(663804)

        _n_(663801, "self", lambda: self).name = _n_(663802, "name", lambda: name)
        _l_(663803)
    _c_(663807, _n_(663805, "print", lambda: print), _a_(663806, self, "name"))
    _l_(663808)

x = _c_(663811, _n_(663810, "foo", lambda: foo), 'it works')
_l_(663812)