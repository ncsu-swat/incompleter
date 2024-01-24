# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45901265/receiving-attributeerror-exit-even-when-with-object-has-exit-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Builder:
    _l_(391869)

    def __init__(self):
        _l_(391862)

        _c_(391860, _n_(391859, "print", lambda: print), "Builder init fires")
        _l_(391861)

    def __getattr__(self, name):
        _l_(391868)

        aux = _c_(391866, _n_(391863, "Element", lambda: Element), _n_(391864, "name", lambda: name), _n_(391865, "self", lambda: self))
        _l_(391867)
        return aux

class Element:
    _l_(391902)

    def __init__(self, name, builder):
        _l_(391881)

        _n_(391870, "self", lambda: self).name = _n_(391871, "name", lambda: name)
        _l_(391872)
        _n_(391873, "self", lambda: self).builder = _n_(391874, "builder", lambda: builder)
        _l_(391875)
        _c_(391879, _n_(391876, "print", lambda: print), "Element init fires for name of", _a_(391878, _n_(391877, "self", lambda: self), "name"))
        _l_(391880)
    def __call__(*args, **kargs):
        _l_(391896)

        _c_(391883, _n_(391882, "print", lambda: print), "CALL fires, now with attributes listed:")
        _l_(391884)
        for attr, value in _c_(391889, _n_(391885, "sorted", lambda: sorted), _c_(391888, _a_(391887, _n_(391886, "kargs", lambda: kargs), "items"))):
            _l_(391895)

            _c_(391893, _n_(391890, "print", lambda: print), ' %s=>%s' % (_n_(391891, "attr", lambda: attr), _n_(391892, "value", lambda: value)))
            _l_(391894)

    def __enter__(self):
        _l_(391899)

        aux = _n_(391897, "self", lambda: self)
        _l_(391898)
        return aux

    def __exit__(self, type, value, traceback):
        _l_(391901)

        pass
        _l_(391900)

aa = _c_(391904, _n_(391903, "Builder", lambda: Builder))        
_l_(391905)        
with _c_(391908, _a_(391907, _n_(391906, "aa", lambda: aa), "feed"), xmlns='http://www.w3.org/2005/Atom'):
    _l_(391912)

    _c_(391910, _n_(391909, "print", lambda: print), "INSIDE THE WITH")
    _l_(391911)