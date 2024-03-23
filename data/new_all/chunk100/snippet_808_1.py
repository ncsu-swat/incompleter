# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def odd_even_transposition(arr: _n_(81171, "list", lambda: list)) -> _n_(81172, "list", lambda: list):
    _l_(81198)

    for _ in _c_(81175, _n_(81173, "range", lambda: range), _n_(81174, "arr_size", lambda: arr_size)):
        _l_(81195)

        for i in _c_(81179, _n_(81176, "range", lambda: range), _n_(81177, "_", lambda: _) % 2, _n_(81178, "arr_size", lambda: arr_size) - 1, 2):
            _l_(81194)

            if _n_(81180, "arr", lambda: arr)[_n_(81181, "i", lambda: i) + 1] < _n_(81182, "arr", lambda: arr)[_n_(81183, "i", lambda: i)]:
                _l_(81193)

                (_n_(81184, "arr", lambda: arr)[_n_(81185, "i", lambda: i)], _n_(81186, "arr", lambda: arr)[_n_(81187, "i", lambda: i) + 1]) = (_n_(81188, "arr", lambda: arr)[_n_(81189, "i", lambda: i) + 1], _n_(81190, "arr", lambda: arr)[_n_(81191, "i", lambda: i)])
                _l_(81192)
    aux = _n_(81196, "arr", lambda: arr)
    _l_(81197)
    return aux
nums = [4, 3, 5, 1, 2]
_l_(81199)
_c_(81201, _n_(81200, "print", lambda: print), '\nOriginal list:')
_l_(81202)
_c_(81205, _n_(81203, "print", lambda: print), _n_(81204, "nums", lambda: nums))
_l_(81206)
_c_(81209, _n_(81207, "odd_even_transposition", lambda: odd_even_transposition), _n_(81208, "nums", lambda: nums))
_l_(81210)
_c_(81213, _n_(81211, "print", lambda: print), 'Sorted order is:', _n_(81212, "nums", lambda: nums))
_l_(81214)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
_l_(81215)
_c_(81217, _n_(81216, "print", lambda: print), '\nOriginal list:')
_l_(81218)
_c_(81221, _n_(81219, "print", lambda: print), _n_(81220, "nums", lambda: nums))
_l_(81222)
_c_(81225, _n_(81223, "odd_even_transposition", lambda: odd_even_transposition), _n_(81224, "nums", lambda: nums))
_l_(81226)
_c_(81229, _n_(81227, "print", lambda: print), 'Sorted order is:', _n_(81228, "nums", lambda: nums))
_l_(81230)