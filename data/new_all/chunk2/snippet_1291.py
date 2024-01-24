# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55131484/python-unittest-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(441961)

except ImportError:
    pass
try:
    from MyCosine import CosineSim, CosineDis
    _l_(441963)

except ImportError:
    pass

class TestMyCosine(_a_(441965, _n_(441964, "unittest", lambda: unittest), "TestCase")):
    _l_(442007)


    x = [3.5 , 3 , 3.5 , 2.5 , 3]
    _l_(441966)
    y = [3.5 , 3 , 4 , 2.5 , 4.5]
    _l_(441967)
    result = 0.9865867
    _l_(441968)

    def testCosineSim(self, result, x, y):
        _l_(441987)

        _n_(441969, "self", lambda: self).x = _n_(441970, "x", lambda: x)
        _l_(441971)
        _n_(441972, "self", lambda: self).y = _n_(441973, "y", lambda: y)
        _l_(441974)
        _n_(441975, "self", lambda: self).result = _n_(441976, "result", lambda: result)
        _l_(441977)
        _c_(441985, _a_(441979, _n_(441978, "self", lambda: self), "assertEqual"), _c_(441983, _n_(441980, "CosineSim", lambda: CosineSim), _n_(441981, "x", lambda: x),_n_(441982, "y", lambda: y)), _n_(441984, "result", lambda: result), "0.9865867" )
        _l_(441986)

    def testCosineDis(self, result, x, y):
        _l_(442006)

        _n_(441988, "self", lambda: self).x = _n_(441989, "x", lambda: x)
        _l_(441990)
        _n_(441991, "self", lambda: self).y = _n_(441992, "y", lambda: y)
        _l_(441993)
        _n_(441994, "self", lambda: self).result = _n_(441995, "result", lambda: result)
        _l_(441996)
        _c_(442004, _a_(441998, _n_(441997, "self", lambda: self), "assertEqual"), _c_(442002, _n_(441999, "CosineDis", lambda: CosineDis), _n_(442000, "x", lambda: x),_n_(442001, "y", lambda: y)) , _n_(442003, "result", lambda: result), "0.9865867")
        _l_(442005)


if _n_(442008, "__name__", lambda: __name__) == '__main__':
    _l_(442013)

    _c_(442011, _a_(442010, _n_(442009, "unittest", lambda: unittest), "main"), exit=False)
    _l_(442012)