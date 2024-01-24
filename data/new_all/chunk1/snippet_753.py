# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60542851/nameerror-name-method-name-is-not-defined-python-unittest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(395469)

except ImportError:
    pass
try:
    from dir import *
    _l_(395471)

except ImportError:
    pass

class TestSum(_a_(395473, _n_(395472, "unittest", lambda: unittest), "TestCase")):
    _l_(395485)

    def test_list_int(self):
        _l_(395484)

        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        _l_(395474)
        result = _c_(395477, _n_(395475, "calculate", lambda: calculate), _n_(395476, "data", lambda: data))
        _l_(395478)
        _c_(395482, _a_(395480, _n_(395479, "self", lambda: self), "assertEqual"), _n_(395481, "result", lambda: result), 6)
        _l_(395483)

if _n_(395486, "__name__", lambda: __name__) == '__main__':
    _l_(395491)

    _c_(395489, _a_(395488, _n_(395487, "unittest", lambda: unittest), "main"))
    _l_(395490)