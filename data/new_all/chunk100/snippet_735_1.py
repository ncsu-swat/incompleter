# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(74130)

    result = []
    _l_(74105)
    ele_val = 0
    _l_(74106)
    for digit in _n_(74107, "lst", lambda: lst):
        _l_(74120)

        if _n_(74108, "digit", lambda: digit) == 0:
            _l_(74119)

            if _n_(74109, "ele_val", lambda: ele_val) != 0:
                _l_(74116)

                _c_(74113, _a_(74111, _n_(74110, "result", lambda: result), "append"), _n_(74112, "ele_val", lambda: ele_val))
                _l_(74114)
                ele_val = 0
                _l_(74115)
        else:
            ele_val += _n_(74117, "digit", lambda: digit)
            _l_(74118)
    if _n_(74121, "ele_val", lambda: ele_val) > 0:
        _l_(74127)

        _c_(74125, _a_(74123, _n_(74122, "result", lambda: result), "append"), _n_(74124, "ele_val", lambda: ele_val))
        _l_(74126)
    aux = _n_(74128, "result", lambda: result)
    _l_(74129)
    return aux
_c_(74132, _n_(74131, "print", lambda: print), '\nOriginal list:')
_l_(74133)
_c_(74136, _n_(74134, "print", lambda: print), _n_(74135, "nums", lambda: nums))
_l_(74137)
_c_(74139, _n_(74138, "print", lambda: print), '\nCompute the sum of non-zero groups (separated by zeros) of the said list of numbers:')
_l_(74140)
_c_(74145, _n_(74141, "print", lambda: print), _c_(74144, _n_(74142, "test", lambda: test), _n_(74143, "nums", lambda: nums)))
_l_(74146)