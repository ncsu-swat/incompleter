# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44011169/python-pycharm-file-structure-issue-attributeerror-module-object-has-no-at
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(431084)

except ImportError:
    pass
try:
    import os, sys
    _l_(431086)

except ImportError:
    pass
try:
    import gmpy2
    _l_(431088)

except ImportError:
    pass
try:
    from gmpy2 import mpz
    _l_(431090)

except ImportError:
    pass

_c_(431107, _a_(431093, _a_(431092, _n_(431091, "sys", lambda: sys), "path"), "append"), _c_(431106, _a_(431096, _a_(431095, _n_(431094, "os", lambda: os), "path"), "dirname"), _c_(431105, _a_(431099, _a_(431098, _n_(431097, "os", lambda: os), "path"), "dirname"), _c_(431104, _a_(431102, _a_(431101, _n_(431100, "os", lambda: os), "path"), "abspath"), _n_(431103, "__file__", lambda: __file__)))))
_l_(431108)
try:
    from Utils.Utils           import AssertInt, AssertClass
    _l_(431110)

except ImportError:
    pass
try:
    from Utils.ToInteger       import ToInteger
    _l_(431112)

except ImportError:
    pass
try:
    from Utils.RecHash         import RecHash
    _l_(431114)

except ImportError:
    pass

def GetGenerators(n):
    _l_(431124)

    _c_(431117, _n_(431115, "AssertInt", lambda: AssertInt), _n_(431116, "n", lambda: n))
    _l_(431118)
    assert _n_(431119, "n", lambda: n) >= 0, "n must be greater than or equal 0"
    _l_(431120)

    generators = []
    _l_(431121)
    aux = _n_(431122, "generators", lambda: generators)
    _l_(431123)

    # ... irrelevant code...

    return aux


class GetGeneratorsTest(_a_(431126, _n_(431125, "unittest", lambda: unittest), "TestCase")):
    _l_(431136)

    def testGetGenerators(self):
        _l_(431135)

        _c_(431133, _a_(431128, _n_(431127, "self", lambda: self), "assertEqual"), _c_(431132, _n_(431129, "len", lambda: len), _c_(431131, _n_(431130, "GetGenerators", lambda: GetGenerators), 50)), 50)
        _l_(431134)


if _n_(431137, "__name__", lambda: __name__) == '__main__':
    _l_(431142)

    _c_(431140, _a_(431139, _n_(431138, "unittest", lambda: unittest), "main"))
    _l_(431141)