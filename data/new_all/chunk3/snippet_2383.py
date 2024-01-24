# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47103106/python3-subclass-is-being-instantiated-as-superclass-subclass-method-not-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Hand(_a_(578743, _n_(578742, "pydealer", lambda: pydealer), "Stack")):
    _l_(578772)


    def __init__(self, showfirst, **kwargs):
        _l_(578753)

        _c_(578747, _a_(578745, _n_(578744, "super", lambda: super)(), "__init__"), **_n_(578746, "kwargs", lambda: kwargs))
        _l_(578748)
        stay = False
        _l_(578749)
        _n_(578750, "self", lambda: self).showfirstcard = _n_(578751, "showfirst", lambda: showfirst)
        _l_(578752)

    ...
    _l_(578754)

    def showcards(self):
        _l_(578771)

        for i, card in _c_(578757, _n_(578755, "enumerate", lambda: enumerate), _n_(578756, "self", lambda: self)):
            _l_(578770)

            if _n_(578758, "i", lambda: i) == 0:
                _l_(578769)

                if _a_(578760, _n_(578759, "self", lambda: self), "showfirstcard") == False:
                    _l_(578768)

                    _c_(578762, _n_(578761, "print", lambda: print), '***FACEDOWN CARD***')
                    _l_(578763)
                else:
                    _c_(578766, _n_(578764, "print", lambda: print), _n_(578765, "card", lambda: card))
                    _l_(578767)