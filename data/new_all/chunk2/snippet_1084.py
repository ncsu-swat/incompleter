# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40243193/getting-python-error-typeerror-nonetype-object-is-not-callable-sometimes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(455868)

except ImportError:
    pass
try:
    from nose_parameterized import parameterized
    _l_(455870)

except ImportError:
    pass
try:
    from CheckFromFile import listFileCheck, RepresentsFloat
    _l_(455872)

except ImportError:
    pass

testParams = _c_(455874, _n_(455873, "listFileCheck", lambda: listFileCheck))
_l_(455875)


class TestSequence(_a_(455877, _n_(455876, "unittest", lambda: unittest), "TestCase")):
    _l_(455899)


    @_c_(455881, _a_(455879, _n_(455878, "parameterized", lambda: parameterized), "expand"), _n_(455880, "testParams", lambda: testParams))
    def test_sequence(self, name, a, b):
        _l_(455898)

        if _c_(455884, _n_(455882, "RepresentsFloat", lambda: RepresentsFloat), _n_(455883, "a", lambda: a)):
            _l_(455897)

            _c_(455889, _a_(455886, _n_(455885, "self", lambda: self), "assertAlmostEqual"), _n_(455887, "a", lambda: a),_n_(455888, "b", lambda: b),2)
            _l_(455890)
        else:
            _c_(455895, _a_(455892, _n_(455891, "self", lambda: self), "assertEqual"), _n_(455893, "a", lambda: a),_n_(455894, "b", lambda: b))
            _l_(455896)


if _n_(455900, "__name__", lambda: __name__) == '__main__':
    _l_(455905)

    _c_(455903, _a_(455902, _n_(455901, "unittest", lambda: unittest), "main"))
    _l_(455904)