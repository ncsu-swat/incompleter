# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def odd_even_transposition(arr_nums: _n_(58080, "list", lambda: list)) -> _n_(58081, "list", lambda: list):
    _l_(58111)

    arr_size = _c_(58084, _n_(58082, "len", lambda: len), _n_(58083, "arr_nums", lambda: arr_nums))
    _l_(58085)
    for _ in _c_(58088, _n_(58086, "range", lambda: range), _n_(58087, "arr_size", lambda: arr_size)):
        _l_(58108)

        for i in _c_(58092, _n_(58089, "range", lambda: range), _n_(58090, "_", lambda: _) % 2, _n_(58091, "arr_size", lambda: arr_size) - 1, 2):
            _l_(58107)

            if _n_(58093, "arr_nums", lambda: arr_nums)[_n_(58094, "i", lambda: i) + 1] < _n_(58095, "arr_nums", lambda: arr_nums)[_n_(58096, "i", lambda: i)]:
                _l_(58106)

                (_n_(58097, "arr_nums", lambda: arr_nums)[_n_(58098, "i", lambda: i)], _n_(58099, "arr_nums", lambda: arr_nums)[_n_(58100, "i", lambda: i) + 1]) = (_n_(58101, "arr_nums", lambda: arr_nums)[_n_(58102, "i", lambda: i) + 1], _n_(58103, "arr_nums", lambda: arr_nums)[_n_(58104, "i", lambda: i)])
                _l_(58105)
    aux = _n_(58109, "arr_nums", lambda: arr_nums)
    _l_(58110)
    return aux
nums = [4, 3, 5, 1, 2]
_l_(58112)
_c_(58114, _n_(58113, "print", lambda: print), '\nOriginal list:')
_l_(58115)
_c_(58118, _n_(58116, "print", lambda: print), _n_(58117, "nums", lambda: nums))
_l_(58119)
_c_(58122, _n_(58120, "odd_even_transposition", lambda: odd_even_transposition), _n_(58121, "nums", lambda: nums))
_l_(58123)
_c_(58126, _n_(58124, "print", lambda: print), 'Sorted order is:', _n_(58125, "nums", lambda: nums))
_l_(58127)
_c_(58129, _n_(58128, "print", lambda: print), '\nOriginal list:')
_l_(58130)
_c_(58133, _n_(58131, "print", lambda: print), _n_(58132, "nums", lambda: nums))
_l_(58134)
_c_(58137, _n_(58135, "odd_even_transposition", lambda: odd_even_transposition), _n_(58136, "nums", lambda: nums))
_l_(58138)
_c_(58141, _n_(58139, "print", lambda: print), 'Sorted order is:', _n_(58140, "nums", lambda: nums))
_l_(58142)