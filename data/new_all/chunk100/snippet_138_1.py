# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_Product(arr):
    _l_(9393)

    arr_len = _c_(9358, _n_(9356, "len", lambda: len), _n_(9357, "arr", lambda: arr))
    _l_(9359)
    if _n_(9360, "arr_len", lambda: arr_len) < 2:
        _l_(9365)

        _c_(9362, _n_(9361, "print", lambda: print), 'No pairs exists')
        _l_(9363)
        aux = ""
        _l_(9364)
        return aux
    x = _n_(9366, "arr", lambda: arr)[0]
    _l_(9367)
    for i in _c_(9370, _n_(9368, "range", lambda: range), 0, _n_(9369, "arr_len", lambda: arr_len)):
        _l_(9389)

        for j in _c_(9374, _n_(9371, "range", lambda: range), _n_(9372, "i", lambda: i) + 1, _n_(9373, "arr_len", lambda: arr_len)):
            _l_(9388)

            if _n_(9375, "arr", lambda: arr)[_n_(9376, "i", lambda: i)] * _n_(9377, "arr", lambda: arr)[_n_(9378, "j", lambda: j)] > _n_(9379, "x", lambda: x) * _n_(9380, "y", lambda: y):
                _l_(9387)

                x = _n_(9381, "arr", lambda: arr)[_n_(9382, "i", lambda: i)]
                _l_(9383)
                y = _n_(9384, "arr", lambda: arr)[_n_(9385, "j", lambda: j)]
                _l_(9386)
    aux = (_n_(9390, "x", lambda: x), _n_(9391, "y", lambda: y))
    _l_(9392)
    return aux
nums = [1, 2, 3, 4, 7, 0, 8, 4]
_l_(9394)
_c_(9397, _n_(9395, "print", lambda: print), 'Original array:', _n_(9396, "nums", lambda: nums))
_l_(9398)
_c_(9403, _n_(9399, "print", lambda: print), 'Maximum product pair is:', _c_(9402, _n_(9400, "max_Product", lambda: max_Product), _n_(9401, "nums", lambda: nums)))
_l_(9404)
nums = [0, -1, -2, -4, 5, 0, -6]
_l_(9405)
_c_(9408, _n_(9406, "print", lambda: print), '\nOriginal array:', _n_(9407, "nums", lambda: nums))
_l_(9409)
_c_(9414, _n_(9410, "print", lambda: print), 'Maximum product pair is:', _c_(9413, _n_(9411, "max_Product", lambda: max_Product), _n_(9412, "nums", lambda: nums)))
_l_(9415)