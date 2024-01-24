# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57485751/nameerror-name-anyname-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Resources.LinkedList import *
    _l_(388081)

except ImportError:
    pass

class Node:
    _l_(388092)

    def __init__(self,name):
        _l_(388091)

        _n_(388082, "self", lambda: self).name = _n_(388083, "name", lambda: name)
        _l_(388084)
        _n_(388085, "self", lambda: self).children = _c_(388087, _n_(388086, "LinkedList", lambda: LinkedList))
        _l_(388088)
        _n_(388089, "self", lambda: self).next = None
        _l_(388090)