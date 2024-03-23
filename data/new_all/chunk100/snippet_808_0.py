# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def odd_even_transposition(arr: _n_(81108, "list", lambda: list)) -> _n_(81109, "list", lambda: list):
    _l_(81139)

    arr_size = _c_(81112, _n_(81110, "len", lambda: len), _n_(81111, "arr", lambda: arr))
    _l_(81113)
    for _ in _c_(81116, _n_(81114, "range", lambda: range), _n_(81115, "arr_size", lambda: arr_size)):
        _l_(81136)

        for i in _c_(81120, _n_(81117, "range", lambda: range), _n_(81118, "_", lambda: _) % 2, _n_(81119, "arr_size", lambda: arr_size) - 1, 2):
            _l_(81135)

            if _n_(81121, "arr", lambda: arr)[_n_(81122, "i", lambda: i) + 1] < _n_(81123, "arr", lambda: arr)[_n_(81124, "i", lambda: i)]:
                _l_(81134)

                (_n_(81125, "arr", lambda: arr)[_n_(81126, "i", lambda: i)], _n_(81127, "arr", lambda: arr)[_n_(81128, "i", lambda: i) + 1]) = (_n_(81129, "arr", lambda: arr)[_n_(81130, "i", lambda: i) + 1], _n_(81131, "arr", lambda: arr)[_n_(81132, "i", lambda: i)])
                _l_(81133)
    aux = _n_(81137, "arr", lambda: arr)
    _l_(81138)
    return aux
nums = [4, 3, 5, 1, 2]
_l_(81140)
_c_(81142, _n_(81141, "print", lambda: print), '\nOriginal list:')
_l_(81143)
_c_(81146, _n_(81144, "print", lambda: print), _n_(81145, "nums", lambda: nums))
_l_(81147)
_c_(81150, _n_(81148, "odd_even_transposition", lambda: odd_even_transposition), _n_(81149, "nums", lambda: nums))
_l_(81151)
_c_(81154, _n_(81152, "print", lambda: print), 'Sorted order is:', _n_(81153, "nums", lambda: nums))
_l_(81155)
_c_(81157, _n_(81156, "print", lambda: print), '\nOriginal list:')
_l_(81158)
_c_(81161, _n_(81159, "print", lambda: print), _n_(81160, "nums", lambda: nums))
_l_(81162)
_c_(81165, _n_(81163, "odd_even_transposition", lambda: odd_even_transposition), _n_(81164, "nums", lambda: nums))
_l_(81166)
_c_(81169, _n_(81167, "print", lambda: print), 'Sorted order is:', _n_(81168, "nums", lambda: nums))
_l_(81170)