# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def odd_even_transposition(arr_nums: _n_(58203, "list", lambda: list)) -> _n_(58204, "list", lambda: list):
    _l_(58234)

    arr_size = _c_(58207, _n_(58205, "len", lambda: len), _n_(58206, "arr_nums", lambda: arr_nums))
    _l_(58208)
    for _ in _c_(58211, _n_(58209, "range", lambda: range), _n_(58210, "arr_size", lambda: arr_size)):
        _l_(58231)

        for i in _c_(58215, _n_(58212, "range", lambda: range), _n_(58213, "_", lambda: _) % 2, _n_(58214, "arr_size", lambda: arr_size) - 1, 2):
            _l_(58230)

            if _n_(58216, "arr_nums", lambda: arr_nums)[_n_(58217, "i", lambda: i) + 1] < _n_(58218, "arr_nums", lambda: arr_nums)[_n_(58219, "i", lambda: i)]:
                _l_(58229)

                (_n_(58220, "arr_nums", lambda: arr_nums)[_n_(58221, "i", lambda: i)], _n_(58222, "arr_nums", lambda: arr_nums)[_n_(58223, "i", lambda: i) + 1]) = (_n_(58224, "arr_nums", lambda: arr_nums)[_n_(58225, "i", lambda: i) + 1], _n_(58226, "arr_nums", lambda: arr_nums)[_n_(58227, "i", lambda: i)])
                _l_(58228)
    aux = _n_(58232, "arr_nums", lambda: arr_nums)
    _l_(58233)
    return aux
_c_(58236, _n_(58235, "print", lambda: print), '\nOriginal list:')
_l_(58237)
_c_(58240, _n_(58238, "print", lambda: print), _n_(58239, "nums", lambda: nums))
_l_(58241)
_c_(58244, _n_(58242, "odd_even_transposition", lambda: odd_even_transposition), _n_(58243, "nums", lambda: nums))
_l_(58245)
_c_(58248, _n_(58246, "print", lambda: print), 'Sorted order is:', _n_(58247, "nums", lambda: nums))
_l_(58249)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
_l_(58250)
_c_(58252, _n_(58251, "print", lambda: print), '\nOriginal list:')
_l_(58253)
_c_(58256, _n_(58254, "print", lambda: print), _n_(58255, "nums", lambda: nums))
_l_(58257)
_c_(58260, _n_(58258, "odd_even_transposition", lambda: odd_even_transposition), _n_(58259, "nums", lambda: nums))
_l_(58261)
_c_(58264, _n_(58262, "print", lambda: print), 'Sorted order is:', _n_(58263, "nums", lambda: nums))
_l_(58265)