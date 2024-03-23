# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_Product(arr):
    _l_(9514)

    arr_len = _c_(9477, _n_(9475, "len", lambda: len), _n_(9476, "arr", lambda: arr))
    _l_(9478)
    if _n_(9479, "arr_len", lambda: arr_len) < 2:
        _l_(9484)

        _c_(9481, _n_(9480, "print", lambda: print), 'No pairs exists')
        _l_(9482)
        aux = ""
        _l_(9483)
        return aux
    x = _n_(9485, "arr", lambda: arr)[0]
    _l_(9486)
    y = _n_(9487, "arr", lambda: arr)[1]
    _l_(9488)
    for i in _c_(9491, _n_(9489, "range", lambda: range), 0, _n_(9490, "arr_len", lambda: arr_len)):
        _l_(9510)

        for j in _c_(9495, _n_(9492, "range", lambda: range), _n_(9493, "i", lambda: i) + 1, _n_(9494, "arr_len", lambda: arr_len)):
            _l_(9509)

            if _n_(9496, "arr", lambda: arr)[_n_(9497, "i", lambda: i)] * _n_(9498, "arr", lambda: arr)[_n_(9499, "j", lambda: j)] > _n_(9500, "x", lambda: x) * _n_(9501, "y", lambda: y):
                _l_(9508)

                x = _n_(9502, "arr", lambda: arr)[_n_(9503, "i", lambda: i)]
                _l_(9504)
                y = _n_(9505, "arr", lambda: arr)[_n_(9506, "j", lambda: j)]
                _l_(9507)
    aux = (_n_(9511, "x", lambda: x), _n_(9512, "y", lambda: y))
    _l_(9513)
    return aux
_c_(9517, _n_(9515, "print", lambda: print), 'Original array:', _n_(9516, "nums", lambda: nums))
_l_(9518)
_c_(9523, _n_(9519, "print", lambda: print), 'Maximum product pair is:', _c_(9522, _n_(9520, "max_Product", lambda: max_Product), _n_(9521, "nums", lambda: nums)))
_l_(9524)
nums = [0, -1, -2, -4, 5, 0, -6]
_l_(9525)
_c_(9528, _n_(9526, "print", lambda: print), '\nOriginal array:', _n_(9527, "nums", lambda: nums))
_l_(9529)
_c_(9534, _n_(9530, "print", lambda: print), 'Maximum product pair is:', _c_(9533, _n_(9531, "max_Product", lambda: max_Product), _n_(9532, "nums", lambda: nums)))
_l_(9535)