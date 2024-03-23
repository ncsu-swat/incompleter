# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(74213)

    result = []
    _l_(74189)
    ele_val = 0
    _l_(74190)
    for digit in _n_(74191, "lst", lambda: lst):
        _l_(74203)

        if _n_(74192, "digit", lambda: digit) == 0:
            _l_(74202)

            if _n_(74193, "ele_val", lambda: ele_val) != 0:
                _l_(74199)

                _c_(74197, _a_(74195, _n_(74194, "result", lambda: result), "append"), _n_(74196, "ele_val", lambda: ele_val))
                _l_(74198)
        else:
            ele_val += _n_(74200, "digit", lambda: digit)
            _l_(74201)
    if _n_(74204, "ele_val", lambda: ele_val) > 0:
        _l_(74210)

        _c_(74208, _a_(74206, _n_(74205, "result", lambda: result), "append"), _n_(74207, "ele_val", lambda: ele_val))
        _l_(74209)
    aux = _n_(74211, "result", lambda: result)
    _l_(74212)
    return aux
nums = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
_l_(74214)
_c_(74216, _n_(74215, "print", lambda: print), '\nOriginal list:')
_l_(74217)
_c_(74220, _n_(74218, "print", lambda: print), _n_(74219, "nums", lambda: nums))
_l_(74221)
_c_(74223, _n_(74222, "print", lambda: print), '\nCompute the sum of non-zero groups (separated by zeros) of the said list of numbers:')
_l_(74224)
_c_(74229, _n_(74225, "print", lambda: print), _c_(74228, _n_(74226, "test", lambda: test), _n_(74227, "nums", lambda: nums)))
_l_(74230)