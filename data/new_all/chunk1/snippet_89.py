# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68439799/typeerror-missing-1-required-positional-argument-while-using-pytest-fixture
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(390479)

except ImportError:
    pass
try:
    import pytest
    _l_(390481)

except ImportError:
    pass

@_a_(390483, _n_(390482, "pytest", lambda: pytest), "fixture")
def base_value():
    _l_(390485)

    aux = 5
    _l_(390484)
    return aux

class Test(_a_(390487, _n_(390486, "unittest", lambda: unittest), "TestCase")):
    _l_(390496)


    def test_add_two(self, base_value):
        _l_(390495)

        result = _n_(390488, "base_value", lambda: base_value) + 2
        _l_(390489)
        _c_(390493, _a_(390491, _n_(390490, "self", lambda: self), "assertEqual"), _n_(390492, "result", lambda: result), 7, "Result doesn't match")
        _l_(390494)