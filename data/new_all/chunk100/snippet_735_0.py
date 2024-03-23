# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(74087)

    result = []
    _l_(74063)
    for digit in _n_(74064, "lst", lambda: lst):
        _l_(74077)

        if _n_(74065, "digit", lambda: digit) == 0:
            _l_(74076)

            if _n_(74066, "ele_val", lambda: ele_val) != 0:
                _l_(74073)

                _c_(74070, _a_(74068, _n_(74067, "result", lambda: result), "append"), _n_(74069, "ele_val", lambda: ele_val))
                _l_(74071)
                ele_val = 0
                _l_(74072)
        else:
            ele_val += _n_(74074, "digit", lambda: digit)
            _l_(74075)
    if _n_(74078, "ele_val", lambda: ele_val) > 0:
        _l_(74084)

        _c_(74082, _a_(74080, _n_(74079, "result", lambda: result), "append"), _n_(74081, "ele_val", lambda: ele_val))
        _l_(74083)
    aux = _n_(74085, "result", lambda: result)
    _l_(74086)
    return aux
nums = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
_l_(74088)
_c_(74090, _n_(74089, "print", lambda: print), '\nOriginal list:')
_l_(74091)
_c_(74094, _n_(74092, "print", lambda: print), _n_(74093, "nums", lambda: nums))
_l_(74095)
_c_(74097, _n_(74096, "print", lambda: print), '\nCompute the sum of non-zero groups (separated by zeros) of the said list of numbers:')
_l_(74098)
_c_(74103, _n_(74099, "print", lambda: print), _c_(74102, _n_(74100, "test", lambda: test), _n_(74101, "nums", lambda: nums)))
_l_(74104)