# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def odd_even_transposition(arr_nums: _n_(58143, "list", lambda: list)) -> _n_(58144, "list", lambda: list):
    _l_(58170)

    for _ in _c_(58147, _n_(58145, "range", lambda: range), _n_(58146, "arr_size", lambda: arr_size)):
        _l_(58167)

        for i in _c_(58151, _n_(58148, "range", lambda: range), _n_(58149, "_", lambda: _) % 2, _n_(58150, "arr_size", lambda: arr_size) - 1, 2):
            _l_(58166)

            if _n_(58152, "arr_nums", lambda: arr_nums)[_n_(58153, "i", lambda: i) + 1] < _n_(58154, "arr_nums", lambda: arr_nums)[_n_(58155, "i", lambda: i)]:
                _l_(58165)

                (_n_(58156, "arr_nums", lambda: arr_nums)[_n_(58157, "i", lambda: i)], _n_(58158, "arr_nums", lambda: arr_nums)[_n_(58159, "i", lambda: i) + 1]) = (_n_(58160, "arr_nums", lambda: arr_nums)[_n_(58161, "i", lambda: i) + 1], _n_(58162, "arr_nums", lambda: arr_nums)[_n_(58163, "i", lambda: i)])
                _l_(58164)
    aux = _n_(58168, "arr_nums", lambda: arr_nums)
    _l_(58169)
    return aux
nums = [4, 3, 5, 1, 2]
_l_(58171)
_c_(58173, _n_(58172, "print", lambda: print), '\nOriginal list:')
_l_(58174)
_c_(58177, _n_(58175, "print", lambda: print), _n_(58176, "nums", lambda: nums))
_l_(58178)
_c_(58181, _n_(58179, "odd_even_transposition", lambda: odd_even_transposition), _n_(58180, "nums", lambda: nums))
_l_(58182)
_c_(58185, _n_(58183, "print", lambda: print), 'Sorted order is:', _n_(58184, "nums", lambda: nums))
_l_(58186)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
_l_(58187)
_c_(58189, _n_(58188, "print", lambda: print), '\nOriginal list:')
_l_(58190)
_c_(58193, _n_(58191, "print", lambda: print), _n_(58192, "nums", lambda: nums))
_l_(58194)
_c_(58197, _n_(58195, "odd_even_transposition", lambda: odd_even_transposition), _n_(58196, "nums", lambda: nums))
_l_(58198)
_c_(58201, _n_(58199, "print", lambda: print), 'Sorted order is:', _n_(58200, "nums", lambda: nums))
_l_(58202)