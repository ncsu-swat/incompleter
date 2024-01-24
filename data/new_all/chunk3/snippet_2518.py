# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73832064/sharing-dictionary-over-multiprocesses-typeerror-cannot-pickle-weakref-objec
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from multiprocessing import Process, Manager
    _l_(526572)

except ImportError:
    pass

class Storage():
    _l_(526601)

    def __init__(self,manager):
        _l_(526582)

        _n_(526573, "self", lambda: self).manager = _n_(526574, "manager", lambda: manager)
        _l_(526575)
        _n_(526576, "self", lambda: self).orderbooks = _c_(526580, _a_(526579, _a_(526578, _n_(526577, "self", lambda: self), "manager"), "dict"))
        _l_(526581)

    def store_value(self,el):
        _l_(526588)

        _a_(526584, _n_(526583, "self", lambda: self), "orderbooks")[_n_(526585, "el", lambda: el)[0]] = _n_(526586, "el", lambda: el)[1]
        _l_(526587)

    def write(self,el:_n_(526589, "list", lambda: list)):
        _l_(526600)

        p = _c_(526594, _n_(526590, "Process", lambda: Process), target=_a_(526592, _n_(526591, "self", lambda: self), "store_value"),args=(_n_(526593, "el", lambda: el),))
        _l_(526595)
        _c_(526598, _a_(526597, _n_(526596, "p", lambda: p), "start"))
        _l_(526599)


if _n_(526602, "__name__", lambda: __name__) == '__main__':
    _l_(526614)


    manager=_c_(526604, _n_(526603, "Manager", lambda: Manager))
    _l_(526605)
    book1 = _c_(526608, _n_(526606, "Storage", lambda: Storage), _n_(526607, "manager", lambda: manager))
    _l_(526609)
    _c_(526612, _a_(526611, _n_(526610, "book1", lambda: book1), "write"), [0,1])
    _l_(526613)