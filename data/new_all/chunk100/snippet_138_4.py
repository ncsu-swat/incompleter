# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_Product(arr):
    _l_(9572)

    arr_len = _c_(9538, _n_(9536, "len", lambda: len), _n_(9537, "arr", lambda: arr))
    _l_(9539)
    if _n_(9540, "arr_len", lambda: arr_len) < 2:
        _l_(9545)

        _c_(9542, _n_(9541, "print", lambda: print), 'No pairs exists')
        _l_(9543)
        aux = ""
        _l_(9544)
        return aux
    x = _n_(9546, "arr", lambda: arr)[0]
    _l_(9547)
    y = _n_(9548, "arr", lambda: arr)[1]
    _l_(9549)
    for i in _c_(9552, _n_(9550, "range", lambda: range), 0, _n_(9551, "arr_len", lambda: arr_len)):
        _l_(9568)

        for j in _c_(9556, _n_(9553, "range", lambda: range), _n_(9554, "i", lambda: i) + 1, _n_(9555, "arr_len", lambda: arr_len)):
            _l_(9567)

            if _n_(9557, "arr", lambda: arr)[_n_(9558, "i", lambda: i)] * _n_(9559, "arr", lambda: arr)[_n_(9560, "j", lambda: j)] > _n_(9561, "x", lambda: x) * _n_(9562, "y", lambda: y):
                _l_(9566)

                x = _n_(9563, "arr", lambda: arr)[_n_(9564, "i", lambda: i)]
                _l_(9565)
    aux = (_n_(9569, "x", lambda: x), _n_(9570, "y", lambda: y))
    _l_(9571)
    return aux
nums = [1, 2, 3, 4, 7, 0, 8, 4]
_l_(9573)
_c_(9576, _n_(9574, "print", lambda: print), 'Original array:', _n_(9575, "nums", lambda: nums))
_l_(9577)
_c_(9582, _n_(9578, "print", lambda: print), 'Maximum product pair is:', _c_(9581, _n_(9579, "max_Product", lambda: max_Product), _n_(9580, "nums", lambda: nums)))
_l_(9583)
nums = [0, -1, -2, -4, 5, 0, -6]
_l_(9584)
_c_(9587, _n_(9585, "print", lambda: print), '\nOriginal array:', _n_(9586, "nums", lambda: nums))
_l_(9588)
_c_(9593, _n_(9589, "print", lambda: print), 'Maximum product pair is:', _c_(9592, _n_(9590, "max_Product", lambda: max_Product), _n_(9591, "nums", lambda: nums)))
_l_(9594)