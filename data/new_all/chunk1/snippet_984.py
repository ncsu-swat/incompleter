# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59118509/defining-property-setter-in-abstract-base-class-gives-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from abc import ABC, abstractmethod
    _l_(404842)

except ImportError:
    pass

def reload_data():
    _l_(404844)

    aux = ['hello']
    _l_(404843)
    return aux


class Base(_n_(404845, "ABC", lambda: ABC)):
    _l_(404855)

    @_n_(404846, "property", lambda: property)
    @_n_(404847, "abstractmethod", lambda: abstractmethod)
    def data(self):
        _l_(404849)

        pass
        _l_(404848)

    @_a_(404850, data, "setter")               # <----- AttributeError if this is defined here
    def data(self, value):
        _l_(404854)

        _n_(404851, "self", lambda: self)._data = _n_(404852, "value", lambda: value)
        _l_(404853)


class Foo(_n_(404856, "Base", lambda: Base)):
    _l_(404872)

    def __init__(self):
        _l_(404859)

        _n_(404857, "self", lambda: self)._data = None
        _l_(404858)

    @_n_(404860, "property", lambda: property)
    def data(self):
        _l_(404871)

        if _a_(404862, _n_(404861, "self", lambda: self), "_data") is None:
            _l_(404867)

            _n_(404863, "self", lambda: self)._data = _c_(404865, _n_(404864, "reload_data", lambda: reload_data))
            _l_(404866)
        aux = _a_(404869, _n_(404868, "self", lambda: self), "_data")
        _l_(404870)
        return aux

foo = _c_(404874, _n_(404873, "Foo", lambda: Foo))
_l_(404875)
_n_(404876, "foo", lambda: foo).data = ['world']
_l_(404877)
_c_(404881, _n_(404878, "print", lambda: print), _a_(404880, _n_(404879, "foo", lambda: foo), "data"))
_l_(404882)