# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_Product(arr):
    _l_(9632)

    arr_len = _c_(9597, _n_(9595, "len", lambda: len), _n_(9596, "arr", lambda: arr))
    _l_(9598)
    if _n_(9599, "arr_len", lambda: arr_len) < 2:
        _l_(9604)

        _c_(9601, _n_(9600, "print", lambda: print), 'No pairs exists')
        _l_(9602)
        aux = ""
        _l_(9603)
        return aux
    y = _n_(9605, "arr", lambda: arr)[1]
    _l_(9606)
    for i in _c_(9609, _n_(9607, "range", lambda: range), 0, _n_(9608, "arr_len", lambda: arr_len)):
        _l_(9628)

        for j in _c_(9613, _n_(9610, "range", lambda: range), _n_(9611, "i", lambda: i) + 1, _n_(9612, "arr_len", lambda: arr_len)):
            _l_(9627)

            if _n_(9614, "arr", lambda: arr)[_n_(9615, "i", lambda: i)] * _n_(9616, "arr", lambda: arr)[_n_(9617, "j", lambda: j)] > _n_(9618, "x", lambda: x) * _n_(9619, "y", lambda: y):
                _l_(9626)

                x = _n_(9620, "arr", lambda: arr)[_n_(9621, "i", lambda: i)]
                _l_(9622)
                y = _n_(9623, "arr", lambda: arr)[_n_(9624, "j", lambda: j)]
                _l_(9625)
    aux = (_n_(9629, "x", lambda: x), _n_(9630, "y", lambda: y))
    _l_(9631)
    return aux
nums = [1, 2, 3, 4, 7, 0, 8, 4]
_l_(9633)
_c_(9636, _n_(9634, "print", lambda: print), 'Original array:', _n_(9635, "nums", lambda: nums))
_l_(9637)
_c_(9642, _n_(9638, "print", lambda: print), 'Maximum product pair is:', _c_(9641, _n_(9639, "max_Product", lambda: max_Product), _n_(9640, "nums", lambda: nums)))
_l_(9643)
nums = [0, -1, -2, -4, 5, 0, -6]
_l_(9644)
_c_(9647, _n_(9645, "print", lambda: print), '\nOriginal array:', _n_(9646, "nums", lambda: nums))
_l_(9648)
_c_(9653, _n_(9649, "print", lambda: print), 'Maximum product pair is:', _c_(9652, _n_(9650, "max_Product", lambda: max_Product), _n_(9651, "nums", lambda: nums)))
_l_(9654)