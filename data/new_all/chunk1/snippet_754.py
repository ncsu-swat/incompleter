# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60542851/nameerror-name-method-name-is-not-defined-python-unittest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(398558)

except ImportError:
    pass
try:
    from dir import *
    _l_(398560)

except ImportError:
    pass

class TestSum(_a_(398562, _n_(398561, "unittest", lambda: unittest), "TestCase")):
    _l_(398574)

    def test_list_int(self):
        _l_(398573)

        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        _l_(398563)
        result = _c_(398566, _n_(398564, "sum", lambda: sum), _n_(398565, "data", lambda: data))
        _l_(398567)
        _c_(398571, _a_(398569, _n_(398568, "self", lambda: self), "assertEqual"), _n_(398570, "result", lambda: result), 6)
        _l_(398572)

if _n_(398575, "__name__", lambda: __name__) == '__main__':
    _l_(398580)

    _c_(398578, _a_(398577, _n_(398576, "unittest", lambda: unittest), "main"))
    _l_(398579)