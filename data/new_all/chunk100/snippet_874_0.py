# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(86161)

except ImportError:
    pass

def bogosort(nums):
    _l_(86192)


    def isSorted(nums):
        _l_(86180)

        if _c_(86164, _n_(86162, "len", lambda: len), _n_(86163, "nums", lambda: nums)) < 2:
            _l_(86166)

            aux = True
            _l_(86165)
            return aux
        for i in _c_(86171, _n_(86167, "range", lambda: range), _c_(86170, _n_(86168, "len", lambda: len), _n_(86169, "nums", lambda: nums)) - 1):
            _l_(86178)

            if _n_(86172, "nums", lambda: nums)[_n_(86173, "i", lambda: i)] > _n_(86174, "nums", lambda: nums)[_n_(86175, "i", lambda: i) + 1]:
                _l_(86177)

                aux = False
                _l_(86176)
                return aux
        aux = True
        _l_(86179)
        return aux
    while not _c_(86183, _n_(86181, "isSorted", lambda: isSorted), _n_(86182, "nums", lambda: nums)):
        _l_(86189)

        _c_(86187, _a_(86185, _n_(86184, "random", lambda: random), "shuffle"), _n_(86186, "nums", lambda: nums))
        _l_(86188)
    aux = _n_(86190, "nums", lambda: nums)
    _l_(86191)
    return aux
nums = [_c_(86195, _n_(86193, "int", lambda: int), _n_(86194, "item", lambda: item)) for item in _c_(86198, _a_(86197, _n_(86196, "num1", lambda: num1), "split"), ',')]
_l_(86199)
_c_(86204, _n_(86200, "print", lambda: print), _c_(86203, _n_(86201, "bogosort", lambda: bogosort), _n_(86202, "nums", lambda: nums)))
_l_(86205)