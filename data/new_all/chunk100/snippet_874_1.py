# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(86207)

except ImportError:
    pass

def bogosort(nums):
    _l_(86238)


    def isSorted(nums):
        _l_(86226)

        if _c_(86210, _n_(86208, "len", lambda: len), _n_(86209, "nums", lambda: nums)) < 2:
            _l_(86212)

            aux = True
            _l_(86211)
            return aux
        for i in _c_(86217, _n_(86213, "range", lambda: range), _c_(86216, _n_(86214, "len", lambda: len), _n_(86215, "nums", lambda: nums)) - 1):
            _l_(86224)

            if _n_(86218, "nums", lambda: nums)[_n_(86219, "i", lambda: i)] > _n_(86220, "nums", lambda: nums)[_n_(86221, "i", lambda: i) + 1]:
                _l_(86223)

                aux = False
                _l_(86222)
                return aux
        aux = True
        _l_(86225)
        return aux
    while not _c_(86229, _n_(86227, "isSorted", lambda: isSorted), _n_(86228, "nums", lambda: nums)):
        _l_(86235)

        _c_(86233, _a_(86231, _n_(86230, "random", lambda: random), "shuffle"), _n_(86232, "nums", lambda: nums))
        _l_(86234)
    aux = _n_(86236, "nums", lambda: nums)
    _l_(86237)
    return aux
num1 = _c_(86242, _a_(86241, _c_(86240, _n_(86239, "input", lambda: input), 'Input  comma separated numbers:\n'), "strip"))
_l_(86243)
_c_(86248, _n_(86244, "print", lambda: print), _c_(86247, _n_(86245, "bogosort", lambda: bogosort), _n_(86246, "nums", lambda: nums)))
_l_(86249)