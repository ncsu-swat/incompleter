# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(74171)

    ele_val = 0
    _l_(74147)
    for digit in _n_(74148, "lst", lambda: lst):
        _l_(74161)

        if _n_(74149, "digit", lambda: digit) == 0:
            _l_(74160)

            if _n_(74150, "ele_val", lambda: ele_val) != 0:
                _l_(74157)

                _c_(74154, _a_(74152, _n_(74151, "result", lambda: result), "append"), _n_(74153, "ele_val", lambda: ele_val))
                _l_(74155)
                ele_val = 0
                _l_(74156)
        else:
            ele_val += _n_(74158, "digit", lambda: digit)
            _l_(74159)
    if _n_(74162, "ele_val", lambda: ele_val) > 0:
        _l_(74168)

        _c_(74166, _a_(74164, _n_(74163, "result", lambda: result), "append"), _n_(74165, "ele_val", lambda: ele_val))
        _l_(74167)
    aux = _n_(74169, "result", lambda: result)
    _l_(74170)
    return aux
nums = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
_l_(74172)
_c_(74174, _n_(74173, "print", lambda: print), '\nOriginal list:')
_l_(74175)
_c_(74178, _n_(74176, "print", lambda: print), _n_(74177, "nums", lambda: nums))
_l_(74179)
_c_(74181, _n_(74180, "print", lambda: print), '\nCompute the sum of non-zero groups (separated by zeros) of the said list of numbers:')
_l_(74182)
_c_(74187, _n_(74183, "print", lambda: print), _c_(74186, _n_(74184, "test", lambda: test), _n_(74185, "nums", lambda: nums)))
_l_(74188)