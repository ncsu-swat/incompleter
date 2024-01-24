# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53148400/pathos-multiprocessing-getting-attributeerror-cant-get-attribute-someclass-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import randint
    _l_(570151)

except ImportError:
    pass
try:
    import os
    _l_(570153)

except ImportError:
    pass
try:
    import pathos
    _l_(570155)

except ImportError:
    pass
mp = _a_(570158, _a_(570157, _n_(570156, "pathos", lambda: pathos), "helpers"), "mp")
_l_(570159)
prc = _a_(570163, _a_(570162, _a_(570161, _n_(570160, "pathos", lambda: pathos), "helpers"), "mp"), "Process")
_l_(570164)
class SomeClass:
    _l_(570209)

    def m1(self):
        _l_(570178)

        _n_(570165, "self", lambda: self).objAttr = _c_(570167, _n_(570166, "randint", lambda: randint), 20000,40000)
        _l_(570168)
        _n_(570169, "self", lambda: self).selfID = _c_(570172, _n_(570170, "id", lambda: id), _n_(570171, "self", lambda: self))
        _l_(570173)
        _c_(570176, _a_(570175, _n_(570174, "self", lambda: self), "m2"))
        _l_(570177)
    def m2(self):
        _l_(570189)

        _c_(570187, _n_(570179, "print", lambda: print), _c_(570182, _a_(570181, _n_(570180, "os", lambda: os), "getpid")), _a_(570184, _n_(570183, "self", lambda: self), "objAttr"),_a_(570186, _n_(570185, "self", lambda: self), "selfID"))
        _l_(570188)

    def checkMultiprocessing(self):
        _l_(570208)

        for c in _c_(570191, _n_(570190, "range", lambda: range), 10):
            _l_(570200)

            _c_(570194, _n_(570192, "exec", lambda: exec), f"p{_n_(570193, 'c', lambda: c)} = prc(target=self.m1)")
            _l_(570195)
            _c_(570198, _n_(570196, "exec", lambda: exec), f"p{_n_(570197, 'c', lambda: c)}.start()")
            _l_(570199)
        for c in _c_(570202, _n_(570201, "range", lambda: range), 10):
            _l_(570207)

            _c_(570205, _n_(570203, "exec", lambda: exec), f"p{_n_(570204, 'c', lambda: c)}.join()")
            _l_(570206)
if _n_(570210, "__name__", lambda: __name__) == "__main__":
    _l_(570220)

    _c_(570213, _a_(570212, _n_(570211, "mp", lambda: mp), "freeze_support"))
    _l_(570214)
    _c_(570218, _a_(570217, _c_(570216, _n_(570215, "SomeClass", lambda: SomeClass)), "checkMultiprocessing"))
    _l_(570219)