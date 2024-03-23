# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_Product(arr):
    _l_(9690)

    if _n_(9655, "arr_len", lambda: arr_len) < 2:
        _l_(9660)

        _c_(9657, _n_(9656, "print", lambda: print), 'No pairs exists')
        _l_(9658)
        aux = ""
        _l_(9659)
        return aux
    x = _n_(9661, "arr", lambda: arr)[0]
    _l_(9662)
    y = _n_(9663, "arr", lambda: arr)[1]
    _l_(9664)
    for i in _c_(9667, _n_(9665, "range", lambda: range), 0, _n_(9666, "arr_len", lambda: arr_len)):
        _l_(9686)

        for j in _c_(9671, _n_(9668, "range", lambda: range), _n_(9669, "i", lambda: i) + 1, _n_(9670, "arr_len", lambda: arr_len)):
            _l_(9685)

            if _n_(9672, "arr", lambda: arr)[_n_(9673, "i", lambda: i)] * _n_(9674, "arr", lambda: arr)[_n_(9675, "j", lambda: j)] > _n_(9676, "x", lambda: x) * _n_(9677, "y", lambda: y):
                _l_(9684)

                x = _n_(9678, "arr", lambda: arr)[_n_(9679, "i", lambda: i)]
                _l_(9680)
                y = _n_(9681, "arr", lambda: arr)[_n_(9682, "j", lambda: j)]
                _l_(9683)
    aux = (_n_(9687, "x", lambda: x), _n_(9688, "y", lambda: y))
    _l_(9689)
    return aux
nums = [1, 2, 3, 4, 7, 0, 8, 4]
_l_(9691)
_c_(9694, _n_(9692, "print", lambda: print), 'Original array:', _n_(9693, "nums", lambda: nums))
_l_(9695)
_c_(9700, _n_(9696, "print", lambda: print), 'Maximum product pair is:', _c_(9699, _n_(9697, "max_Product", lambda: max_Product), _n_(9698, "nums", lambda: nums)))
_l_(9701)
nums = [0, -1, -2, -4, 5, 0, -6]
_l_(9702)
_c_(9705, _n_(9703, "print", lambda: print), '\nOriginal array:', _n_(9704, "nums", lambda: nums))
_l_(9706)
_c_(9711, _n_(9707, "print", lambda: print), 'Maximum product pair is:', _c_(9710, _n_(9708, "max_Product", lambda: max_Product), _n_(9709, "nums", lambda: nums)))
_l_(9712)