# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class C(_n_(1540742, "object", lambda: object)):
    _l_(1540759)

    def __init__(self):
        _l_(1540745)

        _n_(1540743, "self", lambda: self)._x = None
        _l_(1540744)

    @_n_(1540746, "property", lambda: property)
    def x(self):
        _l_(1540750)

        """I'm the 'x' property."""
        aux = _a_(1540748, _n_(1540747, "self", lambda: self), "_x")
        _l_(1540749)
        return aux

    @_a_(1540751, x, "setter")
    def x(self, value):
        _l_(1540755)

        _n_(1540752, "self", lambda: self)._x = _n_(1540753, "value", lambda: value)
        _l_(1540754)

    @_a_(1540756, x, "deleter")
    def x(self):
        _l_(1540758)

        del self._x
        _l_(1540757)

class C(_n_(1540760, "object", lambda: object)):
    _l_(1540777)

    def __init__(self):
        _l_(1540763)

        _n_(1540761, "self", lambda: self)._x = None
        _l_(1540762)

    def _x_get(self):
        _l_(1540767)

        aux = _a_(1540765, _n_(1540764, "self", lambda: self), "_x")
        _l_(1540766)
        return aux

    def _x_set(self, value):
        _l_(1540771)

        _n_(1540768, "self", lambda: self)._x = _n_(1540769, "value", lambda: value)
        _l_(1540770)

    def _x_del(self):
        _l_(1540773)

        del self._x
        _l_(1540772)

    x = _c_(1540775, _n_(1540774, "property", lambda: property), _x_get, _x_set, _x_del, 
                    "I'm the 'x' property.")
    _l_(1540776)

class C(_n_(1540778, "object", lambda: object)):
    _l_(1540801)

    def __init__(self):
        _l_(1540781)

        _n_(1540779, "self", lambda: self)._x = None
        _l_(1540780)

    def _x_get(self):
        _l_(1540785)

        aux = _a_(1540783, _n_(1540782, "self", lambda: self), "_x")
        _l_(1540784)
        return aux

    def _x_set(self, value):
        _l_(1540789)

        _n_(1540786, "self", lambda: self)._x = _n_(1540787, "value", lambda: value)
        _l_(1540788)

    def _x_del(self):
        _l_(1540791)

        del self._x
        _l_(1540790)

    x = _c_(1540793, _n_(1540792, "property", lambda: property), _x_get, doc="I'm the 'x' property.")
    _l_(1540794)
    x = _c_(1540796, _a_(1540795, x, "setter"), _x_set)
    _l_(1540797)
    x = _c_(1540799, _a_(1540798, x, "deleter"), _x_del)
    _l_(1540800)

class C(_n_(1540802, "object", lambda: object)):
    _l_(1540825)

    def __init__(self):
        _l_(1540805)

        _n_(1540803, "self", lambda: self)._x = None
        _l_(1540804)

    def _x_get(self):
        _l_(1540809)

        aux = _a_(1540807, _n_(1540806, "self", lambda: self), "_x")
        _l_(1540808)
        return aux
    x = _c_(1540811, _n_(1540810, "property", lambda: property), _x_get, doc="I'm the 'x' property.")
    _l_(1540812)

    def _x_set(self, value):
        _l_(1540816)

        _n_(1540813, "self", lambda: self)._x = _n_(1540814, "value", lambda: value)
        _l_(1540815)
    x = _c_(1540818, _a_(1540817, x, "setter"), _x_set)
    _l_(1540819)

    def _x_del(self):
        _l_(1540821)

        del self._x
        _l_(1540820)
    x = _c_(1540823, _a_(1540822, x, "deleter"), _x_del)
    _l_(1540824)

class C(_n_(1540826, "object", lambda: object)):
    _l_(1540843)

    def __init__(self):
        _l_(1540829)

        _n_(1540827, "self", lambda: self)._x = None
        _l_(1540828)

    @_n_(1540830, "property", lambda: property)
    def x(self):
        _l_(1540834)

        """I'm the 'x' property."""
        aux = _a_(1540832, _n_(1540831, "self", lambda: self), "_x")
        _l_(1540833)
        return aux

    @_a_(1540835, x, "setter")
    def x(self, value):
        _l_(1540839)

        _n_(1540836, "self", lambda: self)._x = _n_(1540837, "value", lambda: value)
        _l_(1540838)

    @_a_(1540840, x, "deleter")
    def x(self):
        _l_(1540842)

        del self._x
        _l_(1540841)

