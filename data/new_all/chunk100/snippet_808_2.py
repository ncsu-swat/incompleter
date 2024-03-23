# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def odd_even_transposition(arr: _n_(81231, "list", lambda: list)) -> _n_(81232, "list", lambda: list):
    _l_(81262)

    arr_size = _c_(81235, _n_(81233, "len", lambda: len), _n_(81234, "arr", lambda: arr))
    _l_(81236)
    for _ in _c_(81239, _n_(81237, "range", lambda: range), _n_(81238, "arr_size", lambda: arr_size)):
        _l_(81259)

        for i in _c_(81243, _n_(81240, "range", lambda: range), _n_(81241, "_", lambda: _) % 2, _n_(81242, "arr_size", lambda: arr_size) - 1, 2):
            _l_(81258)

            if _n_(81244, "arr", lambda: arr)[_n_(81245, "i", lambda: i) + 1] < _n_(81246, "arr", lambda: arr)[_n_(81247, "i", lambda: i)]:
                _l_(81257)

                (_n_(81248, "arr", lambda: arr)[_n_(81249, "i", lambda: i)], _n_(81250, "arr", lambda: arr)[_n_(81251, "i", lambda: i) + 1]) = (_n_(81252, "arr", lambda: arr)[_n_(81253, "i", lambda: i) + 1], _n_(81254, "arr", lambda: arr)[_n_(81255, "i", lambda: i)])
                _l_(81256)
    aux = _n_(81260, "arr", lambda: arr)
    _l_(81261)
    return aux
_c_(81264, _n_(81263, "print", lambda: print), '\nOriginal list:')
_l_(81265)
_c_(81268, _n_(81266, "print", lambda: print), _n_(81267, "nums", lambda: nums))
_l_(81269)
_c_(81272, _n_(81270, "odd_even_transposition", lambda: odd_even_transposition), _n_(81271, "nums", lambda: nums))
_l_(81273)
_c_(81276, _n_(81274, "print", lambda: print), 'Sorted order is:', _n_(81275, "nums", lambda: nums))
_l_(81277)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
_l_(81278)
_c_(81280, _n_(81279, "print", lambda: print), '\nOriginal list:')
_l_(81281)
_c_(81284, _n_(81282, "print", lambda: print), _n_(81283, "nums", lambda: nums))
_l_(81285)
_c_(81288, _n_(81286, "odd_even_transposition", lambda: odd_even_transposition), _n_(81287, "nums", lambda: nums))
_l_(81289)
_c_(81292, _n_(81290, "print", lambda: print), 'Sorted order is:', _n_(81291, "nums", lambda: nums))
_l_(81293)